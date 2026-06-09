from pathlib import Path
root = Path('.')
for p in root.glob('*.html'):
    text = p.read_text(encoding='utf-8')
    new = text.replace('src="/images/', 'src="images/')
    new = new.replace('href="/images/', 'href="images/')
    if new != text:
        p.write_text(new, encoding='utf-8')
for p in root.joinpath('blog').glob('*.html'):
    text = p.read_text(encoding='utf-8')
    new = text.replace('src="/images/', 'src="../images/')
    new = new.replace('href="/images/', 'href="../images/')
    if new != text:
        p.write_text(new, encoding='utf-8')
for p in root.glob('*.css'):
    text = p.read_text(encoding='utf-8')
    new = text.replace('url("/images/', 'url("images/')
    new = new.replace("url('/images/", "url('images/")
    if new != text:
        p.write_text(new, encoding='utf-8')
print('updated')
