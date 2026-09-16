#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to build Portuguese dataset and enrich dhamir_data.json & dhamir_data.js
"""

import os
import sys
import json

if sys.platform.startswith('win'):
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 1. 114 Surahs Portuguese Names / Meanings
PORTUGUESE_SURAHS = {
    "1": "A Abertura",
    "2": "A Vaca",
    "3": "A Família de Imran",
    "4": "As Mulheres",
    "5": "A Mesa Servida",
    "6": "O Gado",
    "7": "Os Lugares Elevados",
    "8": "Os Espólios de Guerra",
    "9": "O Arrependimento",
    "10": "Jonas",
    "11": "Hud",
    "12": "José",
    "13": "O Trovão",
    "14": "Abraão",
    "15": "Al-Hijr",
    "16": "As Abelhas",
    "17": "A Viagem Noturna",
    "18": "A Caverna",
    "19": "Maria",
    "20": "Ta-Ha",
    "21": "Os Profetas",
    "22": "A Peregrinação",
    "23": "Os Crentes",
    "24": "A Luz",
    "25": "O Discernimento",
    "26": "Os Poetas",
    "27": "As Formigas",
    "28": "As Narrativas",
    "29": "A Aranha",
    "30": "Os Bizantinos",
    "31": "Luqman",
    "32": "A Prostração",
    "33": "Os Confederados",
    "34": "Sabá",
    "35": "O Criador",
    "36": "Ya-Sin",
    "37": "Os Enfileirados",
    "38": "Sad",
    "39": "Os Grupos",
    "40": "O Perdoador",
    "41": "Os Versículos Detalhados",
    "42": "A Consulta",
    "43": "Os Ornamentos de Ouro",
    "44": "A Fumaça",
    "45": "O Genuflexo",
    "46": "As Dunas",
    "47": "Muhammad",
    "48": "A Vitória",
    "49": "Os Aposentos",
    "50": "Qaf",
    "51": "Os Ventos Dispersores",
    "52": "O Monte",
    "53": "A Estrela",
    "54": "A Lua",
    "55": "O Clemente",
    "56": "O Evento Inevitável",
    "57": "O Ferro",
    "58": "A Discussão",
    "59": "A Concentração",
    "60": "A Examinada",
    "61": "As Fileiras",
    "62": "A Sexta-feira",
    "63": "Os Hipócritas",
    "64": "A Ilusão Mútua",
    "65": "O Divórcio",
    "66": "As Proibições",
    "67": "O Domínio",
    "68": "O Cálamo",
    "69": "A Realidade Inevitável",
    "70": "As Vias de Ascensão",
    "71": "Noé",
    "72": "Os Gênios",
    "73": "O Envolto",
    "74": "O Embuçado",
    "75": "A Ressurreição",
    "76": "O Homem",
    "77": "Os Enviados",
    "78": "A Notícia",
    "79": "Os Que Arrancam",
    "80": "O Austero",
    "81": "O Obscurecimento",
    "82": "O Fendimento",
    "83": "Os Fraudadores",
    "84": "A Fenda",
    "85": "As Constelações",
    "86": "O Astro Noturno",
    "87": "O Altíssimo",
    "88": "O Evento Envolvente",
    "89": "A Aurora",
    "90": "A Cidade",
    "91": "O Sol",
    "92": "A Noite",
    "93": "As Horas da Manhã",
    "94": "A Abertura do Peito",
    "95": "O Figo",
    "96": "O Coágulo",
    "97": "O Decreto",
    "98": "A Evidência Clara",
    "99": "O Terremoto",
    "100": "Os Corcéis",
    "101": "A Calamidade",
    "102": "A Cobiça",
    "103": "A Era",
    "104": "O Difamador",
    "105": "O Elefante",
    "106": "Os Coraixitas",
    "107": "A Ajuda Mútua",
    "108": "A Abundância",
    "109": "Os Incrédulos",
    "110": "O Socorro",
    "111": "A Fibra de Palmeira",
    "112": "A Unicidade de Deus",
    "113": "A Alvorada",
    "114": "A Humanidade"
}

# 2. 7 Categories in Portuguese
BENTUK_KATA_PT = {
    '1. Dhamir': '1. Pronomes (Dhamir - Pronomes Pessoais)',
    '2. Mawshul': '2. Pronomes Relativos (Mawshul)',
    '3. Istifham': '3. Interrogativos (Istifham - Pronomes e Partículas Interrogativas)',
    '4. Syarath': '4. Condicionais (Syarath - Partículas Condicionais)',
    '5. Isyarah': '5. Demonstrativos (Isyarah - Pronomes Demonstrativos)',
    "6. Isim Fi'il": "6. Nomes Verbais (Isim Fi'il - Substantivos com Sentido Verbal)",
    "7. Fi'il Jamid": "7. Verbos Inflexíveis (Fi'il Jamid - Verbos Estáticos)"
}

# 3. 76 Grammatical Metadata in Portuguese
PORTUGUESE_GRAMMAR = {
    '1. Dhamir__1a': {
        'arti_pt': 'ELE',
        'desc_pt': 'Ele (3ª pessoa do singular masculino, pronome independente)',
        'jenis_pt': 'Munfashil (Independente)'
    },
    '1. Dhamir__1b': {
        'arti_pt': '..DELE / ..O / ..LHE',
        'desc_pt': '...-dele / o / lhe / seu (3ª pessoa singular masc., pronome sufixo/ligado)',
        'jenis_pt': 'Muttashil (Sufixo / Ligado)'
    },
    '1. Dhamir__1c': {
        'arti_pt': 'SOMENTE A ELE',
        'desc_pt': 'Somente a Ele / a Ele somente (Pronome objeto independente, 3ª pess. masc.)',
        'jenis_pt': 'Munfashil Manshub (Objeto Acusativo)'
    },
    '1. Dhamir__2a': {
        'arti_pt': 'ELES DOIS / ELAS DUAS',
        'desc_pt': 'Eles dois / Elas duas (3ª pessoa dual, pronome independente)',
        'jenis_pt': 'Munfashil (Independente)'
    },
    '1. Dhamir__2b': {
        'arti_pt': '..DELES DOIS / ..DELAS DUAS',
        'desc_pt': '...-deles dois / delas duas (3ª pessoa dual, pronome sufixo/ligado)',
        'jenis_pt': 'Muttashil (Sufixo / Ligado)'
    },
    '1. Dhamir__3a': {
        'arti_pt': 'ELES',
        'desc_pt': 'Eles (3ª pessoa plural masculino, pronome independente)',
        'jenis_pt': 'Munfashil (Independente)'
    },
    '1. Dhamir__3b': {
        'arti_pt': '..DELES / ..OS / ..LHES',
        'desc_pt': '...-deles / seus / os / lhes (3ª pessoa plural masc., pronome sufixo/ligado)',
        'jenis_pt': 'Muttashil (Sufixo / Ligado)'
    },
    '1. Dhamir__3c': {
        'arti_pt': 'SOMENTE A ELES',
        'desc_pt': 'Somente a eles (Pronome objeto independente, 3ª pess. plur. masc.)',
        'jenis_pt': 'Munfashil Manshub (Objeto Acusativo)'
    },
    '1. Dhamir__4a': {
        'arti_pt': 'ELA',
        'desc_pt': 'Ela (3ª pessoa singular feminino, pronome independente)',
        'jenis_pt': 'Munfashil (Independente)'
    },
    '1. Dhamir__4b': {
        'arti_pt': '..DELA / ..A / ..LHE',
        'desc_pt': '...-dela / a / lhe / sua (3ª pessoa singular fem., pronome sufixo/ligado)',
        'jenis_pt': 'Muttashil (Sufixo / Ligado)'
    },
    '1. Dhamir__5a': {
        'arti_pt': 'ELAS',
        'desc_pt': 'Elas (3ª pessoa plural feminino, pronome independente)',
        'jenis_pt': 'Munfashil (Independente)'
    },
    '1. Dhamir__5b': {
        'arti_pt': '..DELAS / ..AS / ..LHES (FEM)',
        'desc_pt': '...-delas / suas / as / lhes (3ª pessoa plural fem., pronome sufixo/ligado)',
        'jenis_pt': 'Muttashil (Sufixo / Ligado)'
    },
    '1. Dhamir__6a': {
        'arti_pt': 'TU / VOCÊ (MASC)',
        'desc_pt': 'Tu / Você (2ª pessoa singular masculino, pronome independente)',
        'jenis_pt': 'Munfashil (Independente)'
    },
    '1. Dhamir__6b': {
        'arti_pt': '..TEU / ..TE / ..TI (MASC)',
        'desc_pt': '...-teu / te / ti / seu (2ª pessoa singular masc., pronome sufixo/ligado)',
        'jenis_pt': 'Muttashil (Sufixo / Ligado)'
    },
    '1. Dhamir__6c': {
        'arti_pt': 'SOMENTE A TI',
        'desc_pt': 'Somente a Ti / a Ti unicamente (Pronome objeto independente, 2ª pess. masc.)',
        'jenis_pt': 'Munfashil Manshub (Objeto Acusativo)'
    },
    '1. Dhamir__7a': {
        'arti_pt': 'VÓS DOIS / VOCÊS DOIS',
        'desc_pt': 'Vós dois / Vocês dois (2ª pessoa dual, pronome independente)',
        'jenis_pt': 'Munfashil (Independente)'
    },
    '1. Dhamir__7b': {
        'arti_pt': '..VOSSO / ..DE VOCÊS DOIS',
        'desc_pt': '...-vosso / de vocês dois (2ª pessoa dual, pronome sufixo/ligado)',
        'jenis_pt': 'Muttashil (Sufixo / Ligado)'
    },
    '1. Dhamir__8a': {
        'arti_pt': 'VÓS / VOCÊS',
        'desc_pt': 'Vós / Vocês (2ª pessoa plural masculino, pronome independente)',
        'jenis_pt': 'Munfashil (Independente)'
    },
    '1. Dhamir__8b': {
        'arti_pt': '..VOSSO / ..DE VOCÊS / ..VOS',
        'desc_pt': '...-vosso / vossos / vos / de vocês (2ª pessoa plural masc., pronome sufixo/ligado)',
        'jenis_pt': 'Muttashil (Sufixo / Ligado)'
    },
    '1. Dhamir__8c': {
        'arti_pt': 'SOMENTE A VÓS / A VOCÊS',
        'desc_pt': 'Somente a vós / a vocês unicamente (Pronome objeto independente, 2ª pess. plur. masc.)',
        'jenis_pt': 'Munfashil Manshub (Objeto Acusativo)'
    },
    '1. Dhamir__9b': {
        'arti_pt': '..TEU / ..TE (FEM)',
        'desc_pt': '...-teu / te / ti (2ª pessoa singular feminino, pronome sufixo/ligado)',
        'jenis_pt': 'Muttashil (Sufixo / Ligado)'
    },
    '1. Dhamir__11a': {
        'arti_pt': 'EU',
        'desc_pt': 'Eu (1ª pessoa singular, pronome independente)',
        'jenis_pt': 'Munfashil (Independente)'
    },
    '1. Dhamir__11b': {
        'arti_pt': '..MEU / ..ME / ..MIM',
        'desc_pt': '...-meu / meus / me / mim (1ª pessoa singular, pronome sufixo/ligado)',
        'jenis_pt': 'Muttashil (Sufixo / Ligado)'
    },
    '1. Dhamir__11c': {
        'arti_pt': 'SOMENTE A MIM',
        'desc_pt': 'Somente a Mim / a Mim unicamente (Pronome objeto independente, 1ª pess. sing.)',
        'jenis_pt': 'Munfashil Manshub (Objeto Acusativo)'
    },
    '1. Dhamir__12a': {
        'arti_pt': 'NÓS',
        'desc_pt': 'Nós (1ª pessoa do plural, pronome independente)',
        'jenis_pt': 'Munfashil (Independente)'
    },
    '1. Dhamir__12b': {
        'arti_pt': '..NOSSO / ..NOS',
        'desc_pt': '...-nosso / nossos / nos (1ª pessoa plural, pronome sufixo/ligado)',
        'jenis_pt': 'Muttashil (Sufixo / Ligado)'
    },
    '1. Dhamir__12c': {
        'arti_pt': 'SOMENTE A NÓS',
        'desc_pt': 'Somente a nós (Pronome objeto independente, 1ª pessoa plural)',
        'jenis_pt': 'Munfashil Manshub (Objeto Acusativo)'
    },

    # 2. Mawshul
    '2. Mawshul__1': {
        'arti_pt': 'AQUELE QUE / O QUAL',
        'desc_pt': 'Aquele que / o qual (Pronome relativo, singular masculino)',
        'jenis_pt': 'Isim Mawshul (Singular Masculino)'
    },
    '2. Mawshul__2': {
        'arti_pt': 'AQUELES DOIS QUE',
        'desc_pt': 'Aqueles dois que (Pronome relativo, dual masculino)',
        'jenis_pt': 'Isim Mawshul (Dual Masculino)'
    },
    '2. Mawshul__3': {
        'arti_pt': 'AQUELES QUE / OS QUAIS',
        'desc_pt': 'Aqueles que / os quais (Pronome relativo, plural masculino)',
        'jenis_pt': 'Isim Mawshul (Plural Masculino)'
    },
    '2. Mawshul__4': {
        'arti_pt': 'AQUELA QUE / A QUAL',
        'desc_pt': 'Aquela que / a qual (Pronome relativo, singular feminino)',
        'jenis_pt': 'Isim Mawshul (Singular Feminino)'
    },
    '2. Mawshul__5': {
        'arti_pt': 'AQUELAS QUE / AS QUAIS',
        'desc_pt': 'Aquelas que / as quais (Pronome relativo, plural feminino)',
        'jenis_pt': 'Isim Mawshul (Plural Feminino)'
    },
    '2. Mawshul__6': {
        'arti_pt': 'QUEM / AQUELE QUE',
        'desc_pt': 'Quem / aquele que (Pronome relativo para seres dotados de razão / akil)',
        'jenis_pt': "Isim Mawshul 'Amm ('Aqil)"
    },
    '2. Mawshul__7': {
        'arti_pt': 'O QUE / AQUILO QUE',
        'desc_pt': 'O que / aquilo que / o qual (Pronome relativo para seres não racionais / ghairu akil)',
        'jenis_pt': "Isim Mawshul 'Amm (Ghairu 'Aqil)"
    },
    '2. Mawshul__8': {
        'arti_pt': 'QUALQUER QUE / QUAL DELES',
        'desc_pt': 'Qual deles / quem quer que (Pronome relativo / seletivo)',
        'jenis_pt': "Isim Mawshul (Mu'rab)"
    },
    '2. Mawshul__9': {
        'arti_pt': 'POSSUIDOR DE / AQUELE QUE TEM',
        'desc_pt': 'Possuidor de / que tem (Pronome relativo dialetal / Ta\'i)',
        'jenis_pt': "Isim Mawshul (Lughah Thayyi')"
    },
    '2. Mawshul__10': {
        'arti_pt': 'O QUE / AQUELE QUE (ISIM FA\'IL/MAF\'UL)',
        'desc_pt': 'Aquele que / o que (Prefixo relativo antes de particípios Isim Fa\'il / Maf\'ul)',
        'jenis_pt': 'Al-Mawshulah'
    },

    # 3. Istifham
    '3. Istifham__1': {
        'arti_pt': 'ACASO / PORVENTURA?',
        'desc_pt': 'Acaso / porventura? (Partícula interrogativa / Hamzah Istifham)',
        'jenis_pt': 'Harf Istifham'
    },
    '3. Istifham__2': {
        'arti_pt': 'SERÁ QUE / ACASO?',
        'desc_pt': 'Será que / acaso? (Partícula interrogativa de confirmação)',
        'jenis_pt': 'Harf Istifham'
    },
    '3. Istifham__3': {
        'arti_pt': 'QUEM?',
        'desc_pt': 'Quem? (Pronome interrogativo para seres racionais)',
        'jenis_pt': "Isim Istifham ('Aqil)"
    },
    '3. Istifham__4': {
        'arti_pt': 'O QUE / QUE COISA?',
        'desc_pt': 'O que? / que coisa? (Pronome interrogativo para não racionais)',
        'jenis_pt': "Isim Istifham (Ghairu 'Aqil)"
    },
    '3. Istifham__5': {
        'arti_pt': 'QUANDO?',
        'desc_pt': 'Quando? (Advérbio interrogativo de tempo)',
        'jenis_pt': 'Isim Istifham (Zaman)'
    },
    '3. Istifham__6': {
        'arti_pt': 'QUANDO EXATAMENTE?',
        'desc_pt': 'Quando exatamente? (Interrogativo enfático de tempo futuro / Dia do Juízo)',
        'jenis_pt': 'Isim Istifham (Zaman Mustaqbal)'
    },
    '3. Istifham__7': {
        'arti_pt': 'ONDE?',
        'desc_pt': 'Onde? (Advérbio interrogativo de lugar)',
        'jenis_pt': 'Isim Istifham (Makan)'
    },
    '3. Istifham__8': {
        'arti_pt': 'COMO?',
        'desc_pt': 'Como? (Interrogativo de modo e estado / Hal)',
        'jenis_pt': 'Isim Istifham (Hal)'
    },
    '3. Istifham__9': {
        'arti_pt': 'DE ONDE / DE QUE MODO?',
        'desc_pt': 'De onde / como / de que modo? (Interrogativo polissêmico de origem ou modo)',
        'jenis_pt': 'Isim Istifham (Makan / Kaifiyah)'
    },
    '3. Istifham__10': {
        'arti_pt': 'QUANTO / QUANTOS?',
        'desc_pt': 'Quantos / quanto tempo? (Interrogativo de quantidade ou número)',
        'jenis_pt': "Isim Istifham ('Adad)"
    },

    # 4. Syarath
    '4. Syarath__1': {
        'arti_pt': 'SE / CASO',
        'desc_pt': 'Se / caso (Partícula condicional fundamental que coloca verbos em Jazm)',
        'jenis_pt': 'Harf Syarat Jazim'
    },
    '4. Syarath__2': {
        'arti_pt': 'QUANDO / SE',
        'desc_pt': 'Quando / logo que (Advérbio condicional temporal para eventos certos)',
        'jenis_pt': 'Dharf Zaman Li ma Yustaqbal'
    },
    '4. Syarath__3': {
        'arti_pt': 'SE AO MENOS / SE TIVESSE',
        'desc_pt': 'Se ao menos / se tivesse sido (Partícula condicional irrealizável / contrafactual)',
        'jenis_pt': "Harf Imtina' Li Imtina'"
    },
    '4. Syarath__4': {
        'arti_pt': 'SE NÃO FOSSE POR',
        'desc_pt': 'Se não fosse por / se não existisse (Partícula condicional de impedimento)',
        'jenis_pt': "Harf Imtina' Li Wujud"
    },
    '4. Syarath__5': {
        'arti_pt': 'QUANDO / ASSIM QUE',
        'desc_pt': 'Quando / assim que (Advérbio condicional temporal para o passado)',
        'jenis_pt': "Dharfiyyah Zaman Li ma Madha"
    },

    # 5. Isyarah
    '5. Isyarah__1': {
        'arti_pt': 'ESTE / ISTO (MASC PROX)',
        'desc_pt': 'Este / isto (Pronome demonstrativo proximal, singular masculino)',
        'jenis_pt': 'Isim Isyarah Qarib (Masc)'
    },
    '5. Isyarah__2': {
        'arti_pt': 'ESTA / ISTO (FEM PROX)',
        'desc_pt': 'Esta / isto (Pronome demonstrativo proximal, singular feminino / plural irracional)',
        'jenis_pt': 'Isim Isyarah Qarib (Fem)'
    },
    '5. Isyarah__3': {
        'arti_pt': 'ESTES / ESTAS (PROX)',
        'desc_pt': 'Estes / estas (Pronome demonstrativo proximal, plural masculino e feminino)',
        'jenis_pt': 'Isim Isyarah Qarib (Jamak)'
    },
    '5. Isyarah__4': {
        'arti_pt': 'AQUELE / AQUILO (DIST)',
        'desc_pt': 'Aquele / aquilo (Pronome demonstrativo distal, singular masculino)',
        'jenis_pt': "Isim Isyarah Ba'id (Masc)"
    },
    '5. Isyarah__5': {
        'arti_pt': 'AQUELA / AQUILO (DIST)',
        'desc_pt': 'Aquela / aquilo (Pronome demonstrativo distal, singular feminino / plural irracional)',
        'jenis_pt': "Isim Isyarah Ba'id (Fem)"
    },
    '5. Isyarah__6': {
        'arti_pt': 'AQUELES / AQUELAS (DIST)',
        'desc_pt': 'Aqueles / aquelas (Pronome demonstrativo distal, plural masculino e feminino)',
        'jenis_pt': "Isim Isyarah Ba'id (Jamak)"
    },
    '5. Isyarah__7': {
        'arti_pt': 'AQUI (LUGAR PROX)',
        'desc_pt': 'Aqui (Advérbio demonstrativo de lugar próximo)',
        'jenis_pt': 'Isim Isyarah Makan (Qarib)'
    },
    '5. Isyarah__8': {
        'arti_pt': 'LÁ / ALI (LUGAR DIST)',
        'desc_pt': 'Lá / ali / naquele momento (Advérbio demonstrativo de lugar distante ou tempo)',
        'jenis_pt': "Isim Isyarah Makan (Ba'id)"
    },

    # 6. Isim Fi'il
    "6. Isim Fi'il__1": {
        'arti_pt': 'QUÃO LONGE ESTÁ!',
        'desc_pt': 'Quão longe está! / Quão improvável! (Nome verbal no pretérito = Ba\'uda)',
        'jenis_pt': "Isim Fi'il Madhi (Makna Ba'uda)"
    },
    "6. Isim Fi'il__2": {
        'arti_pt': 'QUÃO DIFERENTES SÃO!',
        'desc_pt': 'Quão diferentes são! (Nome verbal no pretérito = Iftaraqa)',
        'jenis_pt': "Isim Fi'il Madhi (Makna Iftaraqa)"
    },
    "6. Isim Fi'il__3": {
        'arti_pt': 'UFA! / QUE NOJO / QUE DESDÉM!',
        'desc_pt': 'Ufa! / Que desgosto! (Nome verbal no presente que expressa incômodo = Atadhajjaru)',
        'jenis_pt': "Isim Fi'il Mudhari' (Makna Atadhajjar)"
    },
    "6. Isim Fi'il__4": {
        'arti_pt': 'OH! / QUÃO ADMIRÁVEL!',
        'desc_pt': 'Oh! / Quão admirável! (Nome verbal no presente que expressa espanto = A\'jabu)',
        'jenis_pt': "Isim Fi'il Mudhari' (Makna A'jab)"
    },
    "6. Isim Fi'il__5": {
        'arti_pt': 'ATENDE / ACEITA NOSSA SÚPLICA',
        'desc_pt': 'Atende à nossa prece / aceita (Nome verbal imperativo = Istajib)',
        'jenis_pt': "Isim Fi'il Amr (Makna Istajib)"
    },
    "6. Isim Fi'il__6": {
        'arti_pt': 'VEM CÁ / APROXIMA-TE',
        'desc_pt': 'Vem cá / aproxima-te / trazei (Nome verbal imperativo = Ta\'ala / Ahdir)',
        'jenis_pt': "Isim Fi'il Amr (Makna Ta'ala / Ahdir)"
    },
    "6. Isim Fi'il__7": {
        'arti_pt': 'TOMAI / AQUI TENDES!',
        'desc_pt': 'Tomai / lede aqui (Nome verbal imperativo = Khudzu / Iqra\'u)',
        'jenis_pt': "Isim Fi'il Amr (Makna Khudz)"
    },
    "6. Isim Fi'il__8": {
        'arti_pt': 'CUIDAI DE / INCUMBE-VOS',
        'desc_pt': 'Cuidai de vós mesmos / incumbe-vos (Nome verbal imperativo = Ilzamu)',
        'jenis_pt': "Isim Fi'il Amr (Makna Ilzam)"
    },

    # 7. Fi'il Jamid
    "7. Fi'il Jamid__1": {
        'arti_pt': 'NÃO É / NÃO ESTÁ',
        'desc_pt': 'Não é / não está (Verbo estático de negação dos irmãos de Kana)',
        'jenis_pt': 'Fi\'il Jamid Naqis (Nafi)'
    },
    "7. Fi'il Jamid__2": {
        'arti_pt': 'TALVEZ / É POSSÍVEL QUE',
        'desc_pt': 'Talvez / é de se esperar que (Verbo estático de esperança / Af\'al ar-Raja\')',
        'jenis_pt': 'Fi\'il Jamid Raja\''
    },
    "7. Fi'il Jamid__3": {
        'arti_pt': 'QUÃO EXCELENTE É!',
        'desc_pt': 'Quão excelente é! (Verbo estático de louvor / Af\'al al-Madh)',
        'jenis_pt': 'Fi\'il Jamid Madh (Elogio)'
    },
    "7. Fi'il Jamid__4": {
        'arti_pt': 'QUÃO MISERÁVEL É!',
        'desc_pt': 'Quão miserável é! (Verbo estático de censura / Af\'al adz-Dzamm)',
        'jenis_pt': 'Fi\'il Jamid Dzamm (Censura)'
    },
    "7. Fi'il Jamid__5": {
        'arti_pt': 'QUÃO PÉSSIMO É!',
        'desc_pt': 'Quão péssimo é! (Verbo estático de censura e repúdio)',
        'jenis_pt': 'Fi\'il Jamid Dzamm (Repúdio)'
    },
    "7. Fi'il Jamid__6": {
        'arti_pt': 'QUÃO BOM / EXCELENTE É!',
        'desc_pt': 'Quão excelente é! (Verbo composto de louvor com demonstrativo)',
        'jenis_pt': 'Fi\'il Jamid Madh Murakkab'
    },
    "7. Fi'il Jamid__7": {
        'arti_pt': 'BENDITO SEJA / SUPREMO',
        'desc_pt': 'Bendito seja / Pleno de bênçãos (Verbo exclusivo atribuído a Allah)',
        'jenis_pt': 'Fi\'il Jamid Li Allah Ta\'ala'
    },
    "7. Fi'il Jamid__8": {
        'arti_pt': 'CONSIDERA / SUPÕE',
        'desc_pt': 'Supõe / considera que (Verbo imperativo estático de suposição / Qulub)',
        'jenis_pt': 'Fi\'il Jamid Amr (Zhann)'
    }
}

def main():
    print("Enriching dhamir_data.json and dhamir_data.js with Portuguese...")
    
    with open(os.path.join(BASE_DIR, 'pt_translations.json'), 'r', encoding='utf-8') as f:
        pt_translations = json.load(f)

    with open(os.path.join(BASE_DIR, 'dhamir_data.json'), 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        b = item.get('Bentuk Kata', '')
        nk = item.get('No kata', '')
        g_key = f"{b}__{nk}"
        
        # 1. BentukKataPT
        item['BentukKataPT'] = BENTUK_KATA_PT.get(b, b)
        
        # 2. SuratArtiPT
        surat_num = str(item.get('SURAT', ''))
        item['SuratArtiPT'] = PORTUGUESE_SURAHS.get(surat_num, item.get('SuratArtiEN', ''))
        
        # 3. ArtiKataPT & Grammar PT
        g_info = PORTUGUESE_GRAMMAR.get(g_key, {})
        item['ArtiKataPT'] = g_info.get('arti_pt', item.get('ArtiKataEN', item.get('Arti kata', '')))
        
        if 'Grammar' not in item:
            item['Grammar'] = {}
        if g_info.get('desc_pt'):
            item['Grammar']['desc_pt'] = g_info['desc_pt']
        if g_info.get('jenis_pt'):
            item['Grammar']['jenis_pt'] = g_info['jenis_pt']
            
        # 4. TeksArtiPT
        v_key = f"{item.get('SURAT')}:{item.get('AYAT')}"
        teks_pt = pt_translations.get(v_key, item.get('TeksArtiEN', item.get('TeksArtiID', '')))
        item['TeksArtiPT'] = teks_pt

    # Write dhamir_data.json
    with open(os.path.join(BASE_DIR, 'dhamir_data.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Write dhamir_data.js
    js_content = f"/**\n * Dataset Dhamir & Isim Jamid Mabny Al-Qur'an Multibahasa (ID, EN, MS, FR, DE, UR, HI, BN, RU, ZH, ES, TR, PT)\n */\nconst DHAMIR_DATA = {json.dumps(data, ensure_ascii=False, indent=2)};\n"
    with open(os.path.join(BASE_DIR, 'dhamir_data.js'), 'w', encoding='utf-8') as f:
        f.write(js_content)

    print(f"Successfully enriched {len(data)} items in dhamir_data.json and dhamir_data.js with Portuguese!")

if __name__ == '__main__':
    main()
