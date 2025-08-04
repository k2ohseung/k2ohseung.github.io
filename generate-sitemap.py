import datetime

sitemap_template = '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://k2ohseung.github.io/jongga/</loc>
    <lastmod>{today}</lastmod>
  </url>
</urlset>'''

today = datetime.datetime.today().strftime('%Y-%m-%d')

with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap_template.format(today=today))

print("sitemap.xml 생성 완료!")
