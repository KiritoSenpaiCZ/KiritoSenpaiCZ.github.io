#!/usr/bin/env python3
"""
Releases a new version of one Kodi addon into this repository.

    python dev/release_kodi.py Kodi-Edna 1.2.0

Run from anywhere, with the addon repos cloned next to this repo. It:
  - sets the version in the addon's addon.xml and README.md
  - builds zips/<id>/<id>-<version>.zip (README, addon.xml, icon, service.py, resources/)
  - copies the addon's <addon> entry (all metadata) into addons.xml, rewrites addons.xml.md5
  - updates the version in this repo's README table
  - prints the git commands for the old zip it replaced (it can't delete files itself)
"""
import ast, hashlib, io, os, re, sys, zipfile
from xml.dom import minidom

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(HERE)
ROOT = os.path.dirname(REPO)

def read(p):
    raw = open(p, 'rb').read().decode('utf-8')
    return raw, ('\r\n' if '\r\n' in raw else '\n')

def write(p, text):
    open(p, 'wb').write(text.encode('utf-8'))

def main(folder, version):
    src = os.path.join(ROOT, folder)
    ax_path = os.path.join(src, 'addon.xml')
    ax, _ = read(ax_path)
    m = re.search(r'<addon id="([^"]+)"[^>]*?version="([^"]+)"', ax)
    addon_id, old = m.group(1), m.group(2)
    ax = ax.replace('version="%s" provider-name' % old, 'version="%s" provider-name' % version, 1)
    write(ax_path, ax)
    readme_path = os.path.join(src, 'README.md')
    readme, _ = read(readme_path)
    readme = readme.replace('%s - %s' % (addon_id, old), '%s - %s' % (addon_id, version))
    readme = readme.replace('%s-%s.zip' % (addon_id, old), '%s-%s.zip' % (addon_id, version))
    write(readme_path, readme)
    ast.parse(open(os.path.join(src, 'service.py'), encoding='utf-8').read())

    files = ['README.md', 'addon.xml', 'icon.png', 'service.py']
    res = os.path.join(src, 'resources')
    for base, dirs, names in os.walk(res):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__pycache__']
        for n in sorted(names):
            if not n.startswith('.'):
                files.append(os.path.relpath(os.path.join(base, n), src).replace(os.sep, '/'))
    zdir = os.path.join(REPO, 'zips', addon_id)
    os.makedirs(zdir, exist_ok=True)
    zpath = os.path.join(zdir, '%s-%s.zip' % (addon_id, version))
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as z:
        for f in files:
            z.write(os.path.join(src, f), addon_id + '/' + f)
    open(zpath, 'wb').write(buf.getvalue())
    with zipfile.ZipFile(zpath) as z:
        assert z.testzip() is None
        ast.parse(z.read(addon_id + '/service.py').decode('utf-8'))

    xml_path = os.path.join(REPO, 'addons.xml')
    xml_text, nl = read(xml_path)
    entry = re.search(r'<addon id="%s".*?</addon>' % re.escape(addon_id), ax, re.S).group(0)
    entry = entry.replace('\r\n', '\n').replace('\n', nl)
    pattern = re.compile(r'<addon id="%s".*?</addon>' % re.escape(addon_id), re.S)
    assert len(pattern.findall(xml_text)) == 1
    xml_text = pattern.sub(lambda _: entry, xml_text)
    write(xml_path, xml_text)
    minidom.parse(xml_path)
    open(os.path.join(REPO, 'addons.xml.md5'), 'w', newline='').write(hashlib.md5(open(xml_path, 'rb').read()).hexdigest())

    table_path = os.path.join(REPO, 'README.md')
    table, _ = read(table_path)
    row = [l for l in table.splitlines() if ('/' + folder + ')') in l]
    if len(row) == 1 and ('| %s |' % old) in row[0]:
        write(table_path, table.replace(row[0], row[0].replace('| %s |' % old, '| %s |' % version)))
    else:
        print('NOTE: README table row for %s not updated, check it by hand' % folder)

    print('%s %s -> %s: %s' % (addon_id, old, version, os.path.relpath(zpath, REPO)))
    for f in sorted(os.listdir(zdir)):
        if f.endswith('.zip') and f != os.path.basename(zpath):
            print('  old zip to remove: git -C %s rm zips/%s/%s' % (os.path.basename(REPO), addon_id, f))

if __name__ == '__main__':
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    main(sys.argv[1], sys.argv[2])
