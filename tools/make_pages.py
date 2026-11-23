"""Build the sub-pages (students, play, writing, in English, Spanish and French) from the main pages.
Usage: python3 tools/make_es.py && python3 tools/make_fr.py && python3 tools/make_pages.py"""
import re, os, sys
sys.path.insert(0, os.path.dirname(__file__))
import make_es, make_fr

URL = 'https://alejandraacostap.github.io/'

PAGES = [
  dict(section='students', en='students', es='estudiantes', fr='etudiants',
       h1=('For students', 'Para estudiantes', 'Pour les étudiants'),
       lede=('From a public school in Soacha to nuclear materials research in Canada: what I learned, the programs that helped me, and how to reach me.',
             'De un colegio público en Soacha a la investigación en materiales nucleares en Canadá: lo que aprendí, los programas que me ayudaron y cómo escribirme.',
             'D’une école publique de Soacha à la recherche sur les matériaux nucléaires au Canada\u00a0: ce que j’ai appris, les programmes qui m’ont aidée et comment m’écrire.'),
       desc=('For students from public schools and universities in Colombia and Latin America: how Alejandra Acosta got from Soacha to research in Canada, and the programs that helped.',
             'Para estudiantes de colegios y universidades públicas en Colombia y América Latina: cómo Alejandra Acosta llegó de Soacha a la investigación en Canadá y los programas que le ayudaron.',
             'Pour les étudiants des écoles et universités publiques de Colombie et d’Amérique latine : comment Alejandra Acosta est passée de Soacha à la recherche au Canada, et les programmes qui l’ont aidée.'),
       extra=make_es.TS, extra_fr=make_fr.TS),
  dict(section='play', en='play', es='juega', fr='jouer',
       h1=('Find the damage', 'Encuentra el daño', 'Trouvez les dommages'),
       lede=('A game built on my research: tune a positron beam to find radiation damage hidden inside a steel sample.',
             'Un juego basado en mi investigación: ajusta un haz de positrones para encontrar el daño por radiación escondido dentro de una muestra de acero.',
             'Un jeu basé sur ma recherche\u00a0: réglez un faisceau de positrons pour trouver les dommages d’irradiation cachés dans un échantillon d’acier.'),
       desc=('Play a positron beam game based on real implantation physics: find the radiation damage hidden in a steel sample.',
             'Juega con un haz de positrones basado en física real: encuentra el daño por radiación escondido en una muestra de acero.',
             'Jouez avec un faisceau de positrons basé sur la vraie physique : trouvez les dommages d’irradiation cachés dans un échantillon d’acier.'),
       extra=[], extra_fr=[]),
  dict(section='society', en='writing', es='escritos', fr='ecrits',
       h1=('Science and society', 'Ciencia y sociedad', 'Science et société'),
       lede=('Essays and opinion on what science and engineering can do for people, especially in Colombia.',
             'Ensayos y opinión sobre lo que la ciencia y la ingeniería pueden hacer por la gente, especialmente en Colombia.',
             'Essais et tribunes sur ce que la science et l’ingénierie peuvent faire pour les gens, surtout en Colombie.'),
       desc=('Writing by Alejandra Acosta on science, engineering and society in Colombia.',
             'Escritos de Alejandra Acosta sobre ciencia, ingeniería y sociedad en Colombia.',
             'Écrits d’Alejandra Acosta sur la science, l’ingénierie et la société en Colombie.'),
       extra=[], extra_fr=[]),
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

def build(page, section, intro, img_prefix, self_url, title, desc, lang_links, slugs_here):
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
    for old, new in lang_links:
        s = s.replace('<a class="lang" href="' + old + '"', '<a class="lang" href="' + new + '"')
    return s

def alternates(s, P):
    for l, u in (('en', P['en'] + '/'), ('es', 'es/' + P['es'] + '/'), ('fr', 'fr/' + P['fr'] + '/')):
        s = re.sub(r'<link rel="alternate" hreflang="' + l + '" href="[^"]*">', '<link rel="alternate" hreflang="' + l + '" href="' + URL + u + '">', s)
    return s

en_main, es_main, fr_main = open('index.html').read(), open('es/index.html').read(), open('fr/index.html').read()
for P in PAGES:
    sec = open('tools/%s_section.html' % P['section']).read()
    # English
    intro = INTRO.format(alt='Portrait of Alejandra Acosta', h1=P['h1'][0], lede=P['lede'][0])
    en = build(en_main, sec, intro, '../', P['en'] + '/', P['h1'][0] + ' · Alejandra Acosta', P['desc'][0],
               [('es/', '../es/' + P['es'] + '/'), ('fr/', '../fr/' + P['fr'] + '/')], [p['en'] for p in PAGES])
    os.makedirs(P['en'], exist_ok=True); open(P['en'] + '/index.html', 'w').write(alternates(en, P))
    # Spanish
    sec_es = make_es.tr(make_es.tr(sec, P['extra'], strict=bool(P['extra'])), make_es.T, strict=False)
    intro = INTRO.format(alt='Retrato de Alejandra Acosta', h1=P['h1'][1], lede=P['lede'][1])
    es = build(es_main, sec_es, intro, '../../', 'es/' + P['es'] + '/', P['h1'][1] + ' · Alejandra Acosta', P['desc'][1],
               [('../', '../../' + P['en'] + '/'), ('../fr/', '../../fr/' + P['fr'] + '/')], [p['es'] for p in PAGES])
    os.makedirs('es/' + P['es'], exist_ok=True); open('es/' + P['es'] + '/index.html', 'w').write(alternates(es, P))
    # French
    sec_fr = make_es.tr(make_es.tr(sec, P['extra_fr'], strict=bool(P['extra_fr'])), make_fr.T, strict=False)
    intro = INTRO.format(alt='Portrait d’Alejandra Acosta', h1=P['h1'][2], lede=P['lede'][2])
    fr = build(fr_main, sec_fr, intro, '../../', 'fr/' + P['fr'] + '/', P['h1'][2] + ' · Alejandra Acosta', make_fr.fix(P['desc'][2]),
               [('../', '../../' + P['en'] + '/'), ('../es/', '../../es/' + P['es'] + '/')], [p['fr'] for p in PAGES])
    os.makedirs('fr/' + P['fr'], exist_ok=True); open('fr/' + P['fr'] + '/index.html', 'w').write(alternates(fr, P))
print('pages ok')
