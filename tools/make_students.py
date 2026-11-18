"""Build the standalone students pages (students/ and es/estudiantes/) from the main pages.
Run after tools/make_es.py:  python3 tools/make_students.py"""
import re, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import make_es

URL = 'https://alejandraacostap.github.io/'
section = open('tools/students_section.html').read().replace('<br>For students</h2>', '<br>Guide</h2>')
INTRO = '''<div class="hero page-hero">
  <div class="wrap">
    <div>
      <p class="hello"><a class="back" href="../">← Alejandra Acosta</a></p>
      <div class="name-row">
        <img class="me" src="images/alejandra.jpg" width="480" height="480" alt="Portrait of Alejandra Acosta">
        <h1>For students</h1>
      </div>
      <p class="lede">From a public school in Soacha to nuclear materials research in Canada: what I learned, the programs that helped me, and how to reach me.</p>
    </div>
  </div>
</div>

'''
TI = [  # Spanish for the intro and head of this page
    ('<h1>For students</h1>', '<h1>Para estudiantes</h1>'),
    ('From a public school in Soacha to nuclear materials research in Canada: what I learned, the programs that helped me, and how to reach me.',
     'De un colegio público en Soacha a la investigación en materiales nucleares en Canadá: lo que aprendí, los programas que me ayudaron y cómo escribirme.'),
    ('alt="Portrait of Alejandra Acosta"', 'alt="Retrato de Alejandra Acosta"'),
]

def build(page, body_section, img_prefix, home, self_url, other_url, title, desc, lang_href_old, lang_href_new, students_href):
    s = page
    s = re.sub(r'<div class="hero">.*?<main>', lambda m: '__INTRO__<main>', s, count=1, flags=re.S)
    s = re.sub(r'<main>.*?</main>', lambda m: '<main>\n' + body_section + '</main>', s, count=1, flags=re.S)
    s = s.replace('__INTRO__', INTRO_CUR)
    s = re.sub(r'<title>.*?</title>', '<title>' + title + '</title>', s, count=1)
    s = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="' + desc + '">', s, count=1)
    s = re.sub(r'<meta property="og:title" content="[^"]*">', '<meta property="og:title" content="' + title + '">', s, count=1)
    s = re.sub(r'<meta property="og:url" content="[^"]*">', '<meta property="og:url" content="' + URL + self_url + '">', s, count=1)
    s = re.sub(r'<link rel="alternate" hreflang="en" href="[^"]*">', '<link rel="alternate" hreflang="en" href="' + URL + 'students/">', s)
    s = re.sub(r'<link rel="alternate" hreflang="es" href="[^"]*">', '<link rel="alternate" hreflang="es" href="' + URL + 'es/estudiantes/">', s)
    s = re.sub(r'src="(?:\.\./)?images/', 'src="' + img_prefix + 'images/', s)
    s = re.sub(r'href="#(\w+)"', r'href="../#\1"', s)
    s = s.replace('<a class="mark" href="#">', '<a class="mark" href="../">')
    s = s.replace('href="' + students_href + '"', 'href="./"')
    s = s.replace('<a class="lang" href="' + lang_href_old + '"', '<a class="lang" href="' + lang_href_new + '"')
    return s

# English page
INTRO_CUR = INTRO
en = build(open('index.html').read(), section, '../', '../', 'students/', 'es/estudiantes/',
           'For students · Alejandra Acosta',
           'For students from public schools and universities in Colombia and Latin America: how Alejandra Acosta got from Soacha to research in Canada, and the programs that helped.',
           'es/', '../es/estudiantes/', 'students/')
os.makedirs('students', exist_ok=True); open('students/index.html', 'w').write(en)

# Spanish page
sec_es = make_es.tr(make_es.tr(section.replace('<br>Guide</h2>', '<br>For students</h2>'), make_es.TS), make_es.T, strict=False).replace('<br>Para estudiantes</h2>', '<br>Guía</h2>')
INTRO_CUR = make_es.tr(INTRO, TI)
es = build(open('es/index.html').read(), sec_es, '../../', '../', 'es/estudiantes/', 'students/',
           'Para estudiantes · Alejandra Acosta',
           'Para estudiantes de colegios y universidades públicas en Colombia y América Latina: cómo Alejandra Acosta llegó de Soacha a la investigación en Canadá y los programas que le ayudaron.',
           '../', '../../students/', 'estudiantes/')
os.makedirs('es/estudiantes', exist_ok=True); open('es/estudiantes/index.html', 'w').write(es)
print('students pages ok')
