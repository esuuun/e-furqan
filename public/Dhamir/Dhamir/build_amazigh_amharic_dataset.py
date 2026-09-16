#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Amazigh (ber) and Amharic (am) Dataset Metadata & Enricher:
- 114 Surah Names for Amazigh & Amharic
- 7 Bentuk Kata Categories for Amazigh & Amharic
- 76 Jamid Mabny Grammar details for Amazigh & Amharic
- 17 Bentuk Harf Categories for Amazigh & Amharic
- 52 Harf Grammar details for Amazigh & Amharic
"""

import os
import sys
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

AMAZIGH_SURAHS = {
    "1": "Tawwurt (Al-Fatiḥa)",
    "2": "Tafunast (Al-Baqarah)",
    "3": "Axxam n Ɛimran (Al-Imran)",
    "4": "Tilawin (An-Nisa)",
    "5": "Tadabut (Al-Ma'ida)",
    "6": "Lmal (Al-An'am)",
    "7": "Laɛraf (Al-A'raf)",
    "8": "Lɣanimat (Al-Anfal)",
    "9": "Ttuba (At-Tawba)",
    "10": "Yunes (Yunus)",
    "11": "Hud (Hud)",
    "12": "Yusef (Yusuf)",
    "13": "Rraɛd (Ar-Ra'd)",
    "14": "Ibrahim (Ibrahim)",
    "15": "Lḥijr (Al-Hijr)",
    "16": "Tizizwa (An-Nahl)",
    "17": "Tikli n Yiḍ (Al-Isra)",
    "18": "Lɣar (Al-Kahf)",
    "19": "Meryem (Maryam)",
    "20": "Ṭaha (Ta-Ha)",
    "21": "Lambiya (Al-Anbiya)",
    "22": "Lḥiǧǧ (Al-Hajj)",
    "23": "Imumnen (Al-Mu'minun)",
    "24": "Tafat (An-Nur)",
    "25": "Lferqan (Al-Furqan)",
    "26": "Imedyazen (Ash-Shu'ara)",
    "27": "Twekkin (An-Naml)",
    "28": "Teqsiṭ (Al-Qasas)",
    "29": "Tissist (Al-Ankabut)",
    "30": "Rrum (Ar-Rum)",
    "31": "Luqman (Luqman)",
    "32": "Asjud (As-Sajda)",
    "33": "Lḥizb (Al-Ahzab)",
    "34": "Saba (Saba)",
    "35": "Axlac (Fatir)",
    "36": "Yasin (Ya-Sin)",
    "37": "Isaffen (As-Saffat)",
    "38": "Ṣad (Sad)",
    "39": "Izemmaren (Az-Zumar)",
    "40": "Ghafir (Al-Mu'min)",
    "41": "Tufṣilt (Fussilat)",
    "42": "Ccur (Ash-Shura)",
    "43": "Zzuxruf (Az-Zukhruf)",
    "44": "Dduxan (Ad-Dukhan)",
    "45": "Tajattit (Al-Jathiya)",
    "46": "Laḥqaf (Al-Ahqaf)",
    "47": "Muḥemmed (Muhammad)",
    "48": "Lfetḥ (Al-Fath)",
    "49": "Ixxamen (Al-Hujurat)",
    "50": "Qaf (Qaf)",
    "51": "Idariyen (Adh-Dhariyat)",
    "52": "Ṭṭur (At-Tur)",
    "53": "Itri (An-Najm)",
    "54": "Aggur (Al-Qamar)",
    "55": "Reḥman (Ar-Rahman)",
    "56": "Tawaqit (Al-Waqi'a)",
    "57": "Wuzzal (Al-Hadid)",
    "58": "Amjadel (Al-Mujadila)",
    "59": "Lḥacel (Al-Hashr)",
    "60": "Tamextart (Al-Mumtahana)",
    "61": "Aṣaff (As-Saff)",
    "62": "Lǧemɛa (Al-Jumu'a)",
    "63": "Imnafqen (Al-Munafiqun)",
    "64": "Attaɣabun (At-Taghabun)",
    "65": "Berrat (At-Talaq)",
    "66": "Aḥram (At-Tahrim)",
    "67": "Lmulk (Al-Mulk)",
    "68": "Lqalam (Al-Qalam)",
    "69": "Lḥaqqa (Al-Haqqah)",
    "70": "Isekkiren (Al-Ma'arij)",
    "71": "Nuḥ (Nuh)",
    "72": "Lǧenn (Al-Jinn)",
    "73": "Umlil (Al-Muzzammil)",
    "74": "Amuddeṯṯer (Al-Muddaththir)",
    "75": "Qiyama (Al-Qiyama)",
    "76": "Amkan (Al-Insan)",
    "77": "Imceyɛen (Al-Mursalat)",
    "78": "Nnaba (An-Naba)",
    "79": "Naziɛat (An-Nazi'at)",
    "80": "Ɛbes (Abasa)",
    "81": "Takwir (At-Takwir)",
    "82": "Infiṭar (Al-Infitar)",
    "83": "Ikayyaln (Al-Mutaffifin)",
    "84": "Inciqaq (Al-Inshiqaq)",
    "85": "Buruj (Al-Buruj)",
    "86": "Ṭariq (At-Tariq)",
    "87": "Aɛlayen (Al-A'la)",
    "88": "Ɣaciya (Al-Ghashiya)",
    "89": "Fǧer (Al-Fajr)",
    "90": "Lbalad (Al-Balad)",
    "91": "Iṭij (Ash-Shams)",
    "92": "Iḍ (Al-Layl)",
    "93": "Ḍḍuḥa (Ad-Duha)",
    "94": "Incirah (Ash-Sharh)",
    "95": "Ttin (At-Tin)",
    "96": "Iqqra (Al-Alaq)",
    "97": "Lqadr (Al-Qadr)",
    "98": "Lbayyina (Al-Bayyina)",
    "99": "Zzelzla (Az-Zalzala)",
    "100": "Aɛdiyyat (Al-Adiyat)",
    "101": "Lqariɛa (Al-Qari'a)",
    "102": "Tekatur (At-Takathur)",
    "103": "Lɛaṣr (Al-Asr)",
    "104": "Lhumaza (Al-Humaza)",
    "105": "Lfil (Al-Fil)",
    "106": "Qurayc (Quraysh)",
    "107": "Lmaɛun (Al-Ma'un)",
    "108": "Lkawter (Al-Kawthar)",
    "109": "Ikafiren (Al-Kafirun)",
    "110": "Nnaṣr (An-Nasr)",
    "111": "Lmasad (Al-Masad)",
    "112": "Lixlaṣ (Al-Ikhlas)",
    "113": "Lfalaq (Al-Falaq)",
    "114": "Imdanen (An-Nas)"
}

AMHARIC_SURAHS = {
    "1": "አል-ፋቲሓ (መክፈቻዋ)",
    "2": "አል-በቀራህ (ላሟ)",
    "3": "አሊ-ዒምራን (የዒምራን ቤተሰቦች)",
    "4": "አን-ኒሳእ (ሴቶች)",
    "5": "አል-ማኢዳህ (ማዕድ)",
    "6": "አል-አንዓም (የቤት እንስሳት)",
    "7": "አል-አዕራፍ (ከፍታዎች)",
    "8": "አል-አንፋል (የጦር ምርኮዎች)",
    "9": "አት-ተውባህ (ንስሐ)",
    "10": "ዩኑስ (ነቢዩ ዩኑስ)",
    "11": "ሁድ (ነቢዩ ሁድ)",
    "12": "ዩሱፍ (ነቢዩ ዩሱፍ)",
    "13": "አር-ረዕድ (ነጎድጓድ)",
    "14": "ኢብራሂም (ነቢዩ ኢብራሂም)",
    "15": "አል-ሒጅር (የድንጋይ አገር)",
    "16": "አን-ነሕል (ንብ)",
    "17": "አል-ኢስራእ (የሌሊት ጉዞ)",
    "18": "አል-ካህፍ (ዋሻው)",
    "19": "መርየም (ማርያም)",
    "20": "ጣሀ (ጣሀ)",
    "21": "አል-አንቢያእ (ነቢያት)",
    "22": "አል-ሐጅ (ሐጅ/ስግደት)",
    "23": "አል-ሙእሚኑን (ምእመናን)",
    "24": "አን-ኑር (ብርሃን)",
    "25": "አል-ፉርቃን (መለያው)",
    "26": "አሽ-ሹዐራእ (ገጣሚዎች)",
    "27": "አን-ነምል (ጉንዳን)",
    "28": "አል-ቀሰስ (ታሪኮች)",
    "29": "አል-ዐንከቡት (ሸረሪት)",
    "30": "አር-ሩም (ሮማውያን)",
    "31": "ሉቅማን (ሉቅማን)",
    "32": "አስ-ሰጅዳህ (ስግደት)",
    "33": "አል-አሕዛብ (ጥምር ኃይሎች)",
    "34": "ሰበእ (የሰበእ ሰዎች)",
    "35": "ፋጢር (ፈጣሪ)",
    "36": "ያሲን (ያሲን)",
    "37": "አስ-ሷፍፋት (ተሰላፊዎች)",
    "38": "ሷድ (ሷድ)",
    "39": "አዝ-ዙመር (ጭፍሮች)",
    "40": "ጋፊር (መሀሪው)",
    "41": "ፉስሲለት (የተብራሩት)",
    "42": "አሽ-ሹራ (ምክክር)",
    "43": "አዝ-ዙኽሩፍ (ጌጣጌጥ)",
    "44": "አድ-ዱኻን (ጭስ)",
    "45": "አል-ጃሲያህ (ተንበርካኪዋ)",
    "46": "አል-አሕቃፍ (የአሸዋ ክምሮች)",
    "47": "ሙሐመድ (ነቢዩ ሙሐመድ)",
    "48": "አል-ፈትሕ (ድል)",
    "49": "አል-ሁጁራት (ክፍሎች)",
    "50": "ቃፍ (ቃፍ)",
    "51": "አዝ-ዛሪያት (በታኞች)",
    "52": "አጥ-ጡር (ጡር ተራራ)",
    "53": "አን-ነጅም (ኮከብ)",
    "54": "አል-ቀመር (ጨረቃ)",
    "55": "አር-ረሕማን (እጅግ ሩኅሩኅ)",
    "56": "አል-ዋቂዐህ (ታላቋ ክስተት)",
    "57": "አል-ሐዲድ (ብረት)",
    "58": "አል-ሙጃደላህ (ተከራካሪዋ)",
    "59": "አል-ሐሽር (ስደት/መሰብሰብ)",
    "60": "አል-ሙምተሒናህ (ተፈታኟ)",
    "61": "አስ-ሶፍ (ሰልፍ)",
    "62": "አል-ጁሙዐህ (ዓርብ)",
    "63": "አል-ሙናፊቁን (መናፍቃን)",
    "64": "አት-ተጋቡን (መሸናነፍ)",
    "65": "አጥ-ጦላቅ (ፍቺ)",
    "66": "አት-ተሕሪም (እርም ማድረግ)",
    "67": "አል-ሙልክ (ንግሥና)",
    "68": "አል-ቀለም (ብዕር)",
    "69": "አል-ሓቃህ (እውነቷ ክስተት)",
    "70": "አል-መዓሪጅ (የመወጣጫ መንገዶች)",
    "71": "ኑሕ (ነቢዩ ኑሕ)",
    "72": "አል-ጂን (ጂኖች)",
    "73": "አል-ሙዘሚል (ተጠቅላዩ)",
    "74": "አል-ሙደሲር (ተከናናቢው)",
    "75": "አል-ቂያማህ (ትንሣኤ)",
    "76": "አል-ኢንሳን (የሰው ልጅ)",
    "77": "አል-ሙርሰላት (ተላላኪዎች)",
    "78": "አን-ነበእ (ታላቁ ዜና)",
    "79": "አን-ናዚዓት (ነቃዮች)",
    "80": "ዐበሰ (ፊቱን አጨፈገገ)",
    "81": "አት-ተክዊር (መጠቅለል)",
    "82": "አል-ኢንፊጣር (መሰነጣጠቅ)",
    "83": "አል-ሙጦፊፊን (አጉዳዮች)",
    "84": "አል-ኢንሺቃቅ (መሰንጠቅ)",
    "85": "አል-ቡሩጅ (ህብረ ከዋክብት)",
    "86": "አጥ-ጣሪቅ (የሌሊቱ ኮከብ)",
    "87": "አል-አዕላ (እጅግ የበላይ)",
    "88": "አል-ጋሺያህ (ሸፋኟ)",
    "89": "አል-ፈጅር (ጎህ)",
    "90": "አል-በለድ (ከተማዋ)",
    "91": "አሽ-ሸምስ (ፀሐይ)",
    "92": "አል-ለይል (ሌሊት)",
    "93": "አድ-ዱሓ (ረፋድ)",
    "94": "አሽ-ሸርሕ (ደረትን ማስፋት)",
    "95": "አት-ቲን (በለስ)",
    "96": "አል-ዐለቅ (መርጋጋ ደም)",
    "97": "አል-ቀድር (የተከበረችው ሌሊት)",
    "98": "አል-በይናህ (ግልጽ ማስረጃ)",
    "99": "አዝ-ዘልዘላህ (መንቀጥቀጥ)",
    "100": "አል-ዓዲያት (ፈጣን ፈረሶች)",
    "101": "አል-ቃሪዐህ (መዓት)",
    "102": "አት-ተካሱር (መበላለጥ)",
    "103": "አል-ዐስር (ጊዜ)",
    "104": "አል-ሁመዛህ (አማጊዎች)",
    "105": "አል-ፊል (ዝሆን)",
    "106": "ቁረይሽ (የቁረይሽ ነገድ)",
    "107": "አል-ማዑን (የቤት ዕቃዎች)",
    "108": "አል-ከውሰር (ብዙ በጎ ነገር)",
    "109": "አል-ካፊሩን (ከሓዲዎች)",
    "110": "አን-ነስር (እርዳታ)",
    "111": "አል-መሳድ (የተፈተለ ገመድ)",
    "112": "አል-ኢኽላስ (ንጹሕ እምነት)",
    "113": "አል-ፈselection / አል-ፈcompleting (ጎህ)",
    "114": "አን-ናስ (የሰው ልጆች)"
}
AMHARIC_SURAHS["113"] = "አል-ፈselection (ጎህ)"
AMHARIC_SURAHS["113"] = "አል-ፈcompleting (ፈተለክ / ጎህ)"
AMHARIC_SURAHS["113"] = "አል-ፈለቅ (የማለዳ ጎህ)"

BENTUK_KATA_BER = {
    "1. Dhamir": "1. Imqimen (Dhamir - Iglamen)",
    "2. Isim Mawshul": "2. Imqimen Imassaɣen (Mawshul)",
    "3. Isim Istifham": "3. Isteqsiyen (Istifham - Tisura n Usteqsi)",
    "4. Isim Syarath": "4. Tseddariyin n Tawtilt (Syarath)",
    "5. Isim Isyarah": "5. Imqimen n Usmmal (Isyarah)",
    "6. Isim Fi'il": "6. Ismawen n Tigawt (Isim Fi'il)",
    "7. Fi'il Jamid": "7. Imyagen Ikiwanen (Fi'il Jamid)"
}

BENTUK_KATA_AM = {
    "1. Dhamir": "1. ተውላጠ ስሞች (ዳሚር / Dhamir)",
    "2. Isim Mawshul": "2. አዛማጅ ተውላጠ ስሞች (መውሱል / Mawshul)",
    "3. Isim Istifham": "3. መጠይቅ ቃላት (ኢስቲፍሃም / Istifham)",
    "4. Isim Syarath": "4. ቅድመ-ሁኔታ አመልካች ቃላት (ሻራት / Syarath)",
    "5. Isim Isyarah": "5. አመላካች ተውላጠ ስሞች (ኢሻራህ / Isyarah)",
    "6. Isim Fi'il": "6. ግሳዊ ስሞች (ኢስሙል ፊዕል / Isim Fi'il)",
    "7. Fi'il Jamid": "7. የማይዘረዘሩ ግሦች (ፊዕል ጃሚድ / Fi'il Jamid)"
}

BENTUK_HARF_BER = {
    "1. Harf Nafyi": "1. Tiseddariyin n Tugint (Harf Nafy)",
    "2. Harf Tahqiq Taswif": "2. Tiseddariyin n Usentem d Yimal (Tahqiq & Taswif)",
    "3. Harf Syarat": "3. Tiseddariyin n Tawtilt Ur Nesɛi Asemres (Harf Syarat)",
    "4. Harf Mashdariyah": "4. Tiseddariyin Tasmadarin (Harf Mashdariyah)",
    "5. Harf Zaidah": "5. Tiseddariyin Timerniyin n Usentem (Harf Zaidah)",
    "6. Harf Istifham": "6. Tiseddariyin n Usteqsi (Harf Istifham)",
    "7. Harf Istitsna": "7. Tiseddariyin n Usizdel (Harf Istitsna)",
    "8. Harf Rad'in Wazajrin": "8. Tiseddariyin n Usbedd d Usguri (Harf Rad'in)",
    "9. Harf Rad'in Tahdid": "9. Tiseddariyin n Tuzzya d Usḥulfu (Harf Tahdid)",
    "10. Harf Ijab": "10. Tiseddariyin n Uqevel d Tidet (Harf Ijab)",
    "11. Harf Tafsir": "11. Tiseddariyin n Usegzi (Harf Tafsir)",
    "12. Harf Tanbih": "12. Tiseddariyin n Usḥulfu (Harf Tanbih)",
    "13. Harf Ta'lil": "13. Tiseddariyin n Tmentilt (Harf Ta'lil)",
    "14. Harf Fuja'iyyah": "14. Tiseddariyin n Tifekkit (Harf Fuja'iyyah)",
    "15. Harf Istidrak": "15. Tiseddariyin n Usseɣti (Harf Istidrak)",
    "16. Harf Ta'ajjub": "16. Tiseddariyin n Lwehba (Harf Ta'ajjub)",
    "17. Harf Mabany": "17. Isekkilen n Tazzwara n Tsuratin (Muqatta'at)"
}

BENTUK_HARF_AM = {
    "1. Harf Nafyi": "1. የአሉታ ቅንጣቶች (ሐርፈ ነፍይ / Harf Nafy)",
    "2. Harf Tahqiq Taswif": "2. የማረጋገጫና የወደፊት ጊዜ ቅንጣቶች (ተሕቂቅና ተስዊፍ)",
    "3. Harf Syarat": "3. ቅድመ-ሁኔታ ቅንጣቶች (ሐርፈ ሸርጥ / Harf Syarat)",
    "4. Harf Mashdariyah": "4. ዘይቤያዊ/የድርጊት ስም አድራጊ ቅንጣቶች (ሐርፈ መስደሪየህ)",
    "5. Harf Zaidah": "5. ማጠናከሪያ ትርፍ ቅንጣቶች (ሐርፈ ዛኢዳህ)",
    "6. Harf Istifham": "6. የመጠይቅ ቅንጣቶች (ሐርፈ ኢስቲፍሃም / Harf Istifham)",
    "7. Harf Istitsna": "7. የማግለያ ቅንጣቶች (ሐርፈ ኢስቲስናእ / Harf Istitsna)",
    "8. Harf Rad'in Wazajrin": "8. የመከልከያና የመገሰጫ ቅንጣቶች (ሐርፈ ረድዕ / Harf Rad'in)",
    "9. Harf Rad'in Tahdid": "9. የማበረታቻና የወቀሳ ቅንጣቶች (ሐርፈ ተሕዲድ)",
    "10. Harf Ijab": "10. የማረጋገጫና የእሺታ ቅንጣቶች (ሐርፈ ኢጃብ)",
    "11. Harf Tafsir": "11. የማብራሪያ ቅንጣቶች (ሐርፈ ተፍሲር / Harf Tafsir)",
    "12. Harf Tanbih": "12. የማስጠንቀቂያና የመክፈቻ ቅንጣቶች (ሐርፈ ተንቢህ)",
    "13. Harf Ta'lil": "13. የምክንያት አመልካች ቅንጣቶች (ሐርፈ ተዕሊል)",
    "14. Harf Fuja'iyyah": "14. የድንገቴ ክስተት ቅንጣቶች (ሐርፈ ፉጃኢየህ)",
    "15. Harf Istidrak": "15. የማስተካከያ ቅንጣቶች (ሐርፈ ኢስቲድራክ)",
    "16. Harf Ta'ajjub": "16. የአግራሞት ቅንጣቶች (ሐርፈ ተዓጁብ)",
    "17. Harf Mabany": "17. የሱራ መክፈቻ ምህፃረ ቃላት (ሙቀጣዓት)"
}

AMAZIGH_GRAMMAR = {
    "1. Dhamir__1a": {"arti_ber": "Netta (Amqim n wunti asuf amalay)", "desc_ber": "Amqim imserreḥ i wunti asuf amalay (Munfashil)", "jenis_ber": "Amqim Imserreḥ"},
    "1. Dhamir__1b": {"arti_ber": "-s / -es (Amqim uddis amalay)", "desc_ber": "Amqim uddis i wunti asuf amalay (Muttashil)", "jenis_ber": "Amqim Uddis"},
    "1. Dhamir__1c": {"arti_ber": "I Netta kan (Amqim n usemres usegrawan)", "desc_ber": "Amqim imserreḥ n usemres i wunti amalay", "jenis_ber": "Amqim Imserreḥ"},
    "1. Dhamir__2a": {"arti_ber": "Nutni sin / Nutenti snat", "desc_ber": "Amqim imserreḥ n sin wuddusen", "jenis_ber": "Amqim Imserreḥ"},
    "1. Dhamir__2b": {"arti_ber": "-tsen sin / -tsent snat", "desc_ber": "Amqim uddis n sin wuddusen", "jenis_ber": "Amqim Uddis"},
    "1. Dhamir__3a": {"arti_ber": "Nutni (Asget amalay)", "desc_ber": "Amqim imserreḥ n usget amalay", "jenis_ber": "Amqim Imserreḥ"},
    "1. Dhamir__3b": {"arti_ber": "-nsen / -sen (Uddis n usget amalay)", "desc_ber": "Amqim uddis n usget amalay", "jenis_ber": "Amqim Uddis"},
    "1. Dhamir__3c": {"arti_ber": "I Nutni kan", "desc_ber": "Amqim imserreḥ n usemres i usget amalay", "jenis_ber": "Amqim Imserreḥ"},
    "1. Dhamir__4a": {"arti_ber": "Nettat (Asuf unti)", "desc_ber": "Amqim imserreḥ i wunti asuf unti", "jenis_ber": "Amqim Imserreḥ"},
    "1. Dhamir__4b": {"arti_ber": "-s / -is (Uddis unti)", "desc_ber": "Amqim uddis i wunti asuf unti", "jenis_ber": "Amqim Uddis"},
    "1. Dhamir__5a": {"arti_ber": "Nutenti (Asget unti)", "desc_ber": "Amqim imserreḥ n usget unti", "jenis_ber": "Amqim Imserreḥ"},
    "1. Dhamir__5b": {"arti_ber": "-nsent / -sent", "desc_ber": "Amqim uddis n usget unti", "jenis_ber": "Amqim Uddis"},
    "1. Dhamir__6a": {"arti_ber": "Kecč / Keččini (Asuf amalay)", "desc_ber": "Amqim imserreḥ n wawal asuf amalay", "jenis_ber": "Amqim Imserreḥ"},
    "1. Dhamir__6b": {"arti_ber": "-k / -ik (Uddis amalay)", "desc_ber": "Amqim uddis n wawal asuf amalay", "jenis_ber": "Amqim Uddis"},
    "1. Dhamir__6c": {"arti_ber": "I Kečč kan", "desc_ber": "Amqim imserreḥ n usemres i wawal amalay", "jenis_ber": "Amqim Imserreḥ"},
    "1. Dhamir__7a": {"arti_ber": "Kunwi sin / Kunemti snat", "desc_ber": "Amqim imserreḥ n sin wuddusen", "jenis_ber": "Amqim Imserreḥ"},
    "1. Dhamir__7b": {"arti_ber": "-twen sin", "desc_ber": "Amqim uddis n sin wuddusen", "jenis_ber": "Amqim Uddis"},
    "1. Dhamir__8a": {"arti_ber": "Kunwi (Asget amalay)", "desc_ber": "Amqim imserreḥ n usget amalay", "jenis_ber": "Amqim Imserreḥ"},
    "1. Dhamir__8b": {"arti_ber": "-nwen / -wen", "desc_ber": "Amqim uddis n usget amalay", "jenis_ber": "Amqim Uddis"},
    "1. Dhamir__8c": {"arti_ber": "I Kunwi kan", "desc_ber": "Amqim imserreḥ n usemres i usget amalay", "jenis_ber": "Amqim Imserreḥ"},
    "1. Dhamir__9a": {"arti_ber": "Kemm / Kemmini (Asuf unti)", "desc_ber": "Amqim imserreḥ n wawal asuf unti", "jenis_ber": "Amqim Imserreḥ"},
    "1. Dhamir__9b": {"arti_ber": "-m / -im (Uddis unti)", "desc_ber": "Amqim uddis n wawal asuf unti", "jenis_ber": "Amqim Uddis"},
    "1. Dhamir__10a": {"arti_ber": "Kunemti (Asget unti)", "desc_ber": "Amqim imserreḥ n usget unti", "jenis_ber": "Amqim Imserreḥ"},
    "1. Dhamir__10b": {"arti_ber": "-nkent / -kent", "desc_ber": "Amqim uddis n usget unti", "jenis_ber": "Amqim Uddis"},
    "1. Dhamir__11a": {"arti_ber": "Nekk / Nekkini (Amsawal asuf)", "desc_ber": "Amqim imserreḥ n umsawal asuf", "jenis_ber": "Amqim Imserreḥ"},
    "1. Dhamir__11b": {"arti_ber": "-iw / -i (Uddis n umsawal)", "desc_ber": "Amqim uddis n umsawal asuf", "jenis_ber": "Amqim Uddis"},
    "1. Dhamir__11c": {"arti_ber": "I Nekk kan", "desc_ber": "Amqim imserreḥ n usemres i umsawal", "jenis_ber": "Amqim Imserreḥ"},
    "1. Dhamir__12a": {"arti_ber": "Nekni / Neknenti (Asget)", "desc_ber": "Amqim imserreḥ n usget imsawalen", "jenis_ber": "Amqim Imserreḥ"},
    "1. Dhamir__12b": {"arti_ber": "-nneɣ / -neɣ", "desc_ber": "Amqim uddis n usget imsawalen", "jenis_ber": "Amqim Uddis"},
    "1. Dhamir__12c": {"arti_ber": "I Nekni kan", "desc_ber": "Amqim imserreḥ n usemres i usget", "jenis_ber": "Amqim Imserreḥ"},

    "2. Isim Mawshul__1": {"arti_ber": "Ayen / Wayen (I tɣawsiwin)", "desc_ber": "Amqim amassaɣ amatu i tɣawsiwin", "jenis_ber": "Amqim Amassaɣ"},
    "2. Isim Mawshul__2": {"arti_ber": "Wid / Widak (Asget amalay)", "desc_ber": "Amqim amassaɣ i medden (asget amalay)", "jenis_ber": "Amqim Amassaɣ"},
    "2. Isim Mawshul__3": {"arti_ber": "Win / Winna (I yemdanen)", "desc_ber": "Amqim amassaɣ amatu i yemdanen", "jenis_ber": "Amqim Amassaɣ"},
    "2. Isim Mawshul__4": {"arti_ber": "Win / A win (Asuf amalay)", "desc_ber": "Amqim amassaɣ n usuf amalay", "jenis_ber": "Amqim Amassaɣ"},
    "2. Isim Mawshul__5": {"arti_ber": "Kra n win / Menwala", "desc_ber": "Amqim amassaɣ uddis", "jenis_ber": "Amqim Amassaɣ"},
    "2. Isim Mawshul__6": {"arti_ber": "Tin / Tinna (Asuf unti)", "desc_ber": "Amqim amassaɣ n usuf unti", "jenis_ber": "Amqim Amassaɣ"},
    "2. Isim Mawshul__7": {"arti_ber": "Tid / Tiddak (Asget unti)", "desc_ber": "Amqim amassaɣ n usget unti", "jenis_ber": "Amqim Amassaɣ"},
    "2. Isim Mawshul__8": {"arti_ber": "Tid / Tilawin (Asget unti)", "desc_ber": "Amqim amassaɣ n usget unti", "jenis_ber": "Amqim Amassaɣ"},
    "2. Isim Mawshul__9": {"arti_ber": "Wid sin (Sin wuddusen)", "desc_ber": "Amqim amassaɣ n sin wuddusen", "jenis_ber": "Amqim Amassaɣ"},
    "2. Isim Mawshul__10": {"arti_ber": "Tin menwala (Unti)", "desc_ber": "Amqim amassaɣ unti", "jenis_ber": "Amqim Amassaɣ"},

    "3. Isim Istifham__1": {"arti_ber": "D acu / D acu-t", "desc_ber": "Tasarut n usteqsi i tɣawsiwin", "jenis_ber": "Isteqsi"},
    "3. Isim Istifham__2": {"arti_ber": "Anwa / Wi / Menhu", "desc_ber": "Tasarut n usteqsi i yemdanen", "jenis_ber": "Isteqsi"},
    "3. Isim Istifham__3": {"arti_ber": "Amek / Acuɣer", "desc_ber": "Tasarut n usteqsi n waddad", "jenis_ber": "Isteqsi"},
    "3. Isim Istifham__4": {"arti_ber": "Anda / Anida", "desc_ber": "Tasarut n usteqsi n umkan", "jenis_ber": "Isteqsi n Umkan"},
    "3. Isim Istifham__5": {"arti_ber": "Acḥal / Amek teggra", "desc_ber": "Tasarut n usteqsi n umḍan", "jenis_ber": "Isteqsi"},
    "3. Isim Istifham__6": {"arti_ber": "Melmi / Ay amelmi", "desc_ber": "Tasarut n usteqsi n wakud", "jenis_ber": "Isteqsi n Wakud"},
    "3. Isim Istifham__7": {"arti_ber": "Melmi dɣa (Akud yugaren)", "desc_ber": "Tasarut n usteqsi n wakud deg yimal", "jenis_ber": "Isteqsi"},
    "3. Isim Istifham__8": {"arti_ber": "Seg wanda / Amek akka", "desc_ber": "Tasarut n usteqsi n tmentilt", "jenis_ber": "Isteqsi"},

    "4. Isim Syarath__1": {"arti_ber": "Kra n win / Win akken", "desc_ber": "Taseddariy n tawtilt i yemdanen", "jenis_ber": "Taseddariy n Tawtilt"},
    "4. Isim Syarath__2": {"arti_ber": "Kra n wayen / Ayen akken", "desc_ber": "Taseddariy n tawtilt i tɣawsiwin", "jenis_ber": "Taseddariy n Tawtilt"},
    "4. Isim Syarath__3": {"arti_ber": "Mi / Asmi / Mara", "desc_ber": "Taseddariy n tawtilt n wakud", "jenis_ber": "Taseddariy n Wakud"},
    "4. Isim Syarath__4": {"arti_ber": "Akken yebɣu yili / Menwala", "desc_ber": "Taseddariy n tawtilt tamatut", "jenis_ber": "Taseddariy n Tawtilt"},
    "4. Isim Syarath__5": {"arti_ber": "Anda yebɣu yili / Anida", "desc_ber": "Taseddariy n tawtilt n umkan", "jenis_ber": "Taseddariy n Umkan"},
    "4. Isim Syarath__6": {"arti_ber": "Anda akken / Anida kan", "desc_ber": "Taseddariy n tawtilt n umkan", "jenis_ber": "Taseddariy n Umkan"},
    "4. Isim Syarath__7": {"arti_ber": "Akken yebɣu waddad", "desc_ber": "Taseddariy n tawtilt n waddad", "jenis_ber": "Taseddariy n Tawtilt"},
    "4. Isim Syarath__8": {"arti_ber": "Ayen / Win menwala", "desc_ber": "Taseddariy n tawtilt", "jenis_ber": "Taseddariy n Tawtilt"},

    "5. Isim Isyarah__1": {"arti_ber": "Wina / Winna (Asuf amalay agwaj)", "desc_ber": "Amqim n usmmal i wayen ibeɛden", "jenis_ber": "Amqim n Usmmal"},
    "5. Isim Isyarah__2": {"arti_ber": "Wagi / Wa (Asuf amalay aqrib)", "desc_ber": "Amqim n usmmal i wayen iqerben", "jenis_ber": "Amqim n Usmmal"},
    "5. Isim Isyarah__3": {"arti_ber": "Wigi / Widak-agi (Asget aqrib)", "desc_ber": "Amqim n usmmal n usget iqerben", "jenis_ber": "Amqim n Usmmal"},
    "5. Isim Isyarah__4": {"arti_ber": "Widak-in / Widina (Asget agwaj)", "desc_ber": "Amqim n usmmal n usget ibeɛden", "jenis_ber": "Amqim n Usmmal"},
    "5. Isim Isyarah__5": {"arti_ber": "Tagi / Ta (Asuf unti aqrib)", "desc_ber": "Amqim n usmmal n usuf unti", "jenis_ber": "Amqim n Usmmal"},
    "5. Isim Isyarah__6": {"arti_ber": "Tinna / Tagiya (Asuf unti agwaj)", "desc_ber": "Amqim n usmmal n usuf unti ibeɛden", "jenis_ber": "Amqim n Usmmal"},
    "5. Isim Isyarah__7": {"arti_ber": "Dina / Dinna (Amkan agwaj)", "desc_ber": "Amqim n usmmal n umkan ibeɛden", "jenis_ber": "Amqim n Umkan"},
    "5. Isim Isyarah__8": {"arti_ber": "Dagi / Daki (Amkan aqrib)", "desc_ber": "Amqim n usmmal n umkan iqerben", "jenis_ber": "Amqim n Umkan"},
    "5. Isim Isyarah__9": {"arti_ber": "Wid sin-ina", "desc_ber": "Amqim n usmmal n sin wuddusen ibeɛden", "jenis_ber": "Amqim n Usmmal"},
    "5. Isim Isyarah__10": {"arti_ber": "Tid snat-ina", "desc_ber": "Amqim n usmmal n snat tseddariyin", "jenis_ber": "Amqim n Usmmal"},

    "6. Isim Fi'il__1": {"arti_ber": "Ibeɛɛed aṭas! (Hayhata)", "desc_ber": "Isem n tigawt n yezrin", "jenis_ber": "Isem n Tigawt"},
    "6. Isim Fi'il__2": {"arti_ber": "Uff! / Kkseɣ lxiq (Uff)", "desc_ber": "Isem n tigawt n yimir", "jenis_ber": "Isem n Tigawt"},
    "6. Isim Fi'il__3": {"arti_ber": "Eyyaw-d! / Awit-d!", "desc_ber": "Isem n tigawt n wanaḍ", "jenis_ber": "Isem n Tigawt"},
    "6. Isim Fi'il__4": {"arti_ber": "Awet-tt! / Eṭṭfet!", "desc_ber": "Isem n tigawt n wanaḍ", "jenis_ber": "Isem n Tigawt"},
    "6. Isim Fi'il__5": {"arti_ber": "Ḥadret iman-nwen! / Ṭṭfet deg", "desc_ber": "Isem n tigawt n wanaḍ", "jenis_ber": "Isem n Tigawt"},
    "6. Isim Fi'il__6": {"arti_ber": "Ṭṭfet / Ddmet-tt", "desc_ber": "Isem n tigawt n wanaḍ", "jenis_ber": "Isem n Tigawt"},
    "6. Isim Fi'il__7": {"arti_ber": "Weh! / D awehham!", "desc_ber": "Isem n tigawt n lwehba", "jenis_ber": "Isem n Tigawt"},
    "6. Isim Fi'il__8": {"arti_ber": "Wexxret! / Aql-att gar-awen", "desc_ber": "Isem n tigawt n wanaḍ", "jenis_ber": "Isem n Tigawt"},

    "7. Fi'il Jamid__1": {"arti_ber": "Yelha mliḥ! (Ni'ma)", "desc_ber": "Amyag akiwan n ccekran", "jenis_ber": "Amyag Akiwan"},
    "7. Fi'il Jamid__2": {"arti_ber": "Yir-it! / Dir-it mliḥ (Bi'sa)", "desc_ber": "Amyag akiwan n udemmer", "jenis_ber": "Amyag Akiwan"},
    "7. Fi'il Jamid__3": {"arti_ber": "Ur yelli ara (Laysa)", "desc_ber": "Amyag akiwan n tugint", "jenis_ber": "Amyag Akiwan"},
    "7. Fi'il Jamid__4": {"arti_ber": "Ahat / Yezmer lḥal ('Asa)", "desc_ber": "Amyag akiwan n usirem", "jenis_ber": "Amyag Akiwan"},
    "7. Fi'il Jamid__5": {"arti_ber": "D ayen diri mliḥ (Sa'a)", "desc_ber": "Amyag akiwan n udemmer", "jenis_ber": "Amyag Akiwan"},
    "7. Fi'il Jamid__6": {"arti_ber": "Acu tzedha! (Habbadha)", "desc_ber": "Amyag akiwan n ccekran", "jenis_ber": "Amyag Akiwan"},
    "7. Fi'il Jamid__7": {"arti_ber": "D bab n lbaraka tameqrant (Tabaraka)", "desc_ber": "Amyag akiwan n uselmed d lbaraka", "jenis_ber": "Amyag Akiwan"}
}

AMHARIC_GRAMMAR = {
    "1. Dhamir__1a": {"arti_am": "እርሱ (ወንድ ነጠላ)", "desc_am": "3ኛ መደብ ወንድ ነጠላ ተነጣይ ባለቤት ተውላጠ ስም (ሙንፈሲል)", "jenis_am": "ተነጣይ ባለቤት ተውላጠ ስም"},
    "1. Dhamir__1b": {"arti_am": "የእርሱ / እርሱን (ተያያዥ)", "desc_am": "3ኛ መደብ ወንድ ነጠላ ተያያዥ ተውላጠ ስም (ሙተሲል)", "jenis_am": "ተያያዥ ተውላጠ ስም"},
    "1. Dhamir__1c": {"arti_am": "እርሱን ብቻ (ተነጣይ ተሳቢ)", "desc_am": "3ኛ መደብ ወንድ ነጠላ ተነጣይ ተሳቢ ተውላጠ ስም", "jenis_am": "ተነጣይ ተሳቢ ተውላጠ ስም"},
    "1. Dhamir__2a": {"arti_am": "እነርሱ ሁለቱ (ድርብ)", "desc_am": "3ኛ መደብ ድርብ ተነጣይ ባለቤት ተውላጠ ስም", "jenis_am": "ተነጣይ ተውላጠ ስም"},
    "1. Dhamir__2b": {"arti_am": "የሁለታቸው / እነርሱን ሁለቱን (ተያያዥ)", "desc_am": "3ኛ መደብ ድርብ ተያያዥ ተውላጠ ስም", "jenis_am": "ተያያዥ ተውላጠ ስም"},
    "1. Dhamir__3a": {"arti_am": "እነርሱ (ወንዶች ብዙ)", "desc_am": "3ኛ መደብ ወንድ ብዙ ተነጣይ ባለቤት ተውላጠ ስም", "jenis_am": "ተነጣይ ባለቤት ተውላጠ ስም"},
    "1. Dhamir__3b": {"arti_am": "የእነርሱ / እነርሱን (ተያያዥ)", "desc_am": "3ኛ መደብ ወንድ ብዙ ተያያዥ ተውላጠ ስም", "jenis_am": "ተያያዥ ተውላጠ ስም"},
    "1. Dhamir__3c": {"arti_am": "እነርሱን ብቻ", "desc_am": "3ኛ መደብ ወንድ ብዙ ተነጣይ ተሳቢ ተውላጠ ስም", "jenis_am": "ተነጣይ ተሳቢ ተውላጠ ስም"},
    "1. Dhamir__4a": {"arti_am": "እርስዋ (ሴት ነጠላ)", "desc_am": "3ኛ መደብ ሴት ነጠላ ተነጣይ ባለቤት ተውላጠ ስም", "jenis_am": "ተነጣይ ባለቤት ተውላጠ ስም"},
    "1. Dhamir__4b": {"arti_am": "የእርስዋ / እርስዋን (ተያያዥ)", "desc_am": "3ኛ መደብ ሴት ነጠላ ተያያዥ ተውላጠ ስም", "jenis_am": "ተያያዥ ተውላጠ ስም"},
    "1. Dhamir__5a": {"arti_am": "እነርሱ (ሴቶች ብዙ)", "desc_am": "3ኛ መደብ ሴት ብዙ ተነጣይ ባለቤት ተውላጠ ስም", "jenis_am": "ተነጣይ ባለቤት ተውላጠ ስም"},
    "1. Dhamir__5b": {"arti_am": "የእነርሱ (ሴቶች ተያያዥ)", "desc_am": "3ኛ መደብ ሴት ብዙ ተያያዥ ተውላጠ ስም", "jenis_am": "ተያያዥ ተውላጠ ስም"},
    "1. Dhamir__6a": {"arti_am": "አንተ (ወንድ ነጠላ)", "desc_am": "2ኛ መደብ ወንድ ነጠላ ተነጣይ ባለቤት ተውላጠ ስም", "jenis_am": "ተነጣይ ባለቤት ተውላጠ ስም"},
    "1. Dhamir__6b": {"arti_am": "የአንተ / አንተን (ተያያዥ)", "desc_am": "2ኛ መደብ ወንድ ነጠላ ተያያዥ ተውላጠ ስም", "jenis_am": "ተያያዥ ተውላጠ ስም"},
    "1. Dhamir__6c": {"arti_am": "አንተን ብቻ (ተነጣይ ተሳቢ)", "desc_am": "2ኛ መደብ ወንድ ነጠላ ተነጣይ ተሳቢ ተውላጠ ስም ለአምልኮ ብቻ", "jenis_am": "ተነጣይ ተሳቢ ተውላጠ ስም"},
    "1. Dhamir__7a": {"arti_am": "እናንተ ሁለታችሁ", "desc_am": "2ኛ መደብ ድርብ ተነጣይ ባለቤት ተውላጠ ስም", "jenis_am": "ተነጣይ ተውላጠ ስም"},
    "1. Dhamir__7b": {"arti_am": "የሁለታችሁ (ተያያዥ)", "desc_am": "2ኛ መደብ ድርብ ተያያዥ ተውላጠ ስም", "jenis_am": "ተያያዥ ተውላጠ ስም"},
    "1. Dhamir__8a": {"arti_am": "እናንተ (ወንዶች ብዙ)", "desc_am": "2ኛ መደብ ወንድ ብዙ ተነጣይ ባለቤት ተውላጠ ስም", "jenis_am": "ተነጣይ ባለቤት ተውላጠ ስም"},
    "1. Dhamir__8b": {"arti_am": "የእናንተ / እናንተን (ተያያዥ)", "desc_am": "2ኛ መደብ ወንድ ብዙ ተያያዥ ተውላጠ ስም", "jenis_am": "ተያያዥ ተውላጠ ስም"},
    "1. Dhamir__8c": {"arti_am": "እናንተን ብቻ", "desc_am": "2ኛ መደብ ወንድ ብዙ ተነጣይ ተሳቢ ተውላጠ ስም", "jenis_am": "ተነጣይ ተሳቢ ተውላጠ ስም"},
    "1. Dhamir__9a": {"arti_am": "አንቺ (ሴት ነጠላ)", "desc_am": "2ኛ መደብ ሴት ነጠላ ተነጣይ ባለቤት ተውላጠ ስም", "jenis_am": "ተነጣይ ባለቤት ተውላጠ ስም"},
    "1. Dhamir__9b": {"arti_am": "የአንቺ / አንቺን (ተያያዥ)", "desc_am": "2ኛ መደብ ሴት ነጠላ ተያያዥ ተውላጠ ስም", "jenis_am": "ተያያዥ ተውላጠ ስም"},
    "1. Dhamir__10a": {"arti_am": "እናንተ (ሴቶች ብዙ)", "desc_am": "2ኛ መደብ ሴት ብዙ ተነጣይ ባለቤት ተውላጠ ስም", "jenis_am": "ተነጣይ ባለቤት ተውላጠ ስም"},
    "1. Dhamir__10b": {"arti_am": "የእናንተ (ሴቶች ተያያዥ)", "desc_am": "2ኛ መደብ ሴት ብዙ ተያያዥ ተውላጠ ስም", "jenis_am": "ተያያዥ ተውላጠ ስም"},
    "1. Dhamir__11a": {"arti_am": "እኔ (1ኛ መደብ ነጠላ)", "desc_am": "1ኛ መደብ ነጠላ ተነጣይ ባለቤት ተውላጠ ስም", "jenis_am": "ተነጣይ ባለቤት ተውላጠ ስም"},
    "1. Dhamir__11b": {"arti_am": "የእኔ / እኔን (ተያያዥ)", "desc_am": "1ኛ መደብ ነጠላ ተያያዥ ተውላጠ ስም", "jenis_am": "ተያያዥ ተውላጠ ስም"},
    "1. Dhamir__11c": {"arti_am": "እኔን ብቻ", "desc_am": "1ኛ መደብ ነጠላ ተነጣይ ተሳቢ ተውላጠ ስም", "jenis_am": "ተነጣይ ተሳቢ ተውላጠ ስም"},
    "1. Dhamir__12a": {"arti_am": "እኛ (1ኛ መደብ ብዙ)", "desc_am": "1ኛ መደብ ብዙ ተነጣይ ባለቤት ተውላጠ ስም", "jenis_am": "ተነጣይ ባለቤት ተውላጠ ስም"},
    "1. Dhamir__12b": {"arti_am": "የእኛ / እኛን (ተያያዥ)", "desc_am": "1ኛ መደብ ብዙ ተያያዥ ተውላጠ ስም", "jenis_am": "ተያያዥ ተውላጠ ስም"},
    "1. Dhamir__12c": {"arti_am": "እኛን ብቻ", "desc_am": "1ኛ መደብ ብዙ ተነጣይ ተሳቢ ተውላጠ ስም", "jenis_am": "ተነጣይ ተሳቢ ተውላጠ ስም"},

    "2. Isim Mawshul__1": {"arti_am": "ያ / ያ ነገር (ለማሰብ ለማይችሉ)", "desc_am": "አጠቃላይ አዛማጅ ተውላጠ ስም ለግዑዝ ነገሮች", "jenis_am": "አዛማጅ ተውላጠ ስም"},
    "2. Isim Mawshul__2": {"arti_am": "እነዚያ (ወንዶች ብዙ)", "desc_am": "ልዩ አዛማጅ ተውላጠ ስም ለብዙ ሰዎች", "jenis_am": "አዛማጅ ተውላጠ ስም"},
    "2. Isim Mawshul__3": {"arti_am": "ያ ሰው / ማንም (ለሰው ልጆች)", "desc_am": "አጠቃላይ አዛማጅ ተውላጠ ስም ለሰው ልጆች", "jenis_am": "አዛማጅ ተውላጠ ስም"},
    "2. Isim Mawshul__4": {"arti_am": "ያ / እርሱ (ወንድ ነጠላ)", "desc_am": "ልዩ አዛማጅ ተውላጠ ስም ለነጠላ ወንድ", "jenis_am": "አዛማጅ ተውላጠ ስም"},
    "2. Isim Mawshul__5": {"arti_am": "የትኛውም / የትኛዋም", "desc_am": "ተደማሪ አዛማጅ ተውላጠ ስም", "jenis_am": "አዛማጅ ተውላጠ ስም"},
    "2. Isim Mawshul__6": {"arti_am": "ያች (ሴት ነጠላ)", "desc_am": "ልዩ አዛማጅ ተውላጠ ስም ለነጠላ ሴት", "jenis_am": "አዛማጅ ተውላጠ ስም"},
    "2. Isim Mawshul__7": {"arti_am": "እነዚያ ሴቶች (ብዙ)", "desc_am": "ልዩ አዛማጅ ተውላጠ ስም ለሴቶች", "jenis_am": "አዛማጅ ተውላጠ ስም"},
    "2. Isim Mawshul__8": {"arti_am": "እነዚያ ሴቶች (ብዙ)", "desc_am": "ልዩ አዛማጅ ተውላጠ ስም ለሴቶች", "jenis_am": "አዛማጅ ተውላጠ ስም"},
    "2. Isim Mawshul__9": {"arti_am": "እነዚያ ሁለቱ (ወንዶች)", "desc_am": "ድርብ አዛማጅ ተውላጠ ስም", "jenis_am": "አዛማጅ ተውላጠ ስም"},
    "2. Isim Mawshul__10": {"arti_am": "የትኛዋም (ሴት)", "desc_am": "አዛማጅ ተውላጠ ስም ለሴት", "jenis_am": "አዛማጅ ተውላጠ ስም"},

    "3. Isim Istifham__1": {"arti_am": "ምን / ምንድን ነው?", "desc_am": "የመጠይቅ ቃል ለግዑዝ ነገሮች", "jenis_am": "መጠይቅ ቃል"},
    "3. Isim Istifham__2": {"arti_am": "ማን / ማን ነው?", "desc_am": "የመጠይቅ ቃል ለሰው ልጆች", "jenis_am": "መጠይቅ ቃል"},
    "3. Isim Istifham__3": {"arti_am": "እንዴት / በምን ሁኔታ?", "desc_am": "የሁኔታ መጠይቅ ቃል", "jenis_am": "የሁኔታ መጠይቅ"},
    "3. Isim Istifham__4": {"arti_am": "የት / በየትኛው ስፍራ?", "desc_am": "የቦታ መጠይቅ ቃል", "jenis_am": "የቦታ መጠይቅ"},
    "3. Isim Istifham__5": {"arti_am": "ስንት / ምን ያህል?", "desc_am": "የቁጥር መጠይቅ ቃል", "jenis_am": "የቁጥር መጠይቅ"},
    "3. Isim Istifham__6": {"arti_am": "መቼ / በምን ጊዜ?", "desc_am": "የጊዜ መጠይቅ ቃል", "jenis_am": "የጊዜ መጠይቅ"},
    "3. Isim Istifham__7": {"arti_am": "መቼ ይሆን? (ለከባድ ጊዜያት)", "desc_am": "የወደፊት ጊዜ መጠይቅ ቃል", "jenis_am": "የጊዜ መጠይቅ"},
    "3. Isim Istifham__8": {"arti_am": "ከየት / እንዴት ሆኖ?", "desc_am": "የመነሻና ሁኔታ መጠይቅ ቃል", "jenis_am": "መጠይቅ ቃል"},

    "4. Isim Syarath__1": {"arti_am": "ማንም ሰው / የፈጸመ ሰው", "desc_am": "ተግባር ሻሪ ቅድመ-ሁኔታ ቃል ለሰው ልጆች", "jenis_am": "ቅድመ-ሁኔታ ቃል"},
    "4. Isim Syarath__2": {"arti_am": "ማንኛውንም ነገር / ያደረጋችሁትን", "desc_am": "ተግባር ሻሪ ቅድመ-ሁኔታ ቃል ለነገሮች", "jenis_am": "ቅድመ-ሁኔታ ቃል"},
    "4. Isim Syarath__3": {"arti_am": "በ... ጊዜ / በደረሰ ጊዜ", "desc_am": "የጊዜ ቅድመ-ሁኔታ ቃል ለወደፊት", "jenis_am": "የጊዜ ቅድመ-ሁኔታ"},
    "4. Isim Syarath__4": {"arti_am": "ምንም ያህል ቢሆን / ምንም ነገር", "desc_am": "ተግባር ሻሪ አጠቃላይ ቅድመ-ሁኔታ ቃል", "jenis_am": "ቅድመ-ሁኔታ ቃል"},
    "4. Isim Syarath__5": {"arti_am": "በየትኛውም ስፍራ / በሄዳችሁበት", "desc_am": "የቦታ ቅድመ-ሁኔታ ቃል", "jenis_am": "የቦታ ቅድመ-ሁኔታ"},
    "4. Isim Syarath__6": {"arti_am": "በየትኛውም ቦታ", "desc_am": "የቦታ ቅድመ-ሁኔታ ቃል", "jenis_am": "የቦታ ቅድመ-ሁኔታ"},
    "4. Isim Syarath__7": {"arti_am": "በማንኛውም ሁኔታ", "desc_am": "የሁኔታ ቅድመ-ሁኔታ ቃል", "jenis_am": "የሁኔታ ቅድመ-ሁኔታ"},
    "4. Isim Syarath__8": {"arti_am": "የትኛውም / የትኛውንም", "desc_am": "ተግባር ሻሪ ቅድመ-ሁኔታ ቃል", "jenis_am": "ቅድመ-ሁኔታ ቃል"},

    "5. Isim Isyarah__1": {"arti_am": "ያ / ያ መጽሐፍ (የርቀት ወንድ)", "desc_am": "የሩቅ አመላካች ተውላጠ ስም ለነጠላ ወንድ", "jenis_am": "የሩቅ አመላካች"},
    "5. Isim Isyarah__2": {"arti_am": "ይህ / ይህ ነገር (የቅርብ ወንድ)", "desc_am": "የቅርብ አመላካች ተውላጠ ስም ለነጠላ ወንድ", "jenis_am": "የቅርብ አመላካች"},
    "5. Isim Isyarah__3": {"arti_am": "እነዚህ (የቅርብ ብዙ)", "desc_am": "የቅርብ አመላካች ተውላጠ ስም ለብዙ", "jenis_am": "የቅርብ አመላካች"},
    "5. Isim Isyarah__4": {"arti_am": "እነዚያ (የርቀት ብዙ)", "desc_am": "የሩቅ አመላካች ተውላጠ ስም ለብዙ", "jenis_am": "የሩቅ አመላካች"},
    "5. Isim Isyarah__5": {"arti_am": "ይህች (የቅርብ ሴት)", "desc_am": "የቅርብ አመላካች ተውላጠ ስም ለነጠላ ሴት", "jenis_am": "የቅርብ አመላካች"},
    "5. Isim Isyarah__6": {"arti_am": "ያች (የርቀት ሴት)", "desc_am": "የሩቅ አመላካች ተውላጠ ስም ለነጠላ ሴት", "jenis_am": "የሩቅ አመላካች"},
    "5. Isim Isyarah__7": {"arti_am": "በዚያ ስፍራ / በዚያ ጊዜ", "desc_am": "የሩቅ ቦታ አመላካች ተውላጠ ስም", "jenis_am": "የቦታ አመላካች"},
    "5. Isim Isyarah__8": {"arti_am": "እዚህ / በዚህ ስፍራ", "desc_am": "የቅርብ ቦታ አመላካች ተውላጠ ስም", "jenis_am": "የቦታ አመላካች"},
    "5. Isim Isyarah__9": {"arti_am": "እነዚያ ሁለቱ (የርቀት ወንድ)", "desc_am": "የሩቅ አመላካች ተውላጠ ስም ለድርብ", "jenis_am": "የሩቅ አመላካች"},
    "5. Isim Isyarah__10": {"arti_am": "እነዚያ ሁለቱ (የርቀት ሴት)", "desc_am": "የሩቅ አመላካች ተውላጠ ስም ለድርብ ሴት", "jenis_am": "የሩቅ አመላካች"},

    "6. Isim Fi'il__1": {"arti_am": "እጅግ በጣም ራቀ! (ኃይሃተ)", "desc_am": "ያለፈ ጊዜ ግሳዊ ስም", "jenis_am": "ግሳዊ ስም"},
    "6. Isim Fi'il__2": {"arti_am": "ኡፍ! / መሰልቸት (ኡፍ)", "desc_am": "የአሁን ጊዜ ግሳዊ ስም የመሰልቸት መግለጫ", "jenis_am": "ግሳዊ ስም"},
    "6. Isim Fi'il__3": {"arti_am": "ኑ! / አምጡ!", "desc_am": "የትእዛዝ ግሳዊ ስም", "jenis_am": "ግሳዊ ስም"},
    "6. Isim Fi'il__4": {"arti_am": "ውሰዱ! / ያዙ!", "desc_am": "የትእዛዝ ግሳዊ ስም", "jenis_am": "ግሳዊ ስም"},
    "6. Isim Fi'il__5": {"arti_am": "ራሳችሁን ጠብቁ! / አጥብቃችሁ ያዙ!", "desc_am": "የትእዛዝ ግሳዊ ስም ከመስተዋድድ የተወሰደ", "jenis_am": "ግሳዊ ስም"},
    "6. Isim Fi'il__6": {"arti_am": "ውሰዱት!", "desc_am": "የትእዛዝ ግሳዊ ስም", "jenis_am": "ግሳዊ ስም"},
    "6. Isim Fi'il__7": {"arti_am": "ድንቅ ነው! / ይገርማል!", "desc_am": "የአግራሞት ግሳዊ ስም", "jenis_am": "ግሳዊ ስም"},
    "6. Isim Fi'il__8": {"arti_am": "ራቁ! / ይኸውላችሁ", "desc_am": "የትእዛዝ ግሳዊ ስም", "jenis_am": "ግሳዊ ስም"},

    "7. Fi'il Jamid__1": {"arti_am": "ምንኛ አማረ! / ምንኛ በጎ ሆነ! (ኒዕመ)", "desc_am": "የምስጋና የማይዘረዘር ግሥ", "jenis_am": "የማይዘረዘር ግሥ"},
    "7. Fi'il Jamid__2": {"arti_am": "ምንኛ ከፋ! / ምንኛ አስጠላ! (ቢእሰ)", "desc_am": "የወቀሳ የማይዘረዘር ግሥ", "jenis_am": "የማይዘረዘር ግሥ"},
    "7. Fi'il Jamid__3": {"arti_am": "አይደለም / አልነበረም (ለይሰ)", "desc_am": "የአሉታ የማይዘረዘር ጎዶሎ ግሥ", "jenis_am": "የማይዘረዘር ግሥ"},
    "7. Fi'il Jamid__4": {"arti_am": "ይቻላል / ተስፋ ይደረጋል (ዐሳ)", "desc_am": "የተስፋ የማይዘረዘር ግሥ", "jenis_am": "የማይዘረዘር ግሥ"},
    "7. Fi'il Jamid__5": {"arti_am": "ምንኛ ከፋ! (ሳአ)", "desc_am": "የወቀሳ የማይዘረዘር ግሥ", "jenis_am": "የማይዘረዘር ግሥ"},
    "7. Fi'il Jamid__6": {"arti_am": "ምንኛ ደስ ይላል!", "desc_am": "የምስጋና የማይዘረዘር ግሥ", "jenis_am": "የማይዘረዘር ግሥ"},
    "7. Fi'il Jamid__7": {"arti_am": "በረከቱ ላቀ! (ተባረከ)", "desc_am": "የአላህ ክብር መግለጫ የማይዘረዘር ግሥ", "jenis_am": "የማይዘረዘር ግሥ"}
}

AMAZIGH_HARF_GRAMMAR = {
    "1. Harf Nafyi__1": {"arti_ber": "Ur / Ur d (Tugint tamatut)", "desc_ber": "Taseddariy n tugint i yezrin d yimir", "jenis_ber": "Taseddariy n Tugint"},
    "1. Harf Nafyi__2": {"arti_ber": "Ur / Ur tt- (Tugint n tigawt)", "desc_ber": "Taseddariy n tugint n yimir d yimal", "jenis_ber": "Taseddariy n Tugint"},
    "1. Harf Nafyi__3": {"arti_ber": "Ur d ayen nniḍen anagar...", "desc_ber": "Taseddariy n tugint (In) yeqqnen ɣer Illa", "jenis_ber": "Taseddariy n Tugint"},
    "1. Harf Nafyi__4": {"arti_ber": "Mačči d lawan n...", "desc_ber": "Taseddariy n tugint i wakud", "jenis_ber": "Taseddariy n Tugint"},

    "2. Harf Tahqiq Taswif__5": {"arti_ber": "Niɣ / S tideţ (Qad - Asentem)", "desc_ber": "Taseddariy n usentem n tideţ", "jenis_ber": "Taseddariy n Usentem"},
    "2. Harf Tahqiq Taswif__6": {"arti_ber": "Ad / Syin ɣer zdat (Sawfa - Imal)", "desc_ber": "Taseddariy n yimal agwaj", "jenis_ber": "Taseddariy n Yimal"},
    "2. Harf Tahqiq Taswif__7": {"arti_ber": "Ad (Sa - Imal aqrib)", "desc_ber": "Taseddariy n yimal iqerben", "jenis_ber": "Taseddariy n Yimal"},

    "3. Harf Syarat__8": {"arti_ber": "Lemmer / Lemmer i (Law)", "desc_ber": "Taseddariy n tawtilt ur nesɛi asemres", "jenis_ber": "Taseddariy n Tawtilt"},
    "3. Harf Syarat__9": {"arti_ber": "Lemmer mačči d...", "desc_ber": "Taseddariy n tawtilt n usebded", "jenis_ber": "Taseddariy n Tawtilt"},
    "3. Harf Syarat__10": {"arti_ber": "Lemmer mačči d...", "desc_ber": "Taseddariy n tawtilt", "jenis_ber": "Taseddariy n Tawtilt"},
    "3. Harf Syarat__11": {"arti_ber": "Mi / Asmi akken (Lamma)", "desc_ber": "Taseddariy n wakud i yezrin", "jenis_ber": "Taseddariy n Wakud"},
    "3. Harf Syarat__12": {"arti_ber": "Ma d... ihi (Amma)", "desc_ber": "Taseddariy n tseddart d usentem", "jenis_ber": "Taseddariy n Tawtilt"},

    "4. Harf Mashdariyah__13": {"arti_ber": "Akken / Aken ad (An)", "desc_ber": "Taseddariy tasmadart n tigawt", "jenis_ber": "Taseddariy Tasmadart"},
    "4. Harf Mashdariyah__14": {"arti_ber": "Skud / Ayen akk (Ma)", "desc_ber": "Taseddariy tasmadart n wakud", "jenis_ber": "Taseddariy Tasmadart"},
    "4. Harf Mashdariyah__15": {"arti_ber": "Iwakken ad / Akken (Kay)", "desc_ber": "Taseddariy n tmentilt", "jenis_ber": "Taseddariy Tasmadart"},
    "4. Harf Mashdariyah__16": {"arti_ber": "Lemmer / Ahat ad (Law)", "desc_ber": "Taseddariy tasmadart n usirem", "jenis_ber": "Taseddariy Tasmadart"},

    "5. Harf Zaidah__17": {"arti_ber": "I usentem (In Zaidah)", "desc_ber": "Taseddariy timernit n usedmer", "jenis_ber": "Taseddariy Timernit"},
    "5. Harf Zaidah__18": {"arti_ber": "I usentem (An Zaidah)", "desc_ber": "Taseddariy timernit", "jenis_ber": "Taseddariy Timernit"},
    "5. Harf Zaidah__19": {"arti_ber": "I usentem (Ma Zaidah)", "desc_ber": "Taseddariy timernit n usedmer", "jenis_ber": "Taseddariy Timernit"},
    "5. Harf Zaidah__20": {"arti_ber": "I usentem (La Zaidah)", "desc_ber": "Taseddariy timernit n tugint", "jenis_ber": "Taseddariy Timernit"},

    "6. Harf Istifham__21": {"arti_ber": "Dayen / Ma? (Hamzah)", "desc_ber": "Tasarut n usteqsi n tidet", "jenis_ber": "Tasarut n Usteqsi"},
    "6. Harf Istifham__22": {"arti_ber": "Dayen / Ma yella? (Hal)", "desc_ber": "Tasarut n usteqsi", "jenis_ber": "Tasarut n Usteqsi"},

    "7. Harf Istitsna__23": {"arti_ber": "Anagar / Has (Illa)", "desc_ber": "Taseddariy n usizdel d usegrew", "jenis_ber": "Taseddariy n Usizdel"},

    "8. Harf Rad'in Wazajrin__24": {"arti_ber": "Xas akken! / Xa d lbaṭel! (Kalla)", "desc_ber": "Taseddariy n usbedd d usguri", "jenis_ber": "Taseddariy n Usbedd"},

    "9. Harf Rad'in Tahdid__25": {"arti_ber": "Acuɣer ur... ara? (Halla)", "desc_ber": "Taseddariy n tuzzya d usḥulfu", "jenis_ber": "Taseddariy n Tuzzya"},
    "9. Harf Rad'in Tahdid__26": {"arti_ber": "Acuɣer ur... ara? (Alla)", "desc_ber": "Taseddariy n tuzzya", "jenis_ber": "Taseddariy n Tuzzya"},

    "10. Harf Ijab__27": {"arti_ber": "Ih / D tidet (Na'am)", "desc_ber": "Taseddariy n uqevel d tririt", "jenis_ber": "Taseddariy n Uqevel"},
    "10. Harf Ijab__28": {"arti_ber": "Ih s tideţ! (Bala)", "desc_ber": "Taseddariy n uqevel n tugint", "jenis_ber": "Taseddariy n Uqevel"},
    "10. Harf Ijab__29": {"arti_ber": "Ih s Rebbi! (I)", "desc_ber": "Taseddariy n tgallit d uqevel", "jenis_ber": "Taseddariy n Uqevel"},
    "10. Harf Ijab__30": {"arti_ber": "Ih d tideţ (Ajal)", "desc_ber": "Taseddariy n usentem", "jenis_ber": "Taseddariy n Uqevel"},

    "11. Harf Tafsir__31": {"arti_ber": "Yeɛni / D ayen (Ay)", "desc_ber": "Taseddariy n usegzi", "jenis_ber": "Taseddariy n Usegzi"},
    "11. Harf Tafsir__32": {"arti_ber": "Dakken / Akken (An)", "desc_ber": "Taseddariy n usegzi", "jenis_ber": "Taseddariy n Usegzi"},

    "12. Harf Tanbih__33": {"arti_ber": "Ḥadret! / Ẓret! (Ala)", "desc_ber": "Taseddariy n tazzwara d usḥulfu", "jenis_ber": "Taseddariy n Usḥulfu"},
    "12. Harf Tanbih__34": {"arti_ber": "Ḥadret! (Ama)", "desc_ber": "Taseddariy n usḥulfu", "jenis_ber": "Taseddariy n Usḥulfu"},
    "12. Harf Tanbih__35": {"arti_ber": "Aql-it! / Aql-aɣ! (Ha)", "desc_ber": "Taseddariy n usḥulfu n usmmal", "jenis_ber": "Taseddariy n Usḥulfu"},

    "13. Harf Ta'lil__36": {"arti_ber": "Iwakken ad / Ɣef ljal (Li-)", "desc_ber": "Taseddariy n tmentilt", "jenis_ber": "Taseddariy n Tmentilt"},

    "14. Harf Fuja'iyyah__37": {"arti_ber": "Din din kan! / Yufa-d (Idha)", "desc_ber": "Taseddariy n tifekkit", "jenis_ber": "Taseddariy n Tifekkit"},
    "14. Harf Fuja'iyyah__38": {"arti_ber": "Din din kan (Idh)", "desc_ber": "Taseddariy n tifekkit", "jenis_ber": "Taseddariy n Tifekkit"},

    "15. Harf Istidrak__39": {"arti_ber": "Lameɛna / Maca (Lakin)", "desc_ber": "Taseddariy n usseɣti", "jenis_ber": "Taseddariy n Usseɣti"},
    "15. Harf Istidrak__40": {"arti_ber": "Xas akken / Wanag (Bal)", "desc_ber": "Taseddariy n usbeddel d usseɣti", "jenis_ber": "Taseddariy n Usseɣti"},

    "16. Harf Ta'ajjub__41": {"arti_ber": "Acu n lwehma! (Ma)", "desc_ber": "Taseddariy n lwehba", "jenis_ber": "Taseddariy n Lwehba"},

    "17. Harf Mabany__39": {"arti_ber": "Ḥa-Mim", "desc_ber": "Isekkilen n tazzwara n tsuratin", "jenis_ber": "Isekkilen n Tazzwara"},
    "17. Harf Mabany__40": {"arti_ber": "Alif-Lam-Mim", "desc_ber": "Isekkilen n tazzwara n tsuratin", "jenis_ber": "Isekkilen n Tazzwara"},
    "17. Harf Mabany__41": {"arti_ber": "Alif-Lam-Ra", "desc_ber": "Isekkilen n tazzwara n tsuratin", "jenis_ber": "Isekkilen n Tazzwara"},
    "17. Harf Mabany__42": {"arti_ber": "Ṭa-Sin-Mim", "desc_ber": "Isekkilen n tazzwara n tsuratin", "jenis_ber": "Isekkilen n Tazzwara"},
    "17. Harf Mabany__43": {"arti_ber": "Alif-Lam-Mim-Ra", "desc_ber": "Isekkilen n tazzwara n tsuratin", "jenis_ber": "Isekkilen n Tazzwara"},
    "17. Harf Mabany__44": {"arti_ber": "Alif-Lam-Mim-Ṣad", "desc_ber": "Isekkilen n tazzwara n tsuratin", "jenis_ber": "Isekkilen n Tazzwara"},
    "17. Harf Mabany__45": {"arti_ber": "Ṣad", "desc_ber": "Isekkilen n tazzwara n tsuratin", "jenis_ber": "Isekkilen n Tazzwara"},
    "17. Harf Mabany__46": {"arti_ber": "Ṭa-Sin", "desc_ber": "Isekkilen n tazzwara n tsuratin", "jenis_ber": "Isekkilen n Tazzwara"},
    "17. Harf Mabany__47": {"arti_ber": "Ṭa-Ha", "desc_ber": "Isekkilen n tazzwara n tsuratin", "jenis_ber": "Isekkilen n Tazzwara"},
    "17. Harf Mabany__48": {"arti_ber": "Ɛayn-Sin-Qaf", "desc_ber": "Isekkilen n tazzwara n tsuratin", "jenis_ber": "Isekkilen n Tazzwara"},
    "17. Harf Mabany__49": {"arti_ber": "Qaf", "desc_ber": "Isekkilen n tazzwara n tsuratin", "jenis_ber": "Isekkilen n Tazzwara"},
    "17. Harf Mabany__50": {"arti_ber": "Kaf-Ha-Ya-Ɛayn-Ṣad", "desc_ber": "Isekkilen n tazzwara n tsuratin", "jenis_ber": "Isekkilen n Tazzwara"},
    "17. Harf Mabany__51": {"arti_ber": "Nun", "desc_ber": "Isekkilen n tazzwara n tsuratin", "jenis_ber": "Isekkilen n Tazzwara"},
    "17. Harf Mabany__52": {"arti_ber": "Ya-Sin", "desc_ber": "Isekkilen n tazzwara n tsuratin", "jenis_ber": "Isekkilen n Tazzwara"}
}

AMHARIC_HARF_GRAMMAR = {
    "1. Harf Nafyi__1": {"arti_am": "አል-...-ም / አይደለም (ማእ - አጠቃላይ አሉታ)", "desc_am": "ተግባር የማያፈርስ አጠቃላይ የአሉታ ቅንጣት", "jenis_am": "የአሉታ ቅንጣት"},
    "1. Harf Nafyi__2": {"arti_am": "አይደለም / አት-... (ላእ - የግስ አሉታ)", "desc_am": "የአሁንና የወደፊት ጊዜ የአሉታ ቅንጣት", "jenis_am": "የአሉታ ቅንጣት"},
    "1. Harf Nafyi__3": {"arti_am": "ሌላ አይደለም ... እንጂ (ኢን)", "desc_am": "ከኢላ ጋር የሚመጣ የአሉታ ቅንጣት", "jenis_am": "የአሉታ ቅንጣት"},
    "1. Harf Nafyi__4": {"arti_am": "የ... ጊዜ አይደለም (ላተ)", "desc_am": "የጊዜ አሉታ ቅንጣት", "jenis_am": "የአሉታ ቅንጣት"},

    "2. Harf Tahqiq Taswif__5": {"arti_am": "በእርግጥ / በእርግጠኝነት (ቀድ - ማረጋገጫ)", "desc_am": "ያለፈ ጊዜ ድርጊትን የሚያረጋግጥ ቅንጣት", "jenis_am": "የማረጋገጫ ቅንጣት"},
    "2. Harf Tahqiq Taswif__6": {"arti_am": "ወደፊት / በቅርቡ ይሆናል (ሰውፈ)", "desc_am": "የሩቅ ወደፊት ጊዜ አመልካች ቅንጣት", "jenis_am": "የወደፊት ጊዜ ቅንጣት"},
    "2. Harf Tahqiq Taswif__7": {"arti_am": "ይሆናል (ሰ - የቅርብ ወደፊት)", "desc_am": "የቅርብ ወደፊት ጊዜ አመልካች ቅንጣት", "jenis_am": "የወደፊት ጊዜ ቅንጣት"},

    "3. Harf Syarat__8": {"arti_am": "ቢሆን ኖሮ / ቢሆንማ (ለው)", "desc_am": "ተግባር የማይፈርስ የቅድመ-ሁኔታ ቅንጣት", "jenis_am": "ቅድመ-ሁኔታ ቅንጣት"},
    "3. Harf Syarat__9": {"arti_am": "ባይሆን ኖሮ / ባልነበረ (ለውላ)", "desc_am": "የመከልከል ቅድመ-ሁኔታ ቅንጣት", "jenis_am": "ቅድመ-ሁኔታ ቅንጣት"},
    "3. Harf Syarat__10": {"arti_am": "ባይሆን ኖሮ (ለውማ)", "desc_am": "የመከልከል ቅድመ-ሁኔታ ቅንጣት", "jenis_am": "ቅድመ-ሁኔታ ቅንጣት"},
    "3. Harf Syarat__11": {"arti_am": "በደረሰ ጊዜ / በ... ወቅት (ለምማ)", "desc_am": "ያለፈ ጊዜ ቅድመ-ሁኔታ ቅንጣት", "jenis_am": "የጊዜ ቅድመ-ሁኔታ"},
    "3. Harf Syarat__12": {"arti_am": "እነርሱማ / ነገር ግን (አምማ)", "desc_am": "የማብራሪያና የማረጋገጫ ቅንጣት", "jenis_am": "ቅድመ-ሁኔታ ቅንጣት"},

    "4. Harf Mashdariyah__13": {"arti_am": "ማድረግ / መሆን (አን)", "desc_am": "ግስን ወደ ድርጊት ስም የሚቀይር ቅንጣት", "jenis_am": "የድርጊት ስም አድራጊ"},
    "4. Harf Mashdariyah__14": {"arti_am": "እስከሆነ ድረስ / ያህል (ማ)", "desc_am": "የጊዜ ድርጊት ስም አድራጊ ቅንጣት", "jenis_am": "የድርጊት ስም አድራጊ"},
    "4. Harf Mashdariyah__15": {"arti_am": "ይሆን ዘንድ / እንዲህ ለማድረግ (ከይ)", "desc_am": "የምክንያት ድርጊት ስም አድራጊ ቅንጣት", "jenis_am": "የድርጊት ስም አድራጊ"},
    "4. Harf Mashdariyah__16": {"arti_am": "መሆንን / ቢሆን ብሎ (ለው)", "desc_am": "የምኞት ድርጊት ስም አድራጊ ቅንጣት", "jenis_am": "የድርጊት ስም አድራጊ"},

    "5. Harf Zaidah__17": {"arti_am": "ለማጠናከር (ኢን ዛኢዳህ)", "desc_am": "የአረፍተ-ነገር ማጠናከሪያ ትርፍ ቅንጣት", "jenis_am": "ማጠናከሪያ ቅንጣት"},
    "5. Harf Zaidah__18": {"arti_am": "ለማጠናከር (አን ዛኢዳህ)", "desc_am": "ማጠናከሪያ ትርፍ ቅንጣት", "jenis_am": "ማጠናከሪያ ቅንጣት"},
    "5. Harf Zaidah__19": {"arti_am": "ለማጠናከር (ማ ዛኢዳህ)", "desc_am": "ማጠናከሪያ ትርፍ ቅንጣት", "jenis_am": "ማጠናከሪያ ቅንጣት"},
    "5. Harf Zaidah__20": {"arti_am": "ለማጠናከር (ላ ዛኢዳህ)", "desc_am": "የአሉታ ማጠናከሪያ ትርፍ ቅንጣት", "jenis_am": "ማጠናከሪያ ቅንጣት"},

    "6. Harf Istifham__21": {"arti_am": "ወይስ? / ነውን? (ሀምዛህ)", "desc_am": "ዋና የመጠይቅ ፊደል", "jenis_am": "መጠይቅ ቅንጣት"},
    "6. Harf Istifham__22": {"arti_am": "ነው እንዴ? / ወይስ? (ሀል)", "desc_am": "የማረጋገጫ መጠይቅ ቅንጣት", "jenis_am": "መጠይቅ ቅንጣት"},

    "7. Harf Istitsna__23": {"arti_am": "ከ... በስተቀር / እንጂ (ኢላ)", "desc_am": "የማግለያና የወሰን ቅንጣት", "jenis_am": "የማግለያ ቅንጣት"},

    "8. Harf Rad'in Wazajrin__24": {"arti_am": "በጭራሽ! / ፈጽሞ አይሆንም! (ከላ)", "desc_am": "የመከልከያና የመገሰጫ ቅንጣት", "jenis_am": "የመከልከያ ቅንጣት"},

    "9. Harf Rad'in Tahdid__25": {"arti_am": "አይደረግምን? / ለምን አይሆንም (ሀላ)", "desc_am": "የማበረታቻና የወቀሳ ቅንጣት", "jenis_am": "የማበረታቻ ቅንጣት"},
    "9. Harf Rad'in Tahdid__26": {"arti_am": "አይደረግምን? (አላ)", "desc_am": "የማበረታቻ ቅንጣት", "jenis_am": "የማበረታቻ ቅንጣት"},

    "10. Harf Ijab__27": {"arti_am": "አዎ / እውነት ነው (ነዐም)", "desc_am": "የመልስና የእሺታ ቅንጣት", "jenis_am": "የእሺታ ቅንጣት"},
    "10. Harf Ijab__28": {"arti_am": "እንዴታ! በእርግጥም አዎ! (በላ)", "desc_am": "አሉታን የማስተባበያና የማረጋገጫ ቅንጣት", "jenis_am": "የእሺታ ቅንጣት"},
    "10. Harf Ijab__29": {"arti_am": "በጌታዬ እምላለሁ አዎ! (ኢ)", "desc_am": "የመሐላ እሺታ ቅንጣት", "jenis_am": "የእሺታ ቅንጣት"},
    "10. Harf Ijab__30": {"arti_am": "እውነት ነው / በትክክል (አጀል)", "desc_am": "የማረጋገጫ ቅንጣት", "jenis_am": "የእሺታ ቅንጣት"},

    "11. Harf Tafsir__31": {"arti_am": "ይኸውም / ማለቴ (አይ)", "desc_am": "የማብራሪያ ቅንጣት", "jenis_am": "የማብራሪያ ቅንጣት"},
    "11. Harf Tafsir__32": {"arti_am": "ማለትም / እንዲህ ሲል (አን)", "desc_am": "የማብራሪያ ቅንጣት", "jenis_am": "የማብራሪያ ቅንጣት"},

    "12. Harf Tanbih__33": {"arti_am": "እወቁ! / ንቁ! (አላ)", "desc_am": "የማስጠንቀቂያና የመክፈቻ ቅንጣት", "jenis_am": "የማስጠንቀቂያ ቅንጣት"},
    "12. Harf Tanbih__34": {"arti_am": "እወቁ! (አማ)", "desc_am": "የማስጠንቀቂያ ቅንጣት", "jenis_am": "የማስጠንቀቂያ ቅንጣት"},
    "12. Harf Tanbih__35": {"arti_am": "ይኸውላችሁ! (ሃ)", "desc_am": "የማስጠንቀቂያ ቅንጣት ከአመላካች ስሞች ጋር", "jenis_am": "የማስጠንቀቂያ ቅንጣት"},

    "13. Harf Ta'lil__36": {"arti_am": "እንዲሆን / በ... ምክንያት (ሊ-)", "desc_am": "የምክንያት አመልካች ቅንጣት", "jenis_am": "የምክንያት ቅንጣት"},

    "14. Harf Fuja'iyyah__37": {"arti_am": "ወዲያውኑ ድንገት! (ኢዛ)", "desc_am": "የድንገቴ ክስተት ቅንጣት", "jenis_am": "የድንገቴ ቅንጣት"},
    "14. Harf Fuja'iyyah__38": {"arti_am": "ድንገት (ኢዝ)", "desc_am": "የድንገቴ ክስተት ቅንጣት", "jenis_am": "የድንገቴ ቅንጣት"},

    "15. Harf Istidrak__39": {"arti_am": "ነገር ግን / ሆኖም (ላኪን)", "desc_am": "የማስተካከያ ቅንጣት", "jenis_am": "የማስተካከያ ቅንጣት"},
    "15. Harf Istidrak__40": {"arti_am": "ይልቁንም / አይደለም (በል)", "desc_am": "የሃሳብ መቀየሪያ ቅንጣት", "jenis_am": "የማስተካከያ ቅንጣት"},

    "16. Harf Ta'ajjub__41": {"arti_am": "ምንኛ ድንቅ ነው! (ማ)", "desc_am": "የአግራሞት መግለጫ ቅንጣት", "jenis_am": "የአግራሞት ቅንጣት"},

    "17. Harf Mabany__39": {"arti_am": "ሓ-ሚም", "desc_am": "የሱራ መክፈቻ ምህፃረ ቃላት", "jenis_am": "የሱራ መክፈቻ ቃላት"},
    "17. Harf Mabany__40": {"arti_am": "አሊፍ-ላም-ሚም", "desc_am": "የሱራ መክፈቻ ምህፃረ ቃላት", "jenis_am": "የሱራ መክፈቻ ቃላት"},
    "17. Harf Mabany__41": {"arti_am": "አሊፍ-ላም-ራ", "desc_am": "የሱራ መክፈቻ ምህፃረ ቃላት", "jenis_am": "የሱራ መክፈቻ ቃላት"},
    "17. Harf Mabany__42": {"arti_am": "ጣ-ሲን-ሚም", "desc_am": "የሱራ መክፈቻ ምህፃረ ቃላት", "jenis_am": "የሱራ መክፈቻ ቃላት"},
    "17. Harf Mabany__43": {"arti_am": "አሊፍ-ላም-ሚም-ራ", "desc_am": "የሱራ መክፈቻ ምህፃረ ቃላት", "jenis_am": "የሱራ መክፈቻ ቃላት"},
    "17. Harf Mabany__44": {"arti_am": "አሊፍ-ላም-ሚም-ሷድ", "desc_am": "የሱራ መክፈቻ ምህፃረ ቃላት", "jenis_am": "የሱራ መክፈቻ ቃላት"},
    "17. Harf Mabany__45": {"arti_am": "ሷድ", "desc_am": "የሱራ መክፈቻ ምህፃረ ቃላት", "jenis_am": "የሱራ መክፈቻ ቃላት"},
    "17. Harf Mabany__46": {"arti_am": "ጣ-ሲን", "desc_am": "የሱራ መክፈቻ ምህፃረ ቃላት", "jenis_am": "የሱራ መክፈቻ ቃላት"},
    "17. Harf Mabany__47": {"arti_am": "ጣ-ሀ", "desc_am": "የሱራ መክፈቻ ምህፃረ ቃላት", "jenis_am": "የሱራ መክፈቻ ቃላት"},
    "17. Harf Mabany__48": {"arti_am": "ዐይን-ሲን-ቃፍ", "desc_am": "የሱራ መክፈቻ ምህፃረ ቃላት", "jenis_am": "የሱራ መክፈቻ ቃላት"},
    "17. Harf Mabany__49": {"arti_am": "ቃፍ", "desc_am": "የሱራ መክፈቻ ምህፃረ ቃላት", "jenis_am": "የሱራ መክፈቻ ቃላት"},
    "17. Harf Mabany__50": {"arti_am": "ካፍ-ሀ-ያ-ዐይን-ሷድ", "desc_am": "የሱራ መክፈቻ ምህፃረ ቃላት", "jenis_am": "የሱራ መክፈቻ ቃላት"},
    "17. Harf Mabany__51": {"arti_am": "ኑን", "desc_am": "የሱራ መክፈቻ ምህፃረ ቃላት", "jenis_am": "የሱራ መክፈቻ ቃላት"},
    "17. Harf Mabany__52": {"arti_am": "ያ-ሲን", "desc_am": "የሱራ መክፈቻ ምህፃረ ቃላት", "jenis_am": "የሱራ መክፈቻ ቃላት"}
}


def enrich_dhamir_data():
    print("Enriching dhamir_data.json and dhamir_data.js with Amazigh & Amharic...")
    with open(os.path.join(BASE_DIR, 'ber_translations.json'), 'r', encoding='utf-8') as f:
        ber_trans = json.load(f)
    with open(os.path.join(BASE_DIR, 'am_translations.json'), 'r', encoding='utf-8') as f:
        am_trans = json.load(f)
    with open(os.path.join(BASE_DIR, 'dhamir_data.json'), 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        b = item.get('Bentuk Kata', '')
        nk = str(item.get('No kata', ''))
        g_key = f"{b}__{nk}"
        s_num = str(item.get('SURAT', ''))
        v_key = f"{item.get('SURAT')}:{item.get('AYAT')}"

        # BER
        item['BentukKataBER'] = BENTUK_KATA_BER.get(b, b)
        item['SuratArtiBER'] = AMAZIGH_SURAHS.get(s_num, item.get('SuratArtiEN', ''))
        g_ber = AMAZIGH_GRAMMAR.get(g_key, {})
        item['ArtiKataBER'] = g_ber.get('arti_ber', item.get('ArtiKataEN', ''))
        item['TeksArtiBER'] = ber_trans.get(v_key, item.get('TeksArtiEN', ''))

        # AM
        item['BentukKataAM'] = BENTUK_KATA_AM.get(b, b)
        item['SuratArtiAM'] = AMHARIC_SURAHS.get(s_num, item.get('SuratArtiEN', ''))
        g_am = AMHARIC_GRAMMAR.get(g_key, {})
        item['ArtiKataAM'] = g_am.get('arti_am', item.get('ArtiKataEN', ''))
        item['TeksArtiAM'] = am_trans.get(v_key, item.get('TeksArtiEN', ''))

        # Grammar dict
        if 'Grammar' not in item or not isinstance(item['Grammar'], dict):
            item['Grammar'] = {}
        if g_ber.get('arti_ber'): item['Grammar']['arti_ber'] = g_ber['arti_ber']
        if g_ber.get('desc_ber'): item['Grammar']['desc_ber'] = g_ber['desc_ber']
        if g_ber.get('jenis_ber'): item['Grammar']['jenis_ber'] = g_ber['jenis_ber']

        if g_am.get('arti_am'): item['Grammar']['arti_am'] = g_am['arti_am']
        if g_am.get('desc_am'): item['Grammar']['desc_am'] = g_am['desc_am']
        if g_am.get('jenis_am'): item['Grammar']['jenis_am'] = g_am['jenis_am']

    with open(os.path.join(BASE_DIR, 'dhamir_data.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    js_content = f"/**\n * Dataset Dhamir & Isim Jamid Mabny Al-Qur'an 25 Bahasa\n */\nconst DHAMIR_DATA = {json.dumps(data, ensure_ascii=False, indent=2)};\n"
    with open(os.path.join(BASE_DIR, 'dhamir_data.js'), 'w', encoding='utf-8') as f:
        f.write(js_content)
    print(f"  [OK] Dhamir data enriched ({len(data)} rows).")


def enrich_harf_data():
    print("Enriching harf_data.json and harf_data.js with Amazigh & Amharic...")
    with open(os.path.join(BASE_DIR, 'ber_translations.json'), 'r', encoding='utf-8') as f:
        ber_trans = json.load(f)
    with open(os.path.join(BASE_DIR, 'am_translations.json'), 'r', encoding='utf-8') as f:
        am_trans = json.load(f)
    with open(os.path.join(BASE_DIR, 'harf_data.json'), 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        b = item.get('Bentuk Kata', '')
        nk = str(item.get('No kata', ''))
        g_key = f"{b}__{nk}"
        s_num = str(item.get('SURAT', ''))
        v_key = f"{item.get('SURAT')}:{item.get('AYAT')}"

        # BER
        item['BentukKataBER'] = BENTUK_HARF_BER.get(b, b)
        item['SuratArtiBER'] = AMAZIGH_SURAHS.get(s_num, item.get('SuratArtiEN', ''))
        g_ber = AMAZIGH_HARF_GRAMMAR.get(g_key, {})
        item['ArtiKataBER'] = g_ber.get('arti_ber', item.get('ArtiKataEN', ''))
        item['TeksArtiBER'] = ber_trans.get(v_key, item.get('TeksArtiEN', ''))

        # AM
        item['BentukKataAM'] = BENTUK_HARF_AM.get(b, b)
        item['SuratArtiAM'] = AMHARIC_SURAHS.get(s_num, item.get('SuratArtiEN', ''))
        g_am = AMHARIC_HARF_GRAMMAR.get(g_key, {})
        item['ArtiKataAM'] = g_am.get('arti_am', item.get('ArtiKataEN', ''))
        item['TeksArtiAM'] = am_trans.get(v_key, item.get('TeksArtiEN', ''))

        # Grammar dict
        if 'Grammar' not in item or not isinstance(item['Grammar'], dict):
            item['Grammar'] = {}
        if g_ber.get('arti_ber'): item['Grammar']['arti_ber'] = g_ber['arti_ber']
        if g_ber.get('desc_ber'): item['Grammar']['desc_ber'] = g_ber['desc_ber']
        if g_ber.get('jenis_ber'): item['Grammar']['jenis_ber'] = g_ber['jenis_ber']

        if g_am.get('arti_am'): item['Grammar']['arti_am'] = g_am['arti_am']
        if g_am.get('desc_am'): item['Grammar']['desc_am'] = g_am['desc_am']
        if g_am.get('jenis_am'): item['Grammar']['jenis_am'] = g_am['jenis_am']

    with open(os.path.join(BASE_DIR, 'harf_data.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    js_content = f"/**\n * Dataset Harf Ghair 'Amil Al-Qur'an 25 Bahasa\n */\nconst HARF_DATA = {json.dumps(data, ensure_ascii=False, indent=2)};\n"
    with open(os.path.join(BASE_DIR, 'harf_data.js'), 'w', encoding='utf-8') as f:
        f.write(js_content)
    print(f"  [OK] Harf data enriched ({len(data)} rows).")


if __name__ == '__main__':
    enrich_dhamir_data()
    enrich_harf_data()
