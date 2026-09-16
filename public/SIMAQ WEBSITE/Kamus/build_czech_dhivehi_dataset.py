#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Czech (cs) and Dhivehi (dv) Dataset Metadata & Enricher:
- 114 Surah Names for Czech & Dhivehi
- 7 Bentuk Kata Categories for Czech & Dhivehi
- 76 Jamid Mabny Grammar details for Czech & Dhivehi
- 17 Bentuk Harf Categories for Czech & Dhivehi
- 52 Harf Grammar details for Czech & Dhivehi
"""

import os
import sys
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

CZECH_SURAHS = {
    "1": "Al-Fátiha (Otevíratelka Knihy)",
    "2": "Al-Baqara (Kráva)",
    "3": "Ál 'Imrán (Rod 'Imránův)",
    "4": "An-Nisá' (Ženy)",
    "5": "Al-Má'ida (Prostřený stůl)",
    "6": "Al-An'ám (Dobytek)",
    "7": "Al-A'ráf (Rozpoznání)",
    "8": "Al-Anfál (Kořist)",
    "9": "At-Tawba (Pokání)",
    "10": "Júnus (Jonáš)",
    "11": "Húd (Húd)",
    "12": "Júsuf (Josef)",
    "13": "Ar-Ra'd (Hrom)",
    "14": "Ibráhím (Abraham)",
    "15": "Al-Hidžr (Skalnatá krajina)",
    "16": "An-Nahl (Včely)",
    "17": "Al-Isrá' (Noční cesta)",
    "18": "Al-Kahf (Jeskyně)",
    "19": "Marjam (Marie)",
    "20": "Tá Há (Tá Há)",
    "21": "Al-Anbijá' (Proroci)",
    "22": "Al-Hadždž (Pouť)",
    "23": "Al-Mu'minún (Věřící)",
    "24": "An-Núr (Světlo)",
    "25": "Al-Furqán (Kritérium)",
    "26": "Aš-Šu'ará' (Básníci)",
    "27": "An-Naml (Mravenci)",
    "28": "Al-Qasas (Příběh)",
    "29": "Al-'Ankabút (Pavouk)",
    "30": "Ar-Rúm (Byzantinci)",
    "31": "Luqmán (Luqmán)",
    "32": "As-Sadžda (Padnutí na tvář)",
    "33": "Al-Ahzáb (Spojenci)",
    "34": "Saba' (Sabovci)",
    "35": "Fátir (Stvořitel)",
    "36": "Já Sín (Já Sín)",
    "37": "As-Sáffát (V řadách stojící)",
    "38": "Sád (Sád)",
    "39": "Az-Zumar (Skupiny)",
    "40": "Gháfir (Odpouštějící)",
    "41": "Fussilat (Vyložená)",
    "42": "Aš-Šúrá (Porada)",
    "43": "Az-Zuchruf (Zlaté ozdoby)",
    "44": "Ad-Duchán (Dým)",
    "45": "Al-Džáthija (Klekající)",
    "46": "Al-Ahqáf (Duny)",
    "47": "Muhammad (Muhammad)",
    "48": "Al-Fath (Vítězství)",
    "49": "Al-Hudžurát (Komnaty)",
    "50": "Qáf (Qáf)",
    "51": "Adh-Dháriját (Větry rozprašující)",
    "52": "At-Túr (Hora)",
    "53": "An-Nadžm (Hvězda)",
    "54": "Al-Qamar (Měsíc)",
    "55": "Ar-Rahmán (Milosrdný)",
    "56": "Al-Wáqi'a (Událost)",
    "57": "Al-Hadíd (Železo)",
    "58": "Al-Mudžádala (Hádka)",
    "59": "Al-Hašr (Shromáždění)",
    "60": "Al-Mumtahana (Zkoušená)",
    "61": "As-Saff (Semknutá řada)",
    "62": "Al-Džumu'a (Pátek)",
    "63": "Al-Munáfiqún (Pokrytci)",
    "64": "At-Taghábun (Vzájemné předhánění)",
    "65": "At-Taláq (Rozvod)",
    "66": "At-Tahrím (Zákaz)",
    "67": "Al-Mulk (Království)",
    "68": "Al-Qalam (Třtina)",
    "69": "Al-Háqqa (Nezvratná)",
    "70": "Al-Ma'áridž (Stupně)",
    "71": "Núh (Noe)",
    "72": "Al-Džinn (Džinové)",
    "73": "Al-Muzzammil (Zahalený)",
    "74": "Al-Muddaththir (Přikrytý)",
    "75": "Al-Qijáma (Zmrtvýchvstání)",
    "76": "Al-Insán (Člověk)",
    "77": "Al-Mursalát (Vysílané)",
    "78": "An-Naba' (Zpráva)",
    "79": "An-Názi'át (Vytrhující)",
    "80": "'Abasa (Zamračil se)",
    "81": "At-Takwír (Svinutí)",
    "82": "Al-Infitár (Rozpuknutí)",
    "83": "Al-Mutaffifín (Zkracující na váze)",
    "84": "Al-Inšiqáq (Rozštěpení)",
    "85": "Al-Burúdž (Souhvězdí)",
    "86": "At-Táriq (Noční návštěvník)",
    "87": "Al-A'lá (Nejvyšší)",
    "88": "Al-Ghášija (Zahalující)",
    "89": "Al-Fadžr (Úsvit)",
    "90": "Al-Balad (Město)",
    "91": "Aš-Šams (Slunce)",
    "92": "Al-Lajl (Noc)",
    "93": "Ad-Duhá (Dopoledne)",
    "94": "Aš-Šarh (Otevření)",
    "95": "At-Tín (Fíkovník)",
    "96": "Al-'Alaq (Kapka přilnavá)",
    "97": "Al-Qadr (Úradek)",
    "98": "Al-Bajjina (Jasný důkaz)",
    "99": "Az-Zalzala (Zemětřesení)",
    "100": "Al-'Ádiját (Pádící koně)",
    "101": "Al-Qári'a (Úder)",
    "102": "At-Takáthur (Rozmnožování)",
    "103": "Al-'Asr (Odpolední čas)",
    "104": "Al-Humaza (Pomlouvač)",
    "105": "Al-Fíl (Slon)",
    "106": "Qurajš (Kurajšovci)",
    "107": "Al-Má'ún (Drobné výpomoci)",
    "108": "Al-Kawthar (Hojnost)",
    "109": "Al-Káfirún (Nevěřící)",
    "110": "An-Nasr (Pomoc)",
    "111": "Al-Masad (Zkroucená vlákna)",
    "112": "Al-Ichlás (Čistá víra)",
    "113": "Al-Falaq (Rozbřesk)",
    "114": "An-Nás (Lidé)"
}

DHIVEHI_SURAHS = {
    "1": "އަލްފާތިޙާ (ފޮތް ހުޅުވައިދޭ ސޫރަތް)",
    "2": "އަލްބަޤަރާ (ގެރި)",
    "3": "އާލުޢިމްރާން (ޢިމްރާނުގެ ޢާއިލާ)",
    "4": "އައްނިސާ (އަންހެނުން)",
    "5": "އަލްމާއިދާ (ސުފުރާ)",
    "6": "އަލްއަންޢާމް (ގެރިބަކަރި)",
    "7": "އަލްއަޢުރާފް (އަޢުރާފް)",
    "8": "އަލްއަންފާލް (ޣަނީމާ މުދާ)",
    "9": "އައްތައުބާ (ތައުބާ)",
    "10": "ޔޫނުސް (ޔޫނުސްގެފާނު)",
    "11": "ހޫދު (ހޫދުގެފާނު)",
    "12": "ޔޫސުފް (ޔޫސުފުގެފާނު)",
    "13": "އައްރަޢުދު (ގުގުރި)",
    "14": "އިބްރާހީމް (އިބްރާހީމުގެފާނު)",
    "15": "އަލްޙިޖްރު (ހިޖުރުގެ ވާދީ)",
    "16": "އައްނަޙްލު (ކުޅަނދުރު)",
    "17": "އަލްއިސްރާ (ރޭގަނޑުގެ ދަތުރުފުޅު)",
    "18": "އަލްކަހްފު (ހޮހަޅަ)",
    "19": "މަރްޔަމް (މަރްޔަމްގެފާނު)",
    "20": "ޠާހާ (ޠާހާ)",
    "21": "އަލްއަންބިޔާ (ނަބީބޭކަލުން)",
    "22": "އަލްޙައްޖު (ޙައްޖު)",
    "23": "އަލްމުއުމިނޫން (މުއުމިނުން)",
    "24": "އައްނޫރު (އަލިކަން)",
    "25": "އަލްފުރްޤާން (ޙައްޤާއި ބާޠިލް ވަކިކޮށްދޭ ފޮތް)",
    "26": "އައްޝުޢަރާ (ޅެންވެރިން)",
    "27": "އައްނަމްލު (ހިނި)",
    "28": "އަލްޤަޞަޞް (ވާހަކަތައް)",
    "29": "އަލްޢަންކަބޫތު (ފަންވަތް)",
    "30": "އައްރޫމް (ރޫމީން)",
    "31": "ލުޤްމާން (ލުޤްމާނުގެފާނު)",
    "32": "އައްސަޖްދާ (ސަޖިދަ)",
    "33": "އަލްއަޙްޒާބް (އެކުވި ލަޝްކަރުތައް)",
    "34": "ސަބާ (ސަބާއީން)",
    "35": "ފާޠިރު (ހެއްދެވި ރަސްކަލާނގެ)",
    "36": "ޔާސީން (ޔާސީން)",
    "37": "އައްޞާއްފާތު (ސަފުސަފަށް ތިބޭ މަލާއިކަތުން)",
    "38": "ޞާދު (ޞާދު)",
    "39": "އައްޒުމަރު (ޖަމާޢަތްތައް)",
    "40": "ޣާފިރު (ފާފަފުއްސަވާ ރަސްކަލާނގެ)",
    "41": "ފުޞްޞިލަތު (ތަފްޞީލުކުރައްވާފައިވާ އާޔަތްތައް)",
    "42": "އައްޝޫރާ (މަޝްވަރާ)",
    "43": "އައްޒުޚްރުފް (ރަން ޒީނަތްތެރިކަން)",
    "44": "އައްދުޚާން (ދުން)",
    "45": "އަލްޖާޘިޔާ (ކަކޫމައްޗަށް ތިރިވެފައިވާ މީހުން)",
    "46": "އަލްއަޙްޤާފް (ވެލިފުންޏާއި ފަރުބަދަތައް)",
    "47": "މުޙައްމަދު (މުޙައްމަދުގެފާނު)",
    "48": "އަލްފަތްޙު (ނަޞްރު / ކާމިޔާބު)",
    "49": "އަލްޙުޖުރާތު (ކޮޓަރިކޮޅުތައް)",
    "50": "ޤާފް (ޤާފް)",
    "51": "އައްޛާރިޔާތު (ހިރަފުސް އުފުލާ ވައިރޯޅިތައް)",
    "52": "އައްޠޫރު (ޠޫރު ފަރުބަދަ)",
    "53": "އައްނަޖްމު (ތަރި)",
    "54": "އަލްޤަމަރު (ހަނދު)",
    "55": "އައްރަޙްމާން (ރަޙްމާންވަންތަ ރަސްކަލާނގެ)",
    "56": "އަލްވާޤިޢާ (ޤިޔާމަތް ދުވަސް)",
    "57": "އަލްޙަދީދް (ދަގަނޑު)",
    "58": "އަލްމުޖާދަލާ (ދެބަސްވެ ބަހުސްކުރި އަންހެނާ)",
    "59": "އަލްޙަޝްރު (އެއްކުރެއްވުން)",
    "60": "އަލްމުމްތަޙިނާ (އިމްތިޙާނު ކުރެވޭ އަންހެނާ)",
    "61": "އައްޞައްފު (ސަފު)",
    "62": "އަލްޖުމުޢާ (ހުކުރު ދުވަސް)",
    "63": "އަލްމުނާފިޤޫން (މުނާފިޤުން)",
    "64": "އައްތަޣާބުން (ގެއްލުމާއި ފައިދާ ފާޅުވާ ދުވަސް)",
    "65": "އައްޠަލާޤް (ވަރި)",
    "66": "އައްތަޙްރީމް (ޙަރާމްކުރެއްވުން)",
    "67": "އަލްމުލްކު (ވެރިކަން)",
    "68": "އަލްޤަލަމް (ޤަލަމް)",
    "69": "އަލްޙާޤާ (ޙައްޤުވެގެންވާ ޤިޔާމަތް)",
    "70": "އަލްމަޢާރިޖް (އުޑަށް އަރާ ދަރަޖަތައް)",
    "71": "ނޫޙް (ނޫޙުގެފާނު)",
    "72": "އަލްޖިންނު (ޖިންނީން)",
    "73": "އަލްމުޒައްމިލް (ފޭރާމުން ނިވާވެވަޑައިގެން އިންނެވި ބޭކަލަކު)",
    "74": "އަލްމުއްދައްޘިރު (ފޭރާމުން ނިވާވެވަޑައިގެން އޮންނެވި ބޭކަލަކު)",
    "75": "އަލްޤިޔާމާ (ޤިޔާމަތް ދުވަސް)",
    "76": "އަލްއިންސާން (އިންސާނާ)",
    "77": "އަލްމުރްސަލާތު (ފޮނުއްވާ މަލާއިކަތުން)",
    "78": "އައްނަބާ (ބޮޑުވެގެންވާ ޚަބަރު)",
    "79": "އައްނާޒިޢާތު (ފުރާނަ ދަމައިގަންނަ މަލާއިކަތުން)",
    "80": "ޢަބަސަ (މޫނުފުޅު ކުނިކުރެއްވިއެވެ)",
    "81": "އައްތަކްވީރު (އޮޅައިލެއްވުން)",
    "82": "އަލްއިންފިޠާރު (އުޑު އިރައިގެންދިއުން)",
    "83": "އަލްމުޠައްފިފީން (މިންވަރާއި ބަރުދަނުން އުނިކުރާ މީހުން)",
    "84": "އަލްއިންޝިޤާޤް (އުޑު ފަޅައިގެންދިއުން)",
    "85": "އަލްބުރޫޖް (ބުރުޖުތައް)",
    "86": "އައްޠާރިޤް (ރޭގަނޑު ފާޅުވާ ތަރި)",
    "87": "އަލްއަޢުލާ (އެންމެ މަތިވެރި ރަސްކަލާނގެ)",
    "88": "އަލްޣާޝިޔާ (ފޮރުވައިލާ ޤިޔާމަތް)",
    "89": "އަލްފަޖްރު (ފަތިސްވަގުތު)",
    "90": "އަލްބަލަދު (ރަށް / މައްކާ)",
    "91": "އައްޝަމްސު (އިރު)",
    "92": "އައްލައިލު (ރޭގަނޑު)",
    "93": "އައްޟުޙާ (ހެނދުނުގެ އަލިކަން)",
    "94": "އައްޝަރްޙު (ހިތްޕުޅު ތަނަވަސްކޮށްދެއްވުން)",
    "95": "އައްތީން (ވައްކަންގަސް)",
    "96": "އަލްޢަލަޤް (ގަނޑުލޭކޮޅު)",
    "97": "އަލްޤަދްރު (ޤަދްރު ރޭ)",
    "98": "އަލްބައްޔިނާ (ބަޔާންވެގެންވާ ހެކި)",
    "99": "އައްޒަލްޒަލާ (ބިންހެލުން)",
    "100": "އަލްޢާދިޔާތު (ދުވާ އަސްތައް)",
    "101": "އަލްޤާރިޢާ (ބިރުވެރި އަޑު)",
    "102": "އައްތަކާޘުރު (ގިނަކުރުމުގެ ދަހިވެތިކަން)",
    "103": "އަލްޢަޞްރު (ޒަމާން)",
    "104": "އަލްހުމަޒާ (ދެބައޮޑުވާ މީހާ)",
    "105": "އަލްފީލް (އެތް)",
    "106": "ޤުރައިޝް (ޤުރައިޝު ވަންހަ)",
    "107": "އަލްމާޢޫން (ހިފާގެންގުޅޭ ތަކެތި)",
    "108": "އަލްކައުޘަރު (ކައުޘަރު ކޯރު)",
    "109": "އަލްކާފިރޫން (ކާފިރުން)",
    "110": "އައްނަޞްރު (ނަޞްރު)",
    "111": "އަލްމަސަދު (ކަދުރުރުކުގެ ވާގަނޑު)",
    "112": "އަލްއިޚްލާޞް (އިޚްލާޞްތެރިކަން)",
    "113": "އަލްފަލަޤް (ފަތިހުގެ އަލިކަން)",
    "114": "އައްނާސް (މީސްތަކުން)"
}

BENTUK_KATA_CS = {
    "1. Dhamir": "1. Zájmena (Dhamír / Pronouns)",
    "2. Isim Mawshul": "2. Vztažná zájmena (Ism Mawshúl)",
    "3. Isim Istifham": "3. Tázací zájmena (Ism Istifhám)",
    "4. Isim Syarath": "4. Podmínková slova (Ism Šarath)",
    "5. Isim Isyarah": "5. Ukazovací zájmena (Ism Išárah)",
    "6. Isim Fi'il": "6. Slovesná podstatná jména (Ism Fi'il)",
    "7. Fi'il Jamid": "7. Neohebná slovesa (Fi'il Džámid)"
}

BENTUK_KATA_DV = {
    "1. Dhamir": "1. ޟަމީރުތައް (Dhamir - ކަންކުރާ އިސްމު)",
    "2. Isim Mawshul": "2. އިސްމު މައުޞޫލް (Mawshul - ގުޅުވައިދޭ އިސްމު)",
    "3. Isim Istifham": "3. އިސްމު އިސްތިފްހާމް (Istifham - ސުވާލުކުރާ އިސްމު)",
    "4. Isim Syarath": "4. އިސްމު ޝަރަތު (Syarath - ޝަރުޠުކުރާ އިސްމު)",
    "5. Isim Isyarah": "5. އިސްމު އިޝާރާތް (Isyarah - އިޝާރާތްކުރާ އިސްމު)",
    "6. Isim Fi'il": "6. އިސްމު ފިޢުލު (Isim Fi'il - ފިޢުލުގެ މާނަދޭ އިސްމު)",
    "7. Fi'il Jamid": "7. ފިޢުލު ޖާމިދު (Fi'il Jamid - ބަދަލުނުވާ ފިޢުލު)"
}

BENTUK_HARF_CS = {
    "1. Harf Nafyi": "1. Záporné částice (Harf Nafy)",
    "2. Harf Tahqiq Taswif": "2. Částice potvrzení a budoucnosti (Tahqíq & Taswíf)",
    "3. Harf Syarat": "3. Neřídící podmínkové částice (Harf Šarat)",
    "4. Harf Mashdariyah": "4. Slovesně-jmenné částice (Harf Masdaríja)",
    "5. Harf Zaidah": "5. Zesilující doplňkové částice (Harf Zá'ida)",
    "6. Harf Istifham": "6. Tázací částice (Harf Istifhám)",
    "7. Harf Istitsna": "7. Vylučovací částice (Harf Istithná')",
    "8. Harf Rad'in Wazajrin": "8. Odmítavé a kárací částice (Harf Rad')",
    "9. Harf Rad'in Tahdid": "9. Pobídkové a výčitkové částice (Harf Tahdíd)",
    "10. Harf Ijab": "10. Kladné odpovědní částice (Harf Ídžáb)",
    "11. Harf Tafsir": "11. Vysvětlující částice (Harf Tafsír)",
    "12. Harf Tanbih": "12. Upozorňovací částice (Harf Tanbíh)",
    "13. Harf Ta'lil": "13. Příčinné částice (Harf Ta'líl)",
    "14. Harf Fuja'iyyah": "14. Částice náhlého děje (Harf Fudžá'íja)",
    "15. Harf Istidrak": "15. Opravné a odporovací částice (Harf Istidrák)",
    "16. Harf Ta'ajjub": "16. Zvolací částice podivu (Harf Ta'adžub)",
    "17. Harf Mabany": "17. Počáteční zkratková písmena súr (Muqatta'át)"
}

BENTUK_HARF_DV = {
    "1. Harf Nafyi": "1. ނަފީކުރާ އަކުރު (Harf Nafy)",
    "2. Harf Tahqiq Taswif": "2. ތަޙްޤީޤާއި މުސްތަޤްބަލުގެ އަކުރު (Tahqiq & Taswif)",
    "3. Harf Syarat": "3. ޝަރުޠުގެ އަކުރު (Harf Syarat)",
    "4. Harf Mashdariyah": "4. މަޞްދަރީ އަކުރު (Harf Mashdariyah)",
    "5. Harf Zaidah": "5. އިތުރުކުރެވޭ ގަދަކުރުމުގެ އަކުރު (Harf Zaidah)",
    "6. Harf Istifham": "6. ސުވާލުކުރާ އަކުރު (Harf Istifham)",
    "7. Harf Istitsna": "7. އިސްތިޘްނާގެ އަކުރު (Harf Istitsna)",
    "8. Harf Rad'in Wazajrin": "8. މަނާކުރުމާއި ހުއްޓުވުމުގެ އަކުރު (Harf Rad'in)",
    "9. Harf Rad'in Tahdid": "9. ބާރުއެޅުމާއި ކަންކުރުމަށް އެދޭ އަކުރު (Harf Tahdid)",
    "10. Harf Ijab": "10. ޖަވާބުދިނުމާއި އާނބަސް ބުނާ އަކުރު (Harf Ijab)",
    "11. Harf Tafsir": "11. މާނަބަޔާންކުރާ އަކުރު (Harf Tafsir)",
    "12. Harf Tanbih": "12. ސަމާލުކުރުވާ އަކުރު (Harf Tanbih)",
    "13. Harf Ta'lil": "13. ސަބަބު ބަޔާންކުރާ އަކުރު (Harf Ta'lil)",
    "14. Harf Fuja'iyyah": "14. ކުއްލިއަކަށް ވާކަންކަން އަންގައިދޭ އަކުރު (Harf Fuja'iyyah)",
    "15. Harf Istidrak": "15. އިސްތިދްރާކުގެ އަކުރު (Harf Istidrak)",
    "16. Harf Ta'ajjub": "16. ޢަޖާއިބުވުމުގެ އަކުރު (Harf Ta'ajjub)",
    "17. Harf Mabany": "17. ސޫރަތްތަކުގެ ފެށުމުގައިވާ އަކުރުތައް (Muqatta'at)"
}

CZECH_GRAMMAR = {
    "1. Dhamir__1a": {"arti_cs": "On (3. os. j. č. m. r.)", "desc_cs": "Samostatné osobní zájmeno 3. os. j. č. m. r. (Munfasil)", "jenis_cs": "Samostatné osobní zájmeno"},
    "1. Dhamir__1b": {"arti_cs": "Jeho / Jemu / Ho (Připojené)", "desc_cs": "Připojené zájmeno 3. os. j. č. m. r. (Muttasil)", "jenis_cs": "Připojené zájmeno"},
    "1. Dhamir__1c": {"arti_cs": "Jen Jeho (Samostatné akuzativní)", "desc_cs": "Samostatné akuzativní zájmeno 3. os. j. č. m. r.", "jenis_cs": "Akuzativní zájmeno"},
    "1. Dhamir__2a": {"arti_cs": "Oni dva (Duál)", "desc_cs": "Samostatné zájmeno pro dvojné číslo (duál)", "jenis_cs": "Duálové zájmeno"},
    "1. Dhamir__2b": {"arti_cs": "Jich dvou / Jim dvěma (Připojené)", "desc_cs": "Připojené zájmeno pro dvojné číslo", "jenis_cs": "Připojené duálové zájmeno"},
    "1. Dhamir__3a": {"arti_cs": "Oni (m. r. mn. č.)", "desc_cs": "Samostatné osobní zájmeno 3. os. mn. č. m. r.", "jenis_cs": "Samostatné zájmeno"},
    "1. Dhamir__3b": {"arti_cs": "Jejich / Jim / Je (Připojené)", "desc_cs": "Připojené zájmeno 3. os. mn. č. m. r.", "jenis_cs": "Připojené zájmeno"},
    "1. Dhamir__3c": {"arti_cs": "Jen jim", "desc_cs": "Samostatné akuzativní zájmeno 3. os. mn. č. m. r.", "jenis_cs": "Akuzativní zájmeno"},
    "1. Dhamir__4a": {"arti_cs": "Ona (3. os. j. č. ž. r.)", "desc_cs": "Samostatné osobní zájmeno 3. os. j. č. ž. r.", "jenis_cs": "Samostatné zájmeno"},
    "1. Dhamir__4b": {"arti_cs": "Její / Jí / Ji (Připojené)", "desc_cs": "Připojené zájmeno 3. os. j. č. ž. r.", "jenis_cs": "Připojené zájmeno"},
    "1. Dhamir__5a": {"arti_cs": "Ony (ž. r. mn. č.)", "desc_cs": "Samostatné osobní zájmeno 3. os. mn. č. ž. r.", "jenis_cs": "Samostatné zájmeno"},
    "1. Dhamir__5b": {"arti_cs": "Jejich (ž. r. připojené)", "desc_cs": "Připojené zájmeno 3. os. mn. č. ž. r.", "jenis_cs": "Připojené zájmeno"},
    "1. Dhamir__6a": {"arti_cs": "Ty (2. os. j. č. m. r.)", "desc_cs": "Samostatné osobní zájmeno 2. os. j. č. m. r.", "jenis_cs": "Samostatné zájmeno"},
    "1. Dhamir__6b": {"arti_cs": "Tvůj / Tobě / Tě (Připojené)", "desc_cs": "Připojené zájmeno 2. os. j. č. m. r.", "jenis_cs": "Připojené zájmeno"},
    "1. Dhamir__6c": {"arti_cs": "Pouze Tebe (Vyhrazení uctívání)", "desc_cs": "Samostatné akuzativní zájmeno 2. os. j. č.", "jenis_cs": "Akuzativní zájmeno"},
    "1. Dhamir__7a": {"arti_cs": "Vy dva", "desc_cs": "Samostatné zájmeno pro 2. os. duálu", "jenis_cs": "Duálové zájmeno"},
    "1. Dhamir__7b": {"arti_cs": "Vás dvou (Připojené)", "desc_cs": "Připojené zájmeno pro 2. os. duálu", "jenis_cs": "Připojené duálové zájmeno"},
    "1. Dhamir__8a": {"arti_cs": "Vy (m. r. mn. č.)", "desc_cs": "Samostatné osobní zájmeno 2. os. mn. č. m. r.", "jenis_cs": "Samostatné zájmeno"},
    "1. Dhamir__8b": {"arti_cs": "Váš / Vám / Vás (Připojené)", "desc_cs": "Připojené zájmeno 2. os. mn. č. m. r.", "jenis_cs": "Připojené zájmeno"},
    "1. Dhamir__8c": {"arti_cs": "Pouze vám", "desc_cs": "Samostatné akuzativní zájmeno 2. os. mn. č. m. r.", "jenis_cs": "Akuzativní zájmeno"},
    "1. Dhamir__9a": {"arti_cs": "Ty (2. os. j. č. ž. r.)", "desc_cs": "Samostatné osobní zájmeno 2. os. j. č. ž. r.", "jenis_cs": "Samostatné zájmeno"},
    "1. Dhamir__9b": {"arti_cs": "Tvůj / Tobě (ž. r. připojené)", "desc_cs": "Připojené zájmeno 2. os. j. č. ž. r.", "jenis_cs": "Připojené zájmeno"},
    "1. Dhamir__10a": {"arti_cs": "Vy (ž. r. mn. č.)", "desc_cs": "Samostatné osobní zájmeno 2. os. mn. č. ž. r.", "jenis_cs": "Samostatné zájmeno"},
    "1. Dhamir__10b": {"arti_cs": "Váš (ž. r. připojené)", "desc_cs": "Připojené zájmeno 2. os. mn. č. ž. r.", "jenis_cs": "Připojené zájmeno"},
    "1. Dhamir__11a": {"arti_cs": "Já (1. os. j. č.)", "desc_cs": "Samostatné osobní zájmeno 1. os. j. č.", "jenis_cs": "Samostatné zájmeno"},
    "1. Dhamir__11b": {"arti_cs": "Můj / Mně / Mě (Připojené)", "desc_cs": "Připojené zájmeno 1. os. j. č.", "jenis_cs": "Připojené zájmeno"},
    "1. Dhamir__11c": {"arti_cs": "Pouze mně", "desc_cs": "Samostatné akuzativní zájmeno 1. os. j. č.", "jenis_cs": "Akuzativní zájmeno"},
    "1. Dhamir__12a": {"arti_cs": "My (1. os. mn. č.)", "desc_cs": "Samostatné osobní zájmeno 1. os. mn. č.", "jenis_cs": "Samostatné zájmeno"},
    "1. Dhamir__12b": {"arti_cs": "Náš / Nám / Nás (Připojené)", "desc_cs": "Připojené zájmeno 1. os. mn. č.", "jenis_cs": "Připojené zájmeno"},
    "1. Dhamir__12c": {"arti_cs": "Pouze nám", "desc_cs": "Samostatné akuzativní zájmeno 1. os. mn. č.", "jenis_cs": "Akuzativní zájmeno"},

    "2. Isim Mawshul__1": {"arti_cs": "To, co / Cokoliv (Pro neživotné)", "desc_cs": "Všeobecné vztažné zájmeno pro neživotné věci", "jenis_cs": "Všeobecné vztažné zájmeno"},
    "2. Isim Mawshul__2": {"arti_cs": "Ti, kteří (m. r. mn. č.)", "desc_cs": "Vztažné zájmeno pro rozumné bytosti v množném čísle", "jenis_cs": "Specifické vztažné zájmeno"},
    "2. Isim Mawshul__3": {"arti_cs": "Kdo / Ten, kdo (Pro rozumné)", "desc_cs": "Všeobecné vztažné zájmeno pro lidi a rozumné bytosti", "jenis_cs": "Všeobecné vztažné zájmeno"},
    "2. Isim Mawshul__4": {"arti_cs": "Ten, který (m. r. j. č.)", "desc_cs": "Vztažné zájmeno pro jednotné číslo mužského rodu", "jenis_cs": "Specifické vztažné zájmeno"},
    "2. Isim Mawshul__5": {"arti_cs": "Kterýkoliv / Kdokoliv", "desc_cs": "Přivlastňovací vztažné zájmeno", "jenis_cs": "Vztažné zájmeno"},
    "2. Isim Mawshul__6": {"arti_cs": "Ta, která (ž. r. j. č.)", "desc_cs": "Vztažné zájmeno pro jednotné číslo ženského rodu", "jenis_cs": "Specifické vztažné zájmeno"},
    "2. Isim Mawshul__7": {"arti_cs": "Ty ženy, které (mn. č.)", "desc_cs": "Vztažné zájmeno pro ženy v množném čísle", "jenis_cs": "Specifické ženské vztažné zájmeno"},
    "2. Isim Mawshul__8": {"arti_cs": "Ty ženy, které (mn. č.)", "desc_cs": "Vztažné zájmeno pro ženy v množném čísle", "jenis_cs": "Specifické ženské vztažné zájmeno"},
    "2. Isim Mawshul__9": {"arti_cs": "Ti dva, kteří", "desc_cs": "Duálové vztažné zájmeno", "jenis_cs": "Duálové vztažné zájmeno"},
    "2. Isim Mawshul__10": {"arti_cs": "Kterákoliv (ž. r.)", "desc_cs": "Vztažné zájmeno ženského rodu", "jenis_cs": "Vztažné zájmeno"},

    "3. Isim Istifham__1": {"arti_cs": "Co? / Co je to?", "desc_cs": "Tázací zájmeno pro neživotné věci", "jenis_cs": "Tázací zájmeno"},
    "3. Isim Istifham__2": {"arti_cs": "Kdo? / Kdo je?", "desc_cs": "Tázací zájmeno pro osoby a rozumné bytosti", "jenis_cs": "Tázací zájmeno"},
    "3. Isim Istifham__3": {"arti_cs": "Jak? / Jakým způsobem?", "desc_cs": "Tázací zájmeno tázající se na stav", "jenis_cs": "Tázací zájmeno stavu"},
    "3. Isim Istifham__4": {"arti_cs": "Kde? / Kam?", "desc_cs": "Tázací zájmeno tázající se na místo", "jenis_cs": "Tázací zájmeno místa"},
    "3. Isim Istifham__5": {"arti_cs": "Kolik? / Jaké množství?", "desc_cs": "Tázací zájmeno tázající se na počet", "jenis_cs": "Tázací zájmeno počtu"},
    "3. Isim Istifham__6": {"arti_cs": "Kdy? / V jaký čas?", "desc_cs": "Tázací zájmeno tázající se na čas", "jenis_cs": "Tázací zájmeno času"},
    "3. Isim Istifham__7": {"arti_cs": "Kdy nastane? (Pro Den zmrtvýchvstání)", "desc_cs": "Tázací zájmeno pro velké budoucí události", "jenis_cs": "Tázací zájmeno času"},
    "3. Isim Istifham__8": {"arti_cs": "Odkud? / Jak to?", "desc_cs": "Tázací zájmeno tázající se na původ či příčinu", "jenis_cs": "Tázací zájmeno"},

    "4. Isim Syarath__1": {"arti_cs": "Kdo / Kdokoliv", "desc_cs": "Podmínkové zájmeno pro osoby vyžadující apokopát", "jenis_cs": "Podmínkové zájmeno"},
    "4. Isim Syarath__2": {"arti_cs": "Cokoliv / Co učiníte", "desc_cs": "Podmínkové zájmeno pro věci", "jenis_cs": "Podmínkové zájmeno"},
    "4. Isim Syarath__3": {"arti_cs": "Když / V okamžiku, kdy", "desc_cs": "Časové podmínkové slovo pro budoucnost", "jenis_cs": "Časové podmínkové slovo"},
    "4. Isim Syarath__4": {"arti_cs": "Ať už cokoliv", "desc_cs": "Všeobecné podmínkové zájmeno", "jenis_cs": "Podmínkové zájmeno"},
    "4. Isim Syarath__5": {"arti_cs": "Kdekoliv / Kamkoliv", "desc_cs": "Místní podmínkové slovo", "jenis_cs": "Místní podmínkové slovo"},
    "4. Isim Syarath__6": {"arti_cs": "Kdekoliv se nacházíte", "desc_cs": "Zesílené místní podmínkové slovo", "jenis_cs": "Místní podmínkové slovo"},
    "4. Isim Syarath__7": {"arti_cs": "V jakémkoliv stavu", "desc_cs": "Stavové podmínkové slovo", "jenis_cs": "Stavové podmínkové slovo"},
    "4. Isim Syarath__8": {"arti_cs": "Kterýkoliv", "desc_cs": "Přivlastňovací podmínkové slovo", "jenis_cs": "Podmínkové slovo"},

    "5. Isim Isyarah__1": {"arti_cs": "To / Ona kniha (Vzdálené m. r.)", "desc_cs": "Ukazovací zájmeno pro vzdálené předměty m. r.", "jenis_cs": "Ukazovací zájmeno vzdálené"},
    "5. Isim Isyarah__2": {"arti_cs": "Tento / Toto (Blízké m. r.)", "desc_cs": "Ukazovací zájmeno pro blízké předměty m. r.", "jenis_cs": "Ukazovací zájmeno blízké"},
    "5. Isim Isyarah__3": {"arti_cs": "Tito / Tyto (Blízké mn. č.)", "desc_cs": "Ukazovací zájmeno pro blízké množné číslo", "jenis_cs": "Ukazovací zájmeno blízké"},
    "5. Isim Isyarah__4": {"arti_cs": "Tamti / Oni (Vzdálené mn. č.)", "desc_cs": "Ukazovací zájmeno pro vzdálené množné číslo", "jenis_cs": "Ukazovací zájmeno vzdálené"},
    "5. Isim Isyarah__5": {"arti_cs": "Tato (Blízké ž. r.)", "desc_cs": "Ukazovací zájmeno pro blízké ženské jednotné číslo", "jenis_cs": "Ukazovací zájmeno blízké"},
    "5. Isim Isyarah__6": {"arti_cs": "Tamta (Vzdálené ž. r.)", "desc_cs": "Ukazovací zájmeno pro vzdálené ženské jednotné číslo", "jenis_cs": "Ukazovací zájmeno vzdálené"},
    "5. Isim Isyarah__7": {"arti_cs": "Tam / Na onom místě", "desc_cs": "Ukazovací zájmeno pro vzdálené místo", "jenis_cs": "Místní ukazovací zájmeno"},
    "5. Isim Isyarah__8": {"arti_cs": "Zde / Na tomto místě", "desc_cs": "Ukazovací zájmeno pro blízké místo", "jenis_cs": "Místní ukazovací zájmeno"},
    "5. Isim Isyarah__9": {"arti_cs": "Tyto dvě věci (Vzdálené m. r.)", "desc_cs": "Duálové ukazovací zájmeno", "jenis_cs": "Duálové ukazovací zájmeno"},
    "5. Isim Isyarah__10": {"arti_cs": "Tyto dvě věci (Vzdálené ž. r.)", "desc_cs": "Duálové ukazovací zájmeno", "jenis_cs": "Duálové ukazovací zájmeno"},

    "6. Isim Fi'il__1": {"arti_cs": "Jak je to vzdálené! (Hajháta)", "desc_cs": "Slovesné jméno pro minulý čas", "jenis_cs": "Slovesné jméno minulého času"},
    "6. Isim Fi'il__2": {"arti_cs": "Uff! / Běda! (Uff)", "desc_cs": "Slovesné jméno vyjadřující omrzelost", "jenis_cs": "Slovesné jméno přítomného času"},
    "6. Isim Fi'il__3": {"arti_cs": "Pojďte! / Přineste!", "desc_cs": "Rozkazovací slovesné jméno", "jenis_cs": "Rozkazovací slovesné jméno"},
    "6. Isim Fi'il__4": {"arti_cs": "Vezměte! / Čtěte!", "desc_cs": "Rozkazovací slovesné jméno", "jenis_cs": "Rozkazovací slovesné jméno"},
    "6. Isim Fi'il__5": {"arti_cs": "Mějte se na pozoru! / Držte se!", "desc_cs": "Rozkazovací slovesné jméno vzniklé z předložky", "jenis_cs": "Rozkazovací slovesné jméno"},
    "6. Isim Fi'il__6": {"arti_cs": "Vezměte si to!", "desc_cs": "Rozkazovací slovesné jméno vzniklé z příslovce", "jenis_cs": "Rozkazovací slovesné jméno"},
    "6. Isim Fi'il__7": {"arti_cs": "Jak podivuhodné!", "desc_cs": "Slovesné jméno vyjadřující údiv", "jenis_cs": "Slovesné jméno"},
    "6. Isim Fi'il__8": {"arti_cs": "Ustupte! / Zde to máte", "desc_cs": "Rozkazovací slovesné jméno", "jenis_cs": "Rozkazovací slovesné jméno"},

    "7. Fi'il Jamid__1": {"arti_cs": "Jak výtečný! (Ni'ma)", "desc_cs": "Neohebné chvalné sloveso", "jenis_cs": "Chvalné neohebné sloveso"},
    "7. Fi'il Jamid__2": {"arti_cs": "Jak hanebný! (Bi'sa)", "desc_cs": "Neohebné kárací sloveso", "jenis_cs": "Kárací neohebné sloveso"},
    "7. Fi'il Jamid__3": {"arti_cs": "Není / Nebyl (Laysa)", "desc_cs": "Neohebné záporné sponové sloveso", "jenis_cs": "Záporné neohebné sloveso"},
    "7. Fi'il Jamid__4": {"arti_cs": "Snad / Je naděje ('Asá)", "desc_cs": "Neohebné sloveso naděje", "jenis_cs": "Sloveso naděje"},
    "7. Fi'il Jamid__5": {"arti_cs": "Jak je to zlé! (Sá'a)", "desc_cs": "Neohebné kárací sloveso", "jenis_cs": "Kárací neohebné sloveso"},
    "7. Fi'il Jamid__6": {"arti_cs": "Jak příjemné!", "desc_cs": "Složené chvalné sloveso", "jenis_cs": "Chvalné sloveso"},
    "7. Fi'il Jamid__7": {"arti_cs": "Požehnaný a Vznešený! (Tabáraka)", "desc_cs": "Posvátné neohebné sloveso Boží velikosti", "jenis_cs": "Posvátné neohebné sloveso"}
}

DHIVEHI_GRAMMAR = {
    "1. Dhamir__1a": {"arti_dv": "އޭނާ (ފިރިހެން އެކަކު)", "desc_dv": "3 ވަނަ މީހާގެ ވަކިންވާ ޟަމީރު (މުންފަޞިލް)", "jenis_dv": "ވަކިންވާ ޟަމީރު"},
    "1. Dhamir__1b": {"arti_dv": "އޭނާގެ / އޭނާއަށް (ގުޅިފައިވާ)", "desc_dv": "3 ވަނަ މީހާގެ ގުޅިފައިވާ ޟަމީރު (މުއްތަޞިލް)", "jenis_dv": "ގުޅިފައިވާ ޟަމީރު"},
    "1. Dhamir__1c": {"arti_dv": "ހަމައެކަނި އޭނާއަށް", "desc_dv": "3 ވަނަ މީހާގެ މަފްޢޫލު ވަކިންވާ ޟަމީރު", "jenis_dv": "ވަކިންވާ ޟަމީރު"},
    "1. Dhamir__2a": {"arti_dv": "އެ ދެމީހުން", "desc_dv": "ތަޘްނިޔާ (ދެމީހުންގެ) ވަކިންވާ ޟަމީރު", "jenis_dv": "ތަޘްނިޔާ ޟަމީރު"},
    "1. Dhamir__2b": {"arti_dv": "އެ ދެމީހުންގެ (ގުޅިފައިވާ)", "desc_dv": "ތަޘްނިޔާ ގުޅިފައިވާ ޟަމީރު", "jenis_dv": "ގުޅިފައިވާ ޟަމީރު"},
    "1. Dhamir__3a": {"arti_dv": "އެބައިމީހުން (ފިރިހެން ގިނަ)", "desc_dv": "3 ވަނަ މީހާގެ ގިނަ މީހުންގެ ވަކިންވާ ޟަމީރު", "jenis_dv": "ވަކިންވާ ޟަމީރު"},
    "1. Dhamir__3b": {"arti_dv": "އެބައިމީހުންގެ (ގުޅިފައިވާ)", "desc_dv": "3 ވަނަ މީހާގެ ގިނަ މީހުންގެ ގުޅިފައިވާ ޟަމީރު", "jenis_dv": "ގުޅިފައިވާ ޟަމީރު"},
    "1. Dhamir__3c": {"arti_dv": "ހަމައެކަނި އެބައިމީހުންނަށް", "desc_dv": "ގިނަ މީހުންގެ މަފްޢޫލު ވަކިންވާ ޟަމީރު", "jenis_dv": "ވަކިންވާ ޟަމީރު"},
    "1. Dhamir__4a": {"arti_dv": "އޭނާ (އަންހެން އެކަކު)", "desc_dv": "3 ވަނަ މީހާގެ އަންހެން ވަކިންވާ ޟަމީރު", "jenis_dv": "ވަކިންވާ ޟަމީރު"},
    "1. Dhamir__4b": {"arti_dv": "އޭނާގެ (އަންހެން ގުޅިފައިވާ)", "desc_dv": "3 ވަނަ މީހާގެ އަންހެން ގުޅިފައިވާ ޟަމީރު", "jenis_dv": "ގުޅިފައިވާ ޟަމީރު"},
    "1. Dhamir__5a": {"arti_dv": "އެކަނބަލުން (އަންހެން ގިނަ)", "desc_dv": "3 ވަނަ މީހާގެ އަންހެން ގިނަ މީހުންގެ ވަކިންވާ ޟަމީރު", "jenis_dv": "ވަކިންވާ ޟަމީރު"},
    "1. Dhamir__5b": {"arti_dv": "އެކަނބަލުންގެ (ގުޅިފައިވާ)", "desc_dv": "އަންހެން ގިނަ މީހުންގެ ގުޅިފައިވާ ޟަމީރު", "jenis_dv": "ގުޅިފައިވާ ޟަމީރު"},
    "1. Dhamir__6a": {"arti_dv": "ކަލޭގެފާނު / ތިބާ (ފިރިހެން އެކަކު)", "desc_dv": "2 ވަނަ މީހާގެ ވަކިންވާ ޟަމީރު", "jenis_dv": "ވަކިންވާ ޟަމީރު"},
    "1. Dhamir__6b": {"arti_dv": "ތިބާގެ / ކަލޭގެފާނަށް (ގުޅިފައިވާ)", "desc_dv": "2 ވަނަ މީހާގެ ގުޅިފައިވާ ޟަމީރު", "jenis_dv": "ގުޅިފައިވާ ޟަމީރު"},
    "1. Dhamir__6c": {"arti_dv": "ހަމައެކަނި އިބަރަސްކަލާނގެއަށް (އަޅުކަމުގައި ޚާއްޞަކުރުން)", "desc_dv": "2 ވަނަ މީހާގެ ޚާއްޞަ މަފްޢޫލު ޟަމީރު", "jenis_dv": "ވަކިންވާ ޟަމީރު"},
    "1. Dhamir__7a": {"arti_dv": "ތިޔަ ދެމީހުން", "desc_dv": "2 ވަނަ މީހާގެ ދެމީހުންގެ ވަކިންވާ ޟަމީރު", "jenis_dv": "ތަޘްނިޔާ ޟަމީރު"},
    "1. Dhamir__7b": {"arti_dv": "ތިޔަ ދެމީހުންގެ (ގުޅިފައިވާ)", "desc_dv": "2 ވަނަ މީހާގެ ދެމީހުންގެ ގުޅިފައިވާ ޟަމީރު", "jenis_dv": "ގުޅިފައިވާ ޟަމީރު"},
    "1. Dhamir__8a": {"arti_dv": "ތިޔަބައިމީހުން (ފިރިހެން ގިނަ)", "desc_dv": "2 ވަނަ މީހާގެ ގިނަ މީހުންގެ ވަކިންވާ ޟަމީރު", "jenis_dv": "ވަކިންވާ ޟަމީރު"},
    "1. Dhamir__8b": {"arti_dv": "ތިޔަބައިމީހުންގެ (ގުޅިފައިވާ)", "desc_dv": "2 ވަނަ މީހާގެ ގިނަ މީހުންގެ ގުޅިފައިވާ ޟަމީރު", "jenis_dv": "ގުޅިފައިވާ ޟަމީރު"},
    "1. Dhamir__8c": {"arti_dv": "ހަމައެކަނި ތިޔަބައިމީހުންނަށް", "desc_dv": "2 ވަނަ މީހާގެ ގިނަ މީހުންގެ މަފްޢޫލު ޟަމީރު", "jenis_dv": "ވަކިންވާ ޟަމީރު"},
    "1. Dhamir__9a": {"arti_dv": "ތިބާ (އަންހެން އެކަކު)", "desc_dv": "2 ވަނަ މީހާގެ އަންހެން ވަކިންވާ ޟަމީރު", "jenis_dv": "ވަކިންވާ ޟަމީރު"},
    "1. Dhamir__9b": {"arti_dv": "ތިބާގެ (އަންހެން ގުޅިފައިވާ)", "desc_dv": "2 ވަނަ މީހާގެ އަންހެން ގުޅިފައިވާ ޟަމީރު", "jenis_dv": "ގުޅިފައިވާ ޟަމީރު"},
    "1. Dhamir__10a": {"arti_dv": "ތިޔަކަނބަލުން (އަންހެން ގިނަ)", "desc_dv": "2 ވަނަ މީހާގެ އަންހެން ގިނަ މީހުންގެ ވަކިންވާ ޟަމީރު", "jenis_dv": "ވަކިންވާ ޟަމީރު"},
    "1. Dhamir__10b": {"arti_dv": "ތިޔަކަނބަލުންގެ (ގުޅިފައިވާ)", "desc_dv": "އަންހެން ގިނަ މީހުންގެ ގުޅިފައިވާ ޟަމީރު", "jenis_dv": "ގުޅިފައިވާ ޟަމީރު"},
    "1. Dhamir__11a": {"arti_dv": "ތިމަން (1 ވަނަ މީހާ އެކަކު)", "desc_dv": "1 ވަނަ މީހާގެ ވަކިންވާ ޟަމީރު (މުތަކައްލިމް)", "jenis_dv": "ވަކިންވާ ޟަމީރު"},
    "1. Dhamir__11b": {"arti_dv": "ތިމަންގެ / ތިމަންނާއަށް (ގުޅިފައިވާ)", "desc_dv": "1 ވަނަ މީހާގެ ގުޅިފައިވާ ޟަމީރު", "jenis_dv": "ގުޅިފައިވާ ޟަމީރު"},
    "1. Dhamir__11c": {"arti_dv": "ހަމައެކަނި ތިމަންނާއަށް", "desc_dv": "1 ވަނަ މީހާގެ މަފްޢޫލު ވަކިންވާ ޟަމީރު", "jenis_dv": "ވަކިންވާ ޟަމީރު"},
    "1. Dhamir__12a": {"arti_dv": "ތިމަންމެން / ތިމަންރަސްކަލާނގެ (ގިނަ)", "desc_dv": "1 ވަނަ މީހާގެ ގިނަ މީހުންގެ ވަކިންވާ ޟަމީރު", "jenis_dv": "ވަކިންވާ ޟަމީރު"},
    "1. Dhamir__12b": {"arti_dv": "ތިމަންމެންގެ (ގުޅިފައިވާ)", "desc_dv": "1 ވަނަ މީހާގެ ގިނަ މީހުންގެ ގުޅިފައިވާ ޟަމީރު", "jenis_dv": "ގުޅިފައިވާ ޟަމީރު"},
    "1. Dhamir__12c": {"arti_dv": "ހަމައެކަނި ތިމަންމެންނަށް", "desc_dv": "1 ވަނަ މީހާގެ ގިނަ މީހުންގެ މަފްޢޫލު ޟަމީރު", "jenis_dv": "ވަކިންވާ ޟަމީރު"},

    "2. Isim Mawshul__1": {"arti_dv": "އެ ތަކެތި / އެކަންތައް (ބުއްދިނެތް ތަކެއްޗަށް)", "desc_dv": "ބުއްދިނެތް ތަކެއްޗަށް ބޭނުންކުރާ ޢާންމު އިސްމު މައުޞޫލް", "jenis_dv": "ޢާންމު އިސްމު މައުޞޫލް"},
    "2. Isim Mawshul__2": {"arti_dv": "އެބައިމީހުން (ބުއްދިވެރި ގިނަ މީހުން)", "desc_dv": "ގިނަ މީހުންނަށް ބޭނުންކުރާ ޚާއްޞަ އިސްމު މައުޞޫލް", "jenis_dv": "ޚާއްޞަ އިސްމު މައުޞޫލް"},
    "2. Isim Mawshul__3": {"arti_dv": "އެމީހަކު / ކޮންމެ މީހަކު (ބުއްދިވެރިންނަށް)", "desc_dv": "ބުއްދިވެރިންނަށް ބޭނުންކުރާ ޢާންމު އިސްމު މައުޞޫލް", "jenis_dv": "ޢާންމު އިސްމު މައުޞޫލް"},
    "2. Isim Mawshul__4": {"arti_dv": "އެމީހާ / އެ ފަރާތް (ފިރިހެން އެކަކު)", "desc_dv": "އެއްޗަކަށް ބޭނުންކުރާ ޚާއްޞަ އިސްމު މައުޞޫލް", "jenis_dv": "ޚާއްޞަ އިސްމު މައުޞޫލް"},
    "2. Isim Mawshul__5": {"arti_dv": "ކޮންމެ އެއްޗެއް / ކޮންމެ މީހަކު", "desc_dv": "އިޟާފަތްވާ އިސްމު މައުޞޫލް", "jenis_dv": "އިސްމު މައުޞޫލް"},
    "2. Isim Mawshul__6": {"arti_dv": "އެ އަންހެނާ (އަންހެން އެކަކު)", "desc_dv": "އަންހެން އެކަކަށް ބޭނުންކުރާ އިސްމު މައުޞޫލް", "jenis_dv": "ޚާއްޞަ އިސްމު މައުޞޫލް"},
    "2. Isim Mawshul__7": {"arti_dv": "އެ ކަނބަލުން (އަންހެން ގިނަ)", "desc_dv": "އަންހެން ގިނަ މީހުންނަށް ބޭނުންކުރާ އިސްމު މައުޞޫލް", "jenis_dv": "އިސްމު މައުޞޫލް"},
    "2. Isim Mawshul__8": {"arti_dv": "އެ ކަނބަލުން (އަންހެން ގިނަ)", "desc_dv": "އަންހެން ގިނަ މީހުންނަށް ބޭނުންކުރާ އިސްމު މައުޞޫލް", "jenis_dv": "އިސްމު މައުޞޫލް"},
    "2. Isim Mawshul__9": {"arti_dv": "އެ ދެމީހުން", "desc_dv": "ތަޘްނިޔާ އިސްމު މައުޞޫލް", "jenis_dv": "ތަޘްނިޔާ އިސްމު މައުޞޫލް"},
    "2. Isim Mawshul__10": {"arti_dv": "ކޮންމެ އަންހެނަކު", "desc_dv": "އަންހެން އިސްމު މައުޞޫލް", "jenis_dv": "އިސްމު މައުޞޫލް"},

    "3. Isim Istifham__1": {"arti_dv": "ކޮން އެއްޗެއް؟ / ކީއް؟", "desc_dv": "ތަކެއްޗާމެދު ސުވާލުކުރާ އިސްމު", "jenis_dv": "ސުވާލުކުރާ އިސްމު"},
    "3. Isim Istifham__2": {"arti_dv": "ކާކު؟ / ކޮންބައެއް؟", "desc_dv": "މީހުންނާމެދު ސުވާލުކުރާ އިސްމު", "jenis_dv": "ސުވާލުކުރާ އިސްމު"},
    "3. Isim Istifham__3": {"arti_dv": "ކިހިނެއް؟ / ކޮންފަދައަކުން؟", "desc_dv": "ޙާލަތާމެދު ސުވާލުކުރާ އިސްމު", "jenis_dv": "ޙާލަތުގެ ސުވާލު އިސްމު"},
    "3. Isim Istifham__4": {"arti_dv": "ކޮންތާކު؟ / ކޮންދިމާއަކަށް؟", "desc_dv": "ތަނާމެދު ސުވާލުކުރާ އިސްމު", "jenis_dv": "ތަނުގެ ސުވާލު އިސްމު"},
    "3. Isim Istifham__5": {"arti_dv": "ކިތައް؟ / ކިހާވަރަކަށް؟", "desc_dv": "ޢަދަދާމެދު ސުވާލުކުރާ އިސްމު", "jenis_dv": "ޢަދަދުގެ ސުވާލު އިސްމު"},
    "3. Isim Istifham__6": {"arti_dv": "ކޮންއިރަކު؟", "desc_dv": "ވަގުތާމެދު ސުވާލުކުރާ އިސްމު", "jenis_dv": "ވަގުތުގެ ސުވާލު އިސްމު"},
    "3. Isim Istifham__7": {"arti_dv": "އެކަން ވާނީ ކޮންއިރަކު؟ (ޤިޔާމަތް ފަދަ ބޮޑެތި ކަންކަމަށް)", "desc_dv": "މުސްތަޤްބަލުގެ ބޮޑެތި ކަންކަމަށް ސުވާލުކުރާ އިސްމު", "jenis_dv": "ވަގުތުގެ ސުވާލު އިސްމު"},
    "3. Isim Istifham__8": {"arti_dv": "ކޮންތާކުން؟ / ކިހިނަކުން؟", "desc_dv": "ކަމުގެ އަޞްލާމެދު ސުވާލުކުރާ އިސްމު", "jenis_dv": "ސުވާލުކުރާ އިސްމު"},

    "4. Isim Syarath__1": {"arti_dv": "ކޮންމެ މީހަކު / އެމީހަކު", "desc_dv": "މީހުންނަށް ބޭނުންކުރާ ޝަރުޠުގެ އިސްމު", "jenis_dv": "ޝަރުޠުގެ އިސްމު"},
    "4. Isim Syarath__2": {"arti_dv": "ކޮންމެ ކަމެއް / ކޮންމެ އެއްޗެއް", "desc_dv": "ތަކެއްޗަށް ބޭނުންކުރާ ޝަރުޠުގެ އިސްމު", "jenis_dv": "ޝަރުޠުގެ އިސްމު"},
    "4. Isim Syarath__3": {"arti_dv": "އެހިނދު / އެ ވަގުތު", "desc_dv": "ވަގުތު އަންގައިދޭ ޝަރުޠުގެ އިސްމު", "jenis_dv": "ވަގުތުގެ ޝަރުޠު"},
    "4. Isim Syarath__4": {"arti_dv": "ކޮންމެ މިންވަރަކަށް ނަމަވެސް", "desc_dv": "ޢާންމު ޝަރުޠުގެ އިސްމު", "jenis_dv": "ޝަރުޠުގެ އިސްމު"},
    "4. Isim Syarath__5": {"arti_dv": "ކޮންމެ ތަނެއްގައި ވިޔަސް", "desc_dv": "ތަން އަންގައިދޭ ޝަރުޠުގެ އިސްމު", "jenis_dv": "ތަނުގެ ޝަރުޠު"},
    "4. Isim Syarath__6": {"arti_dv": "ތިޔަބައިމީހުން ތިބި ކޮންމެ ތަނެއްގައި", "desc_dv": "ތަން އަންގައިދޭ ޝަރުޠުގެ އިސްމު", "jenis_dv": "ތަނުގެ ޝަރުޠު"},
    "4. Isim Syarath__7": {"arti_dv": "ކޮންމެ ޙާލަތެއްގައި ވިޔަސް", "desc_dv": "ޙާލަތުގެ ޝަރުޠުގެ އިސްމު", "jenis_dv": "ޙާލަތުގެ ޝަރުޠު"},
    "4. Isim Syarath__8": {"arti_dv": "ކޮންމެ އެއްޗެއް ނަމަވެސް", "desc_dv": "އިޟާފަތްވާ ޝަރުޠުގެ އިސްމު", "jenis_dv": "ޝަރުޠުގެ އިސްމު"},

    "5. Isim Isyarah__1": {"arti_dv": "އެ ފޮތް / އެ އެތި (ދުރު ފިރިހެން)", "desc_dv": "ދުރުގައިވާ ތަކެއްޗަށް އިޝާރާތްކުރާ އިސްމު", "jenis_dv": "ދުރުގެ އިޝާރާތް"},
    "5. Isim Isyarah__2": {"arti_dv": "މި / މިއީ (ކައިރި ފިރިހެން)", "desc_dv": "ކައިރީގައިވާ އެއްޗަކަށް އިޝާރާތްކުރާ އިސްމު", "jenis_dv": "ކައިރީގެ އިޝާރާތް"},
    "5. Isim Isyarah__3": {"arti_dv": "މިބައިމީހުން / މިތަކެތި (ކައިރި ގިނަ)", "desc_dv": "ކައިރީގެ ގިނަ ތަކެއްޗަށް އިޝާރާތްކުރާ އިސްމު", "jenis_dv": "ކައިރީގެ އިޝާރާތް"},
    "5. Isim Isyarah__4": {"arti_dv": "އެބައިމީހުން / އެތަކެތި (ދުރު ގިނަ)", "desc_dv": "ދުރުގެ ގިނަ ތަކެއްޗަށް އިޝާރާތްކުރާ އިސްމު", "jenis_dv": "ދުރުގެ އިޝާރާތް"},
    "5. Isim Isyarah__5": {"arti_dv": "މި (ކައިރި އަންހެން)", "desc_dv": "ކައިރީގައިވާ އަންހެން އެއްޗަކަށް އިޝާރާތްކުރާ އިސްމު", "jenis_dv": "ކައިރީގެ އިޝާރާތް"},
    "5. Isim Isyarah__6": {"arti_dv": "އެ (ދުރު އަންހެން)", "desc_dv": "ދުރުގައިވާ އަންހެން އެއްޗަކަށް އިޝާރާތްކުރާ އިސްމު", "jenis_dv": "ދުރުގެ އިޝާރާތް"},
    "5. Isim Isyarah__7": {"arti_dv": "އެތާނގައި / އެތަނުގައި", "desc_dv": "ދުރު ތަނަކަށް އިޝާރާތްކުރާ އިސްމު", "jenis_dv": "ތަނުގެ އިޝާރާތް"},
    "5. Isim Isyarah__8": {"arti_dv": "މިތާނގައި / މިތަނުގައި", "desc_dv": "ކައިރި ތަނަކަށް އިޝާރާތްކުރާ އިސްމު", "jenis_dv": "ތަނުގެ އިޝާރާތް"},
    "5. Isim Isyarah__9": {"arti_dv": "އެ ދެ އެތި", "desc_dv": "ތަޘްނިޔާ އިޝާރާތްކުރާ އިސްމު", "jenis_dv": "ތަޘްނިޔާ އިޝާރާތް"},
    "5. Isim Isyarah__10": {"arti_dv": "އެ ދެ އެތި (އަންހެން)", "desc_dv": "އަންހެން ތަޘްނިޔާ އިޝާރާތްކުރާ އިސްމު", "jenis_dv": "ތަޘްނިޔާ އިޝާރާތް"},

    "6. Isim Fi'il__1": {"arti_dv": "އެކަން ކިހާ ދުރުހެއްޔެވެ! (ހައިހާތަ)", "desc_dv": "މާޒީގެ މާނަދޭ އިސްމު ފިޢުލު", "jenis_dv": "މާޒީގެ އިސްމު ފިޢުލު"},
    "6. Isim Fi'il__2": {"arti_dv": "އުއްފު! / ފޫހިކަން ފާޅުކުރުން (އުއްފް)", "desc_dv": "މުޟާރިޢުގެ މާނަދޭ ފޫހިކަން ފާޅުކުރާ އިސްމު ފިޢުލު", "jenis_dv": "މުޟާރިޢުގެ އިސްމު ފިޢުލު"},
    "6. Isim Fi'il__3": {"arti_dv": "އަންނާށެވެ! / ގެންނާށެވެ!", "desc_dv": "އަމުރުގެ މާނަދޭ އިސްމު ފިޢުލު", "jenis_dv": "އަމުރުގެ އިސްމު ފިޢުލު"},
    "6. Isim Fi'il__4": {"arti_dv": "ހިފާށެވެ! / ކިޔާށެވެ!", "desc_dv": "އަމުރުގެ މާނަދޭ އިސްމު ފިޢުލު", "jenis_dv": "އަމުރުގެ އިސްމު ފިޢުލު"},
    "6. Isim Fi'il__5": {"arti_dv": "ސަމާލުވާށެވެ! / ހިފަހައްޓާށެވެ!", "desc_dv": "ޖައްރުއަކުރަކުން އުފެދިފައިވާ އަމުރުގެ އިސްމު ފިޢުލު", "jenis_dv": "އަމުރުގެ އިސްމު ފިޢުލު"},
    "6. Isim Fi'il__6": {"arti_dv": "ހިފާށެވެ!", "desc_dv": "ޒަރްފަކުން އުފެދިފައިވާ އަމުރުގެ އިސްމު ފިޢުލު", "jenis_dv": "އަމުރުގެ އިސްމު ފިޢުލު"},
    "6. Isim Fi'il__7": {"arti_dv": "ޢަޖާއިބުވެއްޖެއެވެ!", "desc_dv": "ޢަޖާއިބުވުން ދައްކުވައިދޭ އިސްމު ފިޢުލު", "jenis_dv": "އިސްމު ފިޢުލު"},
    "6. Isim Fi'il__8": {"arti_dv": "ދުރަށްދާށެވެ! / މިއޮތީއެވެ", "desc_dv": "އަމުރުގެ މާނަދޭ އިސްމު ފިޢުލު", "jenis_dv": "އަމުރުގެ އިސްމު ފިޢުލު"},

    "7. Fi'il Jamid__1": {"arti_dv": "ކިހާ ރަނގަޅުހެއްޔެވެ! (ނިޢުމަ)", "desc_dv": "މަދަޙައިގެ ބަދަލުނުވާ ފިޢުލު", "jenis_dv": "މަދަޙައިގެ ފިޢުލު"},
    "7. Fi'il Jamid__2": {"arti_dv": "ކިހާ ނުބައިހެއްޔެވެ! (ބިއުސަ)", "desc_dv": "ނުބައިކަން ބަޔާންކުރާ ބަދަލުނުވާ ފިޢުލު", "jenis_dv": "މަލާމާތުގެ ފިޢުލު"},
    "7. Fi'il Jamid__3": {"arti_dv": "ނޫނެވެ / ނުވެއެވެ (ލައިސަ)", "desc_dv": "ނަފީކުރާ ބަދަލުނުވާ ފިޢުލު", "jenis_dv": "ނަފީގެ ފިޢުލު"},
    "7. Fi'il Jamid__4": {"arti_dv": "އުންމީދުކުރެވެއެވެ / ފަހަރެއްގައި (ޢަސާ)", "desc_dv": "އުންމީދުކުރާ ބަދަލުނުވާ ފިޢުލު", "jenis_dv": "އުންމީދުގެ ފިޢުލު"},
    "7. Fi'il Jamid__5": {"arti_dv": "ކިހާ ނުބައިވެގެންވާ ކަމެއްހެއްޔެވެ! (ސާއަ)", "desc_dv": "ނުބައިކަން ބަޔާންކުރާ ބަދަލުނުވާ ފިޢުލު", "jenis_dv": "މަލާމާތުގެ ފިޢުލު"},
    "7. Fi'il Jamid__6": {"arti_dv": "ކިހާ ހިތްގައިމުހެއްޔެވެ!", "desc_dv": "މަދަޙައިގެ ފިޢުލު", "jenis_dv": "މަދަޙައިގެ ފިޢުލު"},
    "7. Fi'il Jamid__7": {"arti_dv": "ބަރަކާތްތެރިވެ މަތިވެރިވެވޮޑިގެންފިއެވެ! (ތަބާރަކަ)", "desc_dv": "މާތް ﷲ އަށް ޚާއްޞަ މަތިވެރި ބަދަލުނުވާ ފިޢުލު", "jenis_dv": "މާތް ފިޢުލު"}
}

CZECH_HARF_GRAMMAR = {
    "1. Harf Nafyi__1": {"arti_cs": "Ne / Není (Má - všeobecný zápor)", "desc_cs": "Neřídící záporná částice pro minulý, přítomný čas a jmenné věty", "jenis_cs": "Záporná částice"},
    "1. Harf Nafyi__2": {"arti_cs": "Ne / Nikoli (Lá - slovesný zápor)", "desc_cs": "Záporná částice pro přítomný a budoucí čas", "jenis_cs": "Záporná částice"},
    "1. Harf Nafyi__3": {"arti_cs": "Není ničím jiným než... (In)", "desc_cs": "Záporná částice pojící se s Illá", "jenis_cs": "Záporná částice"},
    "1. Harf Nafyi__4": {"arti_cs": "Není čas na (Láta)", "desc_cs": "Časová záporná částice", "jenis_cs": "Časová záporná částice"},

    "2. Harf Tahqiq Taswif__5": {"arti_cs": "Vskutku / Již (Qad - potvrzení)", "desc_cs": "Částice jistoty a důrazu před minulým časem", "jenis_cs": "Potvrzovací částice"},
    "2. Harf Tahqiq Taswif__6": {"arti_cs": "V budoucnu / Později (Sawfa)", "desc_cs": "Částice vzdálené budoucnosti", "jenis_cs": "Částice budoucnosti"},
    "2. Harf Tahqiq Taswif__7": {"arti_cs": "Brzy / Vzápětí (Sa - blízká budoucnost)", "desc_cs": "Částice blízké budoucnosti", "jenis_cs": "Částice budoucnosti"},

    "3. Harf Syarat__8": {"arti_cs": "Kdyby / Kdyby bývalo (Law - neuskutečněná podmínka)", "desc_cs": "Neřídící podmínková částice pro minulé neuskutečněné děje", "jenis_cs": "Podmínková částice"},
    "3. Harf Syarat__9": {"arti_cs": "Nebýt toho, že... (Lawlá)", "desc_cs": "Podmínková částice zabránění", "jenis_cs": "Podmínková částice"},
    "3. Harf Syarat__10": {"arti_cs": "Nebýt toho... (Lawmá)", "desc_cs": "Neřídící podmínková částice", "jenis_cs": "Podmínková částice"},
    "3. Harf Syarat__11": {"arti_cs": "Když / V době, kdy (Lammá)", "desc_cs": "Časová podmínková částice pro minulý čas", "jenis_cs": "Časová podmínková částice"},
    "3. Harf Syarat__12": {"arti_cs": "Co se pak týče... tak (Ammá)", "desc_cs": "Rozvádějící podmínková částice s důrazem", "jenis_cs": "Podmínková částice"},

    "4. Harf Mashdariyah__13": {"arti_cs": "Aby / Že (An - masdarová částice)", "desc_cs": "Částice převádějící sloveso na podstatné jméno slovesné", "jenis_cs": "Masdarová částice"},
    "4. Harf Mashdariyah__14": {"arti_cs": "Dokud / Pokud (Má masdaríja)", "desc_cs": "Časová masdarová částice", "jenis_cs": "Masdarová částice"},
    "4. Harf Mashdariyah__15": {"arti_cs": "Aby / Za účelem (Kay)", "desc_cs": "Účelová masdarová částice", "jenis_cs": "Masdarová částice"},
    "4. Harf Mashdariyah__16": {"arti_cs": "Kéž by / Přání aby (Law)", "desc_cs": "Masdarová částice po slovesech přání", "jenis_cs": "Masdarová částice"},

    "5. Harf Zaidah__17": {"arti_cs": "Pro zesílení významu (In zá'ida)", "desc_cs": "Doplňková zesilující částice", "jenis_cs": "Zesilující částice"},
    "5. Harf Zaidah__18": {"arti_cs": "Pro zesílení významu (An zá'ida)", "desc_cs": "Doplňková zesilující částice", "jenis_cs": "Zesilující částice"},
    "5. Harf Zaidah__19": {"arti_cs": "Pro zesílení významu (Má zá'ida)", "desc_cs": "Doplňková zesilující částice", "jenis_cs": "Zesilující částice"},
    "5. Harf Zaidah__20": {"arti_cs": "Pro zesílení významu (Lá zá'ida)", "desc_cs": "Doplňková částice zesilující zápor", "jenis_cs": "Zesilující částice"},

    "6. Harf Istifham__21": {"arti_cs": "Cožpak? / Zda? (Hamza)", "desc_cs": "Základní tázací částice", "jenis_cs": "Tázací částice"},
    "6. Harf Istifham__22": {"arti_cs": "Zda? / Zdali? (Hal)", "desc_cs": "Tázací částice vyžadující potvrzení či vyvrácení", "jenis_cs": "Tázací částice"},

    "7. Harf Istitsna__23": {"arti_cs": "Kromě / Jedině (Illá)", "desc_cs": "Vylučovací částice vyjadřující výjimku", "jenis_cs": "Vylučovací částice"},

    "8. Harf Rad'in Wazajrin__24": {"arti_cs": "Nikoli! / V žádném případě! (Kallá)", "desc_cs": "Kategoricky odmítavá a kárací částice", "jenis_cs": "Odmítavá částice"},

    "9. Harf Rad'in Tahdid__25": {"arti_cs": "Pročpak ne...? (Hallá)", "desc_cs": "Pobídková a výčitková částice", "jenis_cs": "Pobídková částice"},
    "9. Harf Rad'in Tahdid__26": {"arti_cs": "Proč tedy ne... (Allá)", "desc_cs": "Pobídková částice k rychlému konání dobra", "jenis_cs": "Pobídková částice"},

    "10. Harf Ijab__27": {"arti_cs": "Ano / Tak jest (Na'am)", "desc_cs": "Kladná odpovědní částice", "jenis_cs": "Odpovědní částice"},
    "10. Harf Ijab__28": {"arti_cs": "Ano, zajisté! (Balá)", "desc_cs": "Částice rušící zápor a potvrzující pravdu", "jenis_cs": "Potvrzovací částice"},
    "10. Harf Ijab__29": {"arti_cs": "Ano, při mém Pánu! (Í)", "desc_cs": "Potvrzovací částice při přísaze", "jenis_cs": "Přísahová částice"},
    "10. Harf Ijab__30": {"arti_cs": "Vskutku / Ovšemže (Adžal)", "desc_cs": "Potvrzovací částice", "jenis_cs": "Potvrzovací částice"},

    "11. Harf Tafsir__31": {"arti_cs": "Totiž / To jest (Aj)", "desc_cs": "Vysvětlující částice", "jenis_cs": "Vysvětlující částice"},
    "11. Harf Tafsir__32": {"arti_cs": "Že / Totiž (An tafsíríja)", "desc_cs": "Vysvětlující částice po slovesech promluvy", "jenis_cs": "Vysvětlující částice"},

    "12. Harf Tanbih__33": {"arti_cs": "Hle! / Vězte! (Alá)", "desc_cs": "Upozorňovací částice na začátku věty", "jenis_cs": "Upozorňovací částice"},
    "12. Harf Tanbih__34": {"arti_cs": "Vězte dobře! (Amá)", "desc_cs": "Upozorňovací částice", "jenis_cs": "Upozorňovací částice"},
    "12. Harf Tanbih__35": {"arti_cs": "Pohleďte! (Há tanbíh)", "desc_cs": "Částice přitahující pozornost před zájmeny", "jenis_cs": "Upozorňovací částice"},

    "13. Harf Ta'lil__36": {"arti_cs": "Aby / Protože (Lám ta'líl)", "desc_cs": "Příčinná částice vyjadřující důvod a účel", "jenis_cs": "Příčinná částice"},

    "14. Harf Fuja'iyyah__37": {"arti_cs": "A náhle! / A hle (Idhá fudžá'íja)", "desc_cs": "Částice vyjadřující náhlou a nečekanou událost", "jenis_cs": "Částice náhlého děje"},
    "14. Harf Fuja'iyyah__38": {"arti_cs": "Znenadání (Idh fudžá'íja)", "desc_cs": "Částice náhlého děje", "jenis_cs": "Částice náhlého děje"},

    "15. Harf Istidrak__39": {"arti_cs": "Avšak / Nicméně (Lákin)", "desc_cs": "Odporovací a opravná částice", "jenis_cs": "Odporovací částice"},
    "15. Harf Istidrak__40": {"arti_cs": "Naopak / Dokonce (Bal)", "desc_cs": "Částice změny tvrzení a opravy", "jenis_cs": "Odporovací částice"},

    "16. Harf Ta'ajjub__41": {"arti_cs": "Jak... jen! / Jak podivuhodné! (Má)", "desc_cs": "Zvolací částice vyjadřující údiv a obdiv", "jenis_cs": "Zvolací částice"},

    "17. Harf Mabany__39": {"arti_cs": "Há-Mím", "desc_cs": "Počáteční zkratková písmena súr", "jenis_cs": "Muqatta'át písmena"},
    "17. Harf Mabany__40": {"arti_cs": "Alif-Lám-Mím", "desc_cs": "Počáteční zkratková písmena súr", "jenis_cs": "Muqatta'át písmena"},
    "17. Harf Mabany__41": {"arti_cs": "Alif-Lám-Rá", "desc_cs": "Počáteční zkratková písmena súr", "jenis_cs": "Muqatta'át písmena"},
    "17. Harf Mabany__42": {"arti_cs": "Tá-Sín-Mím", "desc_cs": "Počáteční zkratková písmena súr", "jenis_cs": "Muqatta'át písmena"},
    "17. Harf Mabany__43": {"arti_cs": "Alif-Lám-Mím-Rá", "desc_cs": "Počáteční zkratková písmena súr", "jenis_cs": "Muqatta'át písmena"},
    "17. Harf Mabany__44": {"arti_cs": "Alif-Lám-Mím-Sád", "desc_cs": "Počáteční zkratková písmena súr", "jenis_cs": "Muqatta'át písmena"},
    "17. Harf Mabany__45": {"arti_cs": "Sád", "desc_cs": "Počáteční zkratková písmena súr", "jenis_cs": "Muqatta'át písmena"},
    "17. Harf Mabany__46": {"arti_cs": "Tá-Sín", "desc_cs": "Počáteční zkratková písmena súr", "jenis_cs": "Muqatta'át písmena"},
    "17. Harf Mabany__47": {"arti_cs": "Tá-Há", "desc_cs": "Počáteční zkratková písmena súr", "jenis_cs": "Muqatta'át písmena"},
    "17. Harf Mabany__48": {"arti_cs": "'Ayn-Sín-Qáf", "desc_cs": "Počáteční zkratková písmena súr", "jenis_cs": "Muqatta'át písmena"},
    "17. Harf Mabany__49": {"arti_cs": "Qáf", "desc_cs": "Počáteční zkratková písmena súr", "jenis_cs": "Muqatta'át písmena"},
    "17. Harf Mabany__50": {"arti_cs": "Káf-Há-Já-'Ayn-Sád", "desc_cs": "Počáteční zkratková písmena súr", "jenis_cs": "Muqatta'át písmena"},
    "17. Harf Mabany__51": {"arti_cs": "Nún", "desc_cs": "Počáteční zkratková písmena súr", "jenis_cs": "Muqatta'át písmena"},
    "17. Harf Mabany__52": {"arti_cs": "Já-Sín", "desc_cs": "Počáteční zkratková písmena súr", "jenis_cs": "Muqatta'át písmena"}
}

DHIVEHI_HARF_GRAMMAR = {
    "1. Harf Nafyi__1": {"arti_dv": "ނޫނެވެ / ނުވެއެވެ (މާ - ޢާންމު ނަފީ)", "desc_dv": "މާޒީ، މުޟާރިޢު އަދި އިސްމިއްޔާ ޖުމްލަ ނަފީކުރާ އަކުރު", "jenis_dv": "ނަފީކުރާ އަކުރު"},
    "1. Harf Nafyi__2": {"arti_dv": "ނު / ނޫން (ލާ - ފިޢުލު ނަފީކުރުން)", "desc_dv": "މުޟާރިޢު ފިޢުލު ނަފީކުރާ އަކުރު", "jenis_dv": "ނަފީކުރާ އަކުރު"},
    "1. Harf Nafyi__3": {"arti_dv": "ހަމައެކަނި... މެނުވީ ނޫނެވެ (އިން)", "desc_dv": "އިއްލާއާ އެކު އަންނަ ނަފީގެ އަކުރު", "jenis_dv": "ނަފީކުރާ އަކުރު"},
    "1. Harf Nafyi__4": {"arti_dv": "ވަގުތެއް ނޫނެވެ (ލާތަ)", "desc_dv": "ވަގުތު ނަފީކުރާ އަކުރު", "jenis_dv": "ވަގުތުގެ ނަފީ"},

    "2. Harf Tahqiq Taswif__5": {"arti_dv": "ހަމަކަށަވަރުން / ފަހެ (ޤަދް - ތަޙްޤީޤު)", "desc_dv": "މާޒީ ފިޢުލުގެ ކުރިއަށް އަންނަ ޔަޤީންކަން ދޭ އަކުރު", "jenis_dv": "ތަޙްޤީޤުގެ އަކުރު"},
    "2. Harf Tahqiq Taswif__6": {"arti_dv": "ފަހުން / ފަހަރެއްގައި (ސައުފަ)", "desc_dv": "ދުރު މުސްތަޤްބަލުގެ އަކުރު", "jenis_dv": "މުސްތަޤްބަލުގެ އަކުރު"},
    "2. Harf Tahqiq Taswif__7": {"arti_dv": "ދާދި އަވަހަށް (ސަ)", "desc_dv": "ކައިރި މުސްތަޤްބަލުގެ އަކުރު", "jenis_dv": "މުސްތަޤްބަލުގެ އަކުރު"},

    "3. Harf Syarat__8": {"arti_dv": "ވީނަމަ / ވީހިނދު (ލައު - ނުވާ ކަންކަމަށް)", "desc_dv": "މާޒީގައި ނުވާ ކަންކަމަށް ބޭނުންކުރާ ޝަރުޠުގެ އަކުރު", "jenis_dv": "ޝަރުޠުގެ އަކުރު"},
    "3. Harf Syarat__9": {"arti_dv": "ނުވިނަމަ (ލައުލާ)", "desc_dv": "އެއްކަމެއް ވުމުން އަނެއްކަމެއް މަނާވާ ޝަރުޠުގެ އަކުރު", "jenis_dv": "ޝަރުޠުގެ އަކުރު"},
    "3. Harf Syarat__10": {"arti_dv": "ނުވިނަމަ (ލައުމާ)", "desc_dv": "ޝަރުޠުގެ އަކުރު", "jenis_dv": "ޝަރުޠުގެ އަކުރު"},
    "3. Harf Syarat__11": {"arti_dv": "އެހިނދު / އެ ވަގުތު (ލައްމާ)", "desc_dv": "މާޒީގެ ވަގުތު އަންގައިދޭ ޝަރުޠުގެ އަކުރު", "jenis_dv": "ވަގުތުގެ ޝަރުޠު"},
    "3. Harf Syarat__12": {"arti_dv": "ދެން ފަހެ... އަށް ބަލާއިރު (އައްމާ)", "desc_dv": "ތަފްޞީލާއި ބާރުއެޅުމުގެ ޝަރުޠުގެ އަކުރު", "jenis_dv": "ޝަރުޠުގެ އަކުރު"},

    "4. Harf Mashdariyah__13": {"arti_dv": "ކަމަށް / ވުން (އަން - މަޞްދަރީ އަކުރު)", "desc_dv": "ފިޢުލު މަޞްދަރަކަށް ބަދަލުކުރާ އަކުރު", "jenis_dv": "މަޞްދަރީ އަކުރު"},
    "4. Harf Mashdariyah__14": {"arti_dv": "ދެމިއޮތްހައި ހިނދަކު (މާ މަޞްދަރިއްޔާ)", "desc_dv": "ވަގުތާއި ޙާލަތުގެ މަޞްދަރީ އަކުރު", "jenis_dv": "މަޞްދަރީ އަކުރު"},
    "4. Harf Mashdariyah__15": {"arti_dv": "އެކަމަށްޓަކައި (ކައި)", "desc_dv": "ބޭނުން ބަޔާންކުރާ މަޞްދަރީ އަކުރު", "jenis_dv": "މަޞްދަރީ އަކުރު"},
    "4. Harf Mashdariyah__16": {"arti_dv": "އެދޭކަމުގައި (ލައު)", "desc_dv": "އެދުމުގެ ފިޢުލުތަކަށްފަހު އަންނަ މަޞްދަރީ އަކުރު", "jenis_dv": "މަޞްދަރީ އަކުރު"},

    "5. Harf Zaidah__17": {"arti_dv": "ގަދަކުރުމަށްޓަކައި (އިން ޒާއިދާ)", "desc_dv": "މާނަ ވަރުގަދަކުރުމަށް އިތުރުކުރެވޭ އަކުރު", "jenis_dv": "ގަދަކުރުމުގެ އަކުރު"},
    "5. Harf Zaidah__18": {"arti_dv": "ގަދަކުރުމަށްޓަކައި (އަން ޒާއިދާ)", "desc_dv": "މާނަ ވަރުގަދަކުރުމަށް އިތުރުކުރެވޭ އަކުރު", "jenis_dv": "ގަދަކުރުމުގެ އަކުރު"},
    "5. Harf Zaidah__19": {"arti_dv": "ގަދަކުރުމަށްޓަކައި (މާ ޒާއިދާ)", "desc_dv": "މާނަ ވަރުގަދަކުރުމަށް އިތުރުކުރެވޭ އަކުރު", "jenis_dv": "ގަދަކުރުމުގެ އަކުރު"},
    "5. Harf Zaidah__20": {"arti_dv": "ގަދަކުރުމަށްޓަކައި (ލާ ޒާއިދާ)", "desc_dv": "ނަފީ ވަރުގަދަކުރުމަށް އިތުރުކުރެވޭ އަކުރު", "jenis_dv": "ގަދަކުރުމުގެ އަކުރު"},

    "6. Harf Istifham__21": {"arti_dv": "ހެއްޔެވެ؟ (ހަމްޒާ)", "desc_dv": "އަޞްލު ސުވާލުކުރާ އަކުރު", "jenis_dv": "ސުވާލުކުރާ އަކުރު"},
    "6. Harf Istifham__22": {"arti_dv": "ހެއްޔެވެ؟ / ތޯއެވެ؟ (ހަލް)", "desc_dv": "ސުވާލުކުރާ އަކުރު", "jenis_dv": "ސުވާލުކުރާ އަކުރު"},

    "7. Harf Istitsna__23": {"arti_dv": "މެނުވީ / ފިޔަވައި (އިއްލާ)", "desc_dv": "އިސްތިޘްނާކުރާ އަކުރު", "jenis_dv": "އިސްތިޘްނާގެ އަކުރު"},

    "8. Harf Rad'in Wazajrin__24": {"arti_dv": "ހަމަހިލާ އެހެންނަކުން ނޫނެވެ! (ކައްލާ)", "desc_dv": "މަނާކުރުމާއި ދޮގުކުރުމުގެ ވަރުގަދަ އަކުރު", "jenis_dv": "މަނާކުރުމުގެ އަކުރު"},

    "9. Harf Rad'in Tahdid__25": {"arti_dv": "ނުކުރަނީ ކީއްވެހެއްޔެވެ؟ (ހައްލާ)", "desc_dv": "ހެޔޮކަންކަމަށް ބާރުއެޅުމާއި މަލާމާތްކުރުމުގެ އަކުރު", "jenis_dv": "ބާރުއެޅުމުގެ އަކުރު"},
    "9. Harf Rad'in Tahdid__26": {"arti_dv": "ނުކުރަނީ ކީއްވެ؟ (އައްލާ)", "desc_dv": "ހެޔޮކަމަށް ބާރުއެޅުމުގެ އަކުރު", "jenis_dv": "ބާރުއެޅުމުގެ އަކުރު"},

    "10. Harf Ijab__27": {"arti_dv": "އާނއެކެވެ (ނަޢަމް)", "desc_dv": "ޖަވާބުދިނުމާއި އާނބަސް ބުނާ އަކުރު", "jenis_dv": "ޖަވާބުގެ އަކުރު"},
    "10. Harf Ijab__28": {"arti_dv": "އާނއެކެވެ، ހަމަކަށަވަރުންނެވެ! (ބަލާ)", "desc_dv": "ނަފީ ބާޠިލުކޮށް ޙައްޤު ޔަޤީންކޮށްދޭ އަކުރު", "jenis_dv": "ޔަޤީންކަމުގެ އަކުރު"},
    "10. Harf Ijab__29": {"arti_dv": "އާނއެކެވެ، ތިމަންގެ ވެރިރަސްކަލާނގެ ގަންދެއްވަމެވެ! (އީ)", "desc_dv": "ހުވަޔާއެކު އަންނަ ޖަވާބުގެ އަކުރު", "jenis_dv": "ހުވަޔާއެކު ޖަވާބު"},
    "10. Harf Ijab__30": {"arti_dv": "ތެދެކެވެ (އަޖަލް)", "desc_dv": "ޖަވާބުގެ އަކުރު", "jenis_dv": "ޖަވާބުގެ އަކުރު"},

    "11. Harf Tafsir__31": {"arti_dv": "އެބަހީ (އައި)", "desc_dv": "މާނަ ބަޔާންކުރާ އަކުރު", "jenis_dv": "ތަފްސީރުގެ އަކުރު"},
    "11. Harf Tafsir__32": {"arti_dv": "އެބަހީ / ކަމަށް (އަން ތަފްސީރިއްޔާ)", "desc_dv": "ބަސްބުނުމުގެ ފިޢުލުތަކަށްފަހު އަންނަ ތަފްސީރުގެ އަކުރު", "jenis_dv": "ތަފްސީރުގެ އަކުރު"},

    "12. Harf Tanbih__33": {"arti_dv": "ދަންނާށެވެ! / ހޭލާށެވެ! (އަލާ)", "desc_dv": "ފެށުމުގައްޔާއި ސަމާލުކުރުވާ އަކުރު", "jenis_dv": "ސަމާލުކުރުވާ އަކުރު"},
    "12. Harf Tanbih__34": {"arti_dv": "ދަންނާށެވެ! (އަމާ)", "desc_dv": "ސަމާލުކުރުވާ އަކުރު", "jenis_dv": "ސަމާލުކުރުވާ އަކުރު"},
    "12. Harf Tanbih__35": {"arti_dv": "ބަލާށެވެ! / މިއޮތީއެވެ (ހާ ތަންބީހު)", "desc_dv": "އިޝާރާތާއި ޟަމީރުތަކުގެ ކުރިއަށް އަންނަ ސަމާލުކުރުވާ އަކުރު", "jenis_dv": "ސަމާލުކުރުވާ އަކުރު"},

    "13. Harf Ta'lil__36": {"arti_dv": "އެކަމަށްޓަކައި / ސަބަބަކީ (ލާމު ތަޢުލީލް)", "desc_dv": "ސަބަބާއި ޙިކްމަތް ބަޔާންކުރާ އަކުރު", "jenis_dv": "ސަބަބުގެ އަކުރު"},

    "14. Harf Fuja'iyyah__37": {"arti_dv": "އެހިނދު ކުއްލިއަކަށް! (އިޛާ ފުޖާއިއްޔާ)", "desc_dv": "ކުއްލިއަކަށް ކަމެއް ވާކަން އަންގައިދޭ އަކުރު", "jenis_dv": "ކުއްލި ކަންކަމުގެ އަކުރު"},
    "14. Harf Fuja'iyyah__38": {"arti_dv": "ކުއްލިއަކަށް (އިޛް ފުޖާއިއްޔާ)", "desc_dv": "ކުއްލި ކަންކަމުގެ އަކުރު", "jenis_dv": "ކުއްލި ކަންކަމުގެ އަކުރު"},

    "15. Harf Istidrak__39": {"arti_dv": "އެހެނެއްކަމަކު / އެކަމަކު (ލާކިން)", "desc_dv": "ކުށްހީ ފިލުވައިދޭ އިސްތިދްރާކުގެ އަކުރު", "jenis_dv": "އިސްތިދްރާކުގެ އަކުރު"},
    "15. Harf Istidrak__40": {"arti_dv": "އަދި ކިއެއްތަ / އަދި ބަލާށެވެ (ބަލް)", "desc_dv": "ކުރީގެ ވާހަކަ ބަދަލުކޮށްލާ އަކުރު", "jenis_dv": "އިސްތިދްރާކުގެ އަކުރު"},

    "16. Harf Ta'ajjub__41": {"arti_dv": "ކިހާ... ހެއްޔެވެ! (މާ ޢަޖާއިބު)", "desc_dv": "ޢަޖާއިބުވުމާއި ހައިރާންކަން ފާޅުކުރާ އަކުރު", "jenis_dv": "ޢަޖާއިބުވުމުގެ އަކުރު"},

    "17. Harf Mabany__39": {"arti_dv": "ޙާމީމް", "desc_dv": "ސޫރަތްތަކުގެ ފެށުމުގައިވާ އަކުރުތައް", "jenis_dv": "މުޤައްޠަޢާތު އަކުރު"},
    "17. Harf Mabany__40": {"arti_dv": "އަލިފް-ލާމް-މީމް", "desc_dv": "ސޫރަތްތަކުގެ ފެށުމުގައިވާ އަކުރުތައް", "jenis_dv": "މުޤައްޠަޢާތު އަކުރު"},
    "17. Harf Mabany__41": {"arti_dv": "އަލިފް-ލާމް-ރާ", "desc_dv": "ސޫރަތްތަކުގެ ފެށުމުގައިވާ އަކުރުތައް", "jenis_dv": "މުޤައްޠަޢާތު އަކުރު"},
    "17. Harf Mabany__42": {"arti_dv": "ޠާސީންމީމް", "desc_dv": "ސޫރަތްތަކުގެ ފެށުމުގައިވާ އަކުރުތައް", "jenis_dv": "މުޤައްޠަޢާތު އަކުރު"},
    "17. Harf Mabany__43": {"arti_dv": "އަލިފް-ލާމް-މީމް-ރާ", "desc_dv": "ސޫރަތްތަކުގެ ފެށުމުގައިވާ އަކުރުތައް", "jenis_dv": "މުޤައްޠަޢާތު އަކުރު"},
    "17. Harf Mabany__44": {"arti_dv": "އަލިފް-ލާމް-މީމް-ޞާދު", "desc_dv": "ސޫރަތްތަކުގެ ފެށުމުގައިވާ އަކުރުތައް", "jenis_dv": "މުޤައްޠަޢާތު އަކުރު"},
    "17. Harf Mabany__45": {"arti_dv": "ޞާދު", "desc_dv": "ސޫރަތްތަކުގެ ފެށުމުގައިވާ އަކުރުތައް", "jenis_dv": "މުޤައްޠަޢާތު އަކުރު"},
    "17. Harf Mabany__46": {"arti_dv": "ޠާސީން", "desc_dv": "ސޫރަތްތަކުގެ ފެށުމުގައިވާ އަކުރުތައް", "jenis_dv": "މުޤައްޠަޢާތު އަކުރު"},
    "17. Harf Mabany__47": {"arti_dv": "ޠާހާ", "desc_dv": "ސޫރަތްތަކުގެ ފެށުމުގައިވާ އަކުރުތައް", "jenis_dv": "މުޤައްޠަޢާތު އަކުރު"},
    "17. Harf Mabany__48": {"arti_dv": "ޢައިން-ސީން-ޤާފް", "desc_dv": "ސޫރަތްތަކުގެ ފެށުމުގައިވާ އަކުރުތައް", "jenis_dv": "މުޤައްޠަޢާތު އަކުރު"},
    "17. Harf Mabany__49": {"arti_dv": "ޤާފް", "desc_dv": "ސޫރަތްތަކުގެ ފެށުމުގައިވާ އަކުރުތައް", "jenis_dv": "މުޤައްޠަޢާތު އަކުރު"},
    "17. Harf Mabany__50": {"arti_dv": "ކާފް-ހާ-ޔާ-ޢައިން-ޞާދު", "desc_dv": "ސޫރަތްތަކުގެ ފެށުމުގައިވާ އަކުރުތައް", "jenis_dv": "މުޤައްޠަޢާތު އަކުރު"},
    "17. Harf Mabany__51": {"arti_dv": "ނޫން", "desc_dv": "ސޫރަތްތަކުގެ ފެށުމުގައިވާ އަކުރުތައް", "jenis_dv": "މުޤައްޠަޢާތު އަކުރު"},
    "17. Harf Mabany__52": {"arti_dv": "ޔާސީން", "desc_dv": "ސޫރަތްތަކުގެ ފެށުމުގައިވާ އަކުރުތައް", "jenis_dv": "މުޤައްޠަޢާތު އަކުރު"}
}


def enrich_dhamir_data():
    print("Enriching dhamir_data.json and dhamir_data.js with Czech & Dhivehi...")
    with open(os.path.join(BASE_DIR, 'cs_translations.json'), 'r', encoding='utf-8') as f:
        cs_trans = json.load(f)
    with open(os.path.join(BASE_DIR, 'dv_translations.json'), 'r', encoding='utf-8') as f:
        dv_trans = json.load(f)
    with open(os.path.join(BASE_DIR, 'dhamir_data.json'), 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        b = item.get('Bentuk Kata', '')
        nk = str(item.get('No kata', ''))
        g_key = f"{b}__{nk}"
        s_num = str(item.get('SURAT', ''))
        v_key = f"{item.get('SURAT')}:{item.get('AYAT')}"

        # CS
        item['BentukKataCS'] = BENTUK_KATA_CS.get(b, b)
        item['SuratArtiCS'] = CZECH_SURAHS.get(s_num, item.get('SuratArtiEN', ''))
        g_cs = CZECH_GRAMMAR.get(g_key, {})
        item['ArtiKataCS'] = g_cs.get('arti_cs', item.get('ArtiKataEN', ''))
        item['TeksArtiCS'] = cs_trans.get(v_key, item.get('TeksArtiEN', ''))

        # DV
        item['BentukKataDV'] = BENTUK_KATA_DV.get(b, b)
        item['SuratArtiDV'] = DHIVEHI_SURAHS.get(s_num, item.get('SuratArtiEN', ''))
        g_dv = DHIVEHI_GRAMMAR.get(g_key, {})
        item['ArtiKataDV'] = g_dv.get('arti_dv', item.get('ArtiKataEN', ''))
        item['TeksArtiDV'] = dv_trans.get(v_key, item.get('TeksArtiEN', ''))

        # Grammar dict
        if 'Grammar' not in item or not isinstance(item['Grammar'], dict):
            item['Grammar'] = {}
        if g_cs.get('arti_cs'): item['Grammar']['arti_cs'] = g_cs['arti_cs']
        if g_cs.get('desc_cs'): item['Grammar']['desc_cs'] = g_cs['desc_cs']
        if g_cs.get('jenis_cs'): item['Grammar']['jenis_cs'] = g_cs['jenis_cs']

        if g_dv.get('arti_dv'): item['Grammar']['arti_dv'] = g_dv['arti_dv']
        if g_dv.get('desc_dv'): item['Grammar']['desc_dv'] = g_dv['desc_dv']
        if g_dv.get('jenis_dv'): item['Grammar']['jenis_dv'] = g_dv['jenis_dv']

    with open(os.path.join(BASE_DIR, 'dhamir_data.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    js_content = f"/**\n * Dataset Dhamir & Isim Jamid Mabny Al-Qur'an 29 Bahasa\n */\nconst DHAMIR_DATA = {json.dumps(data, ensure_ascii=False, indent=2)};\n"
    with open(os.path.join(BASE_DIR, 'dhamir_data.js'), 'w', encoding='utf-8') as f:
        f.write(js_content)
    print(f"  [OK] Dhamir data enriched ({len(data)} rows).")


def enrich_harf_data():
    print("Enriching harf_data.json and harf_data.js with Czech & Dhivehi...")
    with open(os.path.join(BASE_DIR, 'cs_translations.json'), 'r', encoding='utf-8') as f:
        cs_trans = json.load(f)
    with open(os.path.join(BASE_DIR, 'dv_translations.json'), 'r', encoding='utf-8') as f:
        dv_trans = json.load(f)
    with open(os.path.join(BASE_DIR, 'harf_data.json'), 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        b = item.get('Bentuk Kata', '')
        nk = str(item.get('No kata', ''))
        g_key = f"{b}__{nk}"
        s_num = str(item.get('SURAT', ''))
        v_key = f"{item.get('SURAT')}:{item.get('AYAT')}"

        # CS
        item['BentukKataCS'] = BENTUK_HARF_CS.get(b, b)
        item['SuratArtiCS'] = CZECH_SURAHS.get(s_num, item.get('SuratArtiEN', ''))
        g_cs = CZECH_HARF_GRAMMAR.get(g_key, {})
        item['ArtiKataCS'] = g_cs.get('arti_cs', item.get('ArtiKataEN', ''))
        item['TeksArtiCS'] = cs_trans.get(v_key, item.get('TeksArtiEN', ''))

        # DV
        item['BentukKataDV'] = BENTUK_HARF_DV.get(b, b)
        item['SuratArtiDV'] = DHIVEHI_SURAHS.get(s_num, item.get('SuratArtiEN', ''))
        g_dv = DHIVEHI_HARF_GRAMMAR.get(g_key, {})
        item['ArtiKataDV'] = g_dv.get('arti_dv', item.get('ArtiKataEN', ''))
        item['TeksArtiDV'] = dv_trans.get(v_key, item.get('TeksArtiEN', ''))

        # Grammar dict
        if 'Grammar' not in item or not isinstance(item['Grammar'], dict):
            item['Grammar'] = {}
        if g_cs.get('arti_cs'): item['Grammar']['arti_cs'] = g_cs['arti_cs']
        if g_cs.get('desc_cs'): item['Grammar']['desc_cs'] = g_cs['desc_cs']
        if g_cs.get('jenis_cs'): item['Grammar']['jenis_cs'] = g_cs['jenis_cs']

        if g_dv.get('arti_dv'): item['Grammar']['arti_dv'] = g_dv['arti_dv']
        if g_dv.get('desc_dv'): item['Grammar']['desc_dv'] = g_dv['desc_dv']
        if g_dv.get('jenis_dv'): item['Grammar']['jenis_dv'] = g_dv['jenis_dv']

    with open(os.path.join(BASE_DIR, 'harf_data.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    js_content = f"/**\n * Dataset Harf Ghair 'Amil Al-Qur'an 29 Bahasa\n */\nconst HARF_DATA = {json.dumps(data, ensure_ascii=False, indent=2)};\n"
    with open(os.path.join(BASE_DIR, 'harf_data.js'), 'w', encoding='utf-8') as f:
        f.write(js_content)
    print(f"  [OK] Harf data enriched ({len(data)} rows).")


if __name__ == '__main__':
    enrich_dhamir_data()
    enrich_harf_data()
