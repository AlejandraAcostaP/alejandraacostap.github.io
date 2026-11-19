"""Build the sub-pages (students, play, writing, in English and Spanish) from the main pages.
Usage: python3 tools/make_es.py && python3 tools/make_pages.py"""
import re, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import make_es

URL = 'https://alejandraacostap.github.io/'

PAGES = [
  dict(section='students', en='students', es='estudiantes',
       h1=('For students', 'Para estudiantes'),
       lede=('From a public school in Soacha to nuclear materials research in Canada: what I learned, the programs that helped me, and how to reach me.',
             'De un colegio público en Soacha a la investigación en materiales nucleares en Canadá: lo que aprendí, los programas que me ayudaron y cómo escribirme.'),
       desc=('For students from public schools and universities in Colombia and Latin America: how Alejandra Acosta got from Soacha to research in Canada, and the programs that helped.',
             'Para estudiantes de colegios y universidades públicas en Colombia y América Latina: cómo Alejandra Acosta llegó de Soacha a la investigación en Canadá y los programas que le ayudaron.'),
       extra=make_es.TS),
  dict(section='play', en='play', es='juega',
       h1=('Find the damage', 'Encuentra el daño'),
       lede=('A game built on my research: tune a positron beam to find radiation damage hidden inside a steel sample.',
             'Un juego basado en mi investigación: ajusta un haz de positrones para encontrar el daño por radiación escondido dentro de una muestra de acero.'),
       desc=('Play a positron beam game based on real implantation physics: find the radiation damage hidden in a steel sample.',
             'Juega con un haz de positrones basado en física real: encuentra el daño por radiación escondido en una muestra de acero.'),
       extra=[]),
  dict(section='society', en='writing', es='escritos',
       h1=('Science and society', 'Ciencia y sociedad'),
       lede=('Essays and opinion on what science and engineering can do for people, especially in Colombia.',
             'Ensayos y opinión sobre lo que la ciencia y la ingeniería pueden hacer por la gente, especialmente en Colombia.'),
       desc=('Writing by Alejandra Acosta on science, engineering and society in Colombia.',
             'Escritos de Alejandra Acosta sobre ciencia, ingeniería y sociedad en Colombia.'),
       extra=[]),
]

INTRO = '''<div class="hero page-hero">
  <div class="wrap">
    <div>
      <p class="hello"><a class="back" href="../">← Alejandra Acosta</a></p>
      <div class="name-row">
        <img class="me" src="images/alejandra.jpg" width="480" height="480" alt="{alt}">
        <h1>{h1}</h1>
      </div>
      <p class="lede">{lede}</p>
    </div>
  </div>
</div>

'''

def build(page, section, intro, img_prefix, self_url, title, desc, lang_old, lang_new, slugs_here):
    s = re.sub(r'<div class="hero">.*?<main>', '__INTRO__<main class="page-body">', page, count=1, flags=re.S)
    s = re.sub(r'<main class="page-body">.*?</main>', lambda m: '<main class="page-body">\n' + section + '</main>', s, count=1, flags=re.S)
    s = s.replace('__INTRO__', intro)
    s = re.sub(r'<title>.*?</title>', '<title>' + title + '</title>', s, count=1)
    s = re.sub(r'<meta name="description" content="[^"]*">', '<meta name="description" content="' + desc + '">', s, count=1)
    s = re.sub(r'<meta property="og:title" content="[^"]*">', '<meta property="og:title" content="' + title + '">', s, count=1)
    s = re.sub(r'<meta property="og:url" content="[^"]*">', '<meta property="og:url" content="' + URL + self_url + '">', s, count=1)
    s = re.sub(r'src="(?:\.\./)?images/', 'src="' + img_prefix + 'images/', s)
    s = re.sub(r'href="(?:\.\./)?docs/', 'href="' + img_prefix + 'docs/', s)
    s = re.sub(r'href="#(\w+)"', r'href="../#\1"', s)
    s = s.replace('<a class="mark" href="#">', '<a class="mark" href="../">')
    for slug in slugs_here:                       # links to sibling sub-pages (same language)
        s = s.replace('href="' + slug + '/"', 'href="../' + slug + '/"')
    s = s.replace('<a class="lang" href="' + lang_old + '"', '<a class="lang" href="' + lang_new + '"')
    return s

en_main, es_main = open('index.html').read(), open('es/index.html').read()
for P in PAGES:
    sec = open('tools/%s_section.html' % P['section']).read()
    alt_en, alt_es = 'Portrait of Alejandra Acosta', 'Retrato de Alejandra Acosta'
    # English
    intro = INTRO.format(alt=alt_en, h1=P['h1'][0], lede=P['lede'][0])
    en = build(en_main, sec, intro, '../', P['en'] + '/', P['h1'][0] + ' · Alejandra Acosta', P['desc'][0],
               'es/', '../es/' + P['es'] + '/', [p['en'] for p in PAGES])
    en = re.sub(r'<link rel="alternate" hreflang="en" href="[^"]*">', '<link rel="alternate" hreflang="en" href="' + URL + P['en'] + '/">', en)
    en = re.sub(r'<link rel="alternate" hreflang="es" href="[^"]*">', '<link rel="alternate" hreflang="es" href="' + URL + 'es/' + P['es'] + '/">', en)
    os.makedirs(P['en'], exist_ok=True); open(P['en'] + '/index.html', 'w').write(en)
    # Spanish
    sec_es = make_es.tr(make_es.tr(sec, P['extra'], strict=bool(P['extra'])), make_es.T, strict=False)
    intro = INTRO.format(alt=alt_es, h1=P['h1'][1], lede=P['lede'][1])
    es = build(es_main, sec_es, intro, '../../', 'es/' + P['es'] + '/', P['h1'][1] + ' · Alejandra Acosta', P['desc'][1],
               '../', '../../' + P['en'] + '/', [p['es'] for p in PAGES])
    es = re.sub(r'<link rel="alternate" hreflang="en" href="[^"]*">', '<link rel="alternate" hreflang="en" href="' + URL + P['en'] + '/">', es)
    es = re.sub(r'<link rel="alternate" hreflang="es" href="[^"]*">', '<link rel="alternate" hreflang="es" href="' + URL + 'es/' + P['es'] + '/">', es)
    os.makedirs('es/' + P['es'], exist_ok=True); open('es/' + P['es'] + '/index.html', 'w').write(es)
print('pages ok')
