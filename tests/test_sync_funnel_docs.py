import hashlib
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location('sync_funnel_docs', Path(__file__).resolve().parents[1] / 'scripts/sync_funnel_docs.py')
sync = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(sync)
REV = 'a' * 40

class SyncTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        root = Path(self.temp.name)
        self.site, self.upstream = root / 'site', root / 'upstream'
        self.source = self.upstream / 'website/content/docs'
        (self.source / 'compute').mkdir(parents=True)
        (self.site / 'docs/tools/funnel/docs').mkdir(parents=True)
        (self.upstream / 'install.sh').write_text('#!/bin/sh\n')
        (self.source / 'tasks.md').write_text('---\ntitle: Tasks\n---\n')
        (self.source / 'compute/example.md').write_text('---\ntitle: Example\n---\nnew\n')
        self.nav = self.site / 'zensical.toml'
        self.nav.write_text('      # BEGIN GENERATED FUNNEL NAV\n      # END GENERATED FUNNEL NAV\n')
        sync.SITE = self.site
        sync.DEST = self.site / 'docs/tools/funnel/docs'
        sync.MANIFEST = self.site / 'docs/tools/funnel/.funnel-docs.json'
        sync.NAV = self.nav

    def tearDown(self):
        self.temp.cleanup()

    def test_sync_is_repeatable_and_updates_navigation_and_removed_pages(self):
        sync.sync(self.upstream, REV)
        page = sync.DEST / 'compute/example.md'
        self.assertIn('new', page.read_text())
        self.assertIn('tools/funnel/docs/compute/example.md', self.nav.read_text())
        old_nav, old_manifest = self.nav.read_text(), sync.MANIFEST.read_text()
        sync.sync(self.upstream, REV)
        self.assertEqual(old_nav, self.nav.read_text())
        self.assertEqual(old_manifest, sync.MANIFEST.read_text())
        (self.source / 'compute/example.md').unlink()
        sync.sync(self.upstream, REV)
        self.assertFalse(page.exists())
        self.assertNotIn('tools/funnel/docs/compute/example.md', self.nav.read_text())

    def test_preserves_live_page_until_reconciled_upstream_arrives(self):
        page = sync.DEST / 'compute/example.md'
        page.parent.mkdir(parents=True)
        page.write_text('live content')
        expected = b'---\ntitle: Example\n---\nreconciled\n'
        sync.MANIFEST.write_text(json.dumps({'files': [], 'pending_reconciliation': {'compute/example.md': hashlib.sha256(expected).hexdigest()}}))
        sync.sync(self.upstream, REV)
        self.assertEqual(page.read_text(), 'live content')
        (self.source / 'compute/example.md').write_bytes(expected)
        sync.sync(self.upstream, REV)
        self.assertEqual(page.read_bytes(), expected)
        self.assertEqual(json.loads(sync.MANIFEST.read_text())['pending_reconciliation'], {})
        (self.source / 'compute/example.md').write_text('later change')
        sync.sync(self.upstream, REV)
        self.assertEqual(page.read_text(), 'later change')

    def test_does_not_delete_a_pending_page_when_upstream_removes_it(self):
        page = sync.DEST / 'compute/example.md'
        page.parent.mkdir(parents=True)
        page.write_text('live content')
        sync.MANIFEST.write_text(json.dumps({'files': ['compute/example.md'], 'pending_reconciliation': {'compute/example.md': 'expected'}}))
        (self.source / 'compute/example.md').unlink()
        with self.assertRaisesRegex(ValueError, 'Reconciliation pages missing upstream'):
            sync.sync(self.upstream, REV)
        self.assertEqual(page.read_text(), 'live content')

    def test_fails_for_unknown_shortcodes(self):
        with self.assertRaisesRegex(ValueError, 'Unconverted Hugo shortcode'):
            sync.convert('{{< surprise >}}', self.upstream)

if __name__ == '__main__':
    unittest.main()
