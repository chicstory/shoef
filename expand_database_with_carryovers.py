"""
Expand ShoeF Master Database with 24 Iconic Carryover Models (Recent 3 Years: 2023-2024).
Total Database: 70 current (2025-2026) + 24 carryover (2023-2024) = 94 Shoes across 10 Brands.
"""

import json
import os

CARRYOVER_SHOES = [
    # --- ADIDAS (2 models) ---
    {
        "id": "adidas_adizero_adios_pro_3",
        "brand_id": "adidas",
        "name_kr": "아디다스 아디제로 아디오스 프로 3",
        "name_en": "Adidas Adizero Adios Pro 3",
        "series": "아디제로",
        "category": "racing",
        "category_name": "레이싱화 (카본 슈퍼슈즈)",
        "release_year": 2023,
        "gen_type": "carryover",
        "msrp_usd": 250,
        "msrp_krw": 279000,
        "widths": ["D"],
        "specs": {
            "weight_g": 220,
            "heel_drop_mm": 6.5,
            "midsole": "Lightstrike Pro 100% + 카본 EnergyRods 2.0",
            "plate": "EnergyRods 2.0 (카본)",
            "stack_height": "39mm / 32.5mm",
            "support_type": "Neutral (전설의 마라톤 레이서)"
        },
        "runrepeat": {
            "score": 92,
            "midsole_foam": "Lightstrike Pro",
            "pros": [
                "전 세계 메이저 마라톤을 휩쓴 역대급 명작 카본화",
                "라이트스트라이크 프로 폼의 쫀득하고 끝없는 반발력",
                "컨티넨탈 러버의 빗길 1위 접지력"
            ],
            "cons": ["상단 어퍼 핏이 거칠어 끈 조절 필요"],
            "verdict": "프로 4 출시 후 역대급 이월 할인가로 풀려 러너들이 가장 열광하는 불멸의 명작 카본화.",
            "url": "https://runrepeat.com/adidas-adizero-adios-pro-3"
        }
    },
    {
        "id": "adidas_adizero_boston_11",
        "brand_id": "adidas",
        "name_kr": "아디다스 아디제로 보스턴 11",
        "name_en": "Adidas Adizero Boston 11",
        "series": "보스턴",
        "category": "super_trainer",
        "category_name": "슈퍼 트레이너",
        "release_year": 2023,
        "gen_type": "carryover",
        "msrp_usd": 160,
        "msrp_krw": 179000,
        "widths": ["D"],
        "specs": {
            "weight_g": 290,
            "heel_drop_mm": 8.5,
            "midsole": "Lightstrike Pro (상단) + Lightstrike EVA (하단) + 에너지로드",
            "plate": "EnergyRods (유리섬유)",
            "stack_height": "39.5mm / 31mm",
            "support_type": "Neutral (탄탄한 훈련화)"
        },
        "runrepeat": {
            "score": 80,
            "midsole_foam": "Lightstrike Pro & EVA",
            "pros": [
                "아울렛 7~8만원대 가성비에 에너지로드 탑재",
                "질긴 내구성과 탄탄한 지지력"
            ],
            "cons": ["하단 EVA 폼이 단단하여 길들이기 필요"],
            "verdict": "단단하지만 가성비 있게 아디제로 훈련 감각을 익힐 수 있는 이월 훈련화.",
            "url": "https://runrepeat.com/adidas-adizero-boston-11"
        }
    },

    # --- NIKE (3 models) ---
    {
        "id": "nike_pegasus_40",
        "brand_id": "nike",
        "name_kr": "나이키 에어 줌 페가수스 40",
        "name_en": "Nike Air Zoom Pegasus 40",
        "series": "페가수스",
        "category": "daily",
        "category_name": "데일리 / 쿠션화",
        "release_year": 2023,
        "gen_type": "carryover",
        "msrp_usd": 130,
        "msrp_krw": 149000,
        "widths": ["D", "2E"],
        "specs": {
            "weight_g": 280,
            "heel_drop_mm": 10,
            "midsole": "React Foam + 앞/뒤 듀얼 Zoom Air 유닛",
            "plate": "없음",
            "stack_height": "33mm / 23mm",
            "support_type": "Neutral (국민 조깅화 이월특가)"
        },
        "runrepeat": {
            "score": 82,
            "midsole_foam": "React Foam",
            "pros": [
                "7~8만원대 이월 러닝화 중 가장 검증된 국민 조깅화",
                "앞뒤 듀얼 줌 에어의 든든한 반발력",
                "내구성 높은 와플 아웃솔"
            ],
            "cons": ["신형 페가수스 41 대비 약간 무거운 무게감"],
            "verdict": "신형 41 정가가 부담스러울 때 가장 합리적으로 선택하는 7~8만원대 국민 조깅화.",
            "url": "https://runrepeat.com/nike-pegasus-40"
        }
    },
    {
        "id": "nike_invincible_3",
        "brand_id": "nike",
        "name_kr": "나이키 줌X 인빈서블 런 3",
        "name_en": "Nike ZoomX Invincible Run 3",
        "series": "인빈서블",
        "category": "daily",
        "category_name": "데일리 / 쿠션화",
        "release_year": 2023,
        "gen_type": "carryover",
        "msrp_usd": 180,
        "msrp_krw": 209000,
        "widths": ["D"],
        "specs": {
            "weight_g": 309,
            "heel_drop_mm": 9,
            "midsole": "100% Full ZoomX Superfoam",
            "plate": "없음",
            "stack_height": "40mm / 31mm",
            "support_type": "Neutral (극강의 줌X 바운스)"
        },
        "runrepeat": {
            "score": 81,
            "midsole_foam": "ZoomX",
            "pros": [
                "100% 줌X 폼이 선사하는 지상 최강의 트램펄린 바운스",
                "넓어진 플랫폼 베이스로 향상된 안정감",
                "무릎 관절 회복 조깅 최적화"
            ],
            "cons": ["힐 슬립 이슈가 있어 러너스 루프 매듭 추천"],
            "verdict": "무릎과 관절을 아끼는 회복 러닝에 이만한 구름 쿠션이 없는 줌X 맥스 쿠션화.",
            "url": "https://runrepeat.com/nike-invincible-3"
        }
    },
    {
        "id": "nike_vaporfly_next_2",
        "brand_id": "nike",
        "name_kr": "나이키 줌X 베이퍼플라이 넥스트% 2",
        "name_en": "Nike Vaporfly Next% 2",
        "series": "베이퍼플라이",
        "category": "racing",
        "category_name": "레이싱화 (카본 슈퍼슈즈)",
        "release_year": 2023,
        "gen_type": "carryover",
        "msrp_usd": 250,
        "msrp_krw": 269000,
        "widths": ["D"],
        "specs": {
            "weight_g": 196,
            "heel_drop_mm": 8,
            "midsole": "ZoomX + 풀렝스 카본 플라이플레이트",
            "plate": "Full Carbon Plate",
            "stack_height": "40mm / 32mm",
            "support_type": "Neutral (불멸의 카본 레이싱 명작)"
        },
        "runrepeat": {
            "score": 89,
            "midsole_foam": "ZoomX",
            "pros": [
                "196g 초경량과 베이퍼플라이 역사상 가장 날카로운 치고 나가는 킥",
                "검증된 베이퍼위브 어퍼의 경량성"
            ],
            "cons": ["내구성이 낮아 대회 전용으로 아껴 신어야 함"],
            "verdict": "여전히 마라톤 출발선에서 수많은 러너들이 애용하는 불멸의 카본 레이싱 명작.",
            "url": "https://runrepeat.com/nike-zoomx-vaporfly-next-2"
        }
    },

    # --- ASICS (6 models) ---
    {
        "id": "asics_novablast_4",
        "brand_id": "asics",
        "name_kr": "아식스 노바블라스트 4",
        "name_en": "Asics Novablast 4",
        "series": "노바블라스트",
        "category": "daily",
        "category_name": "데일리 / 쿠션화",
        "release_year": 2024,
        "gen_type": "carryover",
        "msrp_usd": 140,
        "msrp_krw": 159000,
        "widths": ["D", "2E"],
        "specs": {
            "weight_g": 260,
            "heel_drop_mm": 8,
            "midsole": "FF BLAST+ ECO + 지오메트릭 아웃솔",
            "plate": "없음",
            "stack_height": "41.5mm / 33.5mm",
            "support_type": "Neutral (완성형 트램펄린 데일리)"
        },
        "runrepeat": {
            "score": 86,
            "midsole_foam": "FF BLAST+ ECO",
            "pros": [
                "안정성과 통통 튀는 재미의 완벽한 밸런스",
                "신형 5 출시 후 가성비가 극대화된 10만원 초반대 원픽",
                "발볼 D/2E의 편안한 핏"
            ],
            "cons": ["젖은 대리석 노면에서 접지력 주의"],
            "verdict": "노바블라스트 5 이전 러닝화계를 평정했던 가장 완성도 높은 국민 데일리 트레이너.",
            "url": "https://runrepeat.com/asics-novablast-4"
        }
    },
    {
        "id": "asics_novablast_3",
        "brand_id": "asics",
        "name_kr": "아식스 노바블라스트 3",
        "name_en": "Asics Novablast 3",
        "series": "노바블라스트",
        "category": "daily",
        "category_name": "데일리 / 쿠션화",
        "release_year": 2023,
        "gen_type": "carryover",
        "msrp_usd": 140,
        "msrp_krw": 149000,
        "widths": ["D", "2E"],
        "specs": {
            "weight_g": 253,
            "heel_drop_mm": 8,
            "midsole": "FF BLAST+ 폼",
            "plate": "없음",
            "stack_height": "38mm / 30mm",
            "support_type": "Neutral (경쾌한 바운스)"
        },
        "runrepeat": {
            "score": 87,
            "midsole_foam": "FF BLAST+",
            "pros": [
                "253g의 깃털 같은 무게감",
                "극강의 바운스와 쫄깃한 충격 흡수"
            ],
            "cons": ["설포(텅) 미끄러짐"],
            "verdict": "노바블라스트 시리즈 중 가장 가볍고 경쾌했던 명작.",
            "url": "https://runrepeat.com/asics-novablast-3"
        }
    },
    {
        "id": "asics_gel_nimbus_26",
        "brand_id": "asics",
        "name_kr": "아식스 젤 님버스 26",
        "name_en": "Asics Gel Nimbus 26",
        "series": "젤 님버스",
        "category": "daily",
        "category_name": "데일리 / 쿠션화",
        "release_year": 2024,
        "gen_type": "carryover",
        "msrp_usd": 160,
        "msrp_krw": 189000,
        "widths": ["D", "2E", "4E"],
        "specs": {
            "weight_g": 305,
            "heel_drop_mm": 8,
            "midsole": "FF BLAST+ ECO + PureGEL + 하이브리드 아시스그립",
            "plate": "없음",
            "stack_height": "42mm / 34mm",
            "support_type": "Neutral (프리미엄 구름 쿠션)"
        },
        "runrepeat": {
            "score": 81,
            "midsole_foam": "FF BLAST+ ECO",
            "pros": [
                "아시스그립 아웃솔 적용으로 25의 접지력 문제 완벽 해결",
                "극강의 발목 편안함과 구름 착지"
            ],
            "cons": ["스피드 러닝에는 무거운 무게"],
            "verdict": "님버스 27 대비 합리적인 가격에 최상의 쿠션 보호를 누릴 수 있는 이월 쿠션화.",
            "url": "https://runrepeat.com/asics-gel-nimbus-26"
        }
    },
    {
        "id": "asics_gel_nimbus_25",
        "brand_id": "asics",
        "name_kr": "아식스 젤 님버스 25",
        "name_en": "Asics Gel Nimbus 25",
        "series": "젤 님버스",
        "category": "daily",
        "category_name": "데일리 / 쿠션화",
        "release_year": 2023,
        "gen_type": "carryover",
        "msrp_usd": 160,
        "msrp_krw": 179000,
        "widths": ["D", "2E", "4E"],
        "specs": {
            "weight_g": 290,
            "heel_drop_mm": 8,
            "midsole": "FF BLAST+ ECO + PureGEL",
            "plate": "없음",
            "stack_height": "41.5mm / 33.5mm",
            "support_type": "Neutral (환골탈태 구름화)"
        },
        "runrepeat": {
            "score": 81,
            "midsole_foam": "FF BLAST+ ECO",
            "pros": [
                "님버스 역사를 바꾼 파격적인 맥스스택 디자인",
                "포근한 니트 어퍼 칼라"
            ],
            "cons": ["젖은 노면에서 접지력 아쉬움"],
            "verdict": "님버스를 맥스쿠션의 제왕으로 등극시킨 25주년 기념 기념비적 모델.",
            "url": "https://runrepeat.com/asics-gel-nimbus-25"
        }
    },
    {
        "id": "asics_gel_kayano_30",
        "brand_id": "asics",
        "name_kr": "아식스 젤 카야노 30",
        "name_en": "Asics Gel Kayano 30",
        "series": "젤 카야노",
        "category": "stability",
        "category_name": "안정화 (과회내 서포트)",
        "release_year": 2023,
        "gen_type": "carryover",
        "msrp_usd": 160,
        "msrp_krw": 189000,
        "widths": ["D", "2E", "4E"],
        "specs": {
            "weight_g": 303,
            "heel_drop_mm": 10,
            "midsole": "4D 가이던스 시스템 + PureGEL + FF BLAST+",
            "plate": "없음",
            "stack_height": "40mm / 30mm",
            "support_type": "Stability (맥스쿠션 안정화 전환)"
        },
        "runrepeat": {
            "score": 82,
            "midsole_foam": "FF BLAST+ ECO",
            "pros": [
                "혁신적인 4D 가이던스 시스템 최초 도입",
                "평발과 과회내 러너들의 관절 통증 완벽 방어"
            ],
            "cons": ["300g 초과 중량"],
            "verdict": "30년 역사의 카야노가 맥스쿠션 안정화로 환골탈태한 이월 안정화의 기준점.",
            "url": "https://runrepeat.com/asics-gel-kayano-30"
        }
    },
    {
        "id": "asics_superblast_1",
        "brand_id": "asics",
        "name_kr": "아식스 슈퍼블라스트 1",
        "name_en": "Asics Superblast",
        "series": "슈퍼블라스트",
        "category": "super_trainer",
        "category_name": "슈퍼 트레이너",
        "release_year": 2023,
        "gen_type": "carryover",
        "msrp_usd": 220,
        "msrp_krw": 249000,
        "widths": ["D"],
        "specs": {
            "weight_g": 240,
            "heel_drop_mm": 8,
            "midsole": "FF TURBO (상단) + FF BLAST+ (하단) 듀얼",
            "plate": "없음",
            "stack_height": "45mm / 37mm",
            "support_type": "Neutral (전설의 논카본 슈퍼트레이너)"
        },
        "runrepeat": {
            "score": 89,
            "midsole_foam": "FF TURBO",
            "pros": [
                "논플레이트 슈퍼트레이너라는 새로운 장르를 개척한 전설의 모델",
                "45mm 스택인데도 240g이라는 충격적인 경량성"
            ],
            "cons": ["높은 가격과 여전한 매물 품귀"],
            "verdict": "슈퍼블라스트 2와 함께 러너들에게 '치트키'로 불리는 논카본 최강 트레이너.",
            "url": "https://runrepeat.com/asics-superblast"
        }
    },

    # --- SAUCONY (3 models) ---
    {
        "id": "saucony_endorphin_speed_3",
        "brand_id": "saucony",
        "name_kr": "써코니 엔돌핀 스피드 3",
        "name_en": "Saucony Endorphin Speed 3",
        "series": "엔돌핀 스피드",
        "category": "super_trainer",
        "category_name": "슈퍼 트레이너",
        "release_year": 2023,
        "gen_type": "carryover",
        "msrp_usd": 170,
        "msrp_krw": 189000,
        "widths": ["D", "2E"],
        "specs": {
            "weight_g": 229,
            "heel_drop_mm": 8,
            "midsole": "PWRRUN PB + 윙 나일론 플레이트",
            "plate": "Winged Nylon Plate",
            "stack_height": "36mm / 28mm",
            "support_type": "Neutral (올타임 레전드 슈퍼트레이너)"
        },
        "runrepeat": {
            "score": 86,
            "midsole_foam": "PWRRUN PB",
            "pros": [
                "역대 가장 부드러운 윙 나일론 플레이트 롤링",
                "조깅부터 하프 마라톤까지 만능 커버",
                "초경량 229g"
            ],
            "cons": ["신형 4 출시 후 재고 소진 중"],
            "verdict": "전 세계 수많은 마라토너들이 입을 모아 극찬한 올타임 레전드 슈퍼 트레이너.",
            "url": "https://runrepeat.com/saucony-endorphin-speed-3"
        }
    },
    {
        "id": "saucony_triumph_21",
        "brand_id": "saucony",
        "name_kr": "써코니 트라이엄프 21",
        "name_en": "Saucony Triumph 21",
        "series": "트라이엄프",
        "category": "daily",
        "category_name": "데일리 / 쿠션화",
        "release_year": 2023,
        "gen_type": "carryover",
        "msrp_usd": 160,
        "msrp_krw": 179000,
        "widths": ["D", "2E"],
        "specs": {
            "weight_g": 279,
            "heel_drop_mm": 10,
            "midsole": "PWRRUN+ 풀렝스 비드 발포 폼",
            "plate": "없음",
            "stack_height": "37mm / 27mm",
            "support_type": "Neutral (탄력 넘치는 프리미엄 데일리)"
        },
        "runrepeat": {
            "score": 81,
            "midsole_foam": "PWRRUN+",
            "pros": [
                "영하의 겨울철에도 얼지 않고 쫄깃함을 유지하는 PWRRUN+ 폼",
                "부드러운 프리미엄 니트 어퍼"
            ],
            "cons": ["스피드 레이싱에는 부적합"],
            "verdict": "트라이엄프 22의 PB폼 이전, 든든한 탄성과 내구성으로 사랑받은 프리미엄 쿠션화.",
            "url": "https://runrepeat.com/saucony-triumph-21"
        }
    },
    {
        "id": "saucony_hurricane_24",
        "brand_id": "saucony",
        "name_kr": "써코니 허리케인 24",
        "name_en": "Saucony Hurricane 24",
        "series": "허리케인",
        "category": "stability",
        "category_name": "안정화 (과회내 서포트)",
        "release_year": 2024,
        "gen_type": "carryover",
        "msrp_usd": 160,
        "msrp_krw": 189000,
        "widths": ["D", "2E"],
        "specs": {
            "weight_g": 315,
            "heel_drop_mm": 6,
            "midsole": "PWRRUN PB (상단) + PWRRUN (하단) + Center Path",
            "plate": "없음",
            "stack_height": "40.5mm / 34.5mm",
            "support_type": "Stability (맥스쿠션 안정화)"
        },
        "runrepeat": {
            "score": 88,
            "midsole_foam": "PWRRUN PB & PWRRUN",
            "pros": [
                "안정화에 최초로 최상급 레이싱 폼(PWRRUN PB)을 결합",
                "하늘을 걷는 듯한 40mm 맥스 쿠셔닝과 완벽한 지지력"
            ],
            "cons": ["315g의 묵직한 중량"],
            "verdict": "허리케인 26 이전, 푹신함과 서포트를 동시에 잡으며 화려하게 부활했던 맥스 안정화.",
            "url": "https://runrepeat.com/saucony-hurricane-24"
        }
    },

    # --- HOKA (2 models) ---
    {
        "id": "hoka_clifton_8",
        "brand_id": "hoka",
        "name_kr": "호카 클리프톤 8",
        "name_en": "Hoka Clifton 8",
        "series": "클리프톤",
        "category": "daily",
        "category_name": "데일리 / 쿠션화",
        "release_year": 2023,
        "gen_type": "carryover",
        "msrp_usd": 140,
        "msrp_krw": 169000,
        "widths": ["D", "2E"],
        "specs": {
            "weight_g": 252,
            "heel_drop_mm": 5,
            "midsole": "압축 성형 EVA (CMEVA) + 얼리 메타로커",
            "plate": "없음",
            "stack_height": "32mm / 27mm",
            "support_type": "Neutral (클래식 국민 쿠션화)"
        },
        "runrepeat": {
            "score": 86,
            "midsole_foam": "CMEVA",
            "pros": [
                "호카의 명성을 전 세계에 알린 베스트셀러",
                "푹신한 발바닥 쿠션과 가벼운 무게",
                "아울렛/스마트스토어 10만원 미만 가성비"
            ],
            "cons": ["아치 부분이 다소 좁아 와이드 추천"],
            "verdict": "호카 입문용으로 가장 저렴하게 구할 수 있는 클래식 국민 쿠션화.",
            "url": "https://runrepeat.com/hoka-clifton-8"
        }
    },
    {
        "id": "hoka_mach_5",
        "brand_id": "hoka",
        "name_kr": "호카 마하 5",
        "name_en": "Hoka Mach 5",
        "series": "마하",
        "category": "super_trainer",
        "category_name": "슈퍼 트레이너",
        "release_year": 2023,
        "gen_type": "carryover",
        "msrp_usd": 140,
        "msrp_krw": 159000,
        "widths": ["D", "2E"],
        "specs": {
            "weight_g": 232,
            "heel_drop_mm": 5,
            "midsole": "PROFLY+ 듀얼 덴시티 폼",
            "plate": "없음",
            "stack_height": "29mm / 24mm",
            "support_type": "Neutral (초경량 템포 트레이너)"
        },
        "runrepeat": {
            "score": 82,
            "midsole_foam": "PROFLY+",
            "pros": [
                "232g 초경량에 플레이트 없이 자연스러운 탄력",
                "가벼운 템포런과 인터벌 최적화"
            ],
            "cons": ["고무 없는 노출 폼 아웃솔로 내구성이 다소 아쉬움"],
            "verdict": "가볍고 빠른 발놀림을 원하는 러너의 사랑을 받았던 경량 트레이너.",
            "url": "https://runrepeat.com/hoka-mach-5"
        }
    },

    # --- NEW BALANCE (2 models) ---
    {
        "id": "newbalance_1080_v13",
        "brand_id": "newbalance",
        "name_kr": "뉴발란스 프레시폼X 1080 v13",
        "name_en": "New Balance Fresh Foam X 1080 v13",
        "series": "1080",
        "category": "daily",
        "category_name": "데일리 / 쿠션화",
        "release_year": 2023,
        "gen_type": "carryover",
        "msrp_usd": 165,
        "msrp_krw": 199000,
        "widths": ["D", "2E", "4E"],
        "specs": {
            "weight_g": 262,
            "heel_drop_mm": 6,
            "midsole": "Fresh Foam X 울트라 소프트",
            "plate": "없음",
            "stack_height": "38mm / 32mm",
            "support_type": "Neutral (마시멜로 구름 쿠션)"
        },
        "runrepeat": {
            "score": 82,
            "midsole_foam": "Fresh Foam X",
            "pros": [
                "역대 모든 1080 중 가장 부드러운 마시멜로 쿠션",
                "발볼 2E, 4E 완벽 지원",
                "262g 가벼운 중량"
            ],
            "cons": ["지나치게 푹신하여 스피드런에는 힘 손실"],
            "verdict": "발바닥 충격을 완벽하게 흡수하는 구름 쿠션의 대명사.",
            "url": "https://runrepeat.com/new-balance-fresh-foam-x-1080-v-13"
        }
    },
    {
        "id": "newbalance_rebel_v3",
        "brand_id": "newbalance",
        "name_kr": "뉴발란스 퓨어셀 레벨 v3",
        "name_en": "New Balance FuelCell Rebel v3",
        "series": "레벨",
        "category": "super_trainer",
        "category_name": "슈퍼 트레이너",
        "release_year": 2023,
        "gen_type": "carryover",
        "msrp_usd": 130,
        "msrp_krw": 149000,
        "widths": ["D", "2E"],
        "specs": {
            "weight_g": 209,
            "heel_drop_mm": 6,
            "midsole": "FuelCell 고탄성 슈퍼폼",
            "plate": "없음",
            "stack_height": "27.5mm / 21.5mm",
            "support_type": "Neutral (깃털 무게 논플레이트 템포화)"
        },
        "runrepeat": {
            "score": 86,
            "midsole_foam": "FuelCell",
            "pros": [
                "209g의 경이로운 무게",
                "플레이트 없이 퓨어셀 폼의 통통 튀는 발구름",
                "착한 가격"
            ],
            "cons": ["v4 대비 밑창 폭이 다소 좁음"],
            "verdict": "가벼움과 폼 탄성만으로 경쾌한 달리기의 진수를 보여주는 가성비 스피드화.",
            "url": "https://runrepeat.com/new-balance-fuelcell-rebel-v3"
        }
    },

    # --- BROOKS (3 models) ---
    {
        "id": "brooks_ghost_16",
        "brand_id": "brooks",
        "name_kr": "브룩스 고스트 16",
        "name_en": "Brooks Ghost 16",
        "series": "고스트",
        "category": "daily",
        "category_name": "데일리 / 쿠션화",
        "release_year": 2024,
        "gen_type": "carryover",
        "msrp_usd": 140,
        "msrp_krw": 169000,
        "widths": ["D", "2E", "4E"],
        "specs": {
            "weight_g": 269,
            "heel_drop_mm": 12,
            "midsole": "DNA LOFT v3 (질소 주입 초임계 폼)",
            "plate": "없음",
            "stack_height": "35.5mm / 23.5mm",
            "support_type": "Neutral (질소폼 국민 데일리)"
        },
        "runrepeat": {
            "score": 85,
            "midsole_foam": "DNA LOFT v3",
            "pros": [
                "고스트 시리즈 최초로 질소 주입 DNA LOFT v3 탑재",
                "1,000km 뛰어도 끄떡없는 아웃솔 내구성",
                "힐 스트라이커 최적화"
            ],
            "cons": ["12mm 높은 힐드롭"],
            "verdict": "신형 17 출시 후 가격이 합리화된 브룩스의 완성형 국민 데일리화.",
            "url": "https://runrepeat.com/brooks-ghost-16"
        }
    },
    {
        "id": "brooks_ghost_15",
        "brand_id": "brooks",
        "name_kr": "브룩스 고스트 15",
        "name_en": "Brooks Ghost 15",
        "series": "고스트",
        "category": "daily",
        "category_name": "데일리 / 쿠션화",
        "release_year": 2023,
        "gen_type": "carryover",
        "msrp_usd": 140,
        "msrp_krw": 159000,
        "widths": ["D", "2E", "4E"],
        "specs": {
            "weight_g": 278,
            "heel_drop_mm": 12,
            "midsole": "DNA LOFT v2",
            "plate": "없음",
            "stack_height": "35mm / 23mm",
            "support_type": "Neutral (불멸의 8만원대 국민 조깅화)"
        },
        "runrepeat": {
            "score": 81,
            "midsole_foam": "DNA LOFT v2",
            "pros": [
                "7~8만원대 이월 러닝화 중 발 편함 원탑",
                "튼튼한 내구성과 넉넉한 발볼 옵션"
            ],
            "cons": ["클래식 EVA 기반으로 탄성은 평범"],
            "verdict": "고장 없이 1년 내내 조깅할 든든한 신발을 찾는 입문자용 가성비 이월화.",
            "url": "https://runrepeat.com/brooks-ghost-15"
        }
    },
    {
        "id": "brooks_adrenaline_gts_23",
        "brand_id": "brooks",
        "name_kr": "브룩스 아드레날린 GTS 23",
        "name_en": "Brooks Adrenaline GTS 23",
        "series": "아드레날린",
        "category": "stability",
        "category_name": "안정화 (과회내 서포트)",
        "release_year": 2023,
        "gen_type": "carryover",
        "msrp_usd": 140,
        "msrp_krw": 159000,
        "widths": ["D", "2E", "4E"],
        "specs": {
            "weight_g": 286,
            "heel_drop_mm": 12,
            "midsole": "DNA LOFT v2 + GuideRails 서포트",
            "plate": "없음 (가이드레일)",
            "stack_height": "36mm / 24mm",
            "support_type": "Stability (국민 안정화)"
        },
        "runrepeat": {
            "score": 81,
            "midsole_foam": "DNA LOFT v2",
            "pros": [
                "과회내를 가장 부드럽고 안전하게 잡아주는 가이드레일 범퍼",
                "발목 흔들림 제로"
            ],
            "cons": ["GTS 24 대비 질소폼이 아닌 클래식 폼"],
            "verdict": "무릎과 발목을 아끼는 러너들이 세일 때마다 쟁여두는 정통 안정화.",
            "url": "https://runrepeat.com/brooks-adrenaline-gts-23"
        }
    },

    # --- PUMA (1 model) ---
    {
        "id": "puma_deviate_nitro_2",
        "brand_id": "puma",
        "name_kr": "푸마 디비에이트 나이트로 2",
        "name_en": "Puma Deviate Nitro 2",
        "series": "디비에이트",
        "category": "super_trainer",
        "category_name": "슈퍼 트레이너",
        "release_year": 2023,
        "gen_type": "carryover",
        "msrp_usd": 160,
        "msrp_krw": 179000,
        "widths": ["D"],
        "specs": {
            "weight_g": 257,
            "heel_drop_mm": 6,
            "midsole": "NITRO Elite (상단) + NITRO (하단) + INNOPLATE",
            "plate": "INNOPLATE (카본 복합)",
            "stack_height": "38mm / 32mm",
            "support_type": "Neutral (가성비 1위 카본 트레이너)"
        },
        "runrepeat": {
            "score": 84,
            "midsole_foam": "NITRO Elite & NITRO",
            "pros": [
                "10만원 안팎에 카본 플레이트와 푸마그립(PUMAGRIP) 최강 접지력 확보",
                "매일 신는 카본 훈련화로 가성비 종결"
            ],
            "cons": ["디비에이트 3 대비 스택이 약간 낮음"],
            "verdict": "가장 저렴한 가격으로 고성능 카본 트레이너를 맛볼 수 있는 최고의 이월 명작.",
            "url": "https://runrepeat.com/puma-deviate-nitro-2"
        }
    },

    # --- MIZUNO (1 model) ---
    {
        "id": "mizuno_wave_rider_27",
        "brand_id": "mizuno",
        "name_kr": "미즈노 웨이브 라이더 27",
        "name_en": "Mizuno Wave Rider 27",
        "series": "웨이브 라이더",
        "category": "daily",
        "category_name": "데일리 / 쿠션화",
        "release_year": 2023,
        "gen_type": "carryover",
        "msrp_usd": 140,
        "msrp_krw": 159000,
        "widths": ["D", "2E", "4E"],
        "specs": {
            "weight_g": 280,
            "heel_drop_mm": 12,
            "midsole": "MIZUNO ENERZY + Wave Plate",
            "plate": "Mizuno Wave Plate",
            "stack_height": "38.5mm / 26.5mm",
            "support_type": "Neutral (정통 클래식 데일리)"
        },
        "runrepeat": {
            "score": 81,
            "midsole_foam": "MIZUNO ENERZY",
            "pros": [
                "단단하고 흔들림 없는 정통 클래식 데일리",
                "X10 카본 러버의 질긴 수명",
                "힐 스트라이커 12mm 드롭"
            ],
            "cons": ["푹신한 구름 쿠션을 원하면 다소 단단함"],
            "verdict": "흐물거리는 쿠션이 싫고 탄탄한 지지력을 원하는 러너를 위한 27년 전통의 러닝화.",
            "url": "https://runrepeat.com/mizuno-wave-rider-27"
        }
    },

    # --- ON RUNNING (1 model) ---
    {
        "id": "on_cloudmonster_1",
        "brand_id": "on",
        "name_kr": "온 클라우드몬스터 1",
        "name_en": "On Cloudmonster",
        "series": "클라우드몬스터",
        "category": "daily",
        "category_name": "데일리 / 쿠션화",
        "release_year": 2023,
        "gen_type": "carryover",
        "msrp_usd": 170,
        "msrp_krw": 209000,
        "widths": ["D"],
        "specs": {
            "weight_g": 275,
            "heel_drop_mm": 6,
            "midsole": "Helion 슈퍼폼 + 거대 CloudTec + Speedboard",
            "plate": "Speedboard",
            "stack_height": "35mm / 29mm",
            "support_type": "Neutral (익스트림 락커 몬스터)"
        },
        "runrepeat": {
            "score": 84,
            "midsole_foam": "Helion Superfoam",
            "pros": [
                "온 러닝의 판도를 바꾼 거대한 쿠션 구멍과 극단적 락커 롤링",
                "275g으로 몬스터 2보다 가벼움",
                "일상복에도 어울리는 미래지향적 디자인"
            ],
            "cons": ["클라우드 틈새에 자갈 끼임"],
            "verdict": "온 러닝의 상징적인 락커와 맥스 쿠셔닝을 경험할 수 있는 대표작.",
            "url": "https://runrepeat.com/on-cloudmonster"
        }
    }
]

def main():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    master_json_path = os.path.join(base_dir, "data", "shoes_master.json")
    
    with open(master_json_path, "r", encoding="utf-8") as f:
        current_shoes = json.load(f)
    
    # 1. Update existing 70 shoes with release_year & gen_type
    for s in current_shoes:
        if "gen_type" not in s:
            s["gen_type"] = "current"
        if "release_year" not in s:
            # Check if it's a known 2026 model
            name = s.get("name_en", "").lower()
            if any(k in name for k in ["revel max", "hurricane 26", "clifton pro", "nimbus 27", "novablast 5", "rise 2", "superblast 2", "cloudboom strike"]):
                s["release_year"] = 2026
            else:
                s["release_year"] = 2025

    # 2. Append the 24 carryover shoes if not already present
    existing_ids = set(s["id"] for s in current_shoes)
    added_count = 0
    for cs in CARRYOVER_SHOES:
        if cs["id"] not in existing_ids:
            current_shoes.append(cs)
            added_count += 1

    print(f"Loaded {len(current_shoes) - added_count} existing shoes.")
    print(f"Added {added_count} iconic carryover models.")
    print(f"Total shoes in master: {len(current_shoes)}")

    # 3. Save to data/shoes_master.json
    with open(master_json_path, "w", encoding="utf-8") as f:
        json.dump(current_shoes, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(current_shoes)} shoes to {master_json_path}")

    # 4. Save to data/brands_stores_config.json
    config_path = os.path.join(base_dir, "data", "brands_stores_config.json")
    with open(config_path, "r", encoding="utf-8") as f:
        config = json.load(f)
    
    config["generations"] = {
        "all": "전체 세대 (최신+이월)",
        "current": "✨ 2025-2026 최신형",
        "carryover": "🏷️ 2023-2024 이월할인 명작"
    }
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)
    print(f"Updated config with generation filters at {config_path}")

    # 5. Save data.js
    data_js_path = os.path.join(base_dir, "data.js")
    with open(data_js_path, "w", encoding="utf-8") as f:
        f.write("/** ShoeF Master Database (2023-2026 Full Master Dataset) **/\n")
        f.write("window.SHOEF_CONFIG = " + json.dumps(config, ensure_ascii=False, indent=2) + ";\n\n")
        f.write("window.SHOEF_MASTER = " + json.dumps(current_shoes, ensure_ascii=False, indent=2) + ";\n")
    print(f"Saved data.js at {data_js_path}")

if __name__ == "__main__":
    main()
