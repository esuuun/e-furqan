# scratch/update_dist.py
dist_html = 'Mushaf Per Kata/quran-app/dist/index.html'
with open(dist_html, 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('href="/favicon.svg"', 'href="./favicon.svg"')
c = c.replace('src="/assets/', 'src="./assets/')
c = c.replace('href="/assets/', 'href="./assets/')

with open(dist_html, 'w', encoding='utf-8') as f:
    f.write(c)
print('Updated dist/index.html')

mushaf_root_html = '''<!DOCTYPE html>
<html lang="id">
<head>
  <meta charset="UTF-8" />
  <meta http-equiv="refresh" content="0; url=./quran-app/dist/index.html" />
  <title>Mushaf Per Kata - Pengalihan</title>
</head>
<body style="background:#0f172a; color:#f8fafc; font-family:sans-serif; text-align:center; padding:5rem 1rem;">
  <h2>Membuka Mushaf Per Kata...</h2>
  <p>Jika halaman tidak terbuka otomatis, silakan <a href="./quran-app/dist/index.html" style="color:#38bdf8;">klik di sini</a>.</p>
</body>
</html>'''

with open('Mushaf Per Kata/index.html', 'w', encoding='utf-8') as f:
    f.write(mushaf_root_html)
print('Created Mushaf Per Kata/index.html')
