import datetime

# 오늘 날짜 형식: YYYY-MM-DD
today = datetime.date.today().strftime('%Y-%m-%d')

# 사이트맵 템플릿
sitemap_template = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://k2ohseung.github.io/</loc>
    <lastmod>{today}</lastmod>
  </url>
  <url>
    <loc>https://k2ohseung.github.io/index-ja.html</loc>
    <lastmod>{today}</lastmod>
  </url>
</urlset>'''

# sitemap.xml 파일로 저장
with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap_template)

print("✅ sitemap.xml 생성 완료!")
