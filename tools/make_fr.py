"""Build the French main page (fr/index.html) from index.html.
The English keys come from make_es.T / make_es.TS (same order); only the French side lives here.
Usage: python3 tools/make_es.py && python3 tools/make_fr.py && python3 tools/make_pages.py"""
import os, sys
sys.path.insert(0, os.path.dirname(__file__))
import make_es

GAME_FR = ("<script>window.GAME_TXT={steel:'acier inoxydable 304',layer:'région endommagée',hidden:'dommage : caché quelque part',"
  "start:'Appuie sur l’échantillon, tire vers l’arrière pour charger, vise la région orange et relâche.',"
  "trapped:' % des positrons piégés dans le dommage (',best:' % du meilleur possible). ',bull:'🎯 En plein dans le mille ! ',"
  "deep:'Trop profond : tire moins.',shallow:'Trop en surface : tire plus.',high:'Vise plus bas.',low:'Vise plus haut.',"
  "next:' Niveau suivant : une région plus petite.',out:' Plus de tirs. Niveau suivant.',"
  "lvlHidden:' : le dommage est caché. Utilise les impacts dorés pour le trouver.',lvl:' : région plus petite, même canon.',level:'Niveau ',"
  "r1:'Niveau expert en positrons ! Une place dans notre labo ?',r2:'Belle maîtrise du faisceau : au labo !',"
  "r3:'Pas mal ! Les vrais échantillons sont plus difficiles.',r4:'Continue à régler ce faisceau.',final:' Score final : ',"
  "again:'Rejouer',fire:'Tirer',pull:'tire vers l’arrière'};</script>\n")

FR = [
'<html lang="fr">',  # 0
'content="Alejandra Acosta, physicienne des positrons et des matériaux nucléaires, chercheuse en maîtrise (MASc) en génie physique à l’Université McMaster : spectroscopie d’annihilation de positrons et dommages d’irradiation dans les matériaux pour réacteurs."',
'<meta property="og:url" content="https://alejandraacostap.github.io/fr/">',
'content="Alejandra Acosta · Physicienne des positrons et des matériaux nucléaires"',
'content="Chercheuse en maîtrise à l’Université McMaster : dommages d’irradiation, spectroscopie d’annihilation de positrons (PAS/PALS), Python et Geant4."',
'<meta property="og:type" content="website">\n<meta property="og:locale" content="fr_CA">',  # 5
'aria-label="Sections"',
'<li class="langs"><a class="lang" href="../" hreflang="en" lang="en">EN</a> <a class="lang" href="../es/" hreflang="es" lang="es">ES</a></li>',
'<a href="#research">Recherche</a>',
'<a href="#path">Parcours</a>',
'<a href="#experience">Expérience</a>',  # 10
'<a href="#projects">Projets</a>',
'<a href="#talks">Exposés</a>',
'<a href="#play">Jeu</a>',
'<a href="#contact">Contact</a>',
'<a href="etudiants/">Étudiants</a>',  # 15
'Bonjour, je suis physicienne des positrons et des matériaux nucléaires 👋',
'alt="Portrait d’Alejandra Acosta"',
'src="../images/',
'Physicienne et chercheuse en maîtrise (MASc) en génie physique<br>Université McMaster, Hamilton, Canada',
'J’utilise la spectroscopie d’annihilation de positrons pour mesurer les défauts que l’irradiation laisse dans des matériaux candidats pour les petits réacteurs modulaires et les réacteurs de génération IV.',  # 20
'>Écrivez-moi<',
'Un électron et un positron s’approchent, s’annihilent et produisent deux photons gamma de 511 keV qui partent dans des directions opposées.',
'Un positron rencontre un électron et tous deux se transforment en deux photons. Mesurer cet instant me dit où il manque des atomes.',
'>Annihiler encore<',
'Trois faits sur les positrons que j’adore',  # 25
'La durée de vie d’un positron dans du fer parfait. Dans une lacune il vit plus longtemps, et c’est ainsi que l’on voit les dommages.',
'L’énergie de chaque photon d’annihilation : exactement l’énergie de masse de l’électron, E = mc².',
'La durée de vie de l’ortho-positronium dans le vide, un « atome » formé d’un électron et de son antiparticule.',
'<br>Recherche</h2>',
'Mes travaux de maîtrise, sous la direction du Prof. Peter Mascher au Département de génie physique, portent sur les dommages d’irradiation dans des matériaux structuraux candidats pour les petits réacteurs modulaires (PRM) et les réacteurs de génération IV. Cette recherche est financée par le CRSNG et la Commission canadienne de sûreté nucléaire (CCSN) dans le cadre du programme Alliance CCSN-PRM.',  # 30
'<h3>Matériaux candidats pour réacteurs</h3>',
'Sélection et présélection d’alliages structuraux candidats pour des études d’irradiation, avec des simulations Geant4 et SRIM des atomes primaires de recul, des déplacements et des déplacements par atome (dpa) en parallèle des mesures.',
'<h3>Spectroscopie d’annihilation de positrons</h3>',
'Mesure des défauts induits par l’irradiation par élargissement Doppler (PAS) et spectroscopie de durée de vie des positrons (PALS), analyse des données en Python et construction de notre spectromètre de durée de vie des positrons.',
'Un spectre de durée de vie des positrons en échelle logarithmique : un pic net suivi de droites de décroissance dont les pentes donnent les durées de vie des positrons.',  # 35
'>temps (ns)<',
'>comptes (log)<',
'Ce que je mesure : un spectre de durée de vie des positrons. Chaque pente correspond à une durée de vie ; les positrons piégés dans les lacunes vivent plus longtemps, donc les dommages apparaissent comme une queue plus lente.',
'>Au laboratoire<',
'Élargissement Doppler à énergie variable (faisceau de positrons lents)',  # 40
'Spectroscopie de durée de vie des positrons (PALS) : construction des bases de détecteurs et du porte-échantillon',
'<li>Préparation de sources de positrons Na-22</li>',
'Études de dommages par implantation d’ions hélium',
'Préparation d’échantillons : découpe, montage et polissage',
'Microscopie électronique à balayage : utilisatrice autorisée au Centre canadien de microscopie électronique',  # 45
'Formation en radioprotection et manipulation de matières radioactives',
'<b>Outils :</b>',
'<br>Mon parcours</h2>',
'J’ai grandi à Soacha, en Colombie, et j’ai fréquenté une école publique, l’Institución Educativa San Mateo, où j’ai été présidente du conseil des élèves en dernière année. Je suis la première de ma famille à aller à l’université.',
'J’ai commencé en sociologie à l’Universidad Nacional de Colombia, puis je suis passée à la physique et j’ai appris l’anglais en chemin. En 2023, un stage Mitacs Globalink m’a amenée pour la première fois à McMaster, pour apprendre la spectroscopie d’annihilation de positrons.',  # 50
'En 2025, je suis revenue comme boursière ELAP avec mon propre projet : utiliser les positrons pour étudier les dommages d’irradiation dans les aciers de réacteurs. Ce projet a ouvert une nouvelle ligne de recherche dans notre groupe, est devenu mon mémoire de licence et m’a menée à NuMat 2026 à Halifax. Aujourd’hui, je poursuis ce travail en maîtrise.',
'<span>Institución Educativa San Mateo (école publique) · présidente du conseil des élèves</span>',
'<span>Sociologie → Physique</span>',
'<span>Premiers positrons</span>',
'<span>Mon propre projet</span>',  # 55
'>Vous êtes étudiant ou étudiante et voulez tenter un parcours semblable ? Commencez ici →<',
'<li><a href="jouer/">Jeu</a></li>',
'y compris le <a href="jouer/">jeu du faisceau de positrons</a>',
'<br>Jeu</h2>',
'<h3>Saurez-vous trouver les dommages d’irradiation ?</h3>',  # 60
'Tirez mon canon à positrons vers l’arrière, visez et tirez dans un échantillon d’acier, avec la vraie physique d’implantation que j’utilise au laboratoire. Cinq niveaux.',
'<a class="primary" href="jouer/">Jouer →</a>',
'<h3>Écrire sur la science et ses questions sociales</h3>',
'Ce que la science et l’ingénierie peuvent faire pour les gens, surtout en Colombie, à commencer par mon essai sur les scientifiques, les ingénieurs et l’accord de paix.',
'<a class="primary" href="ecrits/">Lire mes écrits →</a>',  # 65
'NuMat 2026, Halifax : mon affiche, mon badge et l’attestation de présentation. Cliquez pour agrandir.',
'href="../images/numat2026.jpg"',
'<br>Expérience</h2>',
'>Recherche et enseignement<',
'2026 – aujourd’hui',  # 70
'<h3>Chercheuse aux cycles supérieurs (MASc)</h3>',
'Université McMaster, génie physique',
'Je mesure les défauts induits par l’irradiation dans des matériaux candidats pour les PRM et les réacteurs de génération IV par spectroscopie d’annihilation de positrons (PAS/PALS), j’analyse les données en Python et je les compare à des simulations de dommages Geant4 et SRIM. J’ai formé une stagiaire de recherche Mitacs Globalink pendant 10 semaines. Financement : CRSNG et CCSN.',
'<h3>Assistante d’enseignement</h3>',
'J’anime des tutoriels, je tiens des heures de bureau et je corrige les travaux et examens de 170 étudiants de premier cycle en génie physique.',  # 75
'août – déc. 2025',
'<h3>Étudiante chercheuse, boursière ELAP</h3>',
'J’ai introduit des dommages de déplacement dans l’acier inoxydable 304 par implantation d’ions hélium de 50 keV à plusieurs fluences ; j’ai établi un profil de défauts en profondeur par élargissement Doppler à énergie variable (paramètres S et W) ; j’ai comparé les mesures à des simulations SRIM et Geant4. Ce travail est devenu mon mémoire de licence.',
'mai – août 2023',
'<h3>Stagiaire de recherche Mitacs</h3>',  # 80
'Université McMaster, Groupe d’annihilation de positrons',
'Spectroscopie d’annihilation de positrons de structures en couches minces : montage expérimental, mesures et analyse des données ; présentation des résultats lors de séances d’affiches.',
'août – déc. 2022',
'<h3>Étudiante chercheuse</h3>',
'Universidad Nacional de Colombia, Groupe de recherche nucléaire',  # 85
'Simulation Monte Carlo de la désintégration radioactive en Python, avec analyse statistique de mesures nucléaires.',
'Universidad Nacional de Colombia, Groupe d’optique appliquée',
'Conception d’un montage expérimental pour mesurer les états de polarisation et la photoélasticité de matériaux, et analyse des données.',
'>Industrie<',
'mai 2024 – août 2025',  # 90
'<h3>Mentore et associée au soutien des livraisons (SDS)</h3>',
'J’ai créé un assistant IA interne, basé sur Claude, utilisé par plus de 100 associés pour trouver les procédures ; j’ai dirigé l’intégration des nouveaux employés et des ateliers de formation ; j’ai offert un soutien bilingue aux opérations aux États-Unis et au Mexique.',
'<br>Projets</h2>',
'<h3>Assistant de connaissances IA</h3>',
'Création d’un chatbot interne sur Claude (LLM d’Anthropic) que plus de 100 associés ont utilisé pour trouver les procédures plus rapidement.',  # 95
'LLM · Claude · outils de connaissances',
'Recherche · 2025 – aujourd’hui',
'<h3>Analyse de données de positrons en Python</h3>',
'Chaînes de traitement pour traiter, ajuster et interpréter les spectres d’élargissement Doppler et de durée de vie, et les comparer à des simulations de dommages SRIM et Geant4.',
'<h3>Architecture infonuagique pour une entreprise de livraison</h3>',  # 100
'Suivi de colis en temps réel à haute disponibilité : CloudFront et Route 53, un équilibreur de charge avec EC2 Auto Scaling, des mises à jour événementielles avec Lambda et SNS/SQS, IAM à moindre privilège et alarmes CloudWatch.',
'<h3>Analyse des ventes et des stocks</h3>',
'Tableau de bord interactif sur un modèle relationnel avec des indicateurs de revenus et de rentabilité ; données nettoyées avec Power Query, tâches automatisées avec VBA, ventes optimisées avec Solver.',
'Ce site web · 2026',
'<h3>Portfolio fait main avec un jeu de positrons</h3>',  # 105
'HTML, CSS et JavaScript purs sur GitHub Pages, ',
', qui utilise le vrai profil d’implantation de Makhov pour l’acier.',
'>code source sur GitHub<',
'<br>Formation</h2>',
'MASc, génie physique, Université McMaster, Canada (fin prévue en mai 2028). Directeur : Prof. Peter Mascher.',  # 110
'Licence (BSc) en physique, Universidad Nacional de Colombia. Mémoire :',
'. Directeurs : Prof. Carlos Eduardo Sandoval et Prof. Peter Mascher.',
'<br>Présentations</h2>',
'>Présentations<',
'>sept. 2026<',  # 115
'Affiche, NuMat 2026 : The Nuclear Materials Conference (Elsevier), Halifax, Canada',
'<h3>Montage du dispositif PALS : bases de détecteurs et porte-échantillon</h3>',
'Présentation au groupe de recherche, Université McMaster',
'<h3>Préparation de sources Na-22</h3>',
'Affiche de recherche : identification de défauts dans les matériaux par spectrométrie d’annihilation de positrons',  # 120
'Séance d’affiches des stages Mitacs, Université McMaster',
'alt="Collage de NuMat 2026 : Alejandra à côté de son affiche, son badge de conférence à Halifax et son attestation de présentation d’Elsevier."',
'NuMat 2026, Halifax : mon affiche, mon badge et l’attestation de présentation.',
'<br>Science et société</h2>',
'Je m’intéresse à ce que la science et l’ingénierie apportent aux gens qui les entourent, surtout en Colombie. À l’Universidad Nacional, j’ai écrit un essai de cours sur la façon dont les scientifiques et les ingénieurs peuvent soutenir l’accord de paix du pays, et je continue d’écrire sur la science et ses questions sociales.',  # 125
'Je soutiens que les facultés de sciences et d’ingénierie de l’Universidad Nacional doivent jouer un rôle actif dans l’après-accord : ouvrir des espaces de débat entre science, technologie et société, et développer des technologies adaptées aux besoins locaux, afin que le savoir améliore les conditions matérielles de vie des gens. Comprend un entretien que j’ai réalisé avec le Prof. C. A. Hernández.',
' · titre original : <i>¿Están los científicos e ingenieros contribuyendo al posacuerdo?</i>',
'<h3>Les scientifiques et les ingénieurs contribuent-ils à l’accord de paix en Colombie ?</h3>',
'>Lire l’essai (PDF, en espagnol)<',
'href="../docs/',  # 130
'Essai de cours, Universidad Nacional de Colombia',
'<br>Prix et certifications</h2>',
'Recherche aux cycles supérieurs financée par le CRSNG et la CCSN (programme Alliance CCSN-PRM)',
'Bourse du Programme des futurs leaders dans les Amériques (PFLA/ELAP), gouvernement du Canada',
'Stage de recherche Mitacs Globalink',  # 135
'Excel avancé et Power BI',
'<dt>Vulgarisation</dt>',
'Letras a la Ciencia : communication scientifique et médiation de la lecture (12 h)',
'<dt>Langues</dt>',
'Espagnol (langue maternelle), anglais (C1, IELTS Academic 7.0), français (intermédiaire)',  # 140
'<br>Jeu : trouvez les dommages</h2>',
'C’est ainsi que je trouve les dommages d’irradiation au laboratoire. Prenez le canon à positrons : appuyez sur l’échantillon, <b>tirez vers l’arrière</b> (glissez vers la gauche) pour le charger, déplacez vers le haut ou le bas pour <b>viser</b>, et <b>relâchez</b> pour tirer. Plus vous tirez, plus l’énergie du faisceau est élevée et plus les positrons vont loin. Les positrons qui s’arrêtent dans la région endommagée sont piégés dans ses lacunes et s’allument. À partir du niveau 4, les dommages sont cachés, comme dans un vrai échantillon.',
'<span>Niveau <b id="g-level">',
'<span>Tirs restants <b',
'<span>Score <b',  # 145
'aria-label="Coupe d’un échantillon d’acier avec une région endommagée. Un canon à positrons à gauche tire des positrons qui s’arrêtent à une profondeur fixée par l’énergie du faisceau."',
'Énergie <b id="g-e">',
'<span>· profondeur <b',
'class="fire-btn">Tirer</button>',
'<label for="g-aim">Viser</label>',  # 150
'>Appuyez sur l’échantillon, tirez vers l’arrière pour charger, visez la région orange et relâchez.<',
'Vraie physique : les positrons d’un faisceau d’énergie',
's’arrêtent à une profondeur moyenne',
'nm (profil de Makhov, ρ = 7,9 g/cm³ pour l’acier), avec une large dispersion autour. C’est pourquoi aucun tir ne peut piéger 100 % : votre score compare chaque tir à la meilleure énergie possible.',
None,  # 155: game script, built below
'<br>Contact</h2>',
'Je suis toujours heureuse de parler de positrons, de dommages d’irradiation et de matériaux nucléaires, ou de commencer une collaboration.',
'Je remercie mes parents et mon frère ; l’éducation publique colombienne, de mes enseignants de l’Institución Educativa San Mateo à l’Universidad Nacional de Colombia ; ainsi que le Prof. Peter Mascher, le Groupe d’annihilation de positrons de l’Université McMaster et mes collaborateurs pour leur soutien.',
'aria-label="Tirer un positron sur le détecteur de visiteurs"',
'Détecteur de visiteurs · comptage',  # 160
'événements d’annihilation enregistrés (des visiteurs, pas des positrons : aucun rayon gamma n’a été émis)',
'Cliquez sur le détecteur pour tirer un positron ⚡',
"'Positron tiré. Il s’est annihilé. Deux photons de 511 keV, zéro visiteur de plus.'",
"'Encore un ! Vos clics ne comptent pas, seules les vraies visites comptent.'",
"'Vous faites maintenant officiellement de la spectroscopie de positrons.'",  # 165
"'Attention, à ce rythme il vous faudra une formation en radioprotection.'",
"'Celui-là a été piégé dans une lacune et a vécu un peu plus longtemps.'",
"'Positrons tirés : '",
"'. Votre détecteur obtient de bonnes statistiques.'",
# map of Colombia
'Carte de la Colombie avec un repère sur Soacha, à côté de Bogotá, au centre du pays.',  # 170
'>Mer des Caraïbes<',
'>Océan Pacifique<',
'>BRÉSIL<',
'>PÉROU<',
'>PANAMA<',  # 175
'>à côté de Bogotá<',
'>ÉQUATEUR<',
'>COLOMBIE<',
'<b>Soacha, Cundinamarca.</b> C’est là que j’ai grandi, juste au sud-ouest de Bogotá, sur le haut plateau andin à 2\u00a0600\u00a0m.',
]

FS = [
'<br>Pour les étudiants</h2>',
'Si vous étudiez dans une école ou une université publique en Colombie, ou ailleurs en Amérique latine, et que la recherche à l’étranger vous semble hors de portée : cette section est pour vous. Je suis passée par là, moi aussi.',
'<h3>Ce que j’aurais aimé savoir</h3>',
'<b>Pas besoin d’un anglais parfait pour commencer.</b> J’ai appris l’anglais à l’université et je l’ai amélioré en le pratiquant.',
'<b>Il n’est jamais trop tard pour changer de voie.</b> J’ai commencé en sociologie avant la physique, et ces années comptent aussi.',
'<b>Une occasion en ouvre une autre.</b> Un stage de 12 semaines a mené à une bourse, puis à mon mémoire, à une conférence et à une maîtrise.',
'<b>S’engager pour sa communauté compte.</b> Présider le conseil des élèves de mon école m’a appris autant que n’importe quel cours.',
'<h3>Les programmes qui m’ont amenée au Canada</h3>',
'Un stage de recherche rémunéré de 12 semaines auprès d’un professeur d’une université canadienne, pour les étudiants de premier cycle de pays partenaires, dont la Colombie (seules certaines universités sont admissibles). La candidature se fait au second semestre (pour 2027, la date limite était le 16 septembre 2026) et les stages ont lieu entre mai et octobre. Il faut une lettre de recommandation d’un professeur.',
'Une bourse du gouvernement du Canada pour les étudiants d’Amérique latine et des Caraïbes, dont la Colombie, pour un court séjour d’études ou de recherche au Canada, au premier cycle, à la maîtrise ou au doctorat. C’est l’université canadienne qui présente la demande pour vous : il vous faut donc un hôte sur place, soit une entente d’échange avec votre université, soit, pour la recherche, un professeur qui vous invite. À McMaster, la date limite est en mars.',
'<b>Programme des futurs leaders dans les Amériques (PFLA/ELAP).</b>',
'>Page officielle<',
'Les dates et les règles changent chaque année : consultez toujours les pages officielles et renseignez-vous auprès du bureau des relations internationales de votre université.',
'<b>Écrivez-moi.</b> Si vous êtes étudiant ou étudiante et voulez tenter ce parcours, envoyez-moi un courriel avec l’objet « Estudiante ». Je réponds dès que possible, en espagnol ou en anglais.',
]

NBSP = ' '
def fix(t):  # French spacing before high punctuation, outside tags only
    import re
    def txt(x): return re.sub(r' ([:;?!»])', NBSP + r'\1', x.replace('« ', '«' + NBSP))
    return ''.join(p if p.startswith('<') else txt(p) for p in re.split(r'(<[^>]*>)', t))

assert len(FR) == len(make_es.T), (len(FR), len(make_es.T))
assert len(FS) == len(make_es.TS), (len(FS), len(make_es.TS))
STRUCT = {0, 2, 5, 7, 15, 18, 57, 58, 62, 65, 67, 130, 155}
T = []
for i, ((en, _), fr) in enumerate(zip(make_es.T, FR)):
    if i == 155: fr = GAME_FR + en
    elif i not in STRUCT: fr = fix(fr)
    T.append((en, fr))
TS = [(en, fix(fr)) for (en, _), fr in zip(make_es.TS, FS)]

if __name__ == '__main__':
    out = make_es.tr(make_es.s, T, strict=False)
    out = out.replace('<p class="to-students"><a href="students/">', '<p class="to-students"><a href="etudiants/">')
    os.makedirs('fr', exist_ok=True)
    open('fr/index.html', 'w').write(out)
    print('ok')
