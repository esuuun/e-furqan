import json
import re

with open('it_translations.json', 'r', encoding='utf-8') as f:
    it_data = json.load(f)

with open('nl_translations.json', 'r', encoding='utf-8') as f:
    nl_data = json.load(f)

# Italian repair rules
def clean_italian(text):
    if not text:
        return ""
    t = text
    
    # Specific word replacements with \ufffd
    word_map = {
        r'\bQuesto \ufffd\b': 'Questo è',
        r'\bQuesto\ufffd\b': 'Questo è',
        r'\bquesto \ufffd\b': 'questo è',
        r'\bquesto\ufffd\b': 'questo è',
        r'\bquello \ufffd\b': 'quello è',
        r'\bQuello \ufffd\b': 'Quello è',
        r'\bQuelli \ufffd\b': 'Quelli è',
        r'\bEssa \ufffd\b': 'Essa è',
        r'\bessa \ufffd\b': 'essa è',
        r'\bEgli \ufffd\b': 'Egli è',
        r'\begli \ufffd\b': 'egli è',
        r'\bDio \ufffd\b': 'Dio è',
        r'\bAllah \ufffd\b': 'Allah è',
        r'\bchi \ufffd\b': 'chi è',
        r'\bChi \ufffd\b': 'Chi è',
        r'\bnon \ufffd\b': 'non è',
        r'\bNon \ufffd\b': 'Non è',
        r"\bc\'\ufffd\b": "c'è",
        r"\bC\'\ufffd\b": "C'è",
        r"\bdov\'\ufffd\b": "dov'è",
        r"\bqual \ufffd\b": "qual è",
        r"\bqual\'\ufffd\b": "qual è",
        r"\bcos\'\ufffd\b": "cos'è",
        r"\bch\'\ufffd\b": "ch'è",
        r'\bci\ufffd\b': 'ciò',
        r'\bCi\ufffd\b': 'Ciò',
        r'\bn\ufffd\b': 'né',
        r'\bN\ufffd\b': 'Né',
        r'\bpi\ufffd\b': 'più',
        r'\bPi\ufffd\b': 'Più',
        r'\bgi\ufffd\b': 'già',
        r'\bGi\ufffd\b': 'Già',
        r'\bpu\ufffd\b': 'può',
        r'\bPu\ufffd\b': 'Può',
        r'\bperch\ufffd\b': 'perché',
        r'\bPerch\ufffd\b': 'Perché',
        r'\bpoich\ufffd\b': 'poiché',
        r'\bPoich\ufffd\b': 'Poiché',
        r'\baffinch\ufffd\b': 'affinché',
        r'\bAffinch\ufffd\b': 'Affinché',
        r'\bbench\ufffd\b': 'benché',
        r'\bcosicch\ufffd\b': 'cosicché',
        r'\bnonch\ufffd\b': 'nonché',
        r'\bgiacch\ufffd\b': 'giacché',
        r'\bsar\ufffd\b': 'sarà',
        r'\bSar\ufffd\b': 'Sarà',
        r'\bsaran\ufffd\b': 'saranno',
        r'\bfar\ufffd\b': 'farà',
        r'\bFar\ufffd\b': 'Farà',
        r'\bdir\ufffd\b': 'dirà',
        r'\bDir\ufffd\b': 'Dirà',
        r'\bvedr\ufffd\b': 'vedrà',
        r'\bVedr\ufffd\b': 'Vedrà',
        r'\bsapr\ufffd\b': 'saprà',
        r'\bdovr\ufffd\b': 'dovrà',
        r'\bpotr\ufffd\b': 'potrà',
        r'\bavr\ufffd\b': 'avrà',
        r'\bAvr\ufffd\b': 'Avrà',
        r'\bdar\ufffd\b': 'darà',
        r'\bverr\ufffd\b': 'verrà',
        r'\bandr\ufffd\b': 'andrà',
        r'\btoccher\ufffd\b': 'toccherà',
        r'\brisponder\ufffd\b': 'risponderà',
        r'\bguider\ufffd\b': 'guiderà',
        r'\bperdoner\ufffd\b': 'perdonerà',
        r'\bpunir\ufffd\b': 'punirà',
        r'\bgiudicher\ufffd\b': 'giudicherà',
        r'\bricorder\ufffd\b': 'ricorderà',
        r'\bcreer\ufffd\b': 'creerà',
        r'\btrover\ufffd\b': 'troverà',
        r'\blascer\ufffd\b': 'lascerà',
        r'\bmor\ufffd\b': 'morì',
        r'\bfin\ufffd\b': 'finì',
        r'\bstabil\ufffd\b': 'stabilì',
        r'\bscopr\ufffd\b': 'scoprì',
        r'\bcolp\ufffd\b': 'colpì',
        r'\bsent\ufffd\b': 'sentì',
        r'\brap\ufffd\b': 'rapì',
        r'\bfuorich\ufffd\b': 'fuorché',
        r'\bpurcch\ufffd\b': 'purché',
        r'\bpurch\ufffd\b': 'purché',
        r'\bLm\ufffd\b': 'Lam',
        r'\bMm\ufffd\b': 'Mim',
        r'\bSd\ufffd\b': 'Sad',
        r'\bQf\ufffd\b': 'Qaf',
        r'\bNn\ufffd\b': 'Nun',
        r'\bT\ufffd\b': 'Ta',
        r'\bH\ufffd\b': 'Ha',
        r'\bY\ufffd\b': 'Ya',
        r'\bSn\ufffd\b': 'Sin',
        r"\b\'Ayn\ufffd\b": 'Ayn',
        r'\bKf\ufffd\b': 'Kaf',
        r'\bR\ufffd\b': 'Ra',
        r'\bverit\ufffd\b': 'verità',
        r'\bVerit\ufffd\b': 'Verità',
        r'\brealt\ufffd\b': 'realtà',
        r'\bRealt\ufffd\b': 'Realtà',
        r'\bvitalit\ufffd\b': 'vitalità',
        r'\bumilt\ufffd\b': 'umiltà',
        r'\bfedelt\ufffd\b': 'fedeltà',
        r'\bvolont\ufffd\b': 'volontà',
        r'\bVolont\ufffd\b': 'Volontà',
        r'\beternit\ufffd\b': 'eternità',
        r'\bEternit\ufffd\b': 'Eternità',
        r'\bautorit\ufffd\b': 'autorità',
        r'\bpovert\ufffd\b': 'povertà',
        r'\bseriet\ufffd\b': 'serietà',
        r'\bsociet\ufffd\b': 'società',
        r'\bqualit\ufffd\b': 'qualità',
        r'\bquantit\ufffd\b': 'quantità',
        r'\bgenerosit\ufffd\b': 'generosità',
        r'\bmaest\ufffd\b': 'maestà',
        r'\bMaest\ufffd\b': 'Maestà',
        r'\bhostilit\ufffd\b': 'ostilità',
        r'\bprosperit\ufffd\b': 'prosperità',
        r'\bfelicit\ufffd\b': 'felicità',
        r'\bcapacit\ufffd\b': 'capacità',
        r'\bcomunit\ufffd\b': 'comunità',
        r'\bComunit\ufffd\b': 'Comunità',
        r'\bcitt\ufffd\b': 'città',
        r'\bCitt\ufffd\b': 'Città',
        r'\bdivinit\ufffd\b': 'divinità',
        r'\bDivinit\ufffd\b': 'Divinità',
        r'\bvanit\ufffd\b': 'vanità',
        r'\bunichit\ufffd\b': 'unicità',
        r'\bunit\ufffd\b': 'unità',
        r'\bUnit\ufffd\b': 'Unità',
        r'\bpurit\ufffd\b': 'purità',
        r'\bimmensit\ufffd\b': 'immensità',
        r'\bpiet\ufffd\b': 'pietà',
        r'\bPiet\ufffd\b': 'Pietà',
        r'\bnovit\ufffd\b': 'novità',
        r'\bvariet\ufffd\b': 'varietà',
        r'\bmalvagit\ufffd\b': 'malvagità',
        r'\bospitalit\ufffd\b': 'ospitalità',
        r'\biniquit\ufffd\b': 'iniquità',
        r'\bimmoralit\ufffd\b': 'immoralità',
        r'\boscurit\ufffd\b': 'oscurità',
        r'\bnecessit\ufffd\b': 'necessità',
        r'\bveridicit\ufffd\b': 'veridicità',
        r'\bfalsit\ufffd\b': 'falsità',
        r'\bchiarit\ufffd\b': 'chiarezza',
        r'\bavidit\ufffd\b': 'avidità',
        r'\bschivit\ufffd\b': 'schiavitù',
        r'\bvirt\ufffd\b': 'virtù',
        r'\bVirt\ufffd\b': 'Virtù',
        r'\btrib\ufffd\b': 'tribù',
        r'\bTrib\ufffd\b': 'Tribù',
        r'\bGes\ufffd\b': 'Gesù',
        r'\bMos\ufffd\b': 'Mosè',
        r'\bNo\ufffd\b': 'Noè'
    }
    
    for pattern, rep in word_map.items():
        t = re.sub(pattern, rep, t)
        
    # Any solitary \ufffd between words -> 'è'
    t = re.sub(r'(\s)\ufffd(\s)', r'\1è\2', t)
    # Any \ufffd at end of word -> 'à'
    t = re.sub(r'([a-zA-Z]{2,})\ufffd', r'\1à', t)
    # Remaining \ufffd -> ''
    t = t.replace('\ufffd', '')
    return t

# Dutch repair rules
def clean_dutch(text):
    if not text:
        return ""
    t = text
    
    nl_map = {
        r'\bMoettaq\ufffden\b': 'Moettaqien',
        r'\bMoettaq\ufffdn\b': 'Moettaqin',
        r'\bshalt\b': 'shalaat',
        r'\bshal\ufffdt\b': 'shalaat',
        r'\bShal\ufffdt\b': 'Shalaat',
        r'\bShalt\b': 'Shalaat',
        r'\bZak\ufffdt\b': 'Zakaat',
        r'\bzak\ufffdt\b': 'zakaat',
        r'\bv\ufffdr\b': 'vóór',
        r'\bV\ufffdr\b': 'Vóór',
        r'\bDjibr\ufffdl\b': 'Djibriel',
        r"\bM\ufffdk\'\ufffdl\b": 'Mikaïl',
        r'\bIbr\ufffdh\ufffdm\b': 'Ibrahim',
        r'\bIsm\ufffd\ufffdl\b': 'Ismaël',
        r'\bIsh\ufffdq\b': 'Ishaq',
        r"\bJa\'q\ufffdb\b": 'Ja\'qub',
        r'\bH\ufffdr\ufffdn\b': 'Harun',
        r'\bD\ufffdd\ufffd\b': 'Dawud',
        r'\bSoelaim\ufffdn\b': 'Sulaiman',
        r'\bAjj\ufffdb\b': 'Ayyub',
        r'\bJ\ufffdnoes\b': 'Yunus',
        r'\bM\ufffds\ufffd\b': 'Musa',
        r"\b\'\ufffds\ufffd\b": 'Isa',
        r'\bL\ufffdm\b': 'Lam',
        r'\bM\ufffdm\b': 'Mim',
        r'\bS\ufffdd\b': 'Sad',
        r'\bQ\ufffdf\b': 'Qaf',
        r'\bN\ufffdn\b': 'Nun',
        r'\bT\ufffd\b': 'Ta',
        r'\bH\ufffd\b': 'Ha',
        r'\bY\ufffd\b': 'Ya',
        r'\bS\ufffdn\b': 'Sin',
        r'\bK\ufffdf\b': 'Kaf',
        r'\bR\ufffd\b': 'Ra',
        r'\bKoran\b': 'Koran',
        r'\bkoran\b': 'koran',
        r"\bQoer\'\ufffdn\b": 'Qoer\'aan',
        r'\bTaur\ufffdt\b': 'Taurat',
        r'\bIndj\ufffdl\b': 'Indjiel',
        r'\bZab\ufffdr\b': 'Zaboer',
        r"\bKa\'bah\b": 'Ka\'bah'
    }
    for pattern, rep in nl_map.items():
        t = re.sub(pattern, rep, t)
        
    # Any remaining \ufffd inside word replaced by clean letters or removed
    t = re.sub(r'([a-zA-Z])\ufffd([a-zA-Z])', r'\1\2', t)
    t = t.replace('\ufffd', '')
    return t

fixed_it = {}
for k, v in it_data.items():
    fixed_it[k] = clean_italian(v)

fixed_nl = {}
for k, v in nl_data.items():
    fixed_nl[k] = clean_dutch(v)

with open('it_translations.json', 'w', encoding='utf-8') as f:
    json.dump(fixed_it, f, ensure_ascii=False, indent=2)

with open('nl_translations.json', 'w', encoding='utf-8') as f:
    json.dump(fixed_nl, f, ensure_ascii=False, indent=2)

print("Finished cleaning it_translations.json and nl_translations.json!")
print("Sample IT 1:7:", repr(fixed_it.get('1:7')))
print("Sample IT 2:2:", repr(fixed_it.get('2:2')))
print("Sample IT 2:3:", repr(fixed_it.get('2:3')))
print("Sample IT 2:6:", repr(fixed_it.get('2:6')))
print("Sample NL 2:2:", repr(fixed_nl.get('2:2')))
print("Sample NL 2:3:", repr(fixed_nl.get('2:3')))
print("Sample NL 2:4:", repr(fixed_nl.get('2:4')))
