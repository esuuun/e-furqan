#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script to build Korean (ko) dataset and enrich dhamir_data.json, dhamir_data.js,
harf_data.json, and harf_data.js with complete Korean translations and grammatical terms.
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

# 1. 114 Surahs Korean Names & Meanings (Hamid Choi / 최영길 박사)
KOREAN_SURAHS = {
    "1": "개경장 (개막 / 알 파티하)",
    "2": "암소장 (알 바카라)",
    "3": "임란가족장 (아알 이므란)",
    "4": "여성장 (안 니사)",
    "5": "식탁장 (알 마이다)",
    "6": "가축장 (알 안암)",
    "7": "고벽장 (알 아라프)",
    "8": "전리품장 (알 안팔)",
    "9": "회개장 (앗 타우바)",
    "10": "유누스장 (요나)",
    "11": "후드장 (후드)",
    "12": "유수프장 (요셉)",
    "13": "천둥장 (알 라드)",
    "14": "아브라함장 (이브라힘)",
    "15": "알 히즈르장 (암석지대)",
    "16": "꿀벌장 (안 나흘)",
    "17": "밤의 여행장 (이슬라 / 야행)",
    "18": "동굴장 (알 카흐프)",
    "19": "마리아장 (마리암)",
    "20": "따하장 (타하)",
    "21": "예언자장 (알 안비야)",
    "22": "순례장 (알 핫즈)",
    "23": "신도장 (알 무미눈)",
    "24": "빛의 장 (안 누르)",
    "25": "식별장 (알 푸르칸)",
    "26": "시인장 (아쉬 슈아라)",
    "27": "개미장 (안 나믈)",
    "28": "이야기장 (알 카사스)",
    "29": "거미장 (알 안카부트)",
    "30": "로마장 (알 룸)",
    "31": "루끄만장 (현자 루크만)",
    "32": "엎드림장 (아스 사즈다)",
    "33": "부족연합장 (알 아흐잡)",
    "34": "사바장 (사바)",
    "35": "창조자장 (파티르)",
    "36": "야씬장 (야신)",
    "37": "정렬장 (앗 사파트)",
    "38": "사드장 (사드)",
    "39": "군중장 (아즈 주마르)",
    "40": "용서자장 (가피르 / 무민)",
    "41": "명시된 장 (푸실랏)",
    "42": "상의장 (아쉬 슈라)",
    "43": "화려한 장식장 (아즈 주흐루프)",
    "44": "연기장 (앗 두한)",
    "45": "무릎꿇음장 (알 자시야)",
    "46": "모래언덕장 (알 아흐카프)",
    "47": "무함마드장 (예언자 무함마드)",
    "48": "승리장 (알 파트흐)",
    "49": "방장 (알 후주랏)",
    "50": "까프장 (카프)",
    "51": "바람장 (아즈 자리야트)",
    "52": "산장 (앳 투르)",
    "53": "별장 (안 나즘)",
    "54": "달장 (알 카마르)",
    "55": "자비로우신 분장 (알 라흐만)",
    "56": "사건장 (알 와키아 / 부활의 사건)",
    "57": "쇠장 (알 하디드)",
    "58": "변론하는 여인장 (알 무자딜라)",
    "59": "집결장 (알 하슈르)",
    "60": "시험받는 여인장 (알 뭄타하나)",
    "61": "대열장 (앗 사프)",
    "62": "금요예배장 (알 주무아)",
    "63": "위선자장 (알 무나피쿤)",
    "64": "손실장 (앗 타가분)",
    "65": "이혼장 (앗 탈라크)",
    "66": "금지장 (앗 타흐림)",
    "67": "주권장 (알 물크)",
    "68": "펜장 (알 칼람)",
    "69": "진실장 (알 하까)",
    "70": "계단장 (알 마아리즈)",
    "71": "노아장 (누흐)",
    "72": "정령장 (알 진)",
    "73": "감싸인 자장 (알 무잠밀)",
    "74": "겉옷을 입은 자장 (알 뭇다시르)",
    "75": "부활장 (알 키야마)",
    "76": "인간장 (알 인산)",
    "77": "보내진 것들장 (알 무르살라트)",
    "78": "소식장 (안 나바)",
    "79": "뽑아내는 자들장 (안 나지아트)",
    "80": "얼굴을 찌푸림장 (아바사)",
    "81": "감싸임장 (앗 타크위르)",
    "82": "갈라짐장 (알 인피타르)",
    "83": "속이는 자들장 (알 무타피핀)",
    "84": "쪼개짐장 (알 인시카크)",
    "85": "별자리장 (알 부루즈)",
    "86": "밤의 별장 (앗 타리크)",
    "87": "지고자장 (알 알아)",
    "88": "압도하는 사건장 (알 가시야)",
    "89": "새벽장 (알 파즈르)",
    "90": "도시장 (알 발라드)",
    "91": "태양장 (아쉬 샴스)",
    "92": "밤장 (알 라이일)",
    "93": "아침 햇살장 (앗 두하)",
    "94": "가슴의 열림장 (아쉬 샤르흐)",
    "95": "무화과장 (앗 틴)",
    "96": "응혈장 (알 알라크)",
    "97": "권능의 밤장 (알 카드르)",
    "98": "명증장 (알 바이나)",
    "99": "지진장 (아즈 잘잘라)",
    "100": "질주하는 말장 (알 아디야트)",
    "101": "두드리는 소리장 (알 카리아)",
    "102": "축적경쟁장 (앗 타카수르)",
    "103": "시간장 (알 아스르)",
    "104": "비방자장 (알 후마자)",
    "105": "코끼리장 (알 필)",
    "106": "꾸라이쉬장 (쿠라이시)",
    "107": "필수구호품장 (알 마운)",
    "108": "풍요장 (알 카우사르)",
    "109": "불신자들장 (알 카피룬)",
    "110": "구원장 (안 나스르)",
    "111": "야자섬유장 (알 마사드 / 불꽃)",
    "112": "순수신앙장 (알 이클라스 / 유일신)",
    "113": "새벽빛장 (알 팔라크)",
    "114": "인간들장 (안 나스)"
}

# 2. 7 Categories (Bentuk Kata) in Korean
BENTUK_KATA_KO = {
    '1. Dhamir': '1. 대명사 (Dhamir - Pronouns)',
    '2. Mawshul': '2. 관계대명사 (Mawshul - Relative Pronouns)',
    '3. Istifham': '3. 의문사 (Istifham - Interrogatives)',
    '4. Syarath': '4. 조건사 (Syarath - Conditionals)',
    '5. Isyarah': '5. 지시대명사 (Isyarah - Demonstratives)',
    "6. Isim Fi'il": "6. 동사성 명사 (Isim Fi'il - Verbal Nouns)",
    "7. Fi'il Jamid": "7. 불변동사 (Fi'il Jamid - Inflexible Verbs)"
}

# 3. 76 Jamid Mabny Grammatical Metadata in Korean
KOREAN_GRAMMAR = {
    "1. Dhamir__1a": {
        "arti_ko": "그 (남성 단수)",
        "desc_ko": "그 (3인칭 남성 단수 주격 분리대명사)",
        "jenis_ko": "주격 분리대명사"
    },
    "1. Dhamir__1b": {
        "arti_ko": "그의 / 그를",
        "desc_ko": "그의 / 그를 (3인칭 남성 단수 접미대명사)",
        "jenis_ko": "접미대명사"
    },
    "1. Dhamir__1c": {
        "arti_ko": "오직 그분만을",
        "desc_ko": "오직 그를 (3인칭 남성 단수 목적격 분리대명사)",
        "jenis_ko": "목적격 분리대명사"
    },
    "1. Dhamir__2a": {
        "arti_ko": "그들 두 사람",
        "desc_ko": "그들 두 사람 (3인칭 쌍수 주격 분리대명사)",
        "jenis_ko": "주격 분리대명사 (쌍수)"
    },
    "1. Dhamir__2b": {
        "arti_ko": "그들 두 사람의 / 두 사람을",
        "desc_ko": "그들 둘의 / 둘을 (3인칭 쌍수 접미대명사)",
        "jenis_ko": "접미대명사 (쌍수)"
    },
    "1. Dhamir__3a": {
        "arti_ko": "그들 (남성 복수)",
        "desc_ko": "그들 (3인칭 남성 복수 주격 분리대명사)",
        "jenis_ko": "주격 분리대명사 (남성 복수)"
    },
    "1. Dhamir__3b": {
        "arti_ko": "그들의 / 그들을",
        "desc_ko": "그들의 / 그들을 (3인칭 남성 복수 접미대명사)",
        "jenis_ko": "접미대명사 (남성 복수)"
    },
    "1. Dhamir__3c": {
        "arti_ko": "오직 그들만을",
        "desc_ko": "오직 그들을 (3인칭 남성 복수 목적격 분리대명사)",
        "jenis_ko": "목적격 분리대명사 (남성 복수)"
    },
    "1. Dhamir__4a": {
        "arti_ko": "그녀 (여성 단수)",
        "desc_ko": "그녀 (3인칭 여성 단수 주격 분리대명사)",
        "jenis_ko": "주격 분리대명사 (여성 단수)"
    },
    "1. Dhamir__4b": {
        "arti_ko": "그녀의 / 그녀를",
        "desc_ko": "그녀의 / 그녀를 (3인칭 여성 단수 접미대명사)",
        "jenis_ko": "접미대명사 (여성 단수)"
    },
    "1. Dhamir__5a": {
        "arti_ko": "그녀들 (여성 복수)",
        "desc_ko": "그녀들 (3인칭 여성 복수 주격 분리대명사)",
        "jenis_ko": "주격 분리대명사 (여성 복수)"
    },
    "1. Dhamir__5b": {
        "arti_ko": "그녀들의 / 그녀들을",
        "desc_ko": "그녀들의 / 그녀들을 (3인칭 여성 복수 접미대명사)",
        "jenis_ko": "접미대명사 (여성 복수)"
    },
    "1. Dhamir__6a": {
        "arti_ko": "당신 / 너 (남성 단수)",
        "desc_ko": "너 (2인칭 남성 단수 주격 분리대명사)",
        "jenis_ko": "주격 분리대명사 (남성 단수)"
    },
    "1. Dhamir__6b": {
        "arti_ko": "당신의 / 너를",
        "desc_ko": "너의 / 너를 (2인칭 남성 단수 접미대명사)",
        "jenis_ko": "접미대명사 (남성 단수)"
    },
    "1. Dhamir__6c": {
        "arti_ko": "오직 당신만을",
        "desc_ko": "오직 너를 (2인칭 남성 단수 목적격 분리대명사)",
        "jenis_ko": "목적격 분리대명사 (남성 단수)"
    },
    "1. Dhamir__7a": {
        "arti_ko": "당신들 두 사람",
        "desc_ko": "너희 둘 (2인칭 쌍수 주격 분리대명사)",
        "jenis_ko": "주격 분리대명사 (쌍수)"
    },
    "1. Dhamir__7b": {
        "arti_ko": "당신들 두 사람의",
        "desc_ko": "너희 둘의 / 둘을 (2인칭 쌍수 접미대명사)",
        "jenis_ko": "접미대명사 (쌍수)"
    },
    "1. Dhamir__8a": {
        "arti_ko": "당신들 / 너희들 (남성 복수)",
        "desc_ko": "너희들 (2인칭 남성 복수 주격 분리대명사)",
        "jenis_ko": "주격 분리대명사 (남성 복수)"
    },
    "1. Dhamir__8b": {
        "arti_ko": "당신들의 / 너희들을",
        "desc_ko": "너희들의 / 너희들을 (2인칭 남성 복수 접미대명사)",
        "jenis_ko": "접미대명사 (남성 복수)"
    },
    "1. Dhamir__8c": {
        "arti_ko": "오직 당신들만을",
        "desc_ko": "오직 너희들을 (2인칭 남성 복수 목적격 분리대명사)",
        "jenis_ko": "목적격 분리대명사 (남성 복수)"
    },
    "1. Dhamir__9b": {
        "arti_ko": "당신의 / 너를 (여성)",
        "desc_ko": "너의 / 너를 (2인칭 여성 단수 접미대명사)",
        "jenis_ko": "접미대명사 (여성 단수)"
    },
    "1. Dhamir__11a": {
        "arti_ko": "나 / 저",
        "desc_ko": "나 (1인칭 단수 주격 분리대명사)",
        "jenis_ko": "주격 분리대명사 (1인칭 단수)"
    },
    "1. Dhamir__11b": {
        "arti_ko": "나의 / 나를",
        "desc_ko": "나의 / 나를 (1인칭 단수 접미대명사)",
        "jenis_ko": "접미대명사 (1인칭 단수)"
    },
    "1. Dhamir__11c": {
        "arti_ko": "오직 나만을",
        "desc_ko": "오직 나를 (1인칭 단수 목적격 분리대명사)",
        "jenis_ko": "목적격 분리대명사 (1인칭 단수)"
    },
    "1. Dhamir__12a": {
        "arti_ko": "우리",
        "desc_ko": "우리 (1인칭 복수 주격 분리대명사)",
        "jenis_ko": "주격 분리대명사 (1인칭 복수)"
    },
    "1. Dhamir__12b": {
        "arti_ko": "우리의 / 우리를",
        "desc_ko": "우리의 / 우리를 (1인칭 복수 접미대명사)",
        "jenis_ko": "접미대명사 (1인칭 복수)"
    },
    "1. Dhamir__12c": {
        "arti_ko": "오직 우리만을",
        "desc_ko": "오직 우리를 (1인칭 복수 목적격 분리대명사)",
        "jenis_ko": "목적격 분리대명사 (1인칭 복수)"
    },
    "2. Mawshul__1": {
        "arti_ko": "~하는 것 (무이성)",
        "desc_ko": "무이성 명사에 쓰이는 일반 관계사 (마)",
        "jenis_ko": "관계명사 (무이성)"
    },
    "2. Mawshul__2": {
        "arti_ko": "~하는 자들 (남성 복수)",
        "desc_ko": "관계대명사 (남성 복수 유이성)",
        "jenis_ko": "한정 관계대명사"
    },
    "2. Mawshul__3": {
        "arti_ko": "~하는 자 (유이성)",
        "desc_ko": "유이성 명사에 쓰이는 일반 관계사 (만)",
        "jenis_ko": "관계명사 (유이성)"
    },
    "2. Mawshul__4": {
        "arti_ko": "~하는 자 (남성 단수)",
        "desc_ko": "관계대명사 (남성 단수)",
        "jenis_ko": "한정 관계대명사"
    },
    "2. Mawshul__5": {
        "arti_ko": "어느 쪽의 / 어느 것",
        "desc_ko": "어느 쪽의 (관계사 및 의문사)",
        "jenis_ko": "격변화 관계명사"
    },
    "2. Mawshul__6": {
        "arti_ko": "~하는 자 (여성 단수)",
        "desc_ko": "관계대명사 (여성 단수)",
        "jenis_ko": "한정 관계대명사"
    },
    "2. Mawshul__7": {
        "arti_ko": "~하는 자들 (여성 복수 - 알라이)",
        "desc_ko": "관계대명사 (여성 복수 - 알라이)",
        "jenis_ko": "한정 관계대명사"
    },
    "2. Mawshul__8": {
        "arti_ko": "~하는 자들 (여성 복수 - 알라티)",
        "desc_ko": "관계대명사 (여성 복수 - 알라티)",
        "jenis_ko": "한정 관계대명사"
    },
    "2. Mawshul__9": {
        "arti_ko": "~하는 두 사람 (남성 쌍수)",
        "desc_ko": "관계대명사 (남성 쌍수 주격)",
        "jenis_ko": "쌍수 관계대명사"
    },
    "2. Mawshul__10": {
        "arti_ko": "어느 여성",
        "desc_ko": "관계대명사 (여성형)",
        "jenis_ko": "여성 관계대명사"
    },
    "3. Istifham__1": {
        "arti_ko": "무엇이? / 무엇",
        "desc_ko": "사물이나 행위를 묻는 의문사 (마)",
        "jenis_ko": "의문명사 (사물)"
    },
    "3. Istifham__2": {
        "arti_ko": "어떻게? (상태)",
        "desc_ko": "상태나 양태를 묻는 의문사 (카이파)",
        "jenis_ko": "의문부사 (상태)"
    },
    "3. Istifham__3": {
        "arti_ko": "누가? / 누구",
        "desc_ko": "인물이나 유이성 존재를 묻는 의문사 (만)",
        "jenis_ko": "의문명사 (인물)"
    },
    "3. Istifham__4": {
        "arti_ko": "어느 것? / 어느 쪽",
        "desc_ko": "선택을 묻는 의문사 (아이유)",
        "jenis_ko": "선택 의문사"
    },
    "3. Istifham__5": {
        "arti_ko": "어디서부터? / 어떻게?",
        "desc_ko": "장소·방법·상태를 묻는 의문사 (안나)",
        "jenis_ko": "의문부사 (양태/장소)"
    },
    "3. Istifham__6": {
        "arti_ko": "도대체 무엇이?",
        "desc_ko": "강한 의문을 나타내는 복합 의문사 (마다)",
        "jenis_ko": "강조 복합의문사"
    },
    "3. Istifham__7": {
        "arti_ko": "얼마나? / 몇 개",
        "desc_ko": "수량이나 기간을 묻는 의문사 (캄)",
        "jenis_ko": "의문부사 (수량)"
    },
    "3. Istifham__8": {
        "arti_ko": "왜? / 무엇을 위해",
        "desc_ko": "이유나 원인을 묻는 의문사 (리마)",
        "jenis_ko": "전치사+의문사"
    },
    "3. Istifham__9": {
        "arti_ko": "어디에? / 어디서",
        "desc_ko": "장소를 묻는 의문사 (아이나)",
        "jenis_ko": "의문부사 (장소)"
    },
    "3. Istifham__10": {
        "arti_ko": "언제? (심판의 날)",
        "desc_ko": "심판의 날 등 중대한 때를 묻는 의문사 (아야나)",
        "jenis_ko": "의문부사 (중대 시점)"
    },
    "4. Syarath__1": {
        "arti_ko": "누구든지 ~하는 자는",
        "desc_ko": "유이성 명사에 쓰이는 조건명사 (만)",
        "jenis_ko": "조건명사 (유이성)"
    },
    "4. Syarath__2": {
        "arti_ko": "무엇이든 ~하는 것은",
        "desc_ko": "무이성 명사에 쓰이는 조건명사 (마)",
        "jenis_ko": "조건명사 (무이성)"
    },
    "4. Syarath__3": {
        "arti_ko": "~할 때마다 / 언제든",
        "desc_ko": "시간을 나타내는 조건명사 (이즈마 / 쿨라마)",
        "jenis_ko": "시간 조건명사"
    },
    "4. Syarath__4": {
        "arti_ko": "어느 것이든 간에",
        "desc_ko": "포괄적 선택을 나타내는 조건명사 (아이얀)",
        "jenis_ko": "선택 조건명사"
    },
    "4. Syarath__5": {
        "arti_ko": "그 둘 중 어느 것이든",
        "desc_ko": "강조된 양자택일 조건명사 (아이야마)",
        "jenis_ko": "강조 조건명사"
    },
    "5. Isyarah__1": {
        "arti_ko": "이것 / 저것 (남성 단수)",
        "desc_ko": "지시대명사 (남성 단수)",
        "jenis_ko": "지시명사 (남성 단수)"
    },
    "5. Isyarah__2": {
        "arti_ko": "이들 / 저들 (복수)",
        "desc_ko": "지시대명사 (복수)",
        "jenis_ko": "지시명사 (복수)"
    },
    "5. Isyarah__3": {
        "arti_ko": "이것 (여성 단수)",
        "desc_ko": "근칭 지시대명사 (여성 단수)",
        "jenis_ko": "지시명사 (여성 단수)"
    },
    "5. Isyarah__4": {
        "arti_ko": "저것 (여성 단수)",
        "desc_ko": "원칭 지시대명사 (여성 단수)",
        "jenis_ko": "원칭 지시명사 (여성)"
    },
    "5. Isyarah__5": {
        "arti_ko": "여기에",
        "desc_ko": "근칭 장소를 나타내는 지시부사 (하후나)",
        "jenis_ko": "장소 지시부사 (근칭)"
    },
    "5. Isyarah__6": {
        "arti_ko": "저기에 / 그곳에",
        "desc_ko": "원칭 장소를 나타내는 지시부사 (후날리카)",
        "jenis_ko": "장소 지시부사 (원칭)"
    },
    "5. Isyarah__7": {
        "arti_ko": "이 두 사람 (남성 쌍수)",
        "desc_ko": "쌍수 남성 지시대명사 (다니카)",
        "jenis_ko": "지시명사 (남성 쌍수)"
    },
    "5. Isyarah__8": {
        "arti_ko": "이 두 사람 (여성 쌍수)",
        "desc_ko": "쌍수 여성 지시대명사 (타니카)",
        "jenis_ko": "지시명사 (여성 쌍수)"
    },
    "6. Isim Fi'il__1": {
        "arti_ko": "하나님께 영광이! (수브하나)",
        "desc_ko": "찬미·칭송의 절대목적격 명사",
        "jenis_ko": "동사성 찬미명사"
    },
    "6. Isim Fi'il__2": {
        "arti_ko": "자, 가져오라!",
        "desc_ko": "명령을 나타내는 동사성 명사 (하투)",
        "jenis_ko": "명령 동사성 명사"
    },
    "6. Isim Fi'il__3": {
        "arti_ko": "아아! (지겹도다)",
        "desc_ko": "불쾌감과 혐오를 나타내는 현재 동사성 명사 (우프)",
        "jenis_ko": "현재 동사성 명사"
    },
    "6. Isim Fi'il__4": {
        "arti_ko": "하나님의 보호를!",
        "desc_ko": "구원과 보호를 구하는 동사성 명사 (마아달라)",
        "jenis_ko": "기도 동사성 명사"
    },
    "6. Isim Fi'il__5": {
        "arti_ko": "자, 오라!",
        "desc_ko": "재촉과 모임을 나타내는 동사성 명사 (할룸마)",
        "jenis_ko": "명령 동사성 명사"
    },
    "6. Isim Fi'il__6": {
        "arti_ko": "얼마나 아득히 먼가!",
        "desc_ko": "거리의 아득함을 나타내는 과거 동사성 명사 (하이하타)",
        "jenis_ko": "과거 동사성 명사"
    },
    "6. Isim Fi'il__7": {
        "arti_ko": "자, 이것을 받아 읽으라!",
        "desc_ko": "명령을 나타내는 동사성 명사 (하움)",
        "jenis_ko": "명령 동사성 명사"
    },
    "6. Isim Fi'il__8": {
        "arti_ko": "자, 이리로 오라!",
        "desc_ko": "부름과 재촉의 동사성 명사 (하이라 라크)",
        "jenis_ko": "명령 동사성 명사"
    },
    "7. Fi'il Jamid__1": {
        "arti_ko": "~가 아니다 (부정)",
        "desc_ko": "부정을 나타내는 불완전 불변동사 (라이사)",
        "jenis_ko": "불완전 불변동사 (부정)"
    },
    "7. Fi'il Jamid__2": {
        "arti_ko": "~일지도 모른다 (희망)",
        "desc_ko": "희망과 기대를 나타내는 불변동사 (아사)",
        "jenis_ko": "희망 불변동사"
    },
    "7. Fi'il Jamid__3": {
        "arti_ko": "얼마나 훌륭한가! (찬양)",
        "desc_ko": "칭찬과 찬양을 나타내는 불변동사 (니으마)",
        "jenis_ko": "찬양 불변동사"
    },
    "7. Fi'il Jamid__4": {
        "arti_ko": "얼마나 나쁜가! (비난)",
        "desc_ko": "비난과 질책의 불변동사 (비으사)",
        "jenis_ko": "비난 불변동사"
    },
    "7. Fi'il Jamid__5": {
        "arti_ko": "얼마나 사악한 것인가!",
        "desc_ko": "비난을 나타내는 복합 불변동사 (비으사마)",
        "jenis_ko": "복합 비난동사"
    },
    "7. Fi'il Jamid__6": {
        "arti_ko": "~하기 시작했다 (착수)",
        "desc_ko": "시작을 나타내는 불변동사 (타피카)",
        "jenis_ko": "착수동사"
    },
    "7. Fi'il Jamid__7": {
        "arti_ko": "하나님께 결백하도다!",
        "desc_ko": "제외 및 신성화의 불변동사 (하샤 릴라)",
        "jenis_ko": "신성화 불변동사"
    },
    "7. Fi'il Jamid__8": {
        "arti_ko": "얼마나 훌륭한 교훈인가!",
        "desc_ko": "찬양을 나타내는 복합 불변동사 (니임마)",
        "jenis_ko": "복합 찬양동사"
    }
}

# 4. 17 Harf Ghair 'Amil Categories in Korean
BENTUK_HARF_KO = {
    "1. Harf Istifham": "1. 의문사 (Harf Istifham)",
    "2. Harf Nida'": "2. 호격사 (Harf Nida')",
    "3. Harf 'Athaf": "3. 접속사 (Harf 'Athaf)",
    "4. Harf Jawab": "4. 응답사 (Harf Jawab)",
    "5. Harf Rad'": "5. 거절·경계사 (Harf Rad')",
    "6. Harf Tanbih": "6. 주의환기사 (Harf Tanbih)",
    "7. Harf Ijabah": "7. 긍정사 (Harf Ijabah)",
    "8. Harf Syarath": "8. 조건사 (Harf Syarath)",
    "9. Harf Mashdariyah": "9. 어간명사화사 (Harf Mashdariyah)",
    "10. Harf Tahdidh": "10. 촉구·권유사 (Harf Tahdidh)",
    "11. Harf Ta'lil": "11. 이유설명사 (Harf Ta'lil)",
    "12. Harf Nafyi": "12. 부정사 (Harf Nafyi)",
    "13. Harf Nahyi": "13. 금지사 (Harf Nahyi)",
    "14. Harf Istiqbal": "14. 미래사 (Harf Istiqbal)",
    "15. Harf Taukid": "15. 강조사 (Harf Taukid)",
    "16. Harf Ziyadah": "16. 수사적 첨가사 (Harf Ziyadah)",
    "17. Harf Mabany": "17. 독립문자 (Harf Mabany / 서두두문자)"
}

# 5. 52 Harf Grammatical Metadata in Korean
KOREAN_HARF_GRAMMAR = {
    "1. Harf Nafyi__1": {
        "arti_ko": "~하지 않는다 (부정의 라)",
        "desc_ko": "절대 부정 소사 (라)",
        "jenis_ko": "부정 소사"
    },
    "1. Harf Nafyi__2": {
        "arti_ko": "~가 아니다 (부정의 마)",
        "desc_ko": "일반적 부정 소사 (마)",
        "jenis_ko": "부정 소사"
    },
    "1. Harf Nafyi__3": {
        "arti_ko": "~에 지나지 않는다 (인)",
        "desc_ko": "예외를 수반하는 부정 소사 (인)",
        "jenis_ko": "부정 소사"
    },
    "1. Harf Nafyi__4": {
        "arti_ko": "~하겠는가? (반어적 부정)",
        "desc_ko": "부정의 의미를 내포한 의문사 (할)",
        "jenis_ko": "반어 부정 의문사"
    },
    "1. Harf Nafyi__5": {
        "arti_ko": "도망칠 때가 아니다",
        "desc_ko": "시간 명사에 결합하는 부정 소사 (라아타)",
        "jenis_ko": "부정 소사"
    },
    "1. Harf Nafyi__6": {
        "arti_ko": "진리 외에 무엇이 있겠는가",
        "desc_ko": "부정을 내포한 의문사 (마다)",
        "jenis_ko": "반어 부정 의문사"
    },
    "2. Harf Tahqiq Taswif__7": {
        "arti_ko": "과연 ~하였다 (확증의 카드)",
        "desc_ko": "과거형과 함께 확증을 나타내는 소사 (카드)",
        "jenis_ko": "확증 소사"
    },
    "2. Harf Tahqiq Taswif__8": {
        "arti_ko": "머지않아 ~하리라",
        "desc_ko": "미래를 나타내는 소사 (사우파)",
        "jenis_ko": "미래 소사"
    },
    "3. Harf Syarat__9": {
        "arti_ko": "만약 ~라면 (가정의 라우)",
        "desc_ko": "반사실적 조건 소사 (라우)",
        "jenis_ko": "조건 소사"
    },
    "3. Harf Syarat__10": {
        "arti_ko": "만약 ~가 없었다면",
        "desc_ko": "존재의 부정을 전제로 하는 조건 소사 (라우라)",
        "jenis_ko": "유보 조건소사"
    },
    "3. Harf Syarat__11": {
        "arti_ko": "비록 ~일지라도",
        "desc_ko": "양보적 조건 소사 (라우)",
        "jenis_ko": "양보 조건소사"
    },
    "3. Harf Syarat__12": {
        "arti_ko": "만약 ~한다면 (임마)",
        "desc_ko": "강조 조건 소사 (인 + 마)",
        "jenis_ko": "강조 조건소사"
    },
    "3. Harf Syarat__13": {
        "arti_ko": "어떠한 표징을 가져오든",
        "desc_ko": "포괄적 조건명사 (마흐마)",
        "jenis_ko": "포괄 조건명사"
    },
    "4. Harf Mashdariyah__14": {
        "arti_ko": "~하는 한 / ~동안",
        "desc_ko": "시간을 나타내는 명사화 소사 (마)",
        "jenis_ko": "시간 명사화소사"
    },
    "4. Harf Mashdariyah__15": {
        "arti_ko": "~하지 않도록",
        "desc_ko": "부정을 수반하는 명사화 소사 (안 + 라)",
        "jenis_ko": "명사화 부정소사"
    },
    "4. Harf Mashdariyah__16": {
        "arti_ko": "~라는 것 (안)",
        "desc_ko": "동사를 명사구로 만드는 소사 (안)",
        "jenis_ko": "명사화 소사"
    },
    "4. Harf Mashdariyah__17": {
        "arti_ko": "~하기를 바라다",
        "desc_ko": "소망의 명사화 소사 (라우)",
        "jenis_ko": "소망 명사화소사"
    },
    "4. Harf Mashdariyah__18": {
        "arti_ko": "~하지 말 것",
        "desc_ko": "금지를 수반하는 명사화 소사 (안 + 라)",
        "jenis_ko": "명사화 금지소사"
    },
    "4. Harf Mashdariyah__19": {
        "arti_ko": "~라는 사실",
        "desc_ko": "사실의 명사화 소사 (안 축약형)",
        "jenis_ko": "명사화 소사"
    },
    "5. Harf Zaidah__20": {
        "arti_ko": "~처럼 (강조)",
        "desc_ko": "비유 접두사 + 강조 첨가사 (카 + 마)",
        "jenis_ko": "강조 첨가사"
    },
    "5. Harf Zaidah__21": {
        "arti_ko": "모기와 같은 미물이라도",
        "desc_ko": "막연함과 강조의 첨가사 (마)",
        "jenis_ko": "강조 첨가사"
    },
    "5. Harf Zaidah__22": {
        "arti_ko": "내가 맹세하노니",
        "desc_ko": "맹세를 강화하는 첨가사 (라)",
        "jenis_ko": "맹세 강조첨가사"
    },
    "5. Harf Zaidah__23": {
        "arti_ko": "하나님의 자비로 인하여",
        "desc_ko": "전치사에 결합된 강조 첨가사 (비 + 마)",
        "jenis_ko": "전치사 강조첨가사"
    },
    "5. Harf Zaidah__24": {
        "arti_ko": "기쁜 소식을 전하는 자가 왔을 때",
        "desc_ko": "시간 접속사에 수반된 첨가사 (안)",
        "jenis_ko": "시간 강조첨가사"
    },
    "6. Harf Istifham__25": {
        "arti_ko": "~인가? (의문의 할)",
        "desc_ko": "질문과 확인을 나타내는 의문 소사 (할)",
        "jenis_ko": "의문 소사"
    },
    "7. Harf Jawab__26": {
        "arti_ko": "그렇다면 / 과연",
        "desc_ko": "응답과 귀결을 나타내는 소사 (이잔)",
        "jenis_ko": "응답 귀결소사"
    },
    "7. Harf Jawab__27": {
        "arti_ko": "그렇고말고요 / 참으로",
        "desc_ko": "부정에 대한 긍정 응답 소사 (발라)",
        "jenis_ko": "긍정 응답소사"
    },
    "7. Harf Jawab__28": {
        "arti_ko": "예 / 그렇습니다",
        "desc_ko": "긍정 응답 소사 (나암)",
        "jenis_ko": "긍정 응답소사"
    },
    "7. Harf Jawab__29": {
        "arti_ko": "그러하다! 주님을 두고 맹세컨대",
        "desc_ko": "맹세를 수반하는 긍정 응답 소사 (이)",
        "jenis_ko": "맹세 응답소사"
    },
    "8. Harf Ibtida'__30": {
        "arti_ko": "~에 이르기까지",
        "desc_ko": "문두 및 발단을 나타내는 소사 (핫타)",
        "jenis_ko": "발단 소사"
    },
    "9. Harf Tafshil__31": {
        "arti_ko": "~에 관하여는",
        "desc_ko": "상세화 및 주제 제시 소사 (암마)",
        "jenis_ko": "상세화 소사"
    },
    "10. Harf Mufaja'ah__32": {
        "arti_ko": "뜻밖에 ~가 되었다",
        "desc_ko": "돌발적 사태를 나타내는 소사 (이다)",
        "jenis_ko": "돌발 사태소사"
    },
    "11. Harf Mufassirah__33": {
        "arti_ko": "즉 ~라고",
        "desc_ko": "해설 및 설명을 이끄는 소사 (안)",
        "jenis_ko": "설명 소사"
    },
    "12. Harf Istiftahiyah__34": {
        "arti_ko": "보라! / 명심하라",
        "desc_ko": "주의환기 및 개시 소사 (알라)",
        "jenis_ko": "주의환기 소사"
    },
    "13. Harf Rada'__35": {
        "arti_ko": "결코 아니다!",
        "desc_ko": "경계 및 강한 거절의 소사 (칼라)",
        "jenis_ko": "경계 거절소사"
    },
    "14. Harf Ta'ajjub__36": {
        "arti_ko": "어찌 그리 잘 참는가!",
        "desc_ko": "감탄과 놀라움을 나타내는 소사 (마)",
        "jenis_ko": "감탄 소사"
    },
    "15. Harf Fariqah__37": {
        "arti_ko": "정녕 / 진실로",
        "desc_ko": "긍정을 구분하는 강조 람 (인 축약형 수반)",
        "jenis_ko": "구분 강조람"
    },
    "16. Harf Mauthi'ah__38": {
        "arti_ko": "만약 ~한다면 맹세코",
        "desc_ko": "맹세를 이끄는 조건 람 (라 인)",
        "jenis_ko": "맹세 전치람"
    },
    "17. Harf Mabany__39": {
        "arti_ko": "하 밈",
        "desc_ko": "장 서두의 신비로운 독립문자 (حم)",
        "jenis_ko": "독립문자 (무캇타아트)"
    },
    "17. Harf Mabany__40": {
        "arti_ko": "알리프 람 밈",
        "desc_ko": "장 서두의 신비로운 독립문자 (الم)",
        "jenis_ko": "독립문자 (무캇타아트)"
    },
    "17. Harf Mabany__41": {
        "arti_ko": "알리프 람 라",
        "desc_ko": "장 서두의 신비로운 독립문자 (الر)",
        "jenis_ko": "독립문자 (무캇타아트)"
    },
    "17. Harf Mabany__42": {
        "arti_ko": "따 신 밈",
        "desc_ko": "장 서두의 신비로운 독립문자 (طسم)",
        "jenis_ko": "독립문자 (무캇타아트)"
    },
    "17. Harf Mabany__43": {
        "arti_ko": "알리프 람 밈 라",
        "desc_ko": "장 서두의 신비로운 독립문자 (المر)",
        "jenis_ko": "독립문자 (무캇타아트)"
    },
    "17. Harf Mabany__44": {
        "arti_ko": "알리프 람 밈 사드",
        "desc_ko": "장 서두의 신비로운 독립문자 (المص)",
        "jenis_ko": "독립문자 (무캇타아트)"
    },
    "17. Harf Mabany__45": {
        "arti_ko": "사드",
        "desc_ko": "장 서두의 신비로운 독립문자 (ص)",
        "jenis_ko": "독립문자 (무캇타아트)"
    },
    "17. Harf Mabany__46": {
        "arti_ko": "따 신",
        "desc_ko": "장 서두의 신비로운 독립문자 (طس)",
        "jenis_ko": "독립문자 (무캇타아트)"
    },
    "17. Harf Mabany__47": {
        "arti_ko": "따 하",
        "desc_ko": "장 서두의 신비로운 독립문자 (طه)",
        "jenis_ko": "독립문자 (무캇타아트)"
    },
    "17. Harf Mabany__48": {
        "arti_ko": "아인 신 까프",
        "desc_ko": "장 서두의 신비로운 독립문자 (عسق)",
        "jenis_ko": "독립문자 (무캇타아트)"
    },
    "17. Harf Mabany__49": {
        "arti_ko": "까프",
        "desc_ko": "장 서두의 신비로운 독립문자 (ق)",
        "jenis_ko": "독립문자 (무캇타아트)"
    },
    "17. Harf Mabany__50": {
        "arti_ko": "까프 하 야 아인 사드",
        "desc_ko": "장 서두의 신비로운 독립문자 (كهيعص)",
        "jenis_ko": "독립문자 (무캇타아트)"
    },
    "17. Harf Mabany__51": {
        "arti_ko": "눈",
        "desc_ko": "장 서두의 신비로운 독립문자 (ن)",
        "jenis_ko": "독립문자 (무캇타아트)"
    },
    "17. Harf Mabany__52": {
        "arti_ko": "야 씬",
        "desc_ko": "장 서두의 신비로운 독립문자 (يس)",
        "jenis_ko": "독립문자 (무캇타아트)"
    }
}


def enrich_dhamir_data():
    print("Enriching dhamir_data.json and dhamir_data.js with Korean...")
    
    with open(os.path.join(BASE_DIR, 'ko_translations.json'), 'r', encoding='utf-8') as f:
        ko_translations = json.load(f)

    with open(os.path.join(BASE_DIR, 'dhamir_data.json'), 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        b = item.get('Bentuk Kata', '')
        nk = item.get('No kata', '')
        g_key = f"{b}__{nk}"
        
        # 1. BentukKataKO
        item['BentukKataKO'] = BENTUK_KATA_KO.get(b, b)
        
        # 2. SuratArtiKO
        surat_num = str(item.get('SURAT', ''))
        item['SuratArtiKO'] = KOREAN_SURAHS.get(surat_num, item.get('SuratArtiEN', ''))
        
        # 3. ArtiKataKO & Grammar KO
        g_info = KOREAN_GRAMMAR.get(g_key, {})
        item['ArtiKataKO'] = g_info.get('arti_ko', item.get('ArtiKataEN', item.get('Arti kata', '')))
        
        if 'Grammar' not in item:
            item['Grammar'] = {}
        if g_info.get('arti_ko'):
            item['Grammar']['arti_ko'] = g_info['arti_ko']
        if g_info.get('desc_ko'):
            item['Grammar']['desc_ko'] = g_info['desc_ko']
        if g_info.get('jenis_ko'):
            item['Grammar']['jenis_ko'] = g_info['jenis_ko']
            
        # 4. TeksArtiKO
        v_key = f"{item.get('SURAT')}:{item.get('AYAT')}"
        teks_ko = ko_translations.get(v_key, item.get('TeksArtiEN', item.get('TeksArtiID', '')))
        item['TeksArtiKO'] = teks_ko

    # Write dhamir_data.json
    with open(os.path.join(BASE_DIR, 'dhamir_data.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Write dhamir_data.js
    with open(os.path.join(BASE_DIR, 'dhamir_data.js'), 'w', encoding='utf-8') as f:
        f.write("const DHAMIR_DATA = ")
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write(";\n\nif (typeof module !== 'undefined' && module.exports) {\n  module.exports = DHAMIR_DATA;\n}\n")

    print(f"dhamir_data successfully updated with Korean! (Total items: {len(data)})")


def enrich_harf_data():
    print("Enriching harf_data.json and harf_data.js with Korean...")
    
    with open(os.path.join(BASE_DIR, 'ko_translations.json'), 'r', encoding='utf-8') as f:
        ko_translations = json.load(f)

    with open(os.path.join(BASE_DIR, 'harf_data.json'), 'r', encoding='utf-8') as f:
        data = json.load(f)

    for item in data:
        b = item.get('Bentuk Kata', '')
        nk = item.get('No kata', '')
        g_key = f"{b}__{nk}"
        
        # 1. BentukKataKO
        item['BentukKataKO'] = BENTUK_HARF_KO.get(b, b)
        
        # 2. SuratArtiKO
        surat_num = str(item.get('SURAT', ''))
        item['SuratArtiKO'] = KOREAN_SURAHS.get(surat_num, item.get('SuratArtiEN', ''))
        
        # 3. ArtiKataKO & Grammar KO
        g_info = KOREAN_HARF_GRAMMAR.get(g_key, {})
        item['ArtiKataKO'] = g_info.get('arti_ko', item.get('ArtiKataEN', item.get('Arti kata', '')))
        
        if 'Grammar' not in item:
            item['Grammar'] = {}
        if g_info.get('arti_ko'):
            item['Grammar']['arti_ko'] = g_info['arti_ko']
        if g_info.get('desc_ko'):
            item['Grammar']['desc_ko'] = g_info['desc_ko']
        if g_info.get('jenis_ko'):
            item['Grammar']['jenis_ko'] = g_info['jenis_ko']
            
        # 4. TeksArtiKO
        v_key = f"{item.get('SURAT')}:{item.get('AYAT')}"
        teks_ko = ko_translations.get(v_key, item.get('TeksArtiEN', item.get('TeksArtiID', '')))
        item['TeksArtiKO'] = teks_ko

    # Write harf_data.json
    with open(os.path.join(BASE_DIR, 'harf_data.json'), 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    # Write harf_data.js
    with open(os.path.join(BASE_DIR, 'harf_data.js'), 'w', encoding='utf-8') as f:
        f.write("const HARF_DATA = ")
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write(";\n\nif (typeof module !== 'undefined' && module.exports) {\n  module.exports = HARF_DATA;\n}\n")

    print(f"harf_data successfully updated with Korean! (Total items: {len(data)})")


if __name__ == '__main__':
    enrich_dhamir_data()
    enrich_harf_data()
