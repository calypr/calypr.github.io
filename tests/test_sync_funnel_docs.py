import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SPEC = importlib.util.spec_from_file_location(
    "sync_funnel_docs", Path(__file__).resolve().parents[1] / "scripts/sync_funnel_docs.py"
)
sync = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(sync)
REV = "a" * 40


class SyncTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        root = Path(self.temp.name)
        self.site, self.upstream = root / "site", root / "upstream"
        self.source = self.upstream / "docs"
        (self.source / "compute").mkdir(parents=True)
        (self.site / "docs/tools/funnel/docs").mkdir(parents=True)
        (self.upstream / "install.sh").write_text("#!/bin/sh\n")
        (self.source / "README.md").write_text("# Overview\n")
        (self.source / "tasks.md").write_text("# Tasks\n")
        (self.source / "upgrading.md").write_text("# Upgrade Funnel\n")
        (self.source / "compute/example.md").write_text("# GPU tasks\nnew\n")
        self.nav = self.site / "zensical.toml"
        self.nav.write_text("      # BEGIN GENERATED FUNNEL NAV\n      # END GENERATED FUNNEL NAV\n")
        sync.SITE = self.site
        sync.DEST = self.site / "docs/tools/funnel/docs"
        sync.MANIFEST = self.site / "docs/tools/funnel/.funnel-docs.json"
        sync.NAV = self.nav

    def tearDown(self):
        self.temp.cleanup()

    def test_updates_plain_markdown_navigation_and_removes_retired_pages(self):
        download = sync.DEST / "download.md"
        download.write_text("site-owned download page")
        retired = sync.DEST / "databases/elasticsearch.md"
        retired.parent.mkdir()
        retired.write_text("retired")
        sync.sync(self.upstream, REV)
        self.assertFalse(retired.exists())
        self.assertEqual(download.read_text(), "site-owned download page")
        self.assertIn('"GPU tasks"', self.nav.read_text())
        self.assertIn('"Upgrade Funnel"', self.nav.read_text())
        self.assertEqual((sync.DEST / "docs.md").read_text(), "# Overview\n")
        previous = {p.relative_to(self.site): p.read_bytes() for p in self.site.rglob("*") if p.is_file()}
        sync.sync(self.upstream, REV)
        self.assertEqual(previous, {p.relative_to(self.site): p.read_bytes() for p in self.site.rglob("*") if p.is_file()})
        (self.source / "compute/example.md").unlink()
        sync.sync(self.upstream, REV)
        self.assertFalse((sync.DEST / "compute/example.md").exists())
        self.assertNotIn("compute/example.md", self.nav.read_text())

    def test_adopts_reconciled_docs_instead_of_keeping_legacy_hash_locks(self):
        sync.MANIFEST.write_text(json.dumps({"files": [], "pending_reconciliation": {"compute/example.md": "old-hugo-hash"}}))
        sync.sync(self.upstream, REV)
        self.assertIn("new", (sync.DEST / "compute/example.md").read_text())
        self.assertNotIn("pending_reconciliation", json.loads(sync.MANIFEST.read_text()))

    def test_preserves_reference_assets_and_rewrites_repository_links(self):
        templates = self.source / "compute/templates"
        templates.mkdir()
        (templates / "role.yaml").write_text("kind: Role\n")
        (self.upstream / "internal").mkdir()
        (self.upstream / "internal/example.go").write_text("package example\n")
        (self.source / "compute/example.md").write_text(
            "# GPU tasks\n[Overview](../README.md)\n[Template](templates/role.yaml)\n"
            "[Code](../../internal/example.go#L1)\n[code]: ../../internal/example.go\n"
        )
        sync.sync(self.upstream, REV)
        text = (sync.DEST / "compute/example.md").read_text()
        self.assertIn("[Overview](../docs.md)", text)
        self.assertIn("[Template](templates/role.yaml)", text)
        self.assertIn(f"https://github.com/calypr/funnel/blob/{REV}/internal/example.go#L1", text)
        self.assertIn(f"[code]: https://github.com/calypr/funnel/blob/{REV}/internal/example.go", text)
        self.assertEqual((sync.DEST / "compute/templates/role.yaml").read_text(), "kind: Role\n")

    def test_excludes_private_internal_and_hidden_files(self):
        (self.source / "internal").mkdir()
        (self.source / "internal/private-plan.md").write_text("private")
        (self.source / ".private.md").write_text("private")
        sync.sync(self.upstream, REV)
        self.assertFalse((sync.DEST / "internal").exists())
        self.assertFalse((sync.DEST / ".private.md").exists())
        self.assertNotIn("private", self.nav.read_text())

    def test_rejects_unknown_sections_before_modifying_site(self):
        (self.source / "surprise").mkdir()
        (self.source / "surprise/page.md").write_text("# Surprise\n")
        original = self.nav.read_text()
        with self.assertRaisesRegex(ValueError, "Unknown Funnel documentation sections"):
            sync.sync(self.upstream, REV)
        self.assertEqual(original, self.nav.read_text())

    def test_rejects_unknown_shortcodes_before_modifying_site(self):
        (self.source / "compute/example.md").write_text("{{< surprise >}}")
        with self.assertRaisesRegex(ValueError, "Unconverted Hugo shortcode"):
            sync.sync(self.upstream, REV)
        self.assertFalse((sync.DEST / "tasks.md").exists())


if __name__ == "__main__":
    unittest.main()
