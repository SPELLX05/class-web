from pathlib import Path
path = Path(r'C:\Users\Adithyan Dillep\Downloads\protien.html')
content = path.read_text(encoding='utf-8')
old = '''<div class="hero-image">
        <img src="https://images.unsplash.com/photo-1589987601068-92e2e0fdfdc9?auto=format&fit=crop&w=900&q=80" alt="Protein powder container and fitness shaker bottle" />
      </div>'''
new = '''<div class="hero-image gallery">
        <div class="hero-image-card">
          <img src="https://images.unsplash.com/photo-1589987601068-92e2e0fdfdc9?auto=format&fit=crop&w=900&q=80" alt="Protein powder container and fitness shaker bottle" />
        </div>
        <div class="hero-image-card">
          <img src="https://images.unsplash.com/photo-1611158041429-bb4926f2fce9?auto=format&fit=crop&w=900&q=80" alt="Shaker bottle next to a protein powder container" />
        </div>
      </div>'''
if old not in content:
    raise SystemExit('hero block not found')
content = content.replace(old, new)
path.write_text(content, encoding='utf-8')
css_path = Path(r'C:\Users\Adithyan Dillep\Downloads\styles.css')
css = css_path.read_text(encoding='utf-8')
needle = '''.hero-image img {
  border-radius: 1.75rem;
  box-shadow: 0 24px 60px rgba(15, 23, 42, 0.12);
}'''
replacement = '''.hero-image img {
  border-radius: 1.75rem;
  box-shadow: 0 24px 60px rgba(15, 23, 42, 0.12);
  width: 100%;
}

.hero-image.gallery {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 1rem;
}

.hero-image-card img {
  width: 100%;
  border-radius: 1.75rem;
  box-shadow: 0 24px 60px rgba(15, 23, 42, 0.12);
}'''
if needle not in css:
    raise SystemExit('css block not found')
css = css.replace(needle, replacement)
css_path.write_text(css, encoding='utf-8')
print('updated')
