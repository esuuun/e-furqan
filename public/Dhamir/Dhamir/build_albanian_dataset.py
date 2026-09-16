#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script containing complete Albanian (sq) dataset metadata:
- 114 Surah Names (ALBANIAN_SURAHS)
- 7 Bentuk Kata Categories (BENTUK_KATA_SQ)
- 76 Jamid Mabny Words Grammar (ALBANIAN_GRAMMAR)
- 17 Bentuk Harf Categories (BENTUK_HARF_SQ)
- 52 Harf Words Grammar (ALBANIAN_HARF_GRAMMAR)
"""

ALBANIAN_SURAHS = {
    "1": "Hapja (Al-Fatihah)",
    "2": "Lopa (Al-Baqarah)",
    "3": "Familja e Imranit (Ali 'Imran)",
    "4": "Gratë (An-Nisa')",
    "5": "Sofra (Al-Ma'idah)",
    "6": "Bagëtia (Al-An'am)",
    "7": "Lartësitë (Al-A'raf)",
    "8": "Plaçka e Luftës (Al-Anfal)",
    "9": "Pendimi (At-Tawbah)",
    "10": "Junusi (Yunus)",
    "11": "Hudi (Hud)",
    "12": "Jusufi (Yusuf)",
    "13": "Rrufeja (Ar-Ra'd)",
    "14": "Ibrahimi (Ibrahim)",
    "15": "Hixhri (Al-Hijr)",
    "16": "Bletët (An-Nahl)",
    "17": "Udhëtimi Natën (Al-Isra')",
    "18": "Shpella (Al-Kahf)",
    "19": "Merjemja (Maryam)",
    "20": "Ta-Ha (Ta-Ha)",
    "21": "Pejgamberët (Al-Anbiya')",
    "22": "Haxhi (Al-Hajj)",
    "23": "Besimtarët (Al-Mu'minun)",
    "24": "Drita (An-Nur)",
    "25": "Dalluesi (Al-Furqan)",
    "26": "Poetët (Asy-Syu'ara')",
    "27": "Milingonat (An-Naml)",
    "28": "Tregimi (Al-Qasas)",
    "29": "Merimanga (Al-'Ankabut)",
    "30": "Bizantinët (Ar-Rum)",
    "31": "Lukmani (Luqman)",
    "32": "Sexhdeja (As-Sajdah)",
    "33": "Aleatët (Al-Ahzab)",
    "34": "Sebeja (Saba')",
    "35": "Krijuesi (Fatir)",
    "36": "Ja-Sin (Ya-Sin)",
    "37": "Të Rreshtuarit (As-Saffat)",
    "38": "Sad (Sad)",
    "39": "Grupet (Az-Zumar)",
    "40": "Falësi (Ghafir / Al-Mu'min)",
    "41": "Të Shpjeguara Qartë (Fussilat)",
    "42": "Këshillimi (Asy-Syura)",
    "43": "Zbukurimi me Flori (Az-Zukhruf)",
    "44": "Tymi (Ad-Dukhan)",
    "45": "Gjunjëzimi (Al-Jathiyah)",
    "46": "Kodrat e Rërës (Al-Ahqaf)",
    "47": "Muhammedi (Muhammad)",
    "48": "Fitorja (Al-Fath)",
    "49": "Dhomat (Al-Hujurat)",
    "50": "Kaf (Qaf)",
    "51": "Erërat Shpërndarëse (Adz-Dzariyat)",
    "52": "Mali Tur (At-Tur)",
    "53": "Ylli (An-Najm)",
    "54": "Hëna (Al-Qamar)",
    "55": "I Gjithëmëshirshmi (Ar-Rahman)",
    "56": "Ngjarja e Madhe (Al-Waqi'ah)",
    "57": "Hekuri (Al-Hadid)",
    "58": "Ajo që Debaton (Al-Mujadilah)",
    "59": "Dëbimi (Al-Hasyr)",
    "60": "E Sprovuara (Al-Mumtahanah)",
    "61": "Rreshti (As-Saff)",
    "62": "E Xhumaja (Al-Jumu'ah)",
    "63": "Hipokritët (Al-Munafiqun)",
    "64": "Mashtrimi i Ndërsjellë (At-Taghabun)",
    "65": "Shkurorëzimi (At-Talaq)",
    "66": "Ndalimi (At-Tahrim)",
    "67": "Sundimi (Al-Mulk)",
    "68": "Pena (Al-Qalam)",
    "69": "E Vërteta e Madhe (Al-Haqqah)",
    "70": "Shkallët e Larta (Al-Ma'arij)",
    "71": "Nuhi (Nuh)",
    "72": "Xhindët (Al-Jinn)",
    "73": "I Mbështjelli (Al-Muzzammil)",
    "74": "I Mbuluari (Al-Muddaththir)",
    "75": "Ringjallja (Al-Qiyamah)",
    "76": "Njeriu (Al-Insan)",
    "77": "Të Dërguarat (Al-Mursalat)",
    "78": "Lajmi i Madh (An-Naba')",
    "79": "Ata që Shkulin (An-Nazi'at)",
    "80": "Ai u Vrrenjt ('Abasa)",
    "81": "Errësimi (At-Takwir)",
    "82": "Çarja (Al-Infitar)",
    "83": "Mashtruesit në Peshë (Al-Mutaffifin)",
    "84": "Plasaritja (Al-Insyiqaq)",
    "85": "Yjësitë (Al-Buruj)",
    "86": "Ylli i Mbrëmjes (At-Tariq)",
    "87": "Më i Larti (Al-A'la)",
    "88": "E Përgjithshmja (Al-Ghasyiyah)",
    "89": "Agimi (Al-Fajr)",
    "90": "Qyteti (Al-Balad)",
    "91": "Dielli (Asy-Syams)",
    "92": "Nata (Al-Lail)",
    "93": "Paraditja (Ad-Duha)",
    "94": "Hapja e Kraharorit (Asy-Syarh / Al-Insyirah)",
    "95": "Fiku (At-Tin)",
    "96": "Gjaku i Mpiksur (Al-'Alaq)",
    "97": "Nata e Kadrit (Al-Qadr)",
    "98": "Dëshmia e Qartë (Al-Bayyinah)",
    "99": "Dridhja e Tokës (Az-Zalzalah)",
    "100": "Vraponjësit (Al-'Adiyat)",
    "101": "Goditja e Fortë (Al-Qari'ah)",
    "102": "Garimi në Shtim (At-Takathur)",
    "103": "Koha (Al-'Asr)",
    "104": "Përgojuesi (Al-Humazah)",
    "105": "Elefanti (Al-Fil)",
    "106": "Kurejshët (Quraisy)",
    "107": "Ndihma e Vogël (Al-Ma'un)",
    "108": "Mirësia e Madhe (Al-Kautsar)",
    "109": "Jobesimtarët (Al-Kafirun)",
    "110": "Ndihma (An-Nasr)",
    "111": "Fibra e Palmës (Al-Masad / Al-Lahab)",
    "112": "Sinqeriteti (Al-Ikhlas)",
    "113": "Agimi i Hershëm (Al-Falaq)",
    "114": "Njerëzit (An-Nas)"
}

BENTUK_KATA_SQ = {
    "1. Dhamir": "1. Përemrat (Dhamir - Përemrat vetorë dhe pronorë)",
    "2. Isim Mawshul": "2. Përemrat lidhorë (Mawshul - Përemrat relativë)",
    "3. Isim Istifham": "3. Përemrat pyetës (Istifham - Fjalët pyetëse)",
    "4. Isim Syarath": "4. Emrat kushtorë (Syarath - Fjalët kushtore)",
    "5. Isim Isyarah": "5. Përemrat dëftorë (Isyarah - Përemrat demonstrativë)",
    "6. Isim Fi'il": "6. Emrat foljorë (Isim Fi'il - Emrat me kuptim foljeje)",
    "7. Fi'il Jamid": "7. Foljet e ngurosura (Fi'il Jamid - Foljet e pandryshueshme)"
}

ALBANIAN_GRAMMAR = {
    "1. Dhamir__1a": {
        "arti_sq": "Ai (mashkullore njëjës)",
        "desc_sq": "Ai (Veta e 3-të mashkullore njëjës, përemër vetor i veçuar në emërore)",
        "jenis_sq": "Përemër vetor i veçuar në emërore"
    },
    "1. Dhamir__1b": {
        "arti_sq": "E tij / atë / i",
        "desc_sq": "E tij / atë (Veta e 3-të mashkullore njëjës, përemër i ngjitur)",
        "jenis_sq": "Përemër i ngjitur"
    },
    "1. Dhamir__1c": {
        "arti_sq": "Vetëm atë",
        "desc_sq": "Vetëm atë (Veta e 3-të mashkullore njëjës, përemër vetor i veçuar në kallëzore)",
        "jenis_sq": "Përemër vetor i veçuar në kallëzore"
    },
    "1. Dhamir__2a": {
        "arti_sq": "Ata të dy / ato të dyja",
        "desc_sq": "Ata të dy (Veta e 3-të numri dysor, përemër vetor i veçuar në emërore)",
        "jenis_sq": "Përemër vetor i veçuar (dysor)"
    },
    "1. Dhamir__2b": {
        "arti_sq": "Të dyve / atyre të dyve",
        "desc_sq": "Atyre të dyve (Veta e 3-të numri dysor, përemër i ngjitur)",
        "jenis_sq": "Përemër i ngjitur (dysor)"
    },
    "1. Dhamir__3a": {
        "arti_sq": "Ata (mashkullore shumës)",
        "desc_sq": "Ata (Veta e 3-të mashkullore shumës, përemër vetor i veçuar në emërore)",
        "jenis_sq": "Përemër vetor i veçuar (shumës)"
    },
    "1. Dhamir__3b": {
        "arti_sq": "E tyre / ata / u",
        "desc_sq": "E tyre / atyre (Veta e 3-të mashkullore shumës, përemër i ngjitur)",
        "jenis_sq": "Përemër i ngjitur (shumës)"
    },
    "1. Dhamir__3c": {
        "arti_sq": "Vetëm ata",
        "desc_sq": "Vetëm ata (Veta e 3-të mashkullore shumës, përemër vetor i veçuar në kallëzore)",
        "jenis_sq": "Përemër vetor i veçuar në kallëzore (shumës)"
    },
    "1. Dhamir__4a": {
        "arti_sq": "Ajo (femërore njëjës)",
        "desc_sq": "Ajo (Veta e 3-të femërore njëjës, përemër vetor i veçuar në emërore)",
        "jenis_sq": "Përemër vetor i veçuar (femërore)"
    },
    "1. Dhamir__4b": {
        "arti_sq": "E saj / atë / i",
        "desc_sq": "E saj / atë (Veta e 3-të femërore njëjës, përemër i ngjitur)",
        "jenis_sq": "Përemër i ngjitur (femërore)"
    },
    "1. Dhamir__5a": {
        "arti_sq": "Ato (femërore shumës)",
        "desc_sq": "Ato (Veta e 3-të femërore shumës, përemër vetor i veçuar në emërore)",
        "jenis_sq": "Përemër vetor i veçuar (femërore shumës)"
    },
    "1. Dhamir__5b": {
        "arti_sq": "E tyre / ato / u (femërore)",
        "desc_sq": "E tyre / atyre (Veta e 3-të femërore shumës, përemër i ngjitur)",
        "jenis_sq": "Përemër i ngjitur (femërore shumës)"
    },
    "1. Dhamir__6a": {
        "arti_sq": "Ti (mashkullore njëjës)",
        "desc_sq": "Ti (Veta e 2-të mashkullore njëjës, përemër vetor i veçuar në emërore)",
        "jenis_sq": "Përemër vetor i veçuar"
    },
    "1. Dhamir__6b": {
        "arti_sq": "Yt / ty / të",
        "desc_sq": "Yt / ty (Veta e 2-të mashkullore njëjës, përemër i ngjitur)",
        "jenis_sq": "Përemër i ngjitur"
    },
    "1. Dhamir__6c": {
        "arti_sq": "Vetëm ty",
        "desc_sq": "Vetëm ty (Veta e 2-të mashkullore njëjës, përemër vetor i veçuar në kallëzore)",
        "jenis_sq": "Përemër vetor i veçuar në kallëzore"
    },
    "1. Dhamir__7a": {
        "arti_sq": "Ju të dy / ju të dyja",
        "desc_sq": "Ju të dy (Veta e 2-të numri dysor, përemër vetor i veçuar në emërore)",
        "jenis_sq": "Përemër vetor i veçuar (dysor)"
    },
    "1. Dhamir__7b": {
        "arti_sq": "Ju të dyve (ngjitur)",
        "desc_sq": "Ju të dyve (Veta e 2-të numri dysor, përemër i ngjitur)",
        "jenis_sq": "Përemër i ngjitur (dysor)"
    },
    "1. Dhamir__8a": {
        "arti_sq": "Ju (mashkullore shumës)",
        "desc_sq": "Ju (Veta e 2-të mashkullore shumës, përemër vetor i veçuar në emërore)",
        "jenis_sq": "Përemër vetor i veçuar (shumës)"
    },
    "1. Dhamir__8b": {
        "arti_sq": "Tuaj / juve / ju",
        "desc_sq": "Tuaj / juve (Veta e 2-të mashkullore shumës, përemër i ngjitur)",
        "jenis_sq": "Përemër i ngjitur (shumës)"
    },
    "1. Dhamir__8c": {
        "arti_sq": "Vetëm juve / vetëm ju",
        "desc_sq": "Vetëm ju (Veta e 2-të mashkullore shumës, përemër vetor i veçuar në kallëzore)",
        "jenis_sq": "Përemër vetor i veçuar në kallëzore (shumës)"
    },
    "1. Dhamir__9a": {
        "arti_sq": "Ti (femërore njëjës)",
        "desc_sq": "Ti (Veta e 2-të femërore njëjës, përemër vetor i veçuar në emërore)",
        "jenis_sq": "Përemër vetor i veçuar (femërore)"
    },
    "1. Dhamir__9b": {
        "arti_sq": "Yt / ty (femërore njëjës)",
        "desc_sq": "Yt / ty (Veta e 2-të femërore njëjës, përemër i ngjitur)",
        "jenis_sq": "Përemër i ngjitur (femërore)"
    },
    "1. Dhamir__10a": {
        "arti_sq": "Ju (femërore shumës)",
        "desc_sq": "Ju (Veta e 2-të femërore shumës, përemër vetor i veçuar në emërore)",
        "jenis_sq": "Përemër vetor i veçuar (femërore shumës)"
    },
    "1. Dhamir__10b": {
        "arti_sq": "Tuaj / juve (femërore)",
        "desc_sq": "Tuaj / juve (Veta e 2-të femërore shumës, përemër i ngjitur)",
        "jenis_sq": "Përemër i ngjitur (femërore shumës)"
    },
    "1. Dhamir__11a": {
        "arti_sq": "Unë (veta e parë njëjës)",
        "desc_sq": "Unë (Veta e 1-rë njëjës, përemër vetor i veçuar në emërore)",
        "jenis_sq": "Përemër vetor i veçuar"
    },
    "1. Dhamir__11b": {
        "arti_sq": "Im / mua / më",
        "desc_sq": "Im / mua (Veta e 1-rë njëjës, përemër i ngjitur)",
        "jenis_sq": "Përemër i ngjitur"
    },
    "1. Dhamir__11c": {
        "arti_sq": "Vetëm mua",
        "desc_sq": "Vetëm mua (Veta e 1-rë njëjës, përemër vetor i veçuar në kallëzore)",
        "jenis_sq": "Përemër vetor i veçuar në kallëzore"
    },
    "1. Dhamir__12a": {
        "arti_sq": "Ne (veta e parë shumës)",
        "desc_sq": "Ne (Veta e 1-rë shumës, përemër vetor i veçuar në emërore)",
        "jenis_sq": "Përemër vetor i veçuar (shumës)"
    },
    "1. Dhamir__12b": {
        "arti_sq": "Jonë / neve / na",
        "desc_sq": "Jonë / neve (Veta e 1-rë shumës, përemër i ngjitur)",
        "jenis_sq": "Përemër i ngjitur (shumës)"
    },
    "1. Dhamir__12c": {
        "arti_sq": "Vetëm neve / vetëm ne",
        "desc_sq": "Vetëm ne (Veta e 1-rë shumës, përemër vetor i veçuar në kallëzore)",
        "jenis_sq": "Përemër vetor i veçuar në kallëzore (shumës)"
    },
    "2. Mawshul__1": {
        "arti_sq": "Ajo që / çfarë",
        "desc_sq": "Përemër lidhor i përgjithshëm për jofrymorë dhe sende (Maa)",
        "jenis_sq": "Përemër lidhor (për jofrymorë)"
    },
    "2. Mawshul__2": {
        "arti_sq": "Ata që (mashkullore shumës)",
        "desc_sq": "Ata që (Përemër lidhor për mashkullore shumës)",
        "jenis_sq": "Përemër lidhor (shumës mashkullore)"
    },
    "2. Mawshul__3": {
        "arti_sq": "Kush / ai që",
        "desc_sq": "Përemër lidhor i përgjithshëm për frymorë me mendje (Man)",
        "jenis_sq": "Përemër lidhor (për frymorë)"
    },
    "2. Mawshul__4": {
        "arti_sq": "Ai që (mashkullore njëjës)",
        "desc_sq": "Ai që (Përemër lidhor mashkullore njëjës)",
        "jenis_sq": "Përemër lidhor (mashkullore njëjës)"
    },
    "2. Mawshul__5": {
        "arti_sq": "Cili do / kushdo prej tyre",
        "desc_sq": "Cili do / cilido prej tyre (Përemër lidhor i lakueshëm)",
        "jenis_sq": "Përemër lidhor"
    },
    "2. Mawshul__6": {
        "arti_sq": "Ajo që (femërore njëjës)",
        "desc_sq": "Ajo që (Përemër lidhor femërore njëjës)",
        "jenis_sq": "Përemër lidhor (femërore njëjës)"
    },
    "2. Mawshul__7": {
        "arti_sq": "Ato gra që (femërore shumës)",
        "desc_sq": "Ato që (Përemër lidhor femërore shumës)",
        "jenis_sq": "Përemër lidhor (femërore shumës)"
    },
    "2. Mawshul__8": {
        "arti_sq": "Ato gra që (variant)",
        "desc_sq": "Ato që (Variant i përemrit lidhor femërore shumës)",
        "jenis_sq": "Përemër lidhor (femërore shumës)"
    },
    "2. Mawshul__9": {
        "arti_sq": "Ata të dy që (dysor)",
        "desc_sq": "Ata të dy që (Përemër lidhor mashkullore dysor)",
        "jenis_sq": "Përemër lidhor (dysor)"
    },
    "2. Mawshul__10": {
        "arti_sq": "Cila do (femërore)",
        "desc_sq": "Cila do (Përemër lidhor femërore)",
        "jenis_sq": "Përemër lidhor (femërore)"
    },
    "3. Istifham__1": {
        "arti_sq": "Çfarë? / Si?",
        "desc_sq": "Çfarë? (Përemër pyetës për sende dhe çështje)",
        "jenis_sq": "Përemër pyetës"
    },
    "3. Istifham__2": {
        "arti_sq": "Si?",
        "desc_sq": "Si? (Fjalë pyetëse për gjendjen ose mënyrën)",
        "jenis_sq": "Fjalë pyetëse e gjendjes"
    },
    "3. Istifham__3": {
        "arti_sq": "Kush?",
        "desc_sq": "Kush? (Përemër pyetës për persona dhe qenie me arsye)",
        "jenis_sq": "Përemër pyetës"
    },
    "3. Istifham__4": {
        "arti_sq": "Cili? / Cila?",
        "desc_sq": "Cili? (Përemër pyetës përzgjedhjeje)",
        "jenis_sq": "Përemër pyetës përzgjedhjeje"
    },
    "3. Istifham__5": {
        "arti_sq": "Si? / Nga ku?",
        "desc_sq": "Nga ku? / Si? (Fjalë pyetëse për origjinën ose mundësinë)",
        "jenis_sq": "Fjalë pyetëse"
    },
    "3. Istifham__6": {
        "arti_sq": "Çfarë është ajo që?",
        "desc_sq": "Çfarë është ajo? (Përemër pyetës i përforcuar me Dhaa)",
        "jenis_sq": "Përemër pyetës i përbërë"
    },
    "3. Istifham__7": {
        "arti_sq": "Sa? / Sa kohë?",
        "desc_sq": "Sa? / Sa kohë? (Fjalë pyetëse për sasinë ose kohëzgjatjen)",
        "jenis_sq": "Fjalë pyetëse sasie"
    },
    "3. Istifham__8": {
        "arti_sq": "Përse? / Pse?",
        "desc_sq": "Pse? (Pyetje për shkakun ose qëllimin, Li + Maa)",
        "jenis_sq": "Fjalë pyetëse shkaku"
    },
    "3. Istifham__9": {
        "arti_sq": "Ku? / Nga?",
        "desc_sq": "Ku? (Fjalë pyetëse vendi)",
        "jenis_sq": "Fjalë pyetëse vendi"
    },
    "3. Istifham__10": {
        "arti_sq": "Kur?",
        "desc_sq": "Kur? (Fjalë pyetëse kohe)",
        "jenis_sq": "Fjalë pyetëse kohe"
    },
    "4. Syarath__1": {
        "arti_sq": "Kushdo / ai që",
        "desc_sq": "Kushdo (Emër kushtor për qenie me arsye)",
        "jenis_sq": "Emër kushtor (për persona)"
    },
    "4. Syarath__2": {
        "arti_sq": "Çfarëdo / çdo gjë që",
        "desc_sq": "Çfarëdo (Emër kushtor për sende dhe çështje)",
        "jenis_sq": "Emër kushtor (për sende)"
    },
    "4. Syarath__3": {
        "arti_sq": "Sa herë që / kurdoherë",
        "desc_sq": "Sa herë që (Ndajfolje kushtore kohe)",
        "jenis_sq": "Ndajfolje kushtore kohe"
    },
    "4. Syarath__4": {
        "arti_sq": "Cilido / cila do",
        "desc_sq": "Cilido (Emër kushtor përzgjedhjeje)",
        "jenis_sq": "Emër kushtor përzgjedhjeje"
    },
    "4. Syarath__5": {
        "arti_sq": "Cilido afat (theksuar)",
        "desc_sq": "Cilido nga të dy afatet (Emër kushtor i theksuar me Maa)",
        "jenis_sq": "Emër kushtor i përforcuar"
    },
    "5. Isyarah__1": {
        "arti_sq": "Ky / ai / kjo",
        "desc_sq": "Ky / ai (Përemër dëftor mashkullore njëjës për afër/larg)",
        "jenis_sq": "Përemër dëftor (mashkullore)"
    },
    "5. Isyarah__2": {
        "arti_sq": "Këta / ata (shumës)",
        "desc_sq": "Këta / ata (Përemër dëftor shumës për afër/larg)",
        "jenis_sq": "Përemër dëftor (shumës)"
    },
    "5. Isyarah__3": {
        "arti_sq": "Kjo / ajo (femërore)",
        "desc_sq": "Kjo / ajo (Përemër dëftor femërore njëjës)",
        "jenis_sq": "Përemër dëftor (femërore)"
    },
    "5. Isyarah__4": {
        "arti_sq": "Ajo / ato (larg)",
        "desc_sq": "Ajo (Përemër dëftor për largësi)",
        "jenis_sq": "Përemër dëftor për largësi"
    },
    "5. Isyarah__5": {
        "arti_sq": "Këtu (afërsi)",
        "desc_sq": "Këtu (Ndajfolje dëftore vendi për afërsi)",
        "jenis_sq": "Ndajfolje dëftore vendi"
    },
    "5. Isyarah__6": {
        "arti_sq": "Atje / aty (largësi)",
        "desc_sq": "Atje (Ndajfolje dëftore vendi për largësi)",
        "jenis_sq": "Ndajfolje dëftore vendi për largësi"
    },
    "5. Isyarah__7": {
        "arti_sq": "Këta të dy (dysor)",
        "desc_sq": "Këta të dy (Përemër dëftor mashkullore dysor)",
        "jenis_sq": "Përemër dëftor (dysor)"
    },
    "5. Isyarah__8": {
        "arti_sq": "Këto të dyja (femërore dysor)",
        "desc_sq": "Këto të dyja (Përemër dëftor femërore dysor)",
        "jenis_sq": "Përemër dëftor (femërore dysor)"
    },
    "6. Isim Fi'il__1": {
        "arti_sq": "I Pastër e i Lartësuar qoftë! (Lavdërim)",
        "desc_sq": "I Pastër dhe i Lartë është Allahu (Emër foljor madhërimi)",
        "jenis_sq": "Emër foljor madhërimi"
    },
    "6. Isim Fi'il__2": {
        "arti_sq": "Sillni! / Paraqisni!",
        "desc_sq": "Sillni provën tuaj (Emër foljor në mënyrën urdhërore)",
        "jenis_sq": "Emër foljor urdhëror"
    },
    "6. Isim Fi'il__3": {
        "arti_sq": "Uh! / Of! (shprehje neverie)",
        "desc_sq": "Of / uh (Emër foljor i neverisë dhe mospëlqimit)",
        "jenis_sq": "Emër foljor mospëlqimi"
    },
    "6. Isim Fi'il__4": {
        "arti_sq": "Sa larg është! / E pamundur!",
        "desc_sq": "Sa larg është / e pamundur (Emër foljor i së shkuarës)",
        "jenis_sq": "Emër foljor i së shkuarës"
    },
    "6. Isim Fi'il__5": {
        "arti_sq": "Kini kujdes! / Ruani veten!",
        "desc_sq": "Ruani veten / kini kujdes (Emër foljor paralajmërues)",
        "jenis_sq": "Emër foljor paralajmërimi"
    },
    "6. Isim Fi'il__6": {
        "arti_sq": "Ejani! / Urdhëroni!",
        "desc_sq": "Ejani këtu (Emër foljor thirrës)",
        "jenis_sq": "Emër foljor thirrës"
    },
    "6. Isim Fi'il__7": {
        "arti_sq": "Ja, merrni! / Lexoni!",
        "desc_sq": "Ja, merrni e lexoni librin tim (Emër foljor ofrues)",
        "jenis_sq": "Emër foljor dhënieje"
    },
    "6. Isim Fi'il__8": {
        "arti_sq": "Çudi është! / Sa çuditem!",
        "desc_sq": "A nuk e sheh / sa çuditem (Emër foljor habie)",
        "jenis_sq": "Emër foljor habie"
    },
    "7. Fi'il Jamid__1": {
        "arti_sq": "Nuk është / s'ekziston",
        "desc_sq": "Nuk është (Folje e ngurosur e mohimit të gjendjes)",
        "jenis_sq": "Folje e pandryshueshme mohimi"
    },
    "7. Fi'il Jamid__2": {
        "arti_sq": "Sa i mirë që është! / Shkëlqyeshëm!",
        "desc_sq": "Sa i shkëlqyer është (Folje e ngurosur lavdërimi)",
        "jenis_sq": "Folje e pandryshueshme lavdërimi"
    },
    "7. Fi'il Jamid__3": {
        "arti_sq": "Sa i keq që është! / I urryer!",
        "desc_sq": "Sa i keq është (Folje e ngurosur qortimi)",
        "jenis_sq": "Folje e pandryshueshme qortimi"
    },
    "7. Fi'il Jamid__4": {
        "arti_sq": "Ndoshta / ka mundësi",
        "desc_sq": "Ndoshta / shpresohet (Folje e shpresës dhe pritshmërisë)",
        "jenis_sq": "Folje e pandryshueshme shprese"
    },
    "7. Fi'il Jamid__5": {
        "arti_sq": "Sa e tmerrshme! / Sa i keq!",
        "desc_sq": "Sa i shëmtuar është (Folje e ngurosur qortimi)",
        "jenis_sq": "Folje e pandryshueshme qortimi"
    }
}

BENTUK_HARF_SQ = {
    "1. Harf Nafyi": "1. Pjesëzat mohuese (Harf Nafyi - Mohimi)",
    "2. Harf Tahqiq Taswif": "2. Pjesëzat e vërtetimit dhe së ardhmes (Tahqiq & Taswif)",
    "3. Harf Syarat": "3. Pjesëzat kushtore (Harf Syarat)",
    "4. Harf Mashdariyah": "4. Pjesëzat paskajore / masdarike (Harf Mashdariyah)",
    "5. Harf Zaidah": "5. Pjesëzat theksuese / shtesë (Harf Zaidah)",
    "6. Harf Istifham": "6. Pjesëzat pyetëse (Harf Istifham)",
    "7. Harf Jawab": "7. Pjesëzat e përgjigjes (Harf Jawab)",
    "8. Harf Ibtida'": "8. Pjesëzat nismëtare (Harf Ibtida')",
    "9. Harf Tafshil": "9. Pjesëzat e hollësishme / shpjeguese (Harf Tafshil)",
    "10. Harf Mufaja'ah": "10. Pjesëzat e befasimit (Harf Mufaja'ah)",
    "11. Harf Mufassirah": "11. Pjesëzat interpretuese (Harf Mufassirah)",
    "12. Harf Istiftahiyah": "12. Pjesëzat hapëse (Harf Istiftahiyah)",
    "13. Harf Rada'": "13. Pjesëzat qortuese / refuzuese (Harf Rada')",
    "14. Harf Ta'ajjub": "14. Pjesëzat e habisë (Harf Ta'ajjub)",
    "15. Harf Fariqah": "15. Pjesëzat dalluese (Harf Fariqah)",
    "16. Harf Mauthi'ah": "16. Pjesëzat paralajmëruese të betimit (Harf Mauthi'ah)",
    "17. Harf Mabany": "17. Pjesëzat ndërtuese / shkronjat (Harf Mabany)"
}

ALBANIAN_HARF_GRAMMAR = {
    "1. Harf Nafyi__1": {
        "arti_sq": "Nuk / s'ka / jo (mohim)",
        "desc_sq": "Pjesëz e përgjithshme mohuese (Laa)",
        "jenis_sq": "Pjesëz mohuese"
    },
    "1. Harf Nafyi__2": {
        "arti_sq": "Nuk / asgjë / aspak",
        "desc_sq": "Pjesëz mohuese për të shkuarën dhe të tashmen (Maa)",
        "jenis_sq": "Pjesëz mohuese"
    },
    "1. Harf Nafyi__3": {
        "arti_sq": "Vetëm / veçse",
        "desc_sq": "Pjesëz mohuese kufizimi (In... illaa)",
        "jenis_sq": "Pjesëz mohuese kufizuese"
    },
    "1. Harf Nafyi__4": {
        "arti_sq": "A nuk ka? / A mos ka?",
        "desc_sq": "Pjesëz pyetëse retorike mohuese (Hal)",
        "jenis_sq": "Pjesëz retorike mohuese"
    },
    "1. Harf Nafyi__5": {
        "arti_sq": "Nuk ka (kohë)",
        "desc_sq": "Pjesëz mohuese për koncepte kohore (Laata)",
        "jenis_sq": "Pjesëz mohuese kohe"
    },
    "1. Harf Nafyi__6": {
        "arti_sq": "Çfarë tjetër veçse / asgjë",
        "desc_sq": "Pjesëz pyetëse retorike e përbërë mohuese (Maadhaa)",
        "jenis_sq": "Pjesëz retorike e përbërë"
    },
    "2. Harf Tahqiq Taswif__7": {
        "arti_sq": "Vërtet / tashmë (pohim)",
        "desc_sq": "Pjesëz pohuese e sigurisë (Qad)",
        "jenis_sq": "Pjesëz pohuese sigurie"
    },
    "2. Harf Tahqiq Taswif__8": {
        "arti_sq": "Më vonë do të / me siguri",
        "desc_sq": "Pjesëz e së ardhmes së largët (Sawfa)",
        "jenis_sq": "Pjesëz e së ardhmes së largët"
    },
    "3. Harf Syarat__9": {
        "arti_sq": "Sikur të / po të (e parealizueshme)",
        "desc_sq": "Pjesëz kushtore për kusht të parealizuar në të shkuarën (Law)",
        "jenis_sq": "Pjesëz kushtore"
    },
    "3. Harf Syarat__10": {
        "arti_sq": "Po të mos ishte... me siguri",
        "desc_sq": "Pjesëz kushtore pengimi nga ekzistenca e tjetrës (Lawlaa)",
        "jenis_sq": "Pjesëz kushtore penguese"
    },
    "3. Harf Syarat__11": {
        "arti_sq": "Edhe sikur / ndonëse",
        "desc_sq": "Pjesëz kushtore lëshuese (Law)",
        "jenis_sq": "Pjesëz kushtore lëshuese"
    },
    "3. Harf Syarat__12": {
        "arti_sq": "Nëse / kurdoherë që",
        "desc_sq": "Pjesëz kushtore e theksuar (Immaa = In + Maa)",
        "jenis_sq": "Pjesëz kushtore e theksuar"
    },
    "3. Harf Syarat__13": {
        "arti_sq": "Çfarëdo shenje / çfarëdo",
        "desc_sq": "Emër kushtor i përgjithshëm (Mahmaa)",
        "jenis_sq": "Emër kushtor"
    },
    "4. Harf Mashdariyah__14": {
        "arti_sq": "Për sa kohë që / gjatë kohës",
        "desc_sq": "Pjesëz paskajore masdarike kohe (Maa)",
        "jenis_sq": "Pjesëz masdarike kohëzgjatjeje"
    },
    "4. Harf Mashdariyah__15": {
        "arti_sq": "Që të mos / me qëllim që jo",
        "desc_sq": "Pjesëz masdarike mohuese (Allaa = An + Laa)",
        "jenis_sq": "Pjesëz masdarike mohuese"
    },
    "4. Harf Mashdariyah__16": {
        "arti_sq": "Që të / të (masdarike)",
        "desc_sq": "Pjesëz masdarike foljore (An)",
        "jenis_sq": "Pjesëz masdarike"
    },
    "4. Harf Mashdariyah__17": {
        "arti_sq": "Sikur të dëshironte",
        "desc_sq": "Pjesëz masdarike dëshire (Law)",
        "jenis_sq": "Pjesëz masdarike dëshire"
    },
    "4. Harf Mashdariyah__18": {
        "arti_sq": "Që ju të mos adhuroni",
        "desc_sq": "Pjesëz masdarike me ndalim (An + Laa)",
        "jenis_sq": "Pjesëz masdarike ndaluese"
    },
    "4. Harf Mashdariyah__19": {
        "arti_sq": "Që (me të vërtetë)",
        "desc_sq": "Pjesëz masdarike e lehtësuar (An e lehtësuar nga Enne)",
        "jenis_sq": "Pjesëz masdarike e lehtësuar"
    },
    "5. Harf Zaidah__20": {
        "arti_sq": "Ashtu siç / si",
        "desc_sq": "Pjesëz krahasuese me përforcim shtesë (Kamaa = Ka + Maa)",
        "jenis_sq": "Pjesëz përforcuese"
    },
    "5. Harf Zaidah__21": {
        "arti_sq": "Çfarëdo shembulli qoftë",
        "desc_sq": "Pjesëz e papërcaktuar përforcuese (Maa Zaidah)",
        "jenis_sq": "Pjesëz shtesë përforcuese"
    },
    "5. Harf Zaidah__22": {
        "arti_sq": "Betohem me të vërtetë",
        "desc_sq": "Pjesëz përforcuese e betimit (Laa Zaidah)",
        "jenis_sq": "Pjesëz përforcuese betimi"
    },
    "5. Harf Zaidah__23": {
        "arti_sq": "Për shkak të mëshirës së Allahut",
        "desc_sq": "Parafjalë me pjesëz shtesë përforcuese (Bimaa = Bi + Maa)",
        "jenis_sq": "Pjesëz përforcuese pas parafjale"
    },
    "5. Harf Zaidah__24": {
        "arti_sq": "Kur erdhi myzhedhësi",
        "desc_sq": "Pjesëz përforcuese pas lidhëzës kohore (An pas Lammaa)",
        "jenis_sq": "Pjesëz përforcuese kohore"
    },
    "6. Harf Istifham__25": {
        "arti_sq": "A? / Vallë?",
        "desc_sq": "Pjesëz pyetëse pohimi (Hal)",
        "jenis_sq": "Pjesëz pyetëse"
    },
    "7. Harf Jawab__26": {
        "arti_sq": "Në atë rast / atëherë",
        "desc_sq": "Pjesëz përgjigjeje dhe rrjedhimi (Idhan)",
        "jenis_sq": "Pjesëz rrjedhimi"
    },
    "7. Harf Jawab__27": {
        "arti_sq": "Gjithsesi / po sigurisht!",
        "desc_sq": "Pjesëz përgjigjeje pohuese që mohon pyetjen negative (Belaa)",
        "jenis_sq": "Pjesëz pohuese përgjigjeje"
    },
    "7. Harf Jawab__28": {
        "arti_sq": "Po / ashtu është",
        "desc_sq": "Pjesëz përgjigjeje pajtimi dhe pohimi (Na'am)",
        "jenis_sq": "Pjesëz përgjigjeje"
    },
    "7. Harf Jawab__29": {
        "arti_sq": "Po, për Zotin tim!",
        "desc_sq": "Pjesëz përgjigjeje betimi dhe pohimi (I / Ii)",
        "jenis_sq": "Pjesëz betimi përgjigjeje"
    },
    "8. Harf Ibtida'__30": {
        "arti_sq": "Deri sa / aq sa",
        "desc_sq": "Pjesëz nismëtare e synimit (Hattaa)",
        "jenis_sq": "Pjesëz nismëtare"
    },
    "9. Harf Tafshil__31": {
        "arti_sq": "Për sa i përket / sa për",
        "desc_sq": "Pjesëz hyrëse, hollësimi dhe kushti (Ammaa)",
        "jenis_sq": "Pjesëz hollësimi"
    },
    "10. Harf Mufaja'ah__32": {
        "arti_sq": "Kur ja / papritmas",
        "desc_sq": "Pjesëz e befasimit të menjëhershëm (Idhaa)",
        "jenis_sq": "Pjesëz befasimi"
    },
    "11. Harf Mufassirah__33": {
        "arti_sq": "Domethënë / pikërisht",
        "desc_sq": "Pjesëz interpretuese shpjeguese (An)",
        "jenis_sq": "Pjesëz interpretuese"
    },
    "12. Harf Istiftahiyah__34": {
        "arti_sq": "Dijeni mirë! / Vini re!",
        "desc_sq": "Pjesëz hapëse për tërheqje vëmendjeje dhe paralajmërim (Alaa)",
        "jenis_sq": "Pjesëz hapëse vëmendjeje"
    },
    "13. Harf Rada'__35": {
        "arti_sq": "Kurrsesi! / Asnjëherë!",
        "desc_sq": "Pjesëz e qortimit dhe refuzimit të prerë (Kallaa)",
        "jenis_sq": "Pjesëz refuzimi dhe qortimi"
    },
    "14. Harf Ta'ajjub__36": {
        "arti_sq": "Sa të durueshëm janë!",
        "desc_sq": "Pjesëz e habisë dhe çudisë (Maa Ta'ajjubiyyah)",
        "jenis_sq": "Pjesëz habie"
    },
    "15. Harf Fariqah__37": {
        "arti_sq": "Vërtet / me siguri",
        "desc_sq": "Lam dalluese përforcuese (Lam Fariqah te In e lehtësuar)",
        "jenis_sq": "Lam dalluese"
    },
    "16. Harf Mauthi'ah__38": {
        "arti_sq": "Nëse... betohem me siguri",
        "desc_sq": "Pjesëz paralajmëruese e betimit kushtor (La-in)",
        "jenis_sq": "Lam paralajmëruese betimi"
    },
    "17. Harf Mabany__39": {
        "arti_sq": "Haa-Miim",
        "desc_sq": "Shkronja të shkurtuara kur'anore në fillim të sures (حم)",
        "jenis_sq": "Shkronja kur'anore nismëtare (Mukatta'at)"
    },
    "17. Harf Mabany__40": {
        "arti_sq": "Elif-Laam-Miim",
        "desc_sq": "Shkronja të shkurtuara kur'anore në fillim të sures (الم)",
        "jenis_sq": "Shkronja kur'anore nismëtare (Mukatta'at)"
    },
    "17. Harf Mabany__41": {
        "arti_sq": "Elif-Laam-Raa",
        "desc_sq": "Shkronja të shkurtuara kur'anore në fillim të sures (الر)",
        "jenis_sq": "Shkronja kur'anore nismëtare (Mukatta'at)"
    },
    "17. Harf Mabany__42": {
        "arti_sq": "Taa-Siin-Miim",
        "desc_sq": "Shkronja të shkurtuara kur'anore në fillim të sures (طسم)",
        "jenis_sq": "Shkronja kur'anore nismëtare (Mukatta'at)"
    },
    "17. Harf Mabany__43": {
        "arti_sq": "Elif-Laam-Miim-Raa",
        "desc_sq": "Shkronja të shkurtuara kur'anore në fillim të sures (المر)",
        "jenis_sq": "Shkronja kur'anore nismëtare (Mukatta'at)"
    },
    "17. Harf Mabany__44": {
        "arti_sq": "Elif-Laam-Miim-Saad",
        "desc_sq": "Shkronja të shkurtuara kur'anore në fillim të sures (المص)",
        "jenis_sq": "Shkronja kur'anore nismëtare (Mukatta'at)"
    },
    "17. Harf Mabany__45": {
        "arti_sq": "Saad",
        "desc_sq": "Shkronjë e shkurtuar kur'anore në fillim të sures (ص)",
        "jenis_sq": "Shkronjë kur'anore nismëtare (Mukatta'at)"
    },
    "17. Harf Mabany__46": {
        "arti_sq": "Taa-Siin",
        "desc_sq": "Shkronja të shkurtuara kur'anore në fillim të sures (طس)",
        "jenis_sq": "Shkronja kur'anore nismëtare (Mukatta'at)"
    },
    "17. Harf Mabany__47": {
        "arti_sq": "Taa-Haa",
        "desc_sq": "Shkronja të shkurtuara kur'anore në fillim të sures (طه)",
        "jenis_sq": "Shkronja kur'anore nismëtare (Mukatta'at)"
    },
    "17. Harf Mabany__48": {
        "arti_sq": "'Ajn-Siin-Kaaf",
        "desc_sq": "Shkronja të shkurtuara kur'anore në fillim të sures (عسق)",
        "jenis_sq": "Shkronja kur'anore nismëtare (Mukatta'at)"
    },
    "17. Harf Mabany__49": {
        "arti_sq": "Kaaf",
        "desc_sq": "Shkronjë e shkurtuar kur'anore në fillim të sures (ق)",
        "jenis_sq": "Shkronjë kur'anore nismëtare (Mukatta'at)"
    },
    "17. Harf Mabany__50": {
        "arti_sq": "Kaaf-Haa-Jaa-'Ajn-Saad",
        "desc_sq": "Shkronja të shkurtuara kur'anore në fillim të sures (كهيعص)",
        "jenis_sq": "Shkronja kur'anore nismëtare (Mukatta'at)"
    },
    "17. Harf Mabany__51": {
        "arti_sq": "Nuun",
        "desc_sq": "Shkronjë e shkurtuar kur'anore në fillim të sures (ن)",
        "jenis_sq": "Shkronjë kur'anore nismëtare (Mukatta'at)"
    },
    "17. Harf Mabany__52": {
        "arti_sq": "Jaa-Siin",
        "desc_sq": "Shkronja të shkurtuara kur'anore në fillim të sures (يس)",
        "jenis_sq": "Shkronja kur'anore nismëtare (Mukatta'at)"
    },
    "1": {
        "arti_sq": "Nuk / s'ka / jo (mohim)",
        "desc_sq": "Pjesëz e përgjithshme mohuese (Laa)",
        "jenis_sq": "Pjesëz mohuese"
    },
    "2": {
        "arti_sq": "Nuk / asgjë / aspak",
        "desc_sq": "Pjesëz mohuese për të shkuarën dhe të tashmen (Maa)",
        "jenis_sq": "Pjesëz mohuese"
    },
    "3": {
        "arti_sq": "Vetëm / veçse",
        "desc_sq": "Pjesëz mohuese kufizimi (In... illaa)",
        "jenis_sq": "Pjesëz mohuese kufizuese"
    },
    "4": {
        "arti_sq": "A nuk ka? / A mos ka?",
        "desc_sq": "Pjesëz pyetëse retorike mohuese (Hal)",
        "jenis_sq": "Pjesëz retorike mohuese"
    },
    "5": {
        "arti_sq": "Nuk ka (kohë)",
        "desc_sq": "Pjesëz mohuese për koncepte kohore (Laata)",
        "jenis_sq": "Pjesëz mohuese kohe"
    },
    "6": {
        "arti_sq": "Çfarë tjetër veçse / asgjë",
        "desc_sq": "Pjesëz pyetëse retorike e përbërë mohuese (Maadhaa)",
        "jenis_sq": "Pjesëz retorike e përbërë"
    },
    "7": {
        "arti_sq": "Vërtet / tashmë (pohim)",
        "desc_sq": "Pjesëz pohuese e sigurisë (Qad)",
        "jenis_sq": "Pjesëz pohuese sigurie"
    },
    "8": {
        "arti_sq": "Më vonë do të / me siguri",
        "desc_sq": "Pjesëz e së ardhmes së largët (Sawfa)",
        "jenis_sq": "Pjesëz e së ardhmes së largët"
    },
    "9": {
        "arti_sq": "Sikur të / po të (e parealizueshme)",
        "desc_sq": "Pjesëz kushtore për kusht të parealizuar në të shkuarën (Law)",
        "jenis_sq": "Pjesëz kushtore"
    },
    "10": {
        "arti_sq": "Po të mos ishte... me siguri",
        "desc_sq": "Pjesëz kushtore pengimi nga ekzistenca e tjetrës (Lawlaa)",
        "jenis_sq": "Pjesëz kushtore penguese"
    },
    "11": {
        "arti_sq": "Edhe sikur / ndonëse",
        "desc_sq": "Pjesëz kushtore lëshuese (Law)",
        "jenis_sq": "Pjesëz kushtore lëshuese"
    },
    "12": {
        "arti_sq": "Nëse / kurdoherë që",
        "desc_sq": "Pjesëz kushtore e theksuar (Immaa = In + Maa)",
        "jenis_sq": "Pjesëz kushtore e theksuar"
    },
    "13": {
        "arti_sq": "Çfarëdo shenje / çfarëdo",
        "desc_sq": "Emër kushtor i përgjithshëm (Mahmaa)",
        "jenis_sq": "Emër kushtor"
    },
    "14": {
        "arti_sq": "Për sa kohë që / gjatë kohës",
        "desc_sq": "Pjesëz paskajore masdarike kohe (Maa)",
        "jenis_sq": "Pjesëz masdarike kohëzgjatjeje"
    },
    "15": {
        "arti_sq": "Që të mos / me qëllim që jo",
        "desc_sq": "Pjesëz masdarike mohuese (Allaa = An + Laa)",
        "jenis_sq": "Pjesëz masdarike mohuese"
    },
    "16": {
        "arti_sq": "Që të / të (masdarike)",
        "desc_sq": "Pjesëz masdarike foljore (An)",
        "jenis_sq": "Pjesëz masdarike"
    },
    "17": {
        "arti_sq": "Sikur të dëshironte",
        "desc_sq": "Pjesëz masdarike dëshire (Law)",
        "jenis_sq": "Pjesëz masdarike dëshire"
    },
    "18": {
        "arti_sq": "Që ju të mos adhuroni",
        "desc_sq": "Pjesëz masdarike me ndalim (An + Laa)",
        "jenis_sq": "Pjesëz masdarike ndaluese"
    },
    "19": {
        "arti_sq": "Që (me të vërtetë)",
        "desc_sq": "Pjesëz masdarike e lehtësuar (An e lehtësuar nga Enne)",
        "jenis_sq": "Pjesëz masdarike e lehtësuar"
    },
    "20": {
        "arti_sq": "Ashtu siç / si",
        "desc_sq": "Pjesëz krahasuese me përforcim shtesë (Kamaa = Ka + Maa)",
        "jenis_sq": "Pjesëz përforcuese"
    },
    "21": {
        "arti_sq": "Çfarëdo shembulli qoftë",
        "desc_sq": "Pjesëz e papërcaktuar përforcuese (Maa Zaidah)",
        "jenis_sq": "Pjesëz shtesë përforcuese"
    },
    "22": {
        "arti_sq": "Betohem me të vërtetë",
        "desc_sq": "Pjesëz përforcuese e betimit (Laa Zaidah)",
        "jenis_sq": "Pjesëz përforcuese betimi"
    },
    "23": {
        "arti_sq": "Për shkak të mëshirës së Allahut",
        "desc_sq": "Parafjalë me pjesëz shtesë përforcuese (Bimaa = Bi + Maa)",
        "jenis_sq": "Pjesëz përforcuese pas parafjale"
    },
    "24": {
        "arti_sq": "Kur erdhi myzhedhësi",
        "desc_sq": "Pjesëz përforcuese pas lidhëzës kohore (An pas Lammaa)",
        "jenis_sq": "Pjesëz përforcuese kohore"
    },
    "25": {
        "arti_sq": "A? / Vallë?",
        "desc_sq": "Pjesëz pyetëse pohimi (Hal)",
        "jenis_sq": "Pjesëz pyetëse"
    },
    "26": {
        "arti_sq": "Në atë rast / atëherë",
        "desc_sq": "Pjesëz përgjigjeje dhe rrjedhimi (Idhan)",
        "jenis_sq": "Pjesëz rrjedhimi"
    },
    "27": {
        "arti_sq": "Gjithsesi / po sigurisht!",
        "desc_sq": "Pjesëz përgjigjeje pohuese që mohon pyetjen negative (Belaa)",
        "jenis_sq": "Pjesëz pohuese përgjigjeje"
    },
    "28": {
        "arti_sq": "Po / ashtu është",
        "desc_sq": "Pjesëz përgjigjeje pajtimi dhe pohimi (Na'am)",
        "jenis_sq": "Pjesëz përgjigjeje"
    },
    "29": {
        "arti_sq": "Po, për Zotin tim!",
        "desc_sq": "Pjesëz përgjigjeje betimi dhe pohimi (I / Ii)",
        "jenis_sq": "Pjesëz betimi përgjigjeje"
    },
    "30": {
        "arti_sq": "Deri sa / aq sa",
        "desc_sq": "Pjesëz nismëtare e synimit (Hattaa)",
        "jenis_sq": "Pjesëz nismëtare"
    },
    "31": {
        "arti_sq": "Për sa i përket / sa për",
        "desc_sq": "Pjesëz hyrëse, hollësimi dhe kushti (Ammaa)",
        "jenis_sq": "Pjesëz hollësimi"
    },
    "32": {
        "arti_sq": "Kur ja / papritmas",
        "desc_sq": "Pjesëz e befasimit të menjëhershëm (Idhaa)",
        "jenis_sq": "Pjesëz befasimi"
    },
    "33": {
        "arti_sq": "Domethënë / pikërisht",
        "desc_sq": "Pjesëz interpretuese shpjeguese (An)",
        "jenis_sq": "Pjesëz interpretuese"
    },
    "34": {
        "arti_sq": "Dijeni mirë! / Vini re!",
        "desc_sq": "Pjesëz hapëse për tërheqje vëmendjeje dhe paralajmërim (Alaa)",
        "jenis_sq": "Pjesëz hapëse vëmendjeje"
    },
    "35": {
        "arti_sq": "Kurrsesi! / Asnjëherë!",
        "desc_sq": "Pjesëz e qortimit dhe refuzimit të prerë (Kallaa)",
        "jenis_sq": "Pjesëz refuzimi dhe qortimi"
    },
    "36": {
        "arti_sq": "Sa të durueshëm janë!",
        "desc_sq": "Pjesëz e habisë dhe çudisë (Maa Ta'ajjubiyyah)",
        "jenis_sq": "Pjesëz habie"
    },
    "37": {
        "arti_sq": "Vërtet / me siguri",
        "desc_sq": "Lam dalluese përforcuese (Lam Fariqah te In e lehtësuar)",
        "jenis_sq": "Lam dalluese"
    },
    "38": {
        "arti_sq": "Nëse... betohem me siguri",
        "desc_sq": "Pjesëz paralajmëruese e betimit kushtor (La-in)",
        "jenis_sq": "Lam paralajmëruese betimi"
    },
    "39": {
        "arti_sq": "Haa-Miim",
        "desc_sq": "Shkronja të shkurtuara kur'anore në fillim të sures (حم)",
        "jenis_sq": "Shkronja kur'anore nismëtare (Mukatta'at)"
    },
    "40": {
        "arti_sq": "Elif-Laam-Miim",
        "desc_sq": "Shkronja të shkurtuara kur'anore në fillim të sures (الم)",
        "jenis_sq": "Shkronja kur'anore nismëtare (Mukatta'at)"
    },
    "41": {
        "arti_sq": "Elif-Laam-Raa",
        "desc_sq": "Shkronja të shkurtuara kur'anore në fillim të sures (الر)",
        "jenis_sq": "Shkronja kur'anore nismëtare (Mukatta'at)"
    },
    "42": {
        "arti_sq": "Taa-Siin-Miim",
        "desc_sq": "Shkronja të shkurtuara kur'anore në fillim të sures (طسم)",
        "jenis_sq": "Shkronja kur'anore nismëtare (Mukatta'at)"
    },
    "43": {
        "arti_sq": "Elif-Laam-Miim-Raa",
        "desc_sq": "Shkronja të shkurtuara kur'anore në fillim të sures (المر)",
        "jenis_sq": "Shkronja kur'anore nismëtare (Mukatta'at)"
    },
    "44": {
        "arti_sq": "Elif-Laam-Miim-Saad",
        "desc_sq": "Shkronja të shkurtuara kur'anore në fillim të sures (المص)",
        "jenis_sq": "Shkronja kur'anore nismëtare (Mukatta'at)"
    },
    "45": {
        "arti_sq": "Saad",
        "desc_sq": "Shkronjë e shkurtuar kur'anore në fillim të sures (ص)",
        "jenis_sq": "Shkronjë kur'anore nismëtare (Mukatta'at)"
    },
    "46": {
        "arti_sq": "Taa-Siin",
        "desc_sq": "Shkronja të shkurtuara kur'anore në fillim të sures (طس)",
        "jenis_sq": "Shkronja kur'anore nismëtare (Mukatta'at)"
    },
    "47": {
        "arti_sq": "Taa-Haa",
        "desc_sq": "Shkronja të shkurtuara kur'anore në fillim të sures (طه)",
        "jenis_sq": "Shkronja kur'anore nismëtare (Mukatta'at)"
    },
    "48": {
        "arti_sq": "'Ajn-Siin-Kaaf",
        "desc_sq": "Shkronja të shkurtuara kur'anore në fillim të sures (عسق)",
        "jenis_sq": "Shkronja kur'anore nismëtare (Mukatta'at)"
    },
    "49": {
        "arti_sq": "Kaaf",
        "desc_sq": "Shkronjë e shkurtuar kur'anore në fillim të sures (ق)",
        "jenis_sq": "Shkronjë kur'anore nismëtare (Mukatta'at)"
    },
    "50": {
        "arti_sq": "Kaaf-Haa-Jaa-'Ajn-Saad",
        "desc_sq": "Shkronja të shkurtuara kur'anore në fillim të sures (كهيعص)",
        "jenis_sq": "Shkronja kur'anore nismëtare (Mukatta'at)"
    },
    "51": {
        "arti_sq": "Nuun",
        "desc_sq": "Shkronjë e shkurtuar kur'anore në fillim të sures (ن)",
        "jenis_sq": "Shkronjë kur'anore nismëtare (Mukatta'at)"
    },
    "52": {
        "arti_sq": "Jaa-Siin",
        "desc_sq": "Shkronja të shkurtuara kur'anore në fillim të sures (يس)",
        "jenis_sq": "Shkronja kur'anore nismëtare (Mukatta'at)"
    }
}
