#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate complete build_dutch_dataset.py and build_italian_dataset.py
with exact 76 Jamid keys and 52 Harf keys.
"""

import os
import sys
import json
from create_dutch_italian_datasets import (
    DUTCH_SURAHS, ITALIAN_SURAHS,
    BENTUK_KATA_NL, BENTUK_KATA_IT,
    BENTUK_HARF_NL, BENTUK_HARF_IT
)
from build_multilingual_dataset import GRAMMATICAL_METADATA
from build_harf_dataset import GRAMMATICAL_METADATA_HARF
from build_japanese_dataset import JAPANESE_GRAMMAR, JAPANESE_HARF_GRAMMAR

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Precise Dutch Translations for Jamid Mabny
NL_JAMID_MAP = {
    # 1. Dhamir
    "1. Dhamir__1a": {"arti_nl": "Hij (mannelijk enkelvoud)", "desc_nl": "Hij (3e persoon mannelijk enkelvoud losstaand nominatief voornaamwoord)", "jenis_nl": "Losstaand nominatief voornaamwoord"},
    "1. Dhamir__1b": {"arti_nl": "Zijn / hem", "desc_nl": "Zijn / hem (3e persoon mannelijk enkelvoud aangehecht voornaamwoord)", "jenis_nl": "Aangehecht voornaamwoord"},
    "1. Dhamir__1c": {"arti_nl": "Alleen hem", "desc_nl": "Alleen hem (3e persoon mannelijk enkelvoud losstaand accusatief voornaamwoord)", "jenis_nl": "Losstaand accusatief voornaamwoord"},
    "1. Dhamir__2a": {"arti_nl": "Zij beiden", "desc_nl": "Zij beiden (3e persoon tweevoud losstaand nominatief voornaamwoord)", "jenis_nl": "Losstaand nominatief voornaamwoord (tweevoud)"},
    "1. Dhamir__2b": {"arti_nl": "Hun beiden / hen beiden", "desc_nl": "Hun beiden / hen beiden (3e persoon tweevoud aangehecht voornaamwoord)", "jenis_nl": "Aangehecht voornaamwoord (tweevoud)"},
    "1. Dhamir__3a": {"arti_nl": "Zij (mannelijk meervoud)", "desc_nl": "Zij (3e persoon mannelijk meervoud losstaand nominatief voornaamwoord)", "jenis_nl": "Losstaand nominatief voornaamwoord (meervoud)"},
    "1. Dhamir__3b": {"arti_nl": "Hun / hen (mannelijk meervoud)", "desc_nl": "Hun / hen (3e persoon mannelijk meervoud aangehecht voornaamwoord)", "jenis_nl": "Aangehecht voornaamwoord (meervoud)"},
    "1. Dhamir__3c": {"arti_nl": "Alleen hen (mannelijk meervoud)", "desc_nl": "Alleen hen (3e persoon mannelijk meervoud losstaand accusatief voornaamwoord)", "jenis_nl": "Losstaand accusatief voornaamwoord (meervoud)"},
    "1. Dhamir__4a": {"arti_nl": "Zij (vrouwelijk enkelvoud)", "desc_nl": "Zij (3e persoon vrouwelijk enkelvoud losstaand nominatief voornaamwoord)", "jenis_nl": "Losstaand nominatief voornaamwoord (vrouwelijk)"},
    "1. Dhamir__4b": {"arti_nl": "Haar (vrouwelijk enkelvoud)", "desc_nl": "Haar (3e persoon vrouwelijk enkelvoud aangehecht voornaamwoord)", "jenis_nl": "Aangehecht voornaamwoord (vrouwelijk)"},
    "1. Dhamir__5a": {"arti_nl": "Zij (vrouwelijk meervoud)", "desc_nl": "Zij (3e persoon vrouwelijk meervoud losstaand nominatief voornaamwoord)", "jenis_nl": "Losstaand nominatief voornaamwoord (vrouwelijk meervoud)"},
    "1. Dhamir__5b": {"arti_nl": "Hun / hen (vrouwelijk meervoud)", "desc_nl": "Hun / hen (3e persoon vrouwelijk meervoud aangehecht voornaamwoord)", "jenis_nl": "Aangehecht voornaamwoord (vrouwelijk meervoud)"},
    "1. Dhamir__6a": {"arti_nl": "Jij / u (mannelijk enkelvoud)", "desc_nl": "Jij / u (2e persoon mannelijk enkelvoud losstaand nominatief voornaamwoord)", "jenis_nl": "Losstaand nominatief voornaamwoord"},
    "1. Dhamir__6b": {"arti_nl": "Jouw / je / jou (mannelijk enkelvoud)", "desc_nl": "Jouw / je / jou (2e persoon mannelijk enkelvoud aangehecht voornaamwoord)", "jenis_nl": "Aangehecht voornaamwoord"},
    "1. Dhamir__6c": {"arti_nl": "Alleen jou / u (mannelijk enkelvoud)", "desc_nl": "Alleen jou / u (2e persoon mannelijk enkelvoud losstaand accusatief voornaamwoord)", "jenis_nl": "Losstaand accusatief voornaamwoord"},
    "1. Dhamir__7a": {"arti_nl": "Jullie beiden", "desc_nl": "Jullie beiden (2e persoon tweevoud losstaand nominatief voornaamwoord)", "jenis_nl": "Losstaand nominatief voornaamwoord (tweevoud)"},
    "1. Dhamir__7b": {"arti_nl": "Jullie beiden (aangehecht)", "desc_nl": "Jullie beiden (2e persoon tweevoud aangehecht voornaamwoord)", "jenis_nl": "Aangehecht voornaamwoord (tweevoud)"},
    "1. Dhamir__8a": {"arti_nl": "Jullie (mannelijk meervoud)", "desc_nl": "Jullie (2e persoon mannelijk meervoud losstaand nominatief voornaamwoord)", "jenis_nl": "Losstaand nominatief voornaamwoord (meervoud)"},
    "1. Dhamir__8b": {"arti_nl": "Jullie (aangehecht mannelijk meervoud)", "desc_nl": "Jullie / uw (2e persoon mannelijk meervoud aangehecht voornaamwoord)", "jenis_nl": "Aangehecht voornaamwoord (meervoud)"},
    "1. Dhamir__8c": {"arti_nl": "Alleen jullie (mannelijk meervoud)", "desc_nl": "Alleen jullie (2e persoon mannelijk meervoud losstaand accusatief voornaamwoord)", "jenis_nl": "Losstaand accusatief voornaamwoord (meervoud)"},
    "1. Dhamir__9a": {"arti_nl": "Jij / u (vrouwelijk enkelvoud)", "desc_nl": "Jij / u (2e persoon vrouwelijk enkelvoud losstaand nominatief voornaamwoord)", "jenis_nl": "Losstaand nominatief voornaamwoord (vrouwelijk)"},
    "1. Dhamir__9b": {"arti_nl": "Jouw / je (vrouwelijk enkelvoud)", "desc_nl": "Jouw / je (2e persoon vrouwelijk enkelvoud aangehecht voornaamwoord)", "jenis_nl": "Aangehecht voornaamwoord (vrouwelijk)"},
    "1. Dhamir__10a": {"arti_nl": "Jullie (vrouwelijk meervoud)", "desc_nl": "Jullie (2e persoon vrouwelijk meervoud losstaand nominatief voornaamwoord)", "jenis_nl": "Losstaand nominatief voornaamwoord (vrouwelijk meervoud)"},
    "1. Dhamir__10b": {"arti_nl": "Jullie (aangehecht vrouwelijk meervoud)", "desc_nl": "Jullie / uw (2e persoon vrouwelijk meervoud aangehecht voornaamwoord)", "jenis_nl": "Aangehecht voornaamwoord (vrouwelijk meervoud)"},
    "1. Dhamir__11a": {"arti_nl": "Ik (1e persoon enkelvoud)", "desc_nl": "Ik (1e persoon enkelvoud losstaand nominatief voornaamwoord)", "jenis_nl": "Losstaand nominatief voornaamwoord"},
    "1. Dhamir__11b": {"arti_nl": "Mijn / mij", "desc_nl": "Mijn / mij (1e persoon enkelvoud aangehecht voornaamwoord)", "jenis_nl": "Aangehecht voornaamwoord"},
    "1. Dhamir__11c": {"arti_nl": "Alleen mij", "desc_nl": "Alleen mij (1e persoon enkelvoud losstaand accusatief voornaamwoord)", "jenis_nl": "Losstaand accusatief voornaamwoord"},
    "1. Dhamir__12a": {"arti_nl": "Wij (1e persoon meervoud)", "desc_nl": "Wij (1e persoon meervoud losstaand nominatief voornaamwoord)", "jenis_nl": "Losstaand nominatief voornaamwoord (meervoud)"},
    "1. Dhamir__12b": {"arti_nl": "Ons / onze", "desc_nl": "Ons / onze (1e persoon meervoud aangehecht voornaamwoord)", "jenis_nl": "Aangehecht voornaamwoord (meervoud)"},
    "1. Dhamir__12c": {"arti_nl": "Alleen ons", "desc_nl": "Alleen ons (1e persoon meervoud losstaand accusatief voornaamwoord)", "jenis_nl": "Losstaand accusatief voornaamwoord (meervoud)"},

    # 2. Mawshul (10 items)
    "2. Mawshul__1": {"arti_nl": "Wat / datgene wat", "desc_nl": "Algemeen betrekkelijk voornaamwoord voor niet-rationele zaken (Maa)", "jenis_nl": "Betrekkelijk voornaamwoord (niet-rationeel)"},
    "2. Mawshul__2": {"arti_nl": "Degenen die (mannelijk meervoud)", "desc_nl": "Zij die / degenen die (mannelijk meervoud betrekkelijk voornaamwoord)", "jenis_nl": "Betrekkelijk voornaamwoord (meervoud mannelijk)"},
    "2. Mawshul__3": {"arti_nl": "Wie / degene die", "desc_nl": "Algemeen betrekkelijk voornaamwoord voor rationele wezens (Man)", "jenis_nl": "Algemeen betrekkelijk voornaamwoord (rationeel)"},
    "2. Mawshul__4": {"arti_nl": "Degene die (mannelijk enkelvoud)", "desc_nl": "Degene die / dat (mannelijk enkelvoud betrekkelijk voornaamwoord)", "jenis_nl": "Betrekkelijk voornaamwoord (mannelijk enkelvoud)"},
    "2. Mawshul__5": {"arti_nl": "Welke / wie dan ook", "desc_nl": "Welke / wie van hen (verbuigbaar betrekkelijk voornaamwoord)", "jenis_nl": "Betrekkelijk voornaamwoord"},
    "2. Mawshul__6": {"arti_nl": "Zij die (vrouwelijk enkelvoud)", "desc_nl": "Zij die / datgene wat (vrouwelijk enkelvoud betrekkelijk voornaamwoord)", "jenis_nl": "Betrekkelijk voornaamwoord (vrouwelijk enkelvoud)"},
    "2. Mawshul__7": {"arti_nl": "Vrouwen die (meervoud vrouwelijk)", "desc_nl": "Zij die (vrouwelijk meervoud betrekkelijk voornaamwoord)", "jenis_nl": "Betrekkelijk voornaamwoord (meervoud vrouwelijk)"},
    "2. Mawshul__8": {"arti_nl": "Vrouwen die (meervoud vrouwelijk variant)", "desc_nl": "Zij die (vrouwelijk meervoud betrekkelijk voornaamwoord variant)", "jenis_nl": "Betrekkelijk voornaamwoord (meervoud vrouwelijk)"},
    "2. Mawshul__9": {"arti_nl": "Zij beiden die (tweevoud mannelijk)", "desc_nl": "Zij beiden die (tweevoud mannelijk betrekkelijk voornaamwoord)", "jenis_nl": "Betrekkelijk voornaamwoord (tweevoud mannelijk)"},
    "2. Mawshul__10": {"arti_nl": "Welke dan ook (vrouwelijk)", "desc_nl": "Welke dan ook (vrouwelijk betrekkelijk voornaamwoord)", "jenis_nl": "Betrekkelijk voornaamwoord (vrouwelijk)"},

    # 3. Istifham (10 items)
    "3. Istifham__1": {"arti_nl": "Wat? / Hoe?", "desc_nl": "Wat? / Hoe? (Vragend voornaamwoord voor zaken)", "jenis_nl": "Vragend voornaamwoord"},
    "3. Istifham__2": {"arti_nl": "Hoe?", "desc_nl": "Hoe? (Vragend voornaamwoord van toestand of hoedanigheid)", "jenis_nl": "Vragend voornaamwoord van toestand"},
    "3. Istifham__3": {"arti_nl": "Wie?", "desc_nl": "Wie? (Vragend voornaamwoord voor personen)", "jenis_nl": "Vragend voornaamwoord"},
    "3. Istifham__4": {"arti_nl": "Welke? / Wat?", "desc_nl": "Welke? (Vragend voornaamwoord van keuze)", "jenis_nl": "Vragend voornaamwoord van keuze"},
    "3. Istifham__5": {"arti_nl": "Hoe? / Vanwaar?", "desc_nl": "Hoe / vanwaar? (Vragend voornaamwoord van herkomst of mogelijkheid)", "jenis_nl": "Vragend voornaamwoord"},
    "3. Istifham__6": {"arti_nl": "Wat is het dat?", "desc_nl": "Wat is het dat? (Versterkt vragend voornaamwoord samengesteld met Dhaa)", "jenis_nl": "Samengesteld vragend voornaamwoord"},
    "3. Istifham__7": {"arti_nl": "Hoeveel? / Hoe lang?", "desc_nl": "Hoeveel? / Hoe lang? (Vragend voornaamwoord van aantal of duur)", "jenis_nl": "Vragend voornaamwoord van aantal"},
    "3. Istifham__8": {"arti_nl": "Waarom? / Waartoe?", "desc_nl": "Waarom? (Vraag naar reden of doel, Li + Maa)", "jenis_nl": "Vragend voornaamwoord van oorzaak"},
    "3. Istifham__9": {"arti_nl": "Waar? / Waarheen?", "desc_nl": "Waar? (Vragend voornaamwoord van plaats)", "jenis_nl": "Vragend voornaamwoord van plaats"},
    "3. Istifham__10": {"arti_nl": "Wanneer?", "desc_nl": "Wanneer? (Vragend voornaamwoord van tijd)", "jenis_nl": "Vragend voornaamwoord van tijd"},

    # 4. Syarath (5 items)
    "4. Syarath__1": {"arti_nl": "Wie ook maar / al wie", "desc_nl": "Wie ook maar (Voorwaardelijk zelfstandig naamwoord voor personen)", "jenis_nl": "Voorwaardelijk nomen (rationeel)"},
    "4. Syarath__2": {"arti_nl": "Wat ook maar / al wat", "desc_nl": "Wat ook maar (Voorwaardelijk zelfstandig naamwoord voor zaken)", "jenis_nl": "Voorwaardelijk nomen (niet-rationeel)"},
    "4. Syarath__3": {"arti_nl": "Elke keer dat / telkens wanneer", "desc_nl": "Elke keer dat (Tijdsbepalend voorwaardelijk bijwoord)", "jenis_nl": "Tijdsbepalend voorwaardelijk bijwoord"},
    "4. Syarath__4": {"arti_nl": "Welke ook maar", "desc_nl": "Welke van de twee / welke ook maar (Voorwaardelijk nomen van keuze)", "jenis_nl": "Voorwaardelijk nomen van keuze"},
    "4. Syarath__5": {"arti_nl": "Welke van beide ook (benadrukt)", "desc_nl": "Welke termijn ook (Voorwaardelijk nomen versterkt met Maa)", "jenis_nl": "Versterkt voorwaardelijk nomen"},

    # 5. Isyarah (8 items)
    "5. Isyarah__1": {"arti_nl": "Dit / dat (mannelijk enkelvoud)", "desc_nl": "Dit / dat (Aanwijzend voornaamwoord mannelijk enkelvoud dichtbij/veraf)", "jenis_nl": "Aanwijzend voornaamwoord (mannelijk enkelvoud)"},
    "5. Isyarah__2": {"arti_nl": "Dezen / genen (meervoud)", "desc_nl": "Dezen / diegenen (Aanwijzend voornaamwoord meervoud dichtbij/veraf)", "jenis_nl": "Aanwijzend voornaamwoord (meervoud)"},
    "5. Isyarah__3": {"arti_nl": "Dit / dat (vrouwelijk enkelvoud)", "desc_nl": "Dit / dat (Aanwijzend voornaamwoord vrouwelijk enkelvoud dichtbij/veraf)", "jenis_nl": "Aanwijzend voornaamwoord (vrouwelijk enkelvoud)"},
    "5. Isyarah__4": {"arti_nl": "Dat / die (vrouwelijk / meervoud)", "desc_nl": "Dat / die (Aanwijzend voornaamwoord veraf voor vrouwelijk of meervoud)", "jenis_nl": "Aanwijzend voornaamwoord veraf"},
    "5. Isyarah__5": {"arti_nl": "Hier / op deze plaats", "desc_nl": "Hier (Aanwijzend bijwoord van plaats dichtbij)", "jenis_nl": "Aanwijzend bijwoord van plaats"},
    "5. Isyarah__6": {"arti_nl": "Daar / aldaar", "desc_nl": "Daar (Aanwijzend bijwoord van plaats veraf)", "jenis_nl": "Aanwijzend bijwoord van plaats veraf"},
    "5. Isyarah__7": {"arti_nl": "Deze twee (mannelijk tweevoud)", "desc_nl": "Deze twee (Aanwijzend voornaamwoord mannelijk tweevoud dichtbij)", "jenis_nl": "Aanwijzend voornaamwoord tweevoud"},
    "5. Isyarah__8": {"arti_nl": "Deze/die twee (vrouwelijk tweevoud)", "desc_nl": "Deze/die twee (Aanwijzend voornaamwoord vrouwelijk tweevoud)", "jenis_nl": "Aanwijzend voornaamwoord vrouwelijk tweevoud"},

    # 6. Isim Fi'il (8 items)
    "6. Isim Fi'il__1": {"arti_nl": "Heilig is / glorie zij (Glorificatie)", "desc_nl": "Heilig en verheven is Allah (Verbaal nomen van lofprijzing)", "jenis_nl": "Verbaal nomen (Lofprijzing)"},
    "6. Isim Fi'il__2": {"arti_nl": "Breng voort! / Toon aan!", "desc_nl": "Breng jullie bewijs voort (Verbaal nomen gebiedende wijs)", "jenis_nl": "Verbaal nomen (gebiedende wijs)"},
    "6. Isim Fi'il__3": {"arti_nl": "Foei! / Bah! (uitroep van ergernis)", "desc_nl": "Foei / bah (Verbaal nomen tegenwoordige tijd van afkeer)", "jenis_nl": "Verbaal nomen (afkeer)"},
    "6. Isim Fi'il__4": {"arti_nl": "Ik zoek toevlucht (Moge Allah verhoeden)", "desc_nl": "Ik zoek bescherming bij Allah (Verbaal nomen van toevlucht)", "jenis_nl": "Verbaal nomen (toevlucht)"},
    "6. Isim Fi'il__5": {"arti_nl": "Kom hier! / Breng voort!", "desc_nl": "Kom hierheen / breng voort (Verbaal nomen gebiedende wijs)", "jenis_nl": "Verbaal nomen (gebiedende wijs)"},
    "6. Isim Fi'il__6": {"arti_nl": "Verre van! / Onmogelijk!", "desc_nl": "Hoe ver weg is het! (Verbaal nomen verleden tijd)", "jenis_nl": "Verbaal nomen (verleden tijd)"},
    "6. Isim Fi'il__7": {"arti_nl": "Neem hier en lees!", "desc_nl": "Neem en lees mijn boek (Verbaal nomen gebiedende wijs)", "jenis_nl": "Verbaal nomen (gebiedende wijs)"},
    "6. Isim Fi'il__8": {"arti_nl": "Kom hier! / Haast je!", "desc_nl": "Kom tot mij / ik ben gereed (Verbaal nomen van uitnodiging)", "jenis_nl": "Verbaal nomen (uitnodiging)"},

    # 7. Fi'il Jamid (8 items)
    "7. Fi'il Jamid__1": {"arti_nl": "Is niet / zijn niet", "desc_nl": "Is niet / zijn niet (Niet-vervoegbaar werkwoord van ontkenning)", "jenis_nl": "Niet-vervoegbaar werkwoord van ontkenning"},
    "7. Fi'il Jamid__2": {"arti_nl": "Wat een slechte...", "desc_nl": "Hoe slecht is... (Niet-vervoegbaar werkwoord van afkeuring)", "jenis_nl": "Niet-vervoegbaar werkwoord van afkeuring"},
    "7. Fi'il Jamid__3": {"arti_nl": "Moge het zijn / wellicht", "desc_nl": "Moge het zijn dat / wellicht (Niet-vervoegbaar werkwoord van hoop)", "jenis_nl": "Niet-vervoegbaar werkwoord van hoop"},
    "7. Fi'il Jamid__4": {"arti_nl": "Wat een voortreffelijke...", "desc_nl": "Hoe voortreffelijk is... (Niet-vervoegbaar werkwoord van lofprijzing)", "jenis_nl": "Niet-vervoegbaar werkwoord van lofprijzing"},
    "7. Fi'il Jamid__5": {"arti_nl": "Hoe slecht is datgene wat", "desc_nl": "Hoe slecht is wat zij kochten (Niet-vervoegbaar werkwoord van afkeuring samengesteld met Maa)", "jenis_nl": "Niet-vervoegbaar werkwoord van afkeuring"},
    "7. Fi'il Jamid__6": {"arti_nl": "Zij begonnen te...", "desc_nl": "Zij begonnen bladeren over zich heen te leggen (Niet-vervoegbaar werkwoord van aanvang)", "jenis_nl": "Niet-vervoegbaar werkwoord van aanvang"},
    "7. Fi'il Jamid__7": {"arti_nl": "Allah verhoede! / Verheven is Allah", "desc_nl": "Verre zij het van Allah! (Niet-vervoegbaar werkwoord van vrijwaring)", "jenis_nl": "Niet-vervoegbaar werkwoord van vrijwaring"},
    "7. Fi'il Jamid__8": {"arti_nl": "Hoe voortreffelijk is datgene wat", "desc_nl": "Hoe voortreffelijk is waar Hij jullie toe vermaant (Niet-vervoegbaar werkwoord van lof samengesteld met Maa)", "jenis_nl": "Niet-vervoegbaar werkwoord van lofprijzing"}
}

# Duplicate aliases for "2. Isim Mawshul__X", "3. Isim Istifham__X", "4. Isim Syarath__X", "5. Isim Isyarah__X"
for k, v in list(NL_JAMID_MAP.items()):
    if k.startswith("2. Mawshul__"):
        NL_JAMID_MAP[k.replace("2. Mawshul__", "2. Isim Mawshul__")] = v
    elif k.startswith("3. Istifham__"):
        NL_JAMID_MAP[k.replace("3. Istifham__", "3. Isim Istifham__")] = v
    elif k.startswith("4. Syarath__"):
        NL_JAMID_MAP[k.replace("4. Syarath__", "4. Isim Syarath__")] = v
    elif k.startswith("5. Isyarah__"):
        NL_JAMID_MAP[k.replace("5. Isyarah__", "5. Isim Isyarah__")] = v

# Precise Italian Translations for Jamid Mabny (76 items)
IT_JAMID_MAP = {
    # 1. Dhamir (27 items)
    "1. Dhamir__1a": {"arti_it": "Egli / Lui (singolare maschile)", "desc_it": "Egli / Lui (pronome personale isolato nominativo 3a persona maschile singolare)", "jenis_it": "Pronome personale isolato nominativo"},
    "1. Dhamir__1b": {"arti_it": "Suo / lo / gli", "desc_it": "Suo / lo / gli (pronome personale suffisso 3a persona maschile singolare)", "jenis_it": "Pronome suffisso"},
    "1. Dhamir__1c": {"arti_it": "Solo Lui", "desc_it": "Solo Lui (pronome personale isolato accusativo 3a persona maschile singolare)", "jenis_it": "Pronome isolato accusativo"},
    "1. Dhamir__2a": {"arti_it": "Essi due", "desc_it": "Essi due (pronome personale isolato nominativo 3a persona duale)", "jenis_it": "Pronome isolato nominativo (duale)"},
    "1. Dhamir__2b": {"arti_it": "Di loro due / loro due", "desc_it": "Di loro due / loro due (pronome personale suffisso 3a persona duale)", "jenis_it": "Pronome suffisso (duale)"},
    "1. Dhamir__3a": {"arti_it": "Essi / Loro (plurale maschile)", "desc_it": "Essi / Loro (pronome personale isolato nominativo 3a persona maschile plurale)", "jenis_it": "Pronome isolato nominativo (plurale)"},
    "1. Dhamir__3b": {"arti_it": "Loro / li (plurale maschile)", "desc_it": "Loro / li (pronome personale suffisso 3a persona maschile plurale)", "jenis_it": "Pronome suffisso (plurale)"},
    "1. Dhamir__3c": {"arti_it": "Solo loro (plurale maschile)", "desc_it": "Solo loro (pronome personale isolato accusativo 3a persona maschile plurale)", "jenis_it": "Pronome isolato accusativo (plurale)"},
    "1. Dhamir__4a": {"arti_it": "Ella / Lei (singolare femminile)", "desc_it": "Ella / Lei (pronome personale isolato nominativo 3a persona femminile singolare)", "jenis_it": "Pronome isolato nominativo (femminile)"},
    "1. Dhamir__4b": {"arti_it": "Suo / la / le", "desc_it": "Suo / la / le (pronome personale suffisso 3a persona femminile singolare)", "jenis_it": "Pronome suffisso (femminile)"},
    "1. Dhamir__5a": {"arti_it": "Esse / Loro (plurale femminile)", "desc_it": "Esse / Loro (pronome personale isolato nominativo 3a persona femminile plurale)", "jenis_it": "Pronome isolato nominativo (femminile plurale)"},
    "1. Dhamir__5b": {"arti_it": "Loro / le (plurale femminile)", "desc_it": "Loro / le (pronome personale suffisso 3a persona femminile plurale)", "jenis_it": "Pronome suffisso (femminile plurale)"},
    "1. Dhamir__6a": {"arti_it": "Tu (singolare maschile)", "desc_it": "Tu (pronome personale isolato nominativo 2a persona maschile singolare)", "jenis_it": "Pronome isolato nominativo"},
    "1. Dhamir__6b": {"arti_it": "Tuo / ti / te (singolare maschile)", "desc_it": "Tuo / ti / te (pronome personale suffisso 2a persona maschile singolare)", "jenis_it": "Pronome suffisso"},
    "1. Dhamir__6c": {"arti_it": "Solo Te (singolare maschile)", "desc_it": "Solo Te (pronome personale isolato accusativo 2a persona maschile singolare)", "jenis_it": "Pronome isolato accusativo"},
    "1. Dhamir__7a": {"arti_it": "Voi due", "desc_it": "Voi due (pronome personale isolato nominativo 2a persona duale)", "jenis_it": "Pronome isolato nominativo (duale)"},
    "1. Dhamir__7b": {"arti_it": "Di voi due / voi due", "desc_it": "Di voi due / voi due (pronome personale suffisso 2a persona duale)", "jenis_it": "Pronome suffisso (duale)"},
    "1. Dhamir__8a": {"arti_it": "Voi (plurale maschile)", "desc_it": "Voi (pronome personale isolato nominativo 2a persona maschile plurale)", "jenis_it": "Pronome isolato nominativo (plurale)"},
    "1. Dhamir__8b": {"arti_it": "Vostro / vi (plurale maschile)", "desc_it": "Vostro / vi (pronome personale suffisso 2a persona maschile plurale)", "jenis_it": "Pronome suffisso (plurale)"},
    "1. Dhamir__8c": {"arti_it": "Solo voi (plurale maschile)", "desc_it": "Solo voi (pronome personale isolato accusativo 2a persona maschile plurale)", "jenis_it": "Pronome isolato accusativo (plurale)"},
    "1. Dhamir__9a": {"arti_it": "Tu (singolare femminile)", "desc_it": "Tu (pronome personale isolato nominativo 2a persona femminile singolare)", "jenis_it": "Pronome isolato nominativo (femminile)"},
    "1. Dhamir__9b": {"arti_it": "Tuo / ti (singolare femminile)", "desc_it": "Tuo / ti (pronome personale suffisso 2a persona femminile singolare)", "jenis_it": "Pronome suffisso (femminile)"},
    "1. Dhamir__10a": {"arti_it": "Voi (plurale femminile)", "desc_it": "Voi (pronome personale isolato nominativo 2a persona femminile plurale)", "jenis_it": "Pronome isolato nominativo (femminile plurale)"},
    "1. Dhamir__10b": {"arti_it": "Vostro / vi (plurale femminile)", "desc_it": "Vostro / vi (pronome personale suffisso 2a persona femminile plurale)", "jenis_it": "Pronome suffisso (femminile plurale)"},
    "1. Dhamir__11a": {"arti_it": "Io (1a persona singolare)", "desc_it": "Io (pronome personale isolato nominativo 1a persona singolare)", "jenis_it": "Pronome isolato nominativo"},
    "1. Dhamir__11b": {"arti_it": "Mio / mi / me", "desc_it": "Mio / mi / me (pronome personale suffisso 1a persona singolare)", "jenis_it": "Pronome suffisso"},
    "1. Dhamir__11c": {"arti_it": "Solo me", "desc_it": "Solo me (pronome personale isolato accusativo 1a persona singolare)", "jenis_it": "Pronome isolato accusativo"},
    "1. Dhamir__12a": {"arti_it": "Noi (1a persona plurale)", "desc_it": "Noi (pronome personale isolato nominativo 1a persona plurale)", "jenis_it": "Pronome isolato nominativo (plurale)"},
    "1. Dhamir__12b": {"arti_it": "Nostro / ci", "desc_it": "Nostro / ci (pronome personale suffisso 1a persona plurale)", "jenis_it": "Pronome suffisso (plurale)"},
    "1. Dhamir__12c": {"arti_it": "Solo noi", "desc_it": "Solo noi (pronome personale isolato accusativo 1a persona plurale)", "jenis_it": "Pronome isolato accusativo (plurale)"},

    # 2. Mawshul (10 items)
    "2. Mawshul__1": {"arti_it": "Ciò che / quel che", "desc_it": "Pronome relativo generale per entità non razionali (Ma)", "jenis_it": "Pronome relativo generale (non razionale)"},
    "2. Mawshul__2": {"arti_it": "Coloro che (plurale maschile)", "desc_it": "Coloro che / i quali (pronome relativo plurale maschile)", "jenis_it": "Pronome relativo plurale maschile"},
    "2. Mawshul__3": {"arti_it": "Chi / colui che", "desc_it": "Pronome relativo generale per esseri razionali (Man)", "jenis_it": "Pronome relativo generale (razionale)"},
    "2. Mawshul__4": {"arti_it": "Colui che (maschile singolare)", "desc_it": "Colui che / il quale (pronome relativo maschile singolare)", "jenis_it": "Pronome relativo maschile singolare"},
    "2. Mawshul__5": {"arti_it": "Quale / chiunque di loro", "desc_it": "Quale / chiunque tra loro (pronome relativo declinabile)", "jenis_it": "Pronome relativo"},
    "2. Mawshul__6": {"arti_it": "Colei che (femminile singolare)", "desc_it": "Colei che / la quale (pronome relativo femminile singolare)", "jenis_it": "Pronome relativo femminile singolare"},
    "2. Mawshul__7": {"arti_it": "Coloro che / le donne che (plurale femminile)", "desc_it": "Coloro che / le quali (pronome relativo plurale femminile)", "jenis_it": "Pronome relativo plurale femminile"},
    "2. Mawshul__8": {"arti_it": "Coloro che / le donne che (plurale femminile variante)", "desc_it": "Coloro che / le quali (pronome relativo plurale femminile variante)", "jenis_it": "Pronome relativo plurale femminile"},
    "2. Mawshul__9": {"arti_it": "Coloro due che (duale maschile)", "desc_it": "Coloro due che (pronome relativo duale maschile)", "jenis_it": "Pronome relativo duale maschile"},
    "2. Mawshul__10": {"arti_it": "Qualunque / qualsiasi (femminile)", "desc_it": "Qualunque / qualsiasi (pronome relativo femminile)", "jenis_it": "Pronome relativo (femminile)"},

    # 3. Istifham (10 items)
    "3. Istifham__1": {"arti_it": "Cosa? / Che cosa?", "desc_it": "Cosa? / Che cosa? (Pronome interrogativo per cose)", "jenis_it": "Pronome interrogativo"},
    "3. Istifham__2": {"arti_it": "Come?", "desc_it": "Come? (Pronome interrogativo di modo)", "jenis_it": "Pronome interrogativo di modo"},
    "3. Istifham__3": {"arti_it": "Chi?", "desc_it": "Chi? (Pronome interrogativo per persone)", "jenis_it": "Pronome interrogativo"},
    "3. Istifham__4": {"arti_it": "Quale?", "desc_it": "Quale? (Pronome interrogativo di scelta)", "jenis_it": "Pronome interrogativo di scelta"},
    "3. Istifham__5": {"arti_it": "Come? / Da dove?", "desc_it": "Come? / Da dove? (Pronome interrogativo di modo o provenienza)", "jenis_it": "Pronome interrogativo"},
    "3. Istifham__6": {"arti_it": "Che cos'è che?", "desc_it": "Che cos'è che? (Pronome interrogativo composto enfatico)", "jenis_it": "Pronome interrogativo composto"},
    "3. Istifham__7": {"arti_it": "Quanto? / Per quanto tempo?", "desc_it": "Quanto? (Pronome interrogativo di quantità o tempo)", "jenis_it": "Pronome interrogativo di quantità"},
    "3. Istifham__8": {"arti_it": "Perché? / A che scopo?", "desc_it": "Perché? / Per quale motivo? (Interrogativo di causa, Li + Ma)", "jenis_it": "Interrogativo di causa"},
    "3. Istifham__9": {"arti_it": "Dove?", "desc_it": "Dove? (Pronome interrogativo di luogo)", "jenis_it": "Pronome interrogativo di luogo"},
    "3. Istifham__10": {"arti_it": "Quando?", "desc_it": "Quando? (Pronome interrogativo di tempo)", "jenis_it": "Pronome interrogativo di tempo"},

    # 4. Syarath (5 items)
    "4. Syarath__1": {"arti_it": "Chiunque / chi", "desc_it": "Chiunque (Sostantivo condizionale per persone)", "jenis_it": "Sostantivo condizionale (razionale)"},
    "4. Syarath__2": {"arti_it": "Qualsiasi cosa / qualunque cosa", "desc_it": "Qualsiasi cosa (Sostantivo condizionale per cose)", "jenis_it": "Sostantivo condizionale (non razionale)"},
    "4. Syarath__3": {"arti_it": "Ogni volta che / ogniqualvolta", "desc_it": "Ogni volta che (Avverbio condizionale temporale)", "jenis_it": "Avverbio condizionale temporale"},
    "4. Syarath__4": {"arti_it": "Qualunque / qualsiasi", "desc_it": "Qualunque (Sostantivo condizionale di scelta)", "jenis_it": "Sostantivo condizionale di scelta"},
    "4. Syarath__5": {"arti_it": "Qualunque dei due (enfatico)", "desc_it": "Qualunque dei due termini (Sostantivo condizionale con Ma enfatica)", "jenis_it": "Sostantivo condizionale composto"},

    # 5. Isyarah (8 items)
    "5. Isyarah__1": {"arti_it": "Questo / quello (maschile singolare)", "desc_it": "Questo / quello (Pronome dimostrativo maschile singolare)", "jenis_it": "Pronome dimostrativo (maschile singolare)"},
    "5. Isyarah__2": {"arti_it": "Questi / coloro (plurale)", "desc_it": "Questi / quelli (Pronome dimostrativo plurale)", "jenis_it": "Pronome dimostrativo (plurale)"},
    "5. Isyarah__3": {"arti_it": "Questa / quella (femminile singolare)", "desc_it": "Questa / quella (Pronome dimostrativo femminile singolare)", "jenis_it": "Pronome dimostrativo (femminile singolare)"},
    "5. Isyarah__4": {"arti_it": "Quella / quelle (femminile / plurale non razionale)", "desc_it": "Quella / quelle (Dimostrativo lontano per femminile o plurale)", "jenis_it": "Pronome dimostrativo lontano"},
    "5. Isyarah__5": {"arti_it": "Qui / in questo luogo", "desc_it": "Qui (Avverbio dimostrativo di luogo vicino)", "jenis_it": "Avverbio dimostrativo di luogo"},
    "5. Isyarah__6": {"arti_it": "Là / colà / in quel luogo", "desc_it": "Là (Avverbio dimostrativo di luogo lontano)", "jenis_it": "Avverbio dimostrativo di luogo"},
    "5. Isyarah__7": {"arti_it": "Questi due (duale maschile)", "desc_it": "Questi due (Pronome dimostrativo duale maschile)", "jenis_it": "Pronome dimostrativo duale"},
    "5. Isyarah__8": {"arti_it": "Queste due / quelle due (duale femminile)", "desc_it": "Queste due / quelle due (Dimostrativo duale femminile)", "jenis_it": "Pronome dimostrativo duale femminile"},

    # 6. Isim Fi'il (8 items)
    "6. Isim Fi'il__1": {"arti_it": "Gloria a / Gloria sia ad Allah", "desc_it": "Gloria ad Allah, Egli è puro da ogni imperfezione (Nome verbale di lode)", "jenis_it": "Nome verbale (Lode)"},
    "6. Isim Fi'il__2": {"arti_it": "Portate! / Mostrate!", "desc_it": "Portate la vostra prova (Nome verbale imperativo)", "jenis_it": "Nome verbale (imperativo)"},
    "6. Isim Fi'il__3": {"arti_it": "Uffa! / Vergogna! (esclamazione di sdegno)", "desc_it": "Uffa / vergogna (Nome verbale tempo presente esprimente disgusto)", "jenis_it": "Nome verbale (disgusto)"},
    "6. Isim Fi'il__4": {"arti_it": "Mi rifugio in Allah / Che Allah non voglia", "desc_it": "Cerco rifugio in Allah (Nome verbale di rifugio)", "jenis_it": "Nome verbale (rifugio)"},
    "6. Isim Fi'il__5": {"arti_it": "Venite! / Accorrete!", "desc_it": "Venite qui / portate (Nome verbale imperativo)", "jenis_it": "Nome verbale (imperativo)"},
    "6. Isim Fi'il__6": {"arti_it": "Lungi da ciò! / Impossibile!", "desc_it": "Quanto è lontano! (Nome verbale tempo passato)", "jenis_it": "Nome verbale (tempo passato)"},
    "6. Isim Fi'il__7": {"arti_it": "Prendete e leggete!", "desc_it": "Prendete e leggete il mio libro (Nome verbale imperativo)", "jenis_it": "Nome verbale (imperativo)"},
    "6. Isim Fi'il__8": {"arti_it": "Vieni qui! / Fatti avanti!", "desc_it": "Vieni a me (Nome verbale imperativo di invito)", "jenis_it": "Nome verbale (invito)"},

    # 7. Fi'il Jamid (8 items)
    "7. Fi'il Jamid__1": {"arti_it": "Non è / non sono", "desc_it": "Non essere / non è (Verbo difettivo di negazione)", "jenis_it": "Verbo difettivo di negazione"},
    "7. Fi'il Jamid__2": {"arti_it": "Che pessimo...", "desc_it": "Che pessimo... (Verbo difettivo di biasimo)", "jenis_it": "Verbo difettivo di biasimo"},
    "7. Fi'il Jamid__3": {"arti_it": "Forse / può darsi che", "desc_it": "Forse / può darsi che (Verbo difettivo di speranza)", "jenis_it": "Verbo difettivo di speranza"},
    "7. Fi'il Jamid__4": {"arti_it": "Che eccellente...", "desc_it": "Che eccellente... (Verbo difettivo di lode)", "jenis_it": "Verbo difettivo di lode"},
    "7. Fi'il Jamid__5": {"arti_it": "Che pessima cosa è ciò che", "desc_it": "Che pessima cosa è ciò che (Verbo difettivo di biasimo composto con Ma)", "jenis_it": "Verbo difettivo di biasimo"},
    "7. Fi'il Jamid__6": {"arti_it": "Cominciarono a...", "desc_it": "Cominciarono a coprirsi con le foglie (Verbo difettivo di inizio)", "jenis_it": "Verbo difettivo di inizio"},
    "7. Fi'il Jamid__7": {"arti_it": "Che Allah non voglia! / Lungi da Allah", "desc_it": "Che Allah non voglia! (Verbo difettivo di esenzione e purezza)", "jenis_it": "Verbo difettivo di esenzione"},
    "7. Fi'il Jamid__8": {"arti_it": "Che eccellente cosa è ciò che", "desc_it": "Che eccellente cosa è ciò a cui vi esorta (Verbo difettivo di lode composto con Ma)", "jenis_it": "Verbo difettivo di lode"}
}

# Duplicate aliases for "2. Isim Mawshul__X", "3. Isim Istifham__X", "4. Isim Syarath__X", "5. Isim Isyarah__X"
for k, v in list(IT_JAMID_MAP.items()):
    if k.startswith("2. Mawshul__"):
        IT_JAMID_MAP[k.replace("2. Mawshul__", "2. Isim Mawshul__")] = v
    elif k.startswith("3. Istifham__"):
        IT_JAMID_MAP[k.replace("3. Istifham__", "3. Isim Istifham__")] = v
    elif k.startswith("4. Syarath__"):
        IT_JAMID_MAP[k.replace("4. Syarath__", "4. Isim Syarath__")] = v
    elif k.startswith("5. Isyarah__"):
        IT_JAMID_MAP[k.replace("5. Isyarah__", "5. Isim Isyarah__")] = v

# Precise Dutch Translations for Harf Ghair Amil (52 keys)
NL_HARF_MAP = {
    "1. Harf Nafyi__1": {"arti_nl": "Niet / geen (ontkenning)", "desc_nl": "Algemeen ontkennend partikel (Laa)", "jenis_nl": "Ontkennend partikel"},
    "1. Harf Nafyi__2": {"arti_nl": "Niet / niets / geenszins", "desc_nl": "Ontkennend partikel voor verleden en tegenwoordige tijd (Maa)", "jenis_nl": "Ontkennend partikel"},
    "1. Harf Nafyi__3": {"arti_nl": "Niet anders dan / slechts", "desc_nl": "Ontkennend partikel van uitzondering (In... illaa)", "jenis_nl": "Ontkennend partikel van beperking"},
    "1. Harf Nafyi__4": {"arti_nl": "Is er dan geen?", "desc_nl": "Retorisch ontkennend vraagpartikel (Hal)", "jenis_nl": "Retorisch ontkennend partikel"},
    "1. Harf Nafyi__5": {"arti_nl": "Er is geen (tijd)", "desc_nl": "Ontkennend partikel voor tijdsbegrippen (Laata)", "jenis_nl": "Ontkennend partikel van tijd"},
    "1. Harf Nafyi__6": {"arti_nl": "Wat anders dan / niets", "desc_nl": "Retorisch ontkennend samengesteld vraagpartikel (Maadhaa)", "jenis_nl": "Retorisch vraagpartikel"},
    "2. Harf Tahqiq Taswif__7": {"arti_nl": "Voorzeker / waarlijk / reeds", "desc_nl": "Bevestigend partikel van zekerheid (Qad)", "jenis_nl": "Bevestigend partikel (Tahqiq)"},
    "2. Harf Tahqiq Taswif__8": {"arti_nl": "(Binnenkort) zal / zullen", "desc_nl": "Toekomstpartikel voor verre toekomst (Sawfa)", "jenis_nl": "Toekomstpartikel (Taswif)"},
    "3. Harf Syarat__9": {"arti_nl": "Indien / ware het dat (onmogelijk)", "desc_nl": "Irreëel voorwaardelijk partikel (Law)", "jenis_nl": "Voorwaardelijk partikel"},
    "3. Harf Syarat__10": {"arti_nl": "Ware het niet dat / waarom niet", "desc_nl": "Voorwaardelijk partikel van verhindering (Lawlaa)", "jenis_nl": "Voorwaardelijk partikel van verhindering"},
    "3. Harf Syarat__11": {"arti_nl": "Zelfs al / hoewel", "desc_nl": "Toegevend voorwaardelijk partikel (Law)", "jenis_nl": "Toegevend voorwaardelijk partikel"},
    "3. Harf Syarat__12": {"arti_nl": "Als / wanneer dan ook", "desc_nl": "Benadrukt voorwaardelijk partikel (Immaa = In + Maa)", "jenis_nl": "Benadrukt voorwaardelijk partikel"},
    "3. Harf Syarat__13": {"arti_nl": "Wat voor teken dan ook", "desc_nl": "Algemeen voorwaardelijk zelfstandig naamwoord (Mahmaa)", "jenis_nl": "Voorwaardelijk nomen"},
    "4. Harf Mashdariyah__14": {"arti_nl": "Zolang als / tijdens", "desc_nl": "Tijdsbepalend nominaliserend partikel (Maa)", "jenis_nl": "Nominaliserend partikel van tijdsduur"},
    "4. Harf Mashdariyah__15": {"arti_nl": "Opdat niet / zodat niet", "desc_nl": "Nominaliserend partikel met ontkenning (Allaa = An + Laa)", "jenis_nl": "Nominaliserend ontkennend partikel"},
    "4. Harf Mashdariyah__16": {"arti_nl": "Dat / om te (nominaliserend)", "desc_nl": "Werkwoord-nominaliserend partikel (An)", "jenis_nl": "Nominaliserend partikel (Masdariyyah)"},
    "4. Harf Mashdariyah__17": {"arti_nl": "Zou wensen dat", "desc_nl": "Nominaliserend partikel van wens (Law)", "jenis_nl": "Nominaliserend partikel van wens"},
    "4. Harf Mashdariyah__18": {"arti_nl": "Dat jullie niet dienen", "desc_nl": "Nominaliserend partikel met verbod (An + Laa)", "jenis_nl": "Nominaliserend partikel van verbod"},
    "4. Harf Mashdariyah__19": {"arti_nl": "Dat (waarlijk)", "desc_nl": "Verlicht nominaliserend partikel (An verlicht van Anna)", "jenis_nl": "Verlicht nominaliserend partikel"},
    "5. Harf Zaidah__20": {"arti_nl": "Zoals / net zoals", "desc_nl": "Vergelijkend partikel met extra versterking (Kamaa = Ka + Maa)", "jenis_nl": "Versterkend partikel"},
    "5. Harf Zaidah__21": {"arti_nl": "Zelfs een mug of iets daarboven", "desc_nl": "Onbepaald versterkend partikel (Maa Zaa'idah)", "jenis_nl": "Versterkend toevoegsel"},
    "5. Harf Zaidah__22": {"arti_nl": "Ik zweer voorwaar", "desc_nl": "Versterkend partikel voor een eed (Laa Zaa'idah)", "jenis_nl": "Eed-versterkend partikel"},
    "5. Harf Zaidah__23": {"arti_nl": "Door de genade van Allah", "desc_nl": "Voorzetsel met extra versterkend partikel (Bimaa = Bi + Maa)", "jenis_nl": "Versterkend partikel na voorzetsel"},
    "5. Harf Zaidah__24": {"arti_nl": "Toen de brenger van blijde tijding kwam", "desc_nl": "Versterkend partikel na tijdsverbindingswoord (An na Lammaa)", "jenis_nl": "Versterkend tijdsverbindingspartikel"},
    "6. Harf Istifham__25": {"arti_nl": "Is er? / Heeft?", "desc_nl": "Vragend partikel voor vragen en bevestiging (Hal)", "jenis_nl": "Vragend partikel (Istifham)"},
    "7. Harf Jawab__26": {"arti_nl": "In dat geval / dan", "desc_nl": "Antwoordend en gevolg-aanduidend partikel (Idhan)", "jenis_nl": "Antwoord- en gevolgpartikel"},
    "7. Harf Jawab__27": {"arti_nl": "Jawel / zeker wel!", "desc_nl": "Bevestigend antwoordpartikel op ontkennende vraag (Balaa)", "jenis_nl": "Bevestigend antwoordpartikel"},
    "7. Harf Jawab__28": {"arti_nl": "Ja / inderdaad", "desc_nl": "Instemmend antwoordpartikel (Na'am)", "jenis_nl": "Instemmend antwoordpartikel"},
    "7. Harf Jawab__29": {"arti_nl": "Ja, bij mijn Heer!", "desc_nl": "Eed-bevestigend antwoordpartikel (Iiy)", "jenis_nl": "Eed-bevestigend antwoordpartikel"},
    "8. Harf Ibtida'__30": {"arti_nl": "Totdat / zover dat", "desc_nl": "Begin-aanduidend partikel (Hattaa)", "jenis_nl": "Begin-partikel (Ibtidaa')"},
    "9. Harf Tafshil__31": {"arti_nl": "Wat betreft / aangaande", "desc_nl": "Partikel van nadere toelichting en voorwaarde (Ammaa)", "jenis_nl": "Toelichtend partikel (Tafshil)"},
    "10. Harf Mufaja'ah__32": {"arti_nl": "Plotseling / eensklaps", "desc_nl": "Partikel van plotselinge gebeurtenis (Idhaa)", "jenis_nl": "Partikel van plotselinge wending"},
    "11. Harf Mufassirah__33": {"arti_nl": "Namelijk / dat wil zeggen", "desc_nl": "Verklarend partikel (An)", "jenis_nl": "Verklarend partikel (Mufassirah)"},
    "12. Harf Istiftahiyah__34": {"arti_nl": "Weet wel! / Let op!", "desc_nl": "Aandachttrekkend openingspartikel (Alaa)", "jenis_nl": "Openings- en waarschuwingspartikel"},
    "13. Harf Rada'__35": {"arti_nl": "Geenszins! / Absoluut niet!", "desc_nl": "Bestraffend en fel afwijzend partikel (Kallaa)", "jenis_nl": "Afwijzend en bestraffend partikel (Rada')"},
    "14. Harf Ta'ajjub__36": {"arti_nl": "Hoe geduldig zijn zij!", "desc_nl": "Partikel van verbazing en uitroep (Maa Ta'ajjubiyyah)", "jenis_nl": "Uitroep- en verwonderingspartikel"},
    "15. Harf Fariqah__37": {"arti_nl": "Waarlijk / inderdaad", "desc_nl": "Onderscheidende versterkende Laam (Laam Fariqah bij verlichte In)", "jenis_nl": "Onderscheidende Laam"},
    "16. Harf Mauthi'ah__38": {"arti_nl": "Als... dan zweer ik voorzeker", "desc_nl": "Eed-inleidende voorwaardelijke Laam (La-in)", "jenis_nl": "Eed-inleidende Laam"},
    "17. Harf Mabany__39": {"arti_nl": "Haa Miim", "desc_nl": "Mystieke openingsletters van de Soerah (حم)", "jenis_nl": "Losse openingsletters (Muqatta'at)"},
    "17. Harf Mabany__40": {"arti_nl": "Alif Laam Miim", "desc_nl": "Mystieke openingsletters van de Soerah (الم)", "jenis_nl": "Losse openingsletters (Muqatta'at)"},
    "17. Harf Mabany__41": {"arti_nl": "Alif Laam Raa", "desc_nl": "Mystieke openingsletters van de Soerah (الر)", "jenis_nl": "Losse openingsletters (Muqatta'at)"},
    "17. Harf Mabany__42": {"arti_nl": "Thaa Siin Miim", "desc_nl": "Mystieke openingsletters van de Soerah (طسم)", "jenis_nl": "Losse openingsletters (Muqatta'at)"},
    "17. Harf Mabany__43": {"arti_nl": "Alif Laam Miim Raa", "desc_nl": "Mystieke openingsletters van de Soerah (المر)", "jenis_nl": "Losse openingsletters (Muqatta'at)"},
    "17. Harf Mabany__44": {"arti_nl": "Alif Laam Miim Shaad", "desc_nl": "Mystieke openingsletters van de Soerah (المص)", "jenis_nl": "Losse openingsletters (Muqatta'at)"},
    "17. Harf Mabany__45": {"arti_nl": "Shaad", "desc_nl": "Mystieke openingsletter van de Soerah (ص)", "jenis_nl": "Losse openingsletter (Muqatta'at)"},
    "17. Harf Mabany__46": {"arti_nl": "Thaa Siin", "desc_nl": "Mystieke openingsletters van de Soerah (طس)", "jenis_nl": "Losse openingsletters (Muqatta'at)"},
    "17. Harf Mabany__47": {"arti_nl": "Thaa Haa", "desc_nl": "Mystieke openingsletters van de Soerah (طه)", "jenis_nl": "Losse openingsletters (Muqatta'at)"},
    "17. Harf Mabany__48": {"arti_nl": "'Ain Siin Qaaf", "desc_nl": "Mystieke openingsletters van de Soerah (عسق)", "jenis_nl": "Losse openingsletters (Muqatta'at)"},
    "17. Harf Mabany__49": {"arti_nl": "Qaaf", "desc_nl": "Mystieke openingsletter van de Soerah (ق)", "jenis_nl": "Losse openingsletter (Muqatta'at)"},
    "17. Harf Mabany__50": {"arti_nl": "Kaaf Haa Yaa 'Ain Shaad", "desc_nl": "Mystieke openingsletters van de Soerah (كهيعص)", "jenis_nl": "Losse openingsletters (Muqatta'at)"},
    "17. Harf Mabany__51": {"arti_nl": "Noen", "desc_nl": "Mystieke openingsletter van de Soerah (ن)", "jenis_nl": "Losse openingsletter (Muqatta'at)"},
    "17. Harf Mabany__52": {"arti_nl": "Yaa Siin", "desc_nl": "Mystieke openingsletters van de Soerah (يس)", "jenis_nl": "Losse openingsletters (Muqatta'at)"}
}

for k, v in list(NL_HARF_MAP.items()):
    nk = k.split('__')[-1]
    NL_HARF_MAP[nk] = v

for k, v in list(NL_JAMID_MAP.items()):
    nk = k.split('__')[-1]
    NL_JAMID_MAP[nk] = v

# Precise Italian Translations for Harf Ghair Amil (52 keys)
IT_HARF_MAP = {
    "1. Harf Nafyi__1": {"arti_it": "Non / no (negazione)", "desc_it": "Particella negativa generale (La)", "jenis_it": "Particella negativa"},
    "1. Harf Nafyi__2": {"arti_it": "Non / niente / affatto", "desc_it": "Particella negativa per passato e presente (Ma)", "jenis_it": "Particella negativa"},
    "1. Harf Nafyi__3": {"arti_it": "Non... se non / soltanto", "desc_it": "Particella negativa di eccezione e restrizione (In... illa)", "jenis_it": "Particella restrittiva"},
    "1. Harf Nafyi__4": {"arti_it": "Non c'è forse? / Non è così?", "desc_it": "Particella interrogativa con valore di negazione retorica (Hal)", "jenis_it": "Particella interrogativa retorica"},
    "1. Harf Nafyi__5": {"arti_it": "Non è più (tempo)", "desc_it": "Particella negativa applicata ai sostantivi di tempo (Lata)", "jenis_it": "Particella negativa temporale"},
    "1. Harf Nafyi__6": {"arti_it": "Cos'altro se non / niente", "desc_it": "Particella interrogativa composta con valore negativo (Madha)", "jenis_it": "Particella interrogativa retorica"},
    "2. Harf Tahqiq Taswif__7": {"arti_it": "Certamente / davvero / già", "desc_it": "Particella di asseverazione e certezza (Qad)", "jenis_it": "Particella di certezza (Tahqiq)"},
    "2. Harf Tahqiq Taswif__8": {"arti_it": "Presto / in futuro (avverrà)", "desc_it": "Particella indicante il futuro lontano (Sawfa)", "jenis_it": "Particella di futuro (Taswif)"},
    "3. Harf Syarat__9": {"arti_it": "Se / se mai (condizione irreale)", "desc_it": "Particella condizionale irreale o ipotetica (Law)", "jenis_it": "Particella condizionale"},
    "3. Harf Syarat__10": {"arti_it": "Se non fosse per / perché non", "desc_it": "Particella condizionale di impedimento (Lawla)", "jenis_it": "Particella condizionale di impedimento"},
    "3. Harf Syarat__11": {"arti_it": "Anche se / quand'anche", "desc_it": "Particella condizionale concessiva (Law)", "jenis_it": "Particella condizionale concessiva"},
    "3. Harf Syarat__12": {"arti_it": "Qualora / se mai", "desc_it": "Particella condizionale enfatica (Imma = In + Ma)", "jenis_it": "Particella condizionale enfatica"},
    "3. Harf Syarat__13": {"arti_it": "Qualsiasi segno / qualunque cosa", "desc_it": "Sostantivo condizionale generale (Mahma)", "jenis_it": "Sostantivo condizionale"},
    "4. Harf Mashdariyah__14": {"arti_it": "Finché / per tutto il tempo", "desc_it": "Particella infinitiva di durata temporale (Ma)", "jenis_it": "Particella infinitiva temporale"},
    "4. Harf Mashdariyah__15": {"arti_it": "Affinché non / per non", "desc_it": "Particella infinitiva con negazione (Alla = An + La)", "jenis_it": "Particella infinitiva negativa"},
    "4. Harf Mashdariyah__16": {"arti_it": "Che / di (infinitivo)", "desc_it": "Particella che trasforma la proposizione in infinito sostantivato (An)", "jenis_it": "Particella infinitiva (Masdariyyah)"},
    "4. Harf Mashdariyah__17": {"arti_it": "Desidererebbe che", "desc_it": "Particella infinitiva esprimente desiderio (Law)", "jenis_it": "Particella infinitiva di desiderio"},
    "4. Harf Mashdariyah__18": {"arti_it": "Di non adorare", "desc_it": "Particella infinitiva con divieto (An + La)", "jenis_it": "Particella infinitiva di divieto"},
    "4. Harf Mashdariyah__19": {"arti_it": "Che in verità", "desc_it": "Particella infinitiva alleggerita (An alleggerita da Anna)", "jenis_it": "Particella infinitiva alleggerita"},
    "5. Harf Zaidah__20": {"arti_it": "Così come / come", "desc_it": "Prefisso di comparazione con particella enfatica aggiunta (Kama = Ka + Ma)", "jenis_it": "Particella enfatica di comparazione"},
    "5. Harf Zaidah__21": {"arti_it": "Persino un moscerino o cosa superiore", "desc_it": "Particella enfatica esprimente indeterminatezza (Ma Za'idah)", "jenis_it": "Particella enfatica aggiunta"},
    "5. Harf Zaidah__22": {"arti_it": "Giuro solennemente", "desc_it": "Particella enfatica per rafforzare il giuramento (La Za'idah)", "jenis_it": "Particella enfatica di giuramento"},
    "5. Harf Zaidah__23": {"arti_it": "Per misericordia di Allah", "desc_it": "Preposizione con particella enfatica aggiunta (Bima = Bi + Ma)", "jenis_it": "Particella enfatica post-preposizionale"},
    "5. Harf Zaidah__24": {"arti_it": "Quando giunse il nunzio", "desc_it": "Particella enfatica dopo congiunzione temporale (An dopo Lamma)", "jenis_it": "Particella enfatica temporale"},
    "6. Harf Istifham__25": {"arti_it": "È forse? / Ha forse?", "desc_it": "Particella interrogativa per domande dirette e conferme (Hal)", "jenis_it": "Particella interrogativa (Istifham)"},
    "7. Harf Jawab__26": {"arti_it": "In tal caso / allora", "desc_it": "Particella di risposta e conseguenza (Idhan)", "jenis_it": "Particella di risposta e conseguenza"},
    "7. Harf Jawab__27": {"arti_it": "Sì, certamente! / Anzi!", "desc_it": "Particella di risposta affermativa a domanda negativa (Bala)", "jenis_it": "Particella di risposta affermativa"},
    "7. Harf Jawab__28": {"arti_it": "Sì / Certamente", "desc_it": "Particella di risposta affermativa di assenso (Na'am)", "jenis_it": "Particella affermativa"},
    "7. Harf Jawab__29": {"arti_it": "Sì, per il mio Signore!", "desc_it": "Particella di risposta affermativa con giuramento (I)", "jenis_it": "Particella affermativa con giuramento"},
    "8. Harf Ibtida'__30": {"arti_it": "Fino al punto che", "desc_it": "Particella introduttiva e iniziale (Hatta)", "jenis_it": "Particella introduttiva (Ibtida')"},
    "9. Harf Tafshil__31": {"arti_it": "Quanto a / per ciò che riguarda", "desc_it": "Particella di spiegazione dettagliata e condizione (Amma)", "jenis_it": "Particella esplicativa (Tafshil)"},
    "10. Harf Mufaja'ah__32": {"arti_it": "Ed ecco che all'improvviso", "desc_it": "Particella indicante evento improvviso e inaspettato (Idha)", "jenis_it": "Particella di sorpresa (Mufaja'ah)"},
    "11. Harf Mufassirah__33": {"arti_it": "Ossia / vale a dire", "desc_it": "Particella esplicativa introduttiva (An)", "jenis_it": "Particella esplicativa (Mufassirah)"},
    "12. Harf Istiftahiyah__34": {"arti_it": "Badate bene! / Sappiate!", "desc_it": "Particella di apertura e richiamo all'attenzione (Ala)", "jenis_it": "Particella di ammonimento iniziale"},
    "13. Harf Rada'__35": {"arti_it": "No davvero! / Niente affatto!", "desc_it": "Particella di energico rifiuto e severo rimprovero (Kalla)", "jenis_it": "Particella di rifiuto e rimprovero (Rada')"},
    "14. Harf Ta'ajjub__36": {"arti_it": "Quanto sono pazienti!", "desc_it": "Particella di esclamazione e stupore (Ma Ta'ajjubiyyah)", "jenis_it": "Particella esclamativa"},
    "15. Harf Fariqah__37": {"arti_it": "Certamente / per l'appunto", "desc_it": "Lam enfatica distintiva per affermazione (Lam Fariqah con In alleggerita)", "jenis_it": "Lam enfatica distintiva"},
    "16. Harf Mauthi'ah__38": {"arti_it": "Se... giuro certamente", "desc_it": "Lam preparatoria al giuramento condizionale (La-in)", "jenis_it": "Lam introduttiva al giuramento"},
    "17. Harf Mabany__39": {"arti_it": "Ha Mim", "desc_it": "Lettere mistiche isolate all'inizio della Sura (حم)", "jenis_it": "Lettere mistiche (Muqatta'at)"},
    "17. Harf Mabany__40": {"arti_it": "Alif Lam Mim", "desc_it": "Lettere mistiche isolate all'inizio della Sura (الم)", "jenis_it": "Lettere mistiche (Muqatta'at)"},
    "17. Harf Mabany__41": {"arti_it": "Alif Lam Ra", "desc_it": "Lettere mistiche isolate all'inizio della Sura (الر)", "jenis_it": "Lettere mistiche (Muqatta'at)"},
    "17. Harf Mabany__42": {"arti_it": "Ta Sin Mim", "desc_it": "Lettere mistiche isolate all'inizio della Sura (طسم)", "jenis_it": "Lettere mistiche (Muqatta'at)"},
    "17. Harf Mabany__43": {"arti_it": "Alif Lam Mim Ra", "desc_it": "Lettere mistiche isolate all'inizio della Sura (المر)", "jenis_it": "Lettere mistiche (Muqatta'at)"},
    "17. Harf Mabany__44": {"arti_it": "Alif Lam Mim Sad", "desc_it": "Lettere mistiche isolate all'inizio della Sura (المص)", "jenis_it": "Lettere mistiche (Muqatta'at)"},
    "17. Harf Mabany__45": {"arti_it": "Sad", "desc_it": "Lettera mistica isolata all'inizio della Sura (ص)", "jenis_it": "Lettera mistica (Muqatta'at)"},
    "17. Harf Mabany__46": {"arti_it": "Ta Sin", "desc_it": "Lettere mistiche isolate all'inizio della Sura (طس)", "jenis_it": "Lettere mistiche (Muqatta'at)"},
    "17. Harf Mabany__47": {"arti_it": "Ta Ha", "desc_it": "Lettere mistiche isolate all'inizio della Sura (طه)", "jenis_it": "Lettere mistiche (Muqatta'at)"},
    "17. Harf Mabany__48": {"arti_it": "'Ain Sin Qaf", "desc_it": "Lettere mistiche isolate all'inizio della Sura (عسق)", "jenis_it": "Lettere mistiche (Muqatta'at)"},
    "17. Harf Mabany__49": {"arti_it": "Qaf", "desc_it": "Lettera mistica isolata all'inizio della Sura (ق)", "jenis_it": "Lettera mistica (Muqatta'at)"},
    "17. Harf Mabany__50": {"arti_it": "Kaf Ha Ya 'Ain Sad", "desc_it": "Lettere mistiche isolate all'inizio della Sura (كهيعص)", "jenis_it": "Lettere mistiche (Muqatta'at)"},
    "17. Harf Mabany__51": {"arti_it": "Nun", "desc_it": "Lettera mistica isolata all'inizio della Sura (ن)", "jenis_it": "Lettera mistica (Muqatta'at)"},
    "17. Harf Mabany__52": {"arti_it": "Ya Sin", "desc_it": "Lettere mistiche isolate all'inizio della Sura (يس)", "jenis_it": "Lettere mistiche (Muqatta'at)"}
}

for k, v in list(IT_HARF_MAP.items()):
    nk = k.split('__')[-1]
    IT_HARF_MAP[nk] = v

for k, v in list(IT_JAMID_MAP.items()):
    nk = k.split('__')[-1]
    IT_JAMID_MAP[nk] = v

# Write build_dutch_dataset.py
dutch_content = f"""#!/usr/bin/env python3
# -*- coding: utf-8 -*-
\"\"\"
Script containing complete Dutch (nl) dataset metadata:
- 114 Surah Names (DUTCH_SURAHS)
- 7 Bentuk Kata Categories (BENTUK_KATA_NL)
- 76 Jamid Mabny Words Grammar (DUTCH_GRAMMAR)
- 17 Bentuk Harf Categories (BENTUK_HARF_NL)
- 52 Harf Words Grammar (DUTCH_HARF_GRAMMAR)
\"\"\"

DUTCH_SURAHS = {json.dumps(DUTCH_SURAHS, ensure_ascii=False, indent=4)}

BENTUK_KATA_NL = {json.dumps(BENTUK_KATA_NL, ensure_ascii=False, indent=4)}

DUTCH_GRAMMAR = {json.dumps(NL_JAMID_MAP, ensure_ascii=False, indent=4)}

BENTUK_HARF_NL = {json.dumps(BENTUK_HARF_NL, ensure_ascii=False, indent=4)}

DUTCH_HARF_GRAMMAR = {json.dumps(NL_HARF_MAP, ensure_ascii=False, indent=4)}
"""

with open(os.path.join(BASE_DIR, 'build_dutch_dataset.py'), 'w', encoding='utf-8') as f:
    f.write(dutch_content)

print("Saved build_dutch_dataset.py successfully.")

# Write build_italian_dataset.py
italian_content = f"""#!/usr/bin/env python3
# -*- coding: utf-8 -*-
\"\"\"
Script containing complete Italian (it) dataset metadata:
- 114 Surah Names (ITALIAN_SURAHS)
- 7 Bentuk Kata Categories (BENTUK_KATA_IT)
- 76 Jamid Mabny Words Grammar (ITALIAN_GRAMMAR)
- 17 Bentuk Harf Categories (BENTUK_HARF_IT)
- 52 Harf Words Grammar (ITALIAN_HARF_GRAMMAR)
\"\"\"

ITALIAN_SURAHS = {json.dumps(ITALIAN_SURAHS, ensure_ascii=False, indent=4)}

BENTUK_KATA_IT = {json.dumps(BENTUK_KATA_IT, ensure_ascii=False, indent=4)}

ITALIAN_GRAMMAR = {json.dumps(IT_JAMID_MAP, ensure_ascii=False, indent=4)}

BENTUK_HARF_IT = {json.dumps(BENTUK_HARF_IT, ensure_ascii=False, indent=4)}

ITALIAN_HARF_GRAMMAR = {json.dumps(IT_HARF_MAP, ensure_ascii=False, indent=4)}
"""

with open(os.path.join(BASE_DIR, 'build_italian_dataset.py'), 'w', encoding='utf-8') as f:
    f.write(italian_content)

print("Saved build_italian_dataset.py successfully.")

