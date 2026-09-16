import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

# 1. 114 Surahs Spanish Meanings
SPANISH_SURAHS = {
    "1": "La Apertura",
    "2": "La Vaca",
    "3": "La Familia de Imran",
    "4": "Las Mujeres",
    "5": "La Mesa Servida",
    "6": "Los Ganados",
    "7": "Los Lugares Elevados",
    "8": "Los Botines de Guerra",
    "9": "El Arrepentimiento",
    "10": "Jonás",
    "11": "Hud",
    "12": "José",
    "13": "El Trueno",
    "14": "Abraham",
    "15": "Al-Hiyr",
    "16": "Las Abejas",
    "17": "El Viaje Nocturno",
    "18": "La Caverna",
    "19": "María",
    "20": "Ta-Ha",
    "21": "Los Profetas",
    "22": "La Peregrinación",
    "23": "Los Creyentes",
    "24": "La Luz",
    "25": "El Criterio",
    "26": "Los Poetas",
    "27": "Las Hormigas",
    "28": "El Relato",
    "29": "La Araña",
    "30": "Los Bizantinos",
    "31": "Luqman",
    "32": "La Postración",
    "33": "Los Coligados",
    "34": "Saba",
    "35": "El Originador",
    "36": "Ya-Sin",
    "37": "Los Alineados en Filas",
    "38": "Sad",
    "39": "Los Grupos",
    "40": "El Perdonador",
    "41": "Los Versículos Detallados",
    "42": "La Consulta",
    "43": "Los Ornamentos de Oro",
    "44": "El Humo",
    "45": "La Arrodillada",
    "46": "Las Dunas",
    "47": "Muhammad",
    "48": "La Victoria",
    "49": "Las Habitaciones",
    "50": "Qaf",
    "51": "Los Vientos Dispersores",
    "52": "El Monte",
    "53": "La Estrella",
    "54": "La Luna",
    "55": "El Compasivo",
    "56": "El Acontecimiento",
    "57": "El Hierro",
    "58": "La Discusión",
    "59": "La Concentración",
    "60": "La Examinada",
    "61": "Las Filas",
    "62": "El Viernes",
    "63": "Los Hipócritas",
    "64": "El Desengaño Mutuo",
    "65": "El Divorcio",
    "66": "La Prohibición",
    "67": "El Dominio",
    "68": "El Cálamo",
    "69": "La Inevitable",
    "70": "Las Vías de Ascensión",
    "71": "Noé",
    "72": "Los Genios",
    "73": "El Envuelto",
    "74": "El Arropado",
    "75": "La Resurrección",
    "76": "El Hombre",
    "77": "Los Enviados",
    "78": "La Noticia",
    "79": "Los Ángeles que Arrancan",
    "80": "Frunció el Ceño",
    "81": "El Oscurecimiento",
    "82": "La Hendidura",
    "83": "Los Defraudadores",
    "84": "El Resquebrajamiento",
    "85": "Las Grandes Constelaciones",
    "86": "El Astro Nocturno",
    "87": "El Altísimo",
    "88": "La Envolvente",
    "89": "El Alba",
    "90": "La Ciudad",
    "91": "El Sol",
    "92": "La Noche",
    "93": "La Mañana Luminosa",
    "94": "La Apertura del Pecho",
    "95": "La Higuera",
    "96": "El Coágulo",
    "97": "El Destino",
    "98": "La Evidencia Clara",
    "99": "El Terremoto",
    "100": "Los Corceles",
    "101": "La Calamidad",
    "102": "El Afán de Lucro",
    "103": "El Tiempo",
    "104": "El Difamador",
    "105": "El Elefante",
    "106": "Quraish",
    "107": "La Ayuda Mínima",
    "108": "La Abundancia",
    "109": "Los Incrédulos",
    "110": "El Auxilio",
    "111": "Las Fibras de Palmera",
    "112": "La Unicidad Divina",
    "113": "El Amanecer",
    "114": "La Humanidad"
}

# 2. 7 Categories in Spanish
BENTUK_KATA_ES = {
    '1. Dhamir': '1. Pronombres (Dhamir)',
    '2. Mawshul': '2. Pronombres Relativos (Mawshul)',
    '3. Istifham': '3. Interrogativos (Istifham)',
    '4. Syarath': '4. Condicionales (Syarath)',
    '5. Isyarah': '5. Demostrativos (Isyarah)',
    "6. Isim Fi'il": "6. Nombres Verbales (Isim Fi'il)",
    "7. Fi'il Jamid": "7. Verbos Inflexibles (Fi'il Jamid)"
}

# 3. 76 Grammatical Metadata in Spanish
SPANISH_GRAMMAR = {
    '1. Dhamir__1a': {
        'arti_es': 'ÉL',
        'desc_es': 'Él (3ra persona singular masculino, pronombre independiente)',
        'jenis_es': 'Munfashil (Independiente)'
    },
    '1. Dhamir__1b': {
        'arti_es': '..SU / ..LE / ..LO',
        'desc_es': '...-su / le / lo (3ra persona singular masculino, pronombre sufijo/unido)',
        'jenis_es': 'Muttashil (Sufijo / Unido)'
    },
    '1. Dhamir__1c': {
        'arti_es': 'SÓLO A ÉL',
        'desc_es': 'Sólo a Él / a él solo (Pronombre objeto independiente, 3ra pers. masc.)',
        'jenis_es': 'Munfashil Manshub (Objeto Acusativo)'
    },
    '1. Dhamir__2a': {
        'arti_es': 'ELLOS DOS / ELLAS DOS',
        'desc_es': 'Ellos dos / Ellas dos (3ra persona dual, pronombre independiente)',
        'jenis_es': 'Munfashil (Independiente)'
    },
    '1. Dhamir__2b': {
        'arti_es': '..DE AMBOS / ..LES (DUAL)',
        'desc_es': '...-de ellos dos / les (3ra persona dual, pronombre sufijo/unido)',
        'jenis_es': 'Muttashil (Sufijo / Unido)'
    },
    '1. Dhamir__3a': {
        'arti_es': 'ELLOS',
        'desc_es': 'Ellos (3ra persona plural masculino, pronombre independiente)',
        'jenis_es': 'Munfashil (Independiente)'
    },
    '1. Dhamir__3b': {
        'arti_es': '..SU / ..LES / ..LOS',
        'desc_es': '...-su / sus / les / los (3ra persona plural masculino, pronombre sufijo/unido)',
        'jenis_es': 'Muttashil (Sufijo / Unido)'
    },
    '1. Dhamir__3c': {
        'arti_es': 'SÓLO A ELLOS',
        'desc_es': 'Sólo a ellos (Pronombre objeto independiente, 3ra pers. plur. masc.)',
        'jenis_es': 'Munfashil Manshub (Objeto Acusativo)'
    },
    '1. Dhamir__4a': {
        'arti_es': 'ELLA',
        'desc_es': 'Ella (3ra persona singular femenino, pronombre independiente)',
        'jenis_es': 'Munfashil (Independiente)'
    },
    '1. Dhamir__4b': {
        'arti_es': '..SU / ..LA / ..LE (FEM)',
        'desc_es': '...-su / la / le (3ra persona singular femenino, pronombre sufijo/unido)',
        'jenis_es': 'Muttashil (Sufijo / Unido)'
    },
    '1. Dhamir__5a': {
        'arti_es': 'ELLAS',
        'desc_es': 'Ellas (3ra persona plural femenino, pronombre independiente)',
        'jenis_es': 'Munfashil (Independiente)'
    },
    '1. Dhamir__5b': {
        'arti_es': '..SU / ..LES / ..LAS (FEM)',
        'desc_es': '...-su / sus / les / las (3ra persona plural femenino, pronombre sufijo/unido)',
        'jenis_es': 'Muttashil (Sufijo / Unido)'
    },
    '1. Dhamir__6a': {
        'arti_es': 'TÚ / USTED (MASC)',
        'desc_es': 'Tú / Usted (2da persona singular masculino, pronombre independiente)',
        'jenis_es': 'Munfashil (Independiente)'
    },
    '1. Dhamir__6b': {
        'arti_es': '..TU / ..TE / ..TI (MASC)',
        'desc_es': '...-tu / te / ti (2da persona singular masculino, pronombre sufijo/unido)',
        'jenis_es': 'Muttashil (Sufijo / Unido)'
    },
    '1. Dhamir__6c': {
        'arti_es': 'SÓLO A TI',
        'desc_es': 'Sólo a Ti / a ti solo (Pronombre objeto independiente, 2da pers. masc.)',
        'jenis_es': 'Munfashil Manshub (Objeto Acusativo)'
    },
    '1. Dhamir__7a': {
        'arti_es': 'VOSOTROS DOS / USTEDES DOS',
        'desc_es': 'Vosotros dos / Ustedes dos (2da persona dual, pronombre independiente)',
        'jenis_es': 'Munfashil (Independiente)'
    },
    '1. Dhamir__7b': {
        'arti_es': '..VUESTRO / ..DE USTEDES (DUAL)',
        'desc_es': '...-vuestro / de ustedes dos (2da persona dual, pronombre sufijo/unido)',
        'jenis_es': 'Muttashil (Sufijo / Unido)'
    },
    '1. Dhamir__8a': {
        'arti_es': 'VOSOTROS / USTEDES',
        'desc_es': 'Vosotros / Ustedes (2da persona plural masculino, pronombre independiente)',
        'jenis_es': 'Munfashil (Independiente)'
    },
    '1. Dhamir__8b': {
        'arti_es': '..VUESTRO / ..DE USTEDES / ..OS',
        'desc_es': '...-vuestro / vuestros / os / les (2da persona plural masc., pronombre sufijo/unido)',
        'jenis_es': 'Muttashil (Sufijo / Unido)'
    },
    '1. Dhamir__8c': {
        'arti_es': 'SÓLO A VOSOTROS / A USTEDES',
        'desc_es': 'Sólo a vosotros / a ustedes solos (Pronombre objeto independiente, 2da pers. plur. masc.)',
        'jenis_es': 'Munfashil Manshub (Objeto Acusativo)'
    },
    '1. Dhamir__9b': {
        'arti_es': '..TU / ..TE (FEM)',
        'desc_es': '...-tu / te (2da persona singular femenino, pronombre sufijo/unido)',
        'jenis_es': 'Muttashil (Sufijo / Unido)'
    },
    '1. Dhamir__11a': {
        'arti_es': 'YO',
        'desc_es': 'Yo (1ra persona singular, pronombre independiente)',
        'jenis_es': 'Munfashil (Independiente)'
    },
    '1. Dhamir__11b': {
        'arti_es': '..MI / ..ME / ..MÍ',
        'desc_es': '...-mi / mis / me / mí (1ra persona singular, pronombre sufijo/unido)',
        'jenis_es': 'Muttashil (Sufijo / Unido)'
    },
    '1. Dhamir__11c': {
        'arti_es': 'SÓLO A MÍ',
        'desc_es': 'Sólo a Mí / a mí solo (Pronombre objeto independiente, 1ra pers. sing.)',
        'jenis_es': 'Munfashil Manshub (Objeto Acusativo)'
    },
    '1. Dhamir__12a': {
        'arti_es': 'NOSOTROS',
        'desc_es': 'Nosotros / Nosotras (1ra persona plural, pronombre independiente)',
        'jenis_es': 'Munfashil (Independiente)'
    },
    '1. Dhamir__12b': {
        'arti_es': '..NUESTRO / ..NOS',
        'desc_es': '...-nuestro / nuestros / nos (1ra persona plural, pronombre sufijo/unido)',
        'jenis_es': 'Muttashil (Sufijo / Unido)'
    },
    '1. Dhamir__12c': {
        'arti_es': 'SÓLO A NOSOTROS',
        'desc_es': 'Sólo a nosotros (Pronombre objeto independiente, 1ra pers. plur.)',
        'jenis_es': 'Munfashil Manshub (Objeto Acusativo)'
    },
    '2. Mawshul__1': {
        'arti_es': 'LO QUE / LO CUAL / AQUELLO QUE',
        'desc_es': 'Lo que / Lo cual (Pronombre relativo común para seres no racionales / inanimados)',
        'jenis_es': 'Mawshul Mushtarak (Relativo Común)'
    },
    '2. Mawshul__2': {
        'arti_es': 'AQUELLOS QUE / QUIENES',
        'desc_es': 'Aquellos que / Quienes (Pronombre relativo plural masculino)',
        'jenis_es': 'Mawshul Jas (Relativo Específico)'
    },
    '2. Mawshul__3': {
        'arti_es': 'QUIEN / EL QUE / QUIENQUIERA',
        'desc_es': 'Quien / Quienquiera que (Pronombre relativo para seres racionales/personas)',
        'jenis_es': 'Mawshul Mushtarak (Relativo Común)'
    },
    '2. Mawshul__4': {
        'arti_es': 'EL QUE / AQUEL QUE / EL CUAL',
        'desc_es': 'Aquel que / El que / Quien (Pronombre relativo singular masculino)',
        'jenis_es': 'Mawshul Jas (Relativo Específico)'
    },
    '2. Mawshul__5': {
        'arti_es': 'CUALQUIERA DE / QUIENQUIERA',
        'desc_es': 'Cualquiera de ellos / Quienquiera (Pronombre relativo declinable)',
        'jenis_es': 'Mawshul Mubham (Relativo Indeterminado)'
    },
    '2. Mawshul__6': {
        'arti_es': 'LA QUE / AQUELLA QUE',
        'desc_es': 'La que / Aquella que (Pronombre relativo singular femenino)',
        'jenis_es': 'Mawshul Jas (Relativo Específico)'
    },
    '2. Mawshul__7': {
        'arti_es': 'AQUELLAS MUJERES QUE',
        'desc_es': 'Aquellas que / Aquellas mujeres que (Pronombre relativo plural femenino)',
        'jenis_es': 'Mawshul Jas (Relativo Específico)'
    },
    '2. Mawshul__8': {
        'arti_es': 'AQUELLAS QUE (FEM PLUR)',
        'desc_es': 'Aquellas que / Aquellas mujeres que (Pronombre relativo plural femenino)',
        'jenis_es': 'Mawshul Jas (Relativo Específico)'
    },
    '2. Mawshul__9': {
        'arti_es': 'LOS DOS QUE / AMBOS QUE',
        'desc_es': 'Los dos que / Ambos hombres que (Pronombre relativo dual masculino)',
        'jenis_es': 'Mawshul Jas (Relativo Específico)'
    },
    '2. Mawshul__10': {
        'arti_es': 'CUALQUIERA DE (FEM)',
        'desc_es': 'Cualquiera de ellas (Forma femenina de relativo declinable)',
        'jenis_es': 'Mawshul Mubham (Relativo Indeterminado)'
    },
    '3. Istifham__1': {
        'arti_es': '¿QUÉ? / ¿QUÉ ES?',
        'desc_es': '¿Qué? / ¿Qué es aquello? (Interrogativo para cosas y asuntos inanimados)',
        'jenis_es': 'Ism Istifham (Nombre Interrogativo)'
    },
    '3. Istifham__2': {
        'arti_es': '¿CÓMO?',
        'desc_es': '¿Cómo? (Interrogativo sobre el estado, modo o condición)',
        'jenis_es': 'Ism Istifham (Nombre Interrogativo)'
    },
    '3. Istifham__3': {
        'arti_es': '¿QUIÉN?',
        'desc_es': '¿Quién? (Interrogativo para personas y seres dotados de razón)',
        'jenis_es': 'Ism Istifham (Nombre Interrogativo)'
    },
    '3. Istifham__4': {
        'arti_es': '¿CUÁL? / ¿QUIÉN DE?',
        'desc_es': '¿Cuál? / ¿Cuál de ellos? (Interrogativo declinable)',
        'jenis_es': 'Ism Istifham (Nombre Interrogativo)'
    },
    '3. Istifham__5': {
        'arti_es': '¿CÓMO? / ¿DE DÓNDE? / ¿CUÁNDO?',
        'desc_es': '¿Cómo? / ¿De dónde? / ¿Cuándo? (Interrogativo de modo, origen o tiempo)',
        'jenis_es': 'Ism Istifham (Nombre Interrogativo)'
    },
    '3. Istifham__6': {
        'arti_es': '¿QUÉ ES LO QUE?',
        'desc_es': '¿Qué es lo que...? (Interrogativo compuesto Mā + Dzā)',
        'jenis_es': 'Ism Istifham (Nombre Interrogativo)'
    },
    '3. Istifham__7': {
        'arti_es': '¿CUÁNTOS? / ¿CUÁNTO TIEMPO?',
        'desc_es': '¿Cuántos? / ¿Cuánto tiempo? (Interrogativo de cantidad o duración)',
        'jenis_es': 'Ism Istifham (Nombre Interrogativo)'
    },
    '3. Istifham__8': {
        'arti_es': '¿POR QUÉ? / ¿POR CUÁL RAZÓN?',
        'desc_es': '¿Por qué? / ¿Con qué motivo? (Li + Ma)',
        'jenis_es': 'Ism Istifham (Nombre Interrogativo)'
    },
    '3. Istifham__9': {
        'arti_es': '¿DÓNDE? / ¿ADÓNDE?',
        'desc_es': '¿Dónde? / ¿Hacia dónde? (Interrogativo de lugar)',
        'jenis_es': 'Ism Istifham (Nombre Interrogativo)'
    },
    '3. Istifham__10': {
        'arti_es': '¿CUÁNDO?',
        'desc_es': '¿Cuándo? (Interrogativo de tiempo)',
        'jenis_es': 'Ism Istifham (Nombre Interrogativo)'
    },
    '4. Syarath__1': {
        'arti_es': 'QUIENQUIERA QUE / AQUEL QUE',
        'desc_es': 'Quienquiera que / El que (Condicional apocopante para personas)',
        'jenis_es': 'Ism Syarath Yazim (Condicional Apocopante)'
    },
    '4. Syarath__2': {
        'arti_es': 'CUALQUIER COSA QUE / LO QUE SEA QUE',
        'desc_es': 'Cualquier cosa que / Todo lo que (Condicional apocopante para cosas)',
        'jenis_es': 'Ism Syarath Yazim (Condicional Apocopante)'
    },
    '4. Syarath__3': {
        'arti_es': 'CADA VEZ QUE / SIEMPRE QUE',
        'desc_es': 'Cada vez que / Siempre que (Condicional temporal de reiteración no apocopante)',
        'jenis_es': 'Ism Syarath Ghayr Yazim (No Apocopante)'
    },
    '4. Syarath__4': {
        'arti_es': 'CUALQUIERA QUE / SEA CUAL FUERE',
        'desc_es': 'Cualquiera que / Sea cual fuere (Condicional declinable)',
        'jenis_es': 'Ism Syarath Yazim (Condicional Apocopante)'
    },
    '4. Syarath__5': {
        'arti_es': 'SEA CUAL SEA (CON ÉNFASIS)',
        'desc_es': 'Sea cual fuere (Condicional con partícula enfática Mā Zaidah)',
        'jenis_es': 'Ism Syarath Yazim (Condicional Apocopante)'
    },
    '5. Isyarah__1': {
        'arti_es': 'ESTE / ESE / AQUEL (MASC)',
        'desc_es': 'Este / Aquel (Demostrativo singular masculino)',
        'jenis_es': 'Ism Isyarah (Demostrativo)'
    },
    '5. Isyarah__2': {
        'arti_es': 'ESTOS / AQUELLOS',
        'desc_es': 'Estos / Aquellos / Esos (Demostrativo plural)',
        'jenis_es': 'Ism Isyarah (Demostrativo)'
    },
    '5. Isyarah__3': {
        'arti_es': 'ESTA / ESA / AQUELLA (FEM)',
        'desc_es': 'Esta / Aquella (Demostrativo singular femenino)',
        'jenis_es': 'Ism Isyarah (Demostrativo)'
    },
    '5. Isyarah__4': {
        'arti_es': 'AQUELLA / AQUELLAS (FEM/PLUR)',
        'desc_es': 'Aquella / Aquellas (Demostrativo lejano femenino / plural inanimado)',
        'jenis_es': 'Ism Isyarah (Demostrativo)'
    },
    '5. Isyarah__5': {
        'arti_es': 'AQUÍ / ACÁ',
        'desc_es': 'Aquí / En este lugar (Demostrativo de lugar cercano)',
        'jenis_es': 'Ism Isyarah Makan (Lugar Cercano)'
    },
    '5. Isyarah__6': {
        'arti_es': 'ALLÍ / ALLÁ',
        'desc_es': 'Allí / Allá (Demostrativo de lugar lejano)',
        'jenis_es': 'Ism Isyarah Makan (Lugar Lejano)'
    },
    '5. Isyarah__7': {
        'arti_es': 'ESTOS DOS (MASC DUAL)',
        'desc_es': 'Estos dos hombres (Demostrativo dual masculino declinable)',
        'jenis_es': 'Ism Isyarah (Demostrativo)'
    },
    '5. Isyarah__8': {
        'arti_es': 'ESTAS DOS (FEM DUAL)',
        'desc_es': 'Estas dos mujeres (Demostrativo dual femenino declinable)',
        'jenis_es': 'Ism Isyarah (Demostrativo)'
    },
    '6. Isim Fi\'il__1': {
        'arti_es': '¡GLORIFICADO Y ALABADO SEA ALLAH!',
        'desc_es': '¡Glorificado sea Allah! (Nombre verbal/Masdar que expresa purificación y alabanza a Dios)',
        'jenis_es': 'Ism Fi\'il / Masdar (Nombre Verbal)'
    },
    '6. Isim Fi\'il__2': {
        'arti_es': '¡PRESENTAD! / ¡TRAED!',
        'desc_es': '¡Presentad / Traed vuestras pruebas! (Nombre verbal imperativo)',
        'jenis_es': 'Ism Fi\'il Amr (Imperativo)'
    },
    '6. Isim Fi\'il__3': {
        'arti_es': '¡UF! (EXPRESIÓN DE RECHAZO)',
        'desc_es': '¡Uf! / Expresión de disgusto y hastío (Nombre verbal en presente)',
        'jenis_es': 'Ism Fi\'il Mudhari\' (Presente)'
    },
    '6. Isim Fi\'il__4': {
        'arti_es': '¡ME REFUGIO EN ALLAH!',
        'desc_es': '¡Me refugio en Allah! (Ma\'ādzallāh, nombre verbal de protección)',
        'jenis_es': 'Ism Fi\'il / Masdar (Nombre Verbal)'
    },
    '6. Isim Fi\'il__5': {
        'arti_es': '¡ACERCAOS! / ¡VENID ACÁ!',
        'desc_es': '¡Venid acá / Acercaos! (Nombre verbal imperativo)',
        'jenis_es': 'Ism Fi\'il Amr (Imperativo)'
    },
    '6. Isim Fi\'il__6': {
        'arti_es': '¡QUÉ LEJOS ESTÁ! / ¡IMPOSIBLE!',
        'desc_es': '¡Qué lejano está / Es totalmente imposible! (Nombre verbal en pasado)',
        'jenis_es': 'Ism Fi\'il Madhi (Pasado)'
    },
    '6. Isim Fi\'il__7': {
        'arti_es': '¡TOMAD Y LEED ESTO!',
        'desc_es': '¡Tomad y leed esto! (Nombre verbal imperativo)',
        'jenis_es': 'Ism Fi\'il Amr (Imperativo)'
    },
    '6. Isim Fi\'il__8': {
        'arti_es': '¡VEN ACÁ! / ¡ESTOY LISTA!',
        'desc_es': '¡Ven acá / Date prisa! (Nombre verbal imperativo)',
        'jenis_es': 'Ism Fi\'il Amr (Imperativo)'
    },
    '7. Fi\'il Jamid__1': {
        'arti_es': 'NO ES / NO HAY',
        'desc_es': 'No es / No existe (Verbo inflexible de negación)',
        'jenis_es': 'Fi\'il Madhi Yamid (Verbo Inflexible)'
    },
    '7. Fi\'il Jamid__2': {
        'arti_es': '¡QUÉ PÉSIMO! / ¡QUÉ DETESTABLE!',
        'desc_es': '¡Qué pésimo / Qué ruin! (Verbo inflexible de reprobación / Adz-Dzamm)',
        'jenis_es': 'Fi\'il Madhi Yamid (Verbo Inflexible)'
    },
    '7. Fi\'il Jamid__3': {
        'arti_es': 'QUIZÁS / PUEDE SER QUE',
        'desc_es': 'Quizás / Puede que (Verbo inflexible de esperanza / Tarayyi)',
        'jenis_es': 'Fi\'il Madhi Yamid (Verbo Inflexible)'
    },
    '7. Fi\'il Jamid__4': {
        'arti_es': '¡QUÉ EXCELENTE! / ¡QUÉ BUENO!',
        'desc_es': '¡Qué excelente / El mejor! (Verbo inflexible de alabanza / Al-Madh)',
        'jenis_es': 'Fi\'il Madhi Yamid (Verbo Inflexible)'
    },
    '7. Fi\'il Jamid__5': {
        'arti_es': '¡QUÉ PÉSIMO ES LO QUE!',
        'desc_es': '¡Qué pésimo es aquello que...! (Verbo compuesto de censura Bi\'sa + Ma)',
        'jenis_es': 'Fi\'il Madhi Yamid (Verbo Inflexible)'
    },
    '7. Fi\'il Jamid__6': {
        'arti_es': 'COMENZARON A / SE PUSIERON A',
        'desc_es': 'Comenzaron a / Se pusieron a hacer (Verbo de incoación / Af\'al Ash-Shuru\')',
        'jenis_es': 'Fi\'il Madhi Yamid (Verbo Inflexible)'
    },
    '7. Fi\'il Jamid__7': {
        'arti_es': '¡LEJOS ESTÉ ALLAH DE TODA IMPERFECCIÓN!',
        'desc_es': '¡Dios no lo permita / Purificado sea Allah de toda falta! (Tanziih)',
        'jenis_es': 'Fi\'il Yamid (Verbo Inflexible)'
    },
    '7. Fi\'il Jamid__8': {
        'arti_es': '¡QUÉ EXCELENTE ES LO QUE!',
        'desc_es': '¡Qué excelente es aquello que...! (Verbo compuesto de elogio Ni\'ma + Ma)',
        'jenis_es': 'Fi\'il Madhi Yamid (Verbo Inflexible)'
    }
}
