#!/usr/bin/env python3
"""Copy Funnel's reviewed develop docs into the CALYPR website checkout."""
import argparse
import hashlib
import json
import re
from pathlib import Path

SITE = Path(__file__).resolve().parents[1]
DEST = SITE / 'docs/tools/funnel/docs'
MANIFEST = SITE / 'docs/tools/funnel/.funnel-docs.json'
NAV = SITE / 'zensical.toml'
GROUPS = [('Storage', 'storage'), ('Compute', 'compute'), ('Databases', 'databases'),
          ('Security', 'security'), ('Integrations', 'integrations'), ('Events', 'events'),
          ('Metrics', 'metrics'), ('Development', 'development')]
TEMPLATES = {'htcondor': ('htcondor', 'HTCondor'), 'gridengine': ('gridengine', 'GridEngine'),
             'pbs': ('pbs', 'PBS'), 'slurm': ('slurm', 'Slurm')}

def convert(text, upstream):
    text = text.replace('https://ohsu-comp-bio.github.io/funnel/install.sh', 'https://calypr.org/tools/funnel/install.sh')
    text = text.replace('src="/img/k8s-pvc.png"', 'src="../k8s-pvc.png"')
    text = re.sub(r'\{\{< details title="([^"]*)" >\}\}', r'<details markdown="1"><summary>\1</summary>\n', text)
    text = text.replace('{{< /details >}}', '</details>')
    converted_template = False
    for shortcode, (compute, config) in TEMPLATES.items():
        token = '{{< ' + shortcode + '-template >}}'
        if token in text:
            converted_template = True
            template = (upstream / 'website/static/funnel-config-examples' / (shortcode + '-template.txt')).read_text()
            replacement = 'Compute: ' + compute + '\n\n' + config + ':\n  Template: |\n' + ''.join('    ' + line + '\n' for line in template.splitlines())
            text = text.replace(token, replacement.rstrip())
    if re.search(r'\{\{[<%]', text):
        raise ValueError('Unconverted Hugo shortcode; extend the sync before importing this page')
    if converted_template:
        text = re.sub(r'(?m)^[ \t]+$', '', text)
        text = text.replace('as an argument \n', 'as an argument\n')
    return text

def title(path):
    match = re.search(r'^title:\s*["\']?(.+?)["\']?\s*$', path.read_text(), re.MULTILINE)
    return match.group(1) if match else path.stem.replace('-', ' ').title()

def sync(upstream, revision):
    source = upstream / 'website/content/docs'
    files = [p for p in source.rglob('*.md') if p.parent != source or p.name == 'tasks.md']
    unknown = {p.relative_to(source).parts[0] for p in files if p.parent != source} - {folder for _, folder in GROUPS}
    if unknown:
        raise ValueError('Unknown Funnel documentation sections: ' + ', '.join(sorted(unknown)))
    if not files or not (source / 'tasks.md').is_file():
        raise ValueError('Not a Funnel source checkout: website/content/docs/tasks.md is missing')
    old = json.loads(MANIFEST.read_text()) if MANIFEST.exists() else {'files': []}
    pending = old.get('pending_reconciliation', {}).copy()
    new = sorted(p.relative_to(source).as_posix() for p in files)
    for name in old['files']:
        p = Path(name)
        if p.is_absolute() or '..' in p.parts:
            raise ValueError('Invalid path in sync manifest')
        if name not in new:
            (DEST / p).unlink(missing_ok=True)
    for path in files:
        name = path.relative_to(source).as_posix()
        if name in pending:
            if hashlib.sha256(path.read_bytes()).hexdigest() != pending[name]:
                continue
            del pending[name]
        target = DEST / path.relative_to(source)
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(convert(path.read_text(), upstream))
    image = upstream / 'website/static/img/k8s-pvc.png'
    if image.is_file():
        (DEST / 'compute/k8s-pvc.png').write_bytes(image.read_bytes())
    # This public installer is also distributed directly by the CALYPR site.
    (SITE / 'docs/tools/funnel/install.sh').write_bytes((upstream / 'install.sh').read_bytes())

    nav = ['      # BEGIN GENERATED FUNNEL NAV', '      { "Funnel" = [',
           '        "tools/funnel/index.md",', '        { "Overview" = "tools/funnel/docs/docs.md" },',
           '        { "Download" = "tools/funnel/docs/download.md" },',
           '        { "Tasks" = "tools/funnel/docs/tasks.md" },']
    for label, folder in GROUPS:
        entries = sorted((p for p in files if p.relative_to(source).parts[0] == folder), key=lambda p: (title(p).lower(), p.name))
        if not entries:
            continue
        nav.append('        { ' + json.dumps(label) + ' = [')
        if folder == 'storage':
            nav.append('          "tools/funnel/docs/storage/index.md",')
        for p in entries:
            nav.append('          { ' + json.dumps(title(p), ensure_ascii=False) + ' = ' + json.dumps('tools/funnel/docs/' + p.relative_to(source).as_posix()) + ' },')
        nav.append('        ] },')
    nav += ['      ] },', '      # END GENERATED FUNNEL NAV']
    config = NAV.read_text()
    begin, end = '      # BEGIN GENERATED FUNNEL NAV', '      # END GENERATED FUNNEL NAV'
    if begin not in config or end not in config:
        raise ValueError('Missing Funnel navigation markers')
    NAV.write_text(config[:config.index(begin)] + '\n'.join(nav) + config[config.index(end)+len(end):])
    MANIFEST.write_text(json.dumps({'source': 'https://github.com/calypr/funnel', 'branch': 'develop', 'revision': revision, 'files': new, 'pending_reconciliation': pending}, indent=2) + '\n')
    print(f'Synced {len(new)} Funnel pages from {revision}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('upstream', type=Path)
    parser.add_argument('--revision', required=True)
    args = parser.parse_args()
    if not re.fullmatch(r'[a-f0-9]{40}', args.revision):
        parser.error('--revision must be a full Git commit SHA')
    sync(args.upstream.resolve(), args.revision)
