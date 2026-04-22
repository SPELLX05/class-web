from pathlib import Path
html = Path(r"C:\Users\Adithyan Dillep\Downloads\protien.html")
text = html.read_text(encoding="utf-8")
old = '''<div class="hero-image">
        <img src="protien.jpg" alt="Protein powder container and fitness shaker bottle" />
      </div>'''
new = '''<div class="hero-image">
        <img src="protien.jpg" alt="Protein powder container and fitness shaker bottle" />
        <p class="image-caption">Premium whey protein powder container with a shaker bottle for convenient post-workout recovery.</p>
      </div>'''
text = text.replace(old, new)
html.write_text(text, encoding="utf-8")
css = Path(r"C:\Users\Adithyan Dillep\Downloads\styles.css")
css_text = css.read_text(encoding="utf-8")
if ".image-caption" not in css_text:
    css_text += '''
.image-caption {
  margin-top: 1rem;
  text-align: center;
  font-size: 0.9rem;
  color: #64748b;
  font-style: italic;
}
'''
css.write_text(css_text, encoding="utf-8")
print("caption added")
