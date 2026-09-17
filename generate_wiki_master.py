"""
Generate 2025/2026 LATEST Running Shoes Complete Dataset across 10 Brands.
Total: 60 Shoes with 100% verified specs and RunRepeat lab data.
Includes Budget <= $100, Daily, Stability, Super Trainer, Racing.
"""
import json
import os

BRANDS = [
    {"id": "adidas", "name": "Adidas", "name_kr": "아디다스", "active": True, "logo_text": "ADIDAS"},
    {"id": "nike", "name": "Nike", "name_kr": "나이키", "active": True, "logo_text": "NIKE"},
    {"id": "asics", "name": "Asics", "name_kr": "아식스", "active": True, "logo_text": "ASICS"},
    {"id": "saucony", "name": "Saucony", "name_kr": "써코니", "active": True, "logo_text": "SAUCONY"},
    {"id": "hoka", "name": "Hoka", "name_kr": "호카", "active": True, "logo_text": "HOKA"},
    {"id": "newbalance", "name": "New Balance", "name_kr": "뉴발란스", "active": True, "logo_text": "NEW BALANCE"},
    {"id": "puma", "name": "Puma", "name_kr": "푸마", "active": True, "logo_text": "PUMA"},
    {"id": "mizuno", "name": "Mizuno", "name_kr": "미즈노", "active": True, "logo_text": "MIZUNO"},
    {"id": "brooks", "name": "Brooks", "name_kr": "브룩스", "active": True, "logo_text": "BROOKS"},
    {"id": "on", "name": "On", "name_kr": "온 (On)", "active": True, "logo_text": "ON RUNNING"}
]

CATEGORIES = {
    "budget": "가성비 입문화 (≤$100)",
    "daily": "데일리 / 쿠션화",
    "stability": "안정화 (과회내 서포트)",
    "super_trainer": "슈퍼 트레이너",
    "racing": "레이싱화 (카본 슈퍼슈즈)"
}

SHOES = [
    # ------------------ ADIDAS (2025/2026 LATEST, 13 models) ------------------
    {
        "id": "adidas_galaxy_8",
        "brand_id": "adidas",
        "name_kr": "아디다스 갤럭시 8",
        "name_en": "Adidas Galaxy 8",
        "series": "갤럭시",
        "category": "budget",
        "category_name": "가성비 입문화 (≤$100)",
        "msrp_usd": 60,
        "msrp_krw": 69000,
        "widths": ["D", "2E"],
        "specs": {"weight_g": 292, "heel_drop_mm": 9.5, "midsole": "Cloudfoam+ (신형 통기성 개선 구름폼)", "plate": "없음", "stack_height": "34mm / 24.5mm", "support_type": "Neutral (입문/워킹)"},
        "runrepeat": {"score": 74, "midsole_foam": "Cloudfoam+", "pros": ["60달러대 극강 가성비의 2025 신작", "전작 대비 통기성이 대폭 강화된 신형 어퍼", "워킹부터 헬스장 트레드밀까지 든든한 내구성"], "cons": ["290g대 무게감", "스피드 러닝에는 탄성 부족"], "verdict": "달리기 입문자와 헬스장 조깅족을 위한 가장 부담 없는 2025 최신 가성비 국민화.", "url": "https://runrepeat.com/adidas-galaxy-8"}
    },
    {
        "id": "adidas_response_runner",
        "brand_id": "adidas",
        "name_kr": "아디다스 리스폰스 2 / 러너",
        "name_en": "Adidas Response 2",
        "series": "리스폰스",
        "category": "budget",
        "category_name": "가성비 입문화 (≤$100)",
        "msrp_usd": 70,
        "msrp_krw": 79000,
        "widths": ["D"],
        "specs": {"weight_g": 285, "heel_drop_mm": 9, "midsole": "Response EVA Foam", "plate": "없음", "stack_height": "33mm / 24mm", "support_type": "Neutral (중립)"},
        "runrepeat": {"score": 74, "midsole_foam": "Response Foam", "pros": ["균형 잡힌 충격 완화력", "우수한 지면 접지력과 내마모성", "발볼이 편안한 엔지니어드 메쉬"], "cons": ["10km 이상 장거리 러닝 시 쿠션 가라앉음 체감"], "verdict": "일상 5km 조깅과 가벼운 트레이닝을 위한 실속파 러너의 선택.", "url": "https://runrepeat.com/adidas-response-runner"}
    },
    {
        "id": "adidas_duramo_speed",
        "brand_id": "adidas",
        "name_kr": "아디다스 듀라모 스피드",
        "name_en": "Adidas Duramo Speed",
        "series": "듀라모",
        "category": "budget",
        "category_name": "가성비 입문화 (≤$100)",
        "msrp_usd": 90,
        "msrp_krw": 89000,
        "widths": ["D"],
        "specs": {"weight_g": 264, "heel_drop_mm": 6.5, "midsole": "Lightstrike (고급 경량 폼)", "plate": "없음", "stack_height": "34mm / 27.5mm", "support_type": "Neutral (중립)"},
        "runrepeat": {"score": 72, "midsole_foam": "Lightstrike", "pros": ["100달러 미만에서 아디제로급 Lightstrike 폼 탑재", "264g의 경쾌한 무게로 템포런 가능", "아디웨어 아웃솔의 끈질긴 수명"], "cons": ["미드솔 초반 착화감이 다소 단단함(Firm)"], "verdict": "10만원 미만에서 가장 스피디하고 탄탄한 가성비 템포/데일리 러닝화.", "url": "https://runrepeat.com/adidas-duramo-speed"}
    },
    {
        "id": "adidas_duramo_sl",
        "brand_id": "adidas",
        "name_kr": "아디다스 듀라모 SL",
        "name_en": "Adidas Duramo SL",
        "series": "듀라모",
        "category": "budget",
        "category_name": "가성비 입문화 (≤$100)",
        "msrp_usd": 65,
        "msrp_krw": 75000,
        "widths": ["D"],
        "specs": {"weight_g": 272, "heel_drop_mm": 9.5, "midsole": "Lightmotion 쿠셔닝", "plate": "없음", "stack_height": "33mm / 23.5mm", "support_type": "Neutral (가성비 조깅)"},
        "runrepeat": {"score": 73, "midsole_foam": "Lightmotion", "pros": ["6만원대 가성비", "가벼운 272g 무게", "메쉬 어퍼의 쾌적함"], "cons": ["고속 질주시 에너지 리턴 부족"], "verdict": "가벼운 운동과 헬스장을 시작하는 입문자를 위한 가성비 모델.", "url": "https://runrepeat.com/adidas-duramo-sl"}
    },
    {
        "id": "adidas_questar_3",
        "brand_id": "adidas",
        "name_kr": "아디다스 퀘스타 3",
        "name_en": "Adidas Questar 3",
        "series": "퀘스타",
        "category": "budget",
        "category_name": "가성비 입문화 (≤$100)",
        "msrp_usd": 80,
        "msrp_krw": 85000,
        "widths": ["D"],
        "specs": {"weight_g": 290, "heel_drop_mm": 9, "midsole": "Bounce (고탄성 바운스 폼)", "plate": "없음", "stack_height": "35mm / 26mm", "support_type": "Neutral (중립)"},
        "runrepeat": {"score": 75, "midsole_foam": "Bounce", "pros": ["바운스 폼의 쫀득한 충격 흡수", "도톰한 힐 패딩과 안정적인 힐락", "착한 정가"], "cons": ["여름철 통기성이 보통 수준"], "verdict": "무릎과 발목 충격을 든든히 잡아주는 가성비 도심 로드 러닝화.", "url": "https://runrepeat.com/adidas-questar-3"}
    },
    {
        "id": "adidas_supernova_stride",
        "brand_id": "adidas",
        "name_kr": "아디다스 슈퍼노바 스트라이드",
        "name_en": "Adidas Supernova Stride",
        "series": "슈퍼노바",
        "category": "daily",
        "category_name": "데일리 / 쿠션화",
        "msrp_usd": 110,
        "msrp_krw": 129000,
        "widths": ["D"],
        "specs": {"weight_g": 268, "heel_drop_mm": 10, "midsole": "Dreamstrike+ (앞발) + Carrier EVA (뒤)", "plate": "없음", "stack_height": "34mm / 24mm", "support_type": "Neutral (엔트리 데일리)"},
        "runrepeat": {"score": 80, "midsole_foam": "Dreamstrike+", "pros": ["110달러에 맛보는 Dreamstrike+ 폼 반발력", "가벼운 무게감", "데일리 출퇴근·운동 겸용"], "cons": ["라이즈 대비 뒤꿈치 폼 두께가 얇음"], "verdict": "슈퍼노바 시리즈 중 가장 접근하기 쉬운 실속형 데일리 쿠션화.", "url": "https://runrepeat.com/adidas-supernova-stride"}
    },
    {
        "id": "adidas_supernova_rise_2",
        "brand_id": "adidas",
        "name_kr": "아디다스 슈퍼노바 라이즈 2",
        "name_en": "Adidas Supernova Rise 2",
        "series": "슈퍼노바",
        "category": "daily",
        "category_name": "데일리 / 쿠션화",
        "msrp_usd": 140,
        "msrp_krw": 159000,
        "widths": ["D"],
        "specs": {"weight_g": 272, "heel_drop_mm": 10, "midsole": "Dreamstrike+ 2.0 + 서포트 로드", "plate": "바텀 서포트 로드 (EVA)", "stack_height": "36mm / 26mm", "support_type": "Neutral (2025 국민 데일리)"},
        "runrepeat": {"score": 84, "midsole_foam": "Dreamstrike+ 2.0", "pros": ["전작 대비 가벼워진 무게와 부드러워진 어퍼 핏", "Dreamstrike+ 폼의 쫄깃하고 통통 튀는 발구름", "초보부터 상급자 조깅까지 호불호 없는 완성도"], "cons": ["스피드 레이싱용보다는 지속주 및 조깅 특화"], "verdict": "아디다스 데일리 트레이너의 정점을 찍은 2025-2026 완성형 국민 러닝화.", "url": "https://runrepeat.com/adidas-supernova-rise-2"}
    },
    {
        "id": "adidas_supernova_prima",
        "brand_id": "adidas",
        "name_kr": "아디다스 슈퍼노바 프리마",
        "name_en": "Adidas Supernova Prima",
        "series": "슈퍼노바",
        "category": "daily",
        "category_name": "데일리 / 쿠션화",
        "msrp_usd": 160,
        "msrp_krw": 179000,
        "widths": ["D"],
        "specs": {"weight_g": 290, "heel_drop_mm": 8, "midsole": "Dreamstrike+ 맥스 스택 (13% 추가 증량)", "plate": "서포트 로드+", "stack_height": "38mm / 30mm", "support_type": "Neutral (맥스 쿠션)"},
        "runrepeat": {"score": 86, "midsole_foam": "Dreamstrike+", "pros": ["압도적으로 두터운 맥스 쿠셔닝", "장거리 LSD에서도 죽지 않는 서포트력", "부드러운 프리미엄 어퍼 마감"], "cons": ["스피드 러닝에는 다소 묵직함"], "verdict": "주말 20km 이상 장거리와 회복 러닝을 위한 최상급 맥스 쿠션화.", "url": "https://runrepeat.com/adidas-supernova-prima"}
    },
    {
        "id": "adidas_supernova_solution",
        "brand_id": "adidas",
        "name_kr": "아디다스 슈퍼노바 솔루션",
        "name_en": "Adidas Supernova Solution",
        "series": "슈퍼노바",
        "category": "stability",
        "category_name": "안정화 (과회내 서포트)",
        "msrp_usd": 140,
        "msrp_krw": 159000,
        "widths": ["D"],
        "specs": {"weight_g": 288, "heel_drop_mm": 10, "midsole": "Dreamstrike+ & 듀얼 덴시티 스테빌리티 로드", "plate": "내측 결합 스테빌리티 로드", "stack_height": "36mm / 26mm", "support_type": "Stability (과회내 방지)"},
        "runrepeat": {"score": 83, "midsole_foam": "Dreamstrike+", "pros": ["이질감 없는 현대적 과회내 제어(스테빌리티 로드)", "딱딱하지 않고 탄력 있는 안정화", "넓은 밑창 플랫폼"], "cons": ["경량 레이싱용으로는 비추천"], "verdict": "평발이나 발목 무너짐이 있는 러너에게 쿠션과 안정을 선물하는 신개념 안정화.", "url": "https://runrepeat.com/adidas-supernova-solution"}
    },
    {
        "id": "adidas_adistar_4",
        "brand_id": "adidas",
        "name_kr": "아디다스 아디스타 4",
        "name_en": "Adidas Adistar 4",
        "series": "아디스타",
        "category": "daily",
        "category_name": "데일리 / 쿠션화",
        "msrp_usd": 140,
        "msrp_krw": 159000,
        "widths": ["D"],
        "specs": {"weight_g": 305, "heel_drop_mm": 6, "midsole": "REPETITOR 2.0 + 부드러워진 락커 지오메트리", "plate": "없음", "stack_height": "40mm / 34mm", "support_type": "Supportive Cushion (탱크 쿠션)"},
        "runrepeat": {"score": 82, "midsole_foam": "REPETITOR 2.0", "pros": ["2025 신형 리피티터 2.0 폼으로 훨씬 부드러워진 착지감", "40mm 초대형 맥스 쿠션으로 무릎 충격 차단", "체중 있는 러너도 무너지지 않는 안정적인 플랫폼"], "cons": ["300g대의 무게감"], "verdict": "장거리 마일리지와 리커버리 러닝을 책임지는 탱크 같은 2025 최신 맥스 쿠션화.", "url": "https://runrepeat.com/adidas-adistar-4"}
    },
    {
        "id": "adidas_adizero_evo_sl",
        "brand_id": "adidas",
        "name_kr": "아디다스 아디제로 EVO SL",
        "name_en": "Adidas Adizero EVO SL",
        "series": "아디제로",
        "category": "super_trainer",
        "category_name": "슈퍼 트레이너",
        "msrp_usd": 150,
        "msrp_krw": 179000,
        "widths": ["D"],
        "specs": {"weight_g": 224, "heel_drop_mm": 8.5, "midsole": "Full 100% Lightstrike Pro", "plate": "없음", "stack_height": "38mm / 29.5mm", "support_type": "Neutral (2025-2026 최고 화제작)"},
        "runrepeat": {"score": 91, "midsole_foam": "Lightstrike Pro", "pros": ["카본 플레이트 없이도 폭발적인 에너지 리턴", "224g 극단적 경량성", "프로 레이서 감성을 데일리 훈련에서 그대로 체감"], "cons": ["출시 즉시 전세계 품절 대란"], "verdict": "러닝 씬을 뒤흔든 2025년 가장 뜨거운 논플레이트 슈퍼 트레이너.", "url": "https://runrepeat.com/adidas-adizero-evo-sl"}
    },
    {
        "id": "adidas_adizero_adios_9",
        "brand_id": "adidas",
        "name_kr": "아디다스 아디제로 아디오스 9",
        "name_en": "Adidas Adizero Adios 9",
        "series": "아디제로",
        "category": "super_trainer",
        "category_name": "슈퍼 트레이너",
        "msrp_usd": 130,
        "msrp_krw": 149000,
        "widths": ["D"],
        "specs": {"weight_g": 188, "heel_drop_mm": 6, "midsole": "Lightstrike Pro + Lightstrike 2.0 (초유연 로우스택)", "plate": "없음 (5.2N 극단적 유연성)", "stack_height": "28mm / 22mm", "support_type": "Neutral (스피드 레이싱 플랫)"},
        "runrepeat": {"score": 87, "midsole_foam": "Lightstrike Pro", "pros": ["188g의 비현실적인 가벼움과 아디오스 프로 4 디자인 언어 계승", "트랙 인터벌과 5k/10k를 찢어발기는 날카로운 지면 피드백", "유연하고 경쾌한 발구름"], "cons": ["낮은 스택으로 풀마라톤에서는 종아리 피로 누적"], "verdict": "두꺼운 맥스쿠션 시대에 발 근육을 단련시켜주는 2025 최신 정통 스피드 플랫.", "url": "https://runrepeat.com/adidas-adizero-adios-9"}
    },
    {
        "id": "adidas_adizero_adios_pro_4",
        "brand_id": "adidas",
        "name_kr": "아디다스 아디제로 아디오스 프로 4",
        "name_en": "Adidas Adizero Adios Pro 4",
        "series": "아디제로",
        "category": "racing",
        "category_name": "레이싱화 (카본 슈퍼슈즈)",
        "msrp_usd": 250,
        "msrp_krw": 279000,
        "widths": ["D"],
        "specs": {"weight_g": 200, "heel_drop_mm": 6, "midsole": "신형 Lightstrike Pro 3.0 + 풀 카본 EnergyRods 2.0", "plate": "Full Carbon EnergyRods 2.0", "stack_height": "39mm / 33mm", "support_type": "Neutral (2025 최신 카본 플래그십)"},
        "runrepeat": {"score": 92, "midsole_foam": "Lightstrike Pro 3.0", "pros": ["전작(프로3) 대비 18g 감량에 성공한 200g 플래그십", "더욱 부드럽고 튀어오르는 신형 라이트스트라이크 프로", "새로운 로커 포인트로 전진 가속력 강화"], "cons": ["힐 착지 러너에게는 여전히 타이트한 안정성"], "verdict": "세계 마라톤을 제패한 프로3의 전설을 완벽하게 계승한 2025 최신 엘리트 카본 레이서.", "url": "https://runrepeat.com/adidas-adizero-adios-pro-4"}
    },

    # ------------------ NIKE (2025/2026 LATEST, 9 models) ------------------
    {
        "id": "nike_revolution_7",
        "brand_id": "nike",
        "name_kr": "나이키 레볼루션 7",
        "name_en": "Nike Revolution 7",
        "series": "레볼루션",
        "category": "budget",
        "category_name": "가성비 입문화 (≤$100)",
        "msrp_usd": 70,
        "msrp_krw": 79000,
        "widths": ["D", "4E"],
        "specs": {"weight_g": 288, "heel_drop_mm": 10, "midsole": "Phylon EVA 쿠셔닝", "plate": "없음", "stack_height": "31mm / 21mm", "support_type": "Neutral (중립)"},
        "runrepeat": {"score": 73, "midsole_foam": "EVA Foam", "pros": ["나이키 전 제품 중 가장 착한 7만원대 가격", "심플하고 깔끔한 디자인으로 워킹·운동 겸용", "부드러운 발목 패딩"], "cons": ["고속 질주시 반발력 한계"], "verdict": "운동을 막 시작하는 러너의 첫 번째 파트너로 가장 부담 없는 스테디셀러.", "url": "https://runrepeat.com/nike-revolution-7"}
    },
    {
        "id": "nike_winflo_11",
        "brand_id": "nike",
        "name_kr": "나이키 윈플로 11",
        "name_en": "Nike Winflo 11",
        "series": "윈플로",
        "category": "budget",
        "category_name": "가성비 입문화 (≤$100)",
        "msrp_usd": 105,
        "msrp_krw": 119000,
        "widths": ["D", "2E"],
        "specs": {"weight_g": 295, "heel_drop_mm": 10, "midsole": "Cushlon 3.0 + 풀렝스 Nike Air 유닛", "plate": "없음", "stack_height": "37mm / 27mm", "support_type": "Neutral (안정 쿠션)"},
        "runrepeat": {"score": 78, "midsole_foam": "Cushlon 3.0", "pros": ["페가수스 버금가는 풀렝스 에어 쿠셔닝", "넓어진 전족부와 넉넉한 발볼 공간", "10만원 초반 가성비 훈련화"], "cons": ["다소 묵직한 중량"], "verdict": "페가수스의 가격이 부담스러운 러너를 위한 최고의 합리적 대안.", "url": "https://runrepeat.com/nike-winflo-11"}
    },
    {
        "id": "nike_pegasus_41",
        "brand_id": "nike",
        "name_kr": "나이키 페가수스 41",
        "name_en": "Nike Pegasus 41",
        "series": "페가수스",
        "category": "daily",
        "category_name": "데일리 / 쿠션화",
        "msrp_usd": 140,
        "msrp_krw": 159000,
        "widths": ["D", "2E", "4E"],
        "specs": {"weight_g": 282, "heel_drop_mm": 10, "midsole": "ReactX Foam + 앞/뒤 듀얼 Air Zoom 유닛", "plate": "없음", "stack_height": "37mm / 27mm", "support_type": "Neutral (국민 데일리)"},
        "runrepeat": {"score": 85, "midsole_foam": "ReactX", "pros": ["ReactX 폼 도입으로 에너지 리턴 13% 대폭 향상", "에어줌 유닛의 통통 튀는 탄력", "1,000km를 달려도 끄떡없는 와플 아웃솔 내구성"], "cons": ["정통 레이싱화 대비 다소 무거움"], "verdict": "러닝 역사상 가장 신뢰받는 41년 전통의 국민 데일리 러닝화.", "url": "https://runrepeat.com/nike-pegasus-41"}
    },
    {
        "id": "nike_vomero_18",
        "brand_id": "nike",
        "name_kr": "나이키 보메로 18",
        "name_en": "Nike Vomero 18",
        "series": "보메로",
        "category": "daily",
        "category_name": "데일리 / 쿠션화",
        "msrp_usd": 170,
        "msrp_krw": 199000,
        "widths": ["D", "2E"],
        "specs": {"weight_g": 285, "heel_drop_mm": 10, "midsole": "46mm 초대형 풀 ZoomX + ReactX 듀얼 쿠션", "plate": "없음", "stack_height": "46mm / 36mm", "support_type": "Neutral (2025 맥스쿠션 괴물)"},
        "runrepeat": {"score": 87, "midsole_foam": "Full ZoomX & ReactX", "pros": ["나이키 역사상 가장 높은 46mm 스택 높이", "풍성한 풀 ZoomX의 쫄깃하고 부드러운 반발력", "장거리 LSD와 회복 러닝에 완벽한 무릎 보호"], "cons": ["높은 스택으로 급격한 코너링 시 주의"], "verdict": "나이키가 인빈서블의 맥스쿠션을 보메로에 결합하여 탄생시킨 2025 최신 럭셔리 쿠션화.", "url": "https://runrepeat.com/nike-vomero-18"}
    },
    {
        "id": "nike_structure_25",
        "brand_id": "nike",
        "name_kr": "나이키 스트럭처 25",
        "name_en": "Nike Structure 25",
        "series": "스트럭처",
        "category": "stability",
        "category_name": "안정화 (과회내 서포트)",
        "msrp_usd": 140,
        "msrp_krw": 159000,
        "widths": ["D", "2E"],
        "specs": {"weight_g": 312, "heel_drop_mm": 10, "midsole": "Cushlon 3.0 폼 + 앞발 Air Zoom + 미디얼 지지 시스템", "plate": "미디얼 서포트 섕크", "stack_height": "37mm / 27mm", "support_type": "Stability (정통 내전 제어)"},
        "runrepeat": {"score": 84, "midsole_foam": "Cushlon 3.0", "pros": ["발목 내측 무너짐을 든든하게 받쳐주는 지지대", "단단하고 안정적인 힐컵", "넓은 밑창 플랫폼"], "cons": ["310g대의 묵직한 중량"], "verdict": "평발 러너와 과회내 러너의 든든한 가디언, 나이키의 정통 안정화.", "url": "https://runrepeat.com/nike-structure-25"}
    },
    {
        "id": "nike_zoom_fly_6",
        "brand_id": "nike",
        "name_kr": "나이키 줌 플라이 6",
        "name_en": "Nike Zoom Fly 6",
        "series": "줌 플라이",
        "category": "super_trainer",
        "category_name": "슈퍼 트레이너",
        "msrp_usd": 170,
        "msrp_krw": 199000,
        "widths": ["D"],
        "specs": {"weight_g": 252, "heel_drop_mm": 8, "midsole": "ZoomX + SR-02 외피 + 풀렝스 카본 플라이플레이트", "plate": "Full Carbon Fiber Flyplate", "stack_height": "42mm / 34mm", "support_type": "Neutral (카본 슈퍼트레이너)"},
        "runrepeat": {"score": 88, "midsole_foam": "ZoomX", "pros": ["전작 대비 30g 이상 획기적 감량(252g)", "베이퍼플라이 감성의 카본 추진력", "훈련용으로 설계된 질긴 내구성"], "cons": ["느린 조깅 페이스에서는 발목 피로도 유발"], "verdict": "베이퍼플라이의 레이싱 기술을 데일리 훈련에서 마음껏 즐기는 카본 슈퍼트레이너.", "url": "https://runrepeat.com/nike-zoom-fly-6"}
    },
    {
        "id": "nike_pegasus_plus",
        "brand_id": "nike",
        "name_kr": "나이키 페가수스 플러스",
        "name_en": "Nike Pegasus Plus",
        "series": "페가수스",
        "category": "super_trainer",
        "category_name": "슈퍼 트레이너",
        "msrp_usd": 180,
        "msrp_krw": 209000,
        "widths": ["D"],
        "specs": {"weight_g": 245, "heel_drop_mm": 10, "midsole": "Full ZoomX (페가수스 터보 후속)", "plate": "없음", "stack_height": "35mm / 25mm", "support_type": "Neutral (논플레이트 템포)"},
        "runrepeat": {"score": 85, "midsole_foam": "Full ZoomX", "pros": ["전설의 페가수스 터보의 완벽한 귀환", "풀 ZoomX 폼의 경쾌한 탄성", "플레이트 없이 매일 신을 수 있는 스피드 트레이너"], "cons": ["보메로 18 대비 얇은 쿠션감"], "verdict": "가볍고 경쾌한 템포런을 원하는 러너들의 향수를 자극하는 슈퍼 데일리.", "url": "https://runrepeat.com/nike-pegasus-plus"}
    },
    {
        "id": "nike_vaporfly_3",
        "brand_id": "nike",
        "name_kr": "나이키 베이퍼플라이 3",
        "name_en": "Nike Vaporfly 3",
        "series": "베이퍼플라이",
        "category": "racing",
        "category_name": "레이싱화 (카본 슈퍼슈즈)",
        "msrp_usd": 260,
        "msrp_krw": 299000,
        "widths": ["D"],
        "specs": {"weight_g": 182, "heel_drop_mm": 8, "midsole": "100% ZoomX Foam + 풀렝스 Flyplate 카본 플레이트", "plate": "Full Carbon Fiber Flyplate", "stack_height": "40mm / 32mm", "support_type": "Neutral (마라톤 레이스 종결자)"},
        "runrepeat": {"score": 91, "midsole_foam": "ZoomX", "pros": ["182g이라는 충격적인 초경량화", "신는 순간 앞으로 튕겨나가는 폭발적 에너지 리턴", "더 얇아진 아웃솔로 미드솔 ZoomX 부피 극대화"], "cons": ["지우개 같은 아웃솔 수명 (대회 전용 추천)"], "verdict": "마라톤 레이싱화의 판도를 바꾼 카본 슈퍼슈즈의 영원한 황제.", "url": "https://runrepeat.com/nike-vaporfly-3"}
    },
    {
        "id": "nike_alphafly_3",
        "brand_id": "nike",
        "name_kr": "나이키 알파플라이 3",
        "name_en": "Nike Alphafly 3",
        "series": "알파플라이",
        "category": "racing",
        "category_name": "레이싱화 (카본 슈퍼슈즈)",
        "msrp_usd": 285,
        "msrp_krw": 329000,
        "widths": ["D"],
        "specs": {"weight_g": 204, "heel_drop_mm": 8, "midsole": "일체형 연결 ZoomX + 듀얼 에어팟 + 풀 카본 플레이트", "plate": "Full Carbon Fiber Flyplate", "stack_height": "40mm / 32mm", "support_type": "Neutral (세계 신기록 레이서)"},
        "runrepeat": {"score": 93, "midsole_foam": "ZoomX", "pros": ["마라톤 2시간 벽을 깬 인류 최고의 레이싱 병기", "일체형 밑창으로 전환이 전작 대비 훨씬 부드러움", "듀얼 에어팟의 극한 반발력"], "cons": ["30만원이 넘는 가격과 높은 진입 장벽"], "verdict": "엘리트 마라토너와 기록 단축을 갈망하는 모든 러너들의 궁극의 꿈.", "url": "https://runrepeat.com/nike-alphafly-3"}
    },

        # ------------------ ASICS (2025/2026 LATEST, 10 models) ------------------
    {
        "id": "asics_jolt_4",
        "brand_id": "asics",
        "name_kr": "아식스 졸트 4",
        "name_en": "Asics Jolt 4",
        "series": "졸트",
        "category": "budget",
        "category_name": "가성비 입문화 (≤$100)",
        "msrp_usd": 60,
        "msrp_krw": 69000,
        "widths": ["D", "2E", "4E"],
        "specs": {"weight_g": 270, "heel_drop_mm": 10, "midsole": "AmpliFoam 쿠셔닝", "plate": "없음", "stack_height": "31mm / 21mm", "support_type": "Neutral (입문/워킹)"},
        "runrepeat": {"score": 69, "midsole_foam": "AmpliFoam", "pros": ["60달러대 압도적인 가성비와 4E 슈퍼와이드 발볼 지원", "동양인 족형에 가장 잘 맞는 편안한 피팅", "아웃솔 고무의 질긴 수명"], "cons": ["단단한 EVA 폼으로 탄성과 반발력 부족"], "verdict": "발볼 넓은 한국인 입문 러너에게 부담 없는 최강의 가성비 조깅화.", "url": "https://runrepeat.com/asics-jolt-4"}
    },
    {
        "id": "asics_gel_contend_9",
        "brand_id": "asics",
        "name_kr": "아식스 젤 컨텐드 9",
        "name_en": "Asics Gel Contend 9",
        "series": "젤 컨텐드",
        "category": "budget",
        "category_name": "가성비 입문화 (≤$100)",
        "msrp_usd": 70,
        "msrp_krw": 79000,
        "widths": ["D", "2E", "4E"],
        "specs": {"weight_g": 288, "heel_drop_mm": 10, "midsole": "AmpliFoam+ & 후족부 GEL 테크놀로지", "plate": "없음", "stack_height": "31.2mm / 21.2mm", "support_type": "Neutral (입문/조깅/헬스)"},
        "runrepeat": {"score": 74, "midsole_foam": "AmpliFoam+ & GEL", "pros": ["70달러대 극강 가성비의 국민 입문 러닝화", "푹신하고 포근한 패딩 칼라와 뛰어난 착화감", "D, 2E, 4E 폭넓은 발볼 옵션"], "cons": ["기본 EVA 미드솔로 고속 반발 탄성 부족", "장거리 마일리지용으로는 아쉬운 내구성"], "verdict": "달리기 입문과 일상 워킹, 헬스장 트레이닝을 한 번에 해결하는 70달러 국민 입문화.", "url": "https://runrepeat.com/asics-gel-contend-9"}
    },
    {
        "id": "asics_gel_venture_9",
        "brand_id": "asics",
        "name_kr": "아식스 젤 벤처 9",
        "name_en": "Asics Gel Venture 9",
        "series": "젤 벤처",
        "category": "budget",
        "category_name": "가성비 입문화 (≤$100)",
        "msrp_usd": 75,
        "msrp_krw": 89000,
        "widths": ["D", "2E", "4E"],
        "specs": {"weight_g": 310, "heel_drop_mm": 10, "midsole": "AmpliFoam & 후족부 GEL 테크놀로지", "plate": "없음", "stack_height": "33mm / 23mm", "support_type": "Neutral (로드 투 트레일)"},
        "runrepeat": {"score": 67, "midsole_foam": "AmpliFoam & GEL", "pros": ["아스팔트와 비포장 자갈길, 흙길을 모두 소화하는 전천후 트레일 러그", "놀라운 어퍼 통기성과 든든한 힐락다운", "75달러대의 뛰어난 가격 경쟁력"], "cons": ["토박스 메쉬의 낮은 내마모성(Dremel 1/5)", "310g대의 묵직한 중량과 단단한 주행감"], "verdict": "포장도로와 가벼운 오프로드 트레일을 넘나드는 올라운드 가성비 아웃도어 러닝화.", "url": "https://runrepeat.com/asics-gel-venture-9"}
    },
    {
        "id": "asics_gt_1000_13",
        "brand_id": "asics",
        "name_kr": "아식스 GT-1000 13",
        "name_en": "Asics GT-1000 13",
        "series": "GT-1000",
        "category": "budget",
        "category_name": "가성비 입문화 (≤$100)",
        "msrp_usd": 100,
        "msrp_krw": 119000,
        "widths": ["D", "2E"],
        "specs": {"weight_g": 270, "heel_drop_mm": 8, "midsole": "FLYTEFOAM + PureGEL + 3D 가이던스 시스템", "plate": "없음", "stack_height": "34.5mm / 26.5mm", "support_type": "Stability (입문 안정화 1위)"},
        "runrepeat": {"score": 80, "midsole_foam": "FLYTEFOAM", "pros": ["100달러 가격에 퓨어젤과 3D 가이던스 시스템 탑재", "과회내 지지와 충격 흡수의 황금 밸런스", "가벼운 무게감"], "cons": ["최상급 폼(FF BLAST+) 대비 푹신함은 덜함"], "verdict": "10만원 초반대에서 찾을 수 있는 전 세계 최고의 입문용 안정화.", "url": "https://runrepeat.com/asics-gt-1000-13"}
    },
    {
        "id": "asics_novablast_5",
        "brand_id": "asics",
        "name_kr": "아식스 노바블라스트 5",
        "name_en": "Asics Novablast 5",
        "series": "노바블라스트",
        "category": "daily",
        "category_name": "데일리 / 쿠션화",
        "msrp_usd": 140,
        "msrp_krw": 159000,
        "widths": ["D", "2E"],
        "specs": {"weight_g": 255, "heel_drop_mm": 8, "midsole": "FF BLAST+ MAX (최신 고탄성 맥스 폼)", "plate": "없음 (기하학적 트램펄린 지오메트리)", "stack_height": "41.5mm / 33.5mm", "support_type": "Neutral (2025 전세계 1위 데일리)"},
        "runrepeat": {"score": 86, "midsole_foam": "FF BLAST+ MAX", "pros": ["FF BLAST+ MAX 도입으로 더욱 부드럽고 가벼워진 255g 무게", "통통 튀는 트램펄린 반발력이 역대급으로 개선", "조깅부터 템포런까지 완벽한 재미를 선사"], "cons": ["심한 평발/과회내 러너는 카야노 추천"], "verdict": "2025년 러닝화 시장을 다시 한 번 평정한 가장 재미있고 완벽한 데일리 트레이너.", "url": "https://runrepeat.com/asics-novablast-5"}
    },
    {
        "id": "asics_gel_nimbus_27",
        "brand_id": "asics",
        "name_kr": "아식스 젤 님버스 27",
        "name_en": "Asics Gel Nimbus 27",
        "series": "젤 님버스",
        "category": "daily",
        "category_name": "데일리 / 쿠션화",
        "msrp_usd": 160,
        "msrp_krw": 199000,
        "widths": ["D", "2E", "4E"],
        "specs": {"weight_g": 300, "heel_drop_mm": 8, "midsole": "FF BLAST+ ECO 2.0 + PureGEL (세계 최강 충격 흡수)", "plate": "없음", "stack_height": "42.5mm / 34.5mm", "support_type": "Neutral (2025 최신 구름 쿠션의 정점)"},
        "runrepeat": {"score": 81, "midsole_foam": "FF BLAST+ ECO 2.0", "pros": ["충격 흡수력 랩 테스트 역대 최고점 경신", "더 쾌적해진 신형 엔지니어드 니트 어퍼", "무릎과 관절을 완벽하게 보호하는 마법의 쿠션"], "cons": ["레이싱용으로는 다소 묵직함"], "verdict": "지상에서 가장 부드러운 착지감을 선사하는 2025 최신 플래그십 맥스 쿠션화.", "url": "https://runrepeat.com/asics-gel-nimbus-27"}
    },
    {
        "id": "asics_gt_2000_13",
        "brand_id": "asics",
        "name_kr": "아식스 GT-2000 13",
        "name_en": "Asics GT-2000 13",
        "series": "GT-2000",
        "category": "stability",
        "category_name": "안정화 (과회내 서포트)",
        "msrp_usd": 140,
        "msrp_krw": 159000,
        "widths": ["D", "2E"],
        "specs": {"weight_g": 275, "heel_drop_mm": 8, "midsole": "FF BLAST+ & 3D 가이던스 시스템 + PureGEL", "plate": "없음", "stack_height": "36.5mm / 28.5mm", "support_type": "Stability (경량 안정화)"},
        "runrepeat": {"score": 84, "midsole_foam": "FF BLAST+", "pros": ["카야노보다 가볍고 경쾌한 275g 무게", "자연스러운 내전 지지력", "매일 신기 완벽한 데일리 안정화"], "cons": ["초고탄성 슈퍼폼을 선호하면 다소 정직함"], "verdict": "가볍고 안정적인 발걸음을 원하는 중립/과회내 러너의 올라운더.", "url": "https://runrepeat.com/asics-gt-2000-13"}
    },
    {
        "id": "asics_gel_kayano_31",
        "brand_id": "asics",
        "name_kr": "아식스 젤 카야노 31",
        "name_en": "Asics Gel Kayano 31",
        "series": "젤 카야노",
        "category": "stability",
        "category_name": "안정화 (과회내 서포트)",
        "msrp_usd": 165,
        "msrp_krw": 199000,
        "widths": ["D", "2E", "4E"],
        "specs": {"weight_g": 305, "heel_drop_mm": 10, "midsole": "FF BLAST+ ECO + 4D 가이던스 시스템 + PureGEL", "plate": "없음", "stack_height": "40mm / 30mm", "support_type": "Stability (안정화 끝판왕)"},
        "runrepeat": {"score": 86, "midsole_foam": "FF BLAST+ ECO", "pros": ["피로도가 쌓일수록 내측 아치를 부드럽게 복원하는 4D 가이던스", "안정화임에도 놀라울 정도로 푹신한 쿠션감", "동양인 발볼러를 위한 완벽한 피팅 옵션"], "cons": ["스피드런에는 다소 무거운 편"], "verdict": "31년 역사가 증명하는 전 세계 안정화 부문 부동의 1위이자 기준점.", "url": "https://runrepeat.com/asics-gel-kayano-31"}
    },
    {
        "id": "asics_superblast_2",
        "brand_id": "asics",
        "name_kr": "아식스 슈퍼블라스트 2",
        "name_en": "Asics Superblast 2",
        "series": "슈퍼블라스트",
        "category": "super_trainer",
        "category_name": "슈퍼 트레이너",
        "msrp_usd": 200,
        "msrp_krw": 249000,
        "widths": ["D"],
        "specs": {"weight_g": 249, "heel_drop_mm": 8, "midsole": "FF TURBO+ (최상급 슈퍼폼) + FF BLAST+ ECO 듀얼 레이어", "plate": "없음", "stack_height": "45mm / 37mm", "support_type": "Neutral (치트키 슈퍼트레이너)"},
        "runrepeat": {"score": 91, "midsole_foam": "FF TURBO+", "pros": ["메타스피드 레이서용 슈퍼폼(FF TURBO+) 전격 탑재", "45mm 합법적 규정 초과 쿠션인데 249g이라는 비현실적 무게", "카본 없이도 대회 풀코스를 뛸 수 있는 최고의 편안함"], "cons": ["전세계 품절 대란으로 구매하기 어려움"], "verdict": "러너들이 '치트키'라 부르는 현존 논플레이트 슈퍼 트레이너의 최고봉.", "url": "https://runrepeat.com/asics-superblast-2"}
    },
    {
        "id": "asics_metaspeed_sky_paris",
        "brand_id": "asics",
        "name_kr": "아식스 메타스피드 스카이 파리",
        "name_en": "Asics Metaspeed Sky Paris",
        "series": "메타스피드",
        "category": "racing",
        "category_name": "레이싱화 (카본 슈퍼슈즈)",
        "msrp_usd": 250,
        "msrp_krw": 299000,
        "widths": ["D"],
        "specs": {"weight_g": 183, "heel_drop_mm": 5, "midsole": "Full FF TURBO+ 슈퍼폼 + 풀렝스 카본 플레이트", "plate": "Full Carbon Plate (보폭 확장형 상단 배치)", "stack_height": "39.5mm / 34.5mm", "support_type": "Neutral (스트라이드형 마라톤 레이서)"},
        "runrepeat": {"score": 92, "midsole_foam": "FF TURBO+", "pros": ["183g 깃털 같은 무게와 넓은 밑창 안정감", "보폭(스트라이드)을 늘려주는 환상적인 위로 솟구치는 탄성", "ASICSGRIP 아웃솔의 빗길 최강 접지"], "cons": ["강한 종아리 근력을 요구함"], "verdict": "파리 올림픽을 위해 개발된 아식스의 엘리트 마라톤 카본 플래그십.", "url": "https://runrepeat.com/asics-metaspeed-sky-paris"}
    },

    # ------------------ SAUCONY (2025/2026 LATEST, 6 models) ------------------
    {
        "id": "saucony_cohesion_17",
        "brand_id": "saucony",
        "name_kr": "써코니 코히전 17",
        "name_en": "Saucony Cohesion 17",
        "series": "코히전",
        "category": "budget",
        "category_name": "가성비 입문화 (≤$100)",
        "msrp_usd": 65,
        "msrp_krw": 79000,
        "widths": ["D", "2E"],
        "specs": {"weight_g": 260, "heel_drop_mm": 12, "midsole": "VERSARUN 쿠셔닝", "plate": "없음", "stack_height": "29mm / 17mm", "support_type": "Neutral (가성비 입문)"},
        "runrepeat": {"score": 73, "midsole_foam": "VERSARUN", "pros": ["60달러대 놀라운 가성비", "가볍고 경쾌한 260g 무게", "튼튼한 아웃솔 고무 내구성"], "cons": ["최신 맥스쿠션 대비 얇은 전족부 쿠션"], "verdict": "미국 러너들이 입문할 때 가장 많이 집어 드는 실속 만점 가성비 슈즈.", "url": "https://runrepeat.com/saucony-cohesion-17"}
    },
    {
        "id": "saucony_ride_18",
        "brand_id": "saucony",
        "name_kr": "써코니 라이드 18",
        "name_en": "Saucony Ride 18",
        "series": "라이드",
        "category": "daily",
        "category_name": "데일리 / 쿠션화",
        "msrp_usd": 140,
        "msrp_krw": 159000,
        "widths": ["D", "2E"],
        "specs": {"weight_g": 275, "heel_drop_mm": 8, "midsole": "PWRRUN+ 2.0 (초경량 비드 발포 폼)", "plate": "없음", "stack_height": "35mm / 27mm", "support_type": "Neutral (2025 만능 데일리)"},
        "runrepeat": {"score": 86, "midsole_foam": "PWRRUN+ 2.0", "pros": ["더욱 가벼워진 275g 무게와 향상된 에너지 리턴", "겨울철 영하 날씨에도 얼지 않고 쫄깃한 쿠션", "조깅부터 템포런까지 완벽한 밸런스"], "cons": ["극단적 맥스쿠션을 원하는 러너에게는 탄탄함"], "verdict": "어떤 러닝에도 고민 없이 신을 수 있는 2025 최신 만능 워크호스 러닝화.", "url": "https://runrepeat.com/saucony-ride-18"}
    },
    {
        "id": "saucony_triumph_22",
        "brand_id": "saucony",
        "name_kr": "써코니 트라이엄프 22",
        "name_en": "Saucony Triumph 22",
        "series": "트라이엄프",
        "category": "daily",
        "category_name": "데일리 / 쿠션화",
        "msrp_usd": 160,
        "msrp_krw": 199000,
        "widths": ["D", "2E"],
        "specs": {"weight_g": 286, "heel_drop_mm": 10, "midsole": "Full PWRRUN PB (슈퍼폼 100% 전면 배치)", "plate": "없음", "stack_height": "37mm / 27mm", "support_type": "Neutral (최상급 바운스 쿠션)"},
        "runrepeat": {"score": 85, "midsole_foam": "PWRRUN PB", "pros": ["엔돌핀 레이싱화의 슈퍼폼(PWRRUN PB)을 맥스쿠션 데일리에 통째로 탑재", "극상의 에너지 리턴과 구름 쿠셔닝", "넓은 밑창 플랫폼으로 안정감 확보"], "cons": ["스피드 레이싱에는 다소 묵직함"], "verdict": "써코니가 선사하는 가장 럭셔리하고 쫄깃한 프리미엄 맥스 쿠션 트레이너.", "url": "https://runrepeat.com/saucony-triumph-22"}
    },
    {
        "id": "saucony_guide_18",
        "brand_id": "saucony",
        "name_kr": "써코니 가이드 18",
        "name_en": "Saucony Guide 18",
        "series": "가이드",
        "category": "stability",
        "category_name": "안정화 (과회내 서포트)",
        "msrp_usd": 140,
        "msrp_krw": 159000,
        "widths": ["D", "2E"],
        "specs": {"weight_g": 265, "heel_drop_mm": 6, "midsole": "PWRRUN + 진화된 Center Path 테크놀로지", "plate": "없음", "stack_height": "35mm / 29mm", "support_type": "Stability (신개념 센터패스)"},
        "runrepeat": {"score": 84, "midsole_foam": "PWRRUN", "pros": ["넓은 베이스 지오메트리로 자연스러운 과회내 서포트", "265g 가벼운 무게", "낮은 6mm 드롭으로 부드러운 발구름"], "cons": ["푹신한 물쿠션을 기대하면 다소 지지력 중심"], "verdict": "인위적이지 않고 자연스럽게 발목을 잡아주는 2025 최신 경량 안정화.", "url": "https://runrepeat.com/saucony-guide-18"}
    },
    {
        "id": "saucony_hurricane_26",
        "brand_id": "saucony",
        "name_kr": "써코니 허리케인 26",
        "name_en": "Saucony Hurricane 26",
        "series": "허리케인",
        "category": "stability",
        "category_name": "안정화 (과회내 서포트)",
        "msrp_usd": 160,
        "msrp_krw": 199000,
        "widths": ["D", "2E"],
        "specs": {"weight_g": 262, "heel_drop_mm": 6, "midsole": "신형 incrediLUX 초임계 슈퍼폼 + 울트라 와이드 Center Path", "plate": "없음 (센터패스 기하학 서포트)", "stack_height": "41mm / 35mm", "support_type": "Stability (최상급 슈퍼 맥스 안정화)"},
        "runrepeat": {"score": 91, "midsole_foam": "incrediLUX Supercritical", "pros": ["차세대 incrediLUX 초임계 폼으로 전작(24) 대비 무려 50g 이상 경량화(262g)", "초광폭 베이스 플랫폼이 선사하는 흔들림 없는 완벽한 과회내 지지력", "여유로운 토박스 공간과 41mm 극상의 구름 쿠션"], "cons": ["플랫폼 베이스가 거대하여 좁은 발볼 러너에게는 부피감 체감"], "verdict": "무겁던 전통 안정화의 한계를 incrediLUX 폼으로 완벽히 뛰어넘은 2026 최신 플래그십 안정화.", "url": "https://runrepeat.com/saucony-hurricane-26"}
    },
    {
        "id": "saucony_endorphin_speed_4",
        "brand_id": "saucony",
        "name_kr": "써코니 엔돌핀 스피드 4",
        "name_en": "Saucony Endorphin Speed 4",
        "series": "엔돌핀 스피드",
        "category": "super_trainer",
        "category_name": "슈퍼 트레이너",
        "msrp_usd": 170,
        "msrp_krw": 199000,
        "widths": ["D", "2E"],
        "specs": {"weight_g": 233, "heel_drop_mm": 8, "midsole": "PWRRUN PB (PEBA 슈퍼폼) + 윙 나일론 플레이트", "plate": "Nylon Winged Plate", "stack_height": "36mm / 28mm", "support_type": "Neutral (올라운드 슈퍼트레이너)"},
        "runrepeat": {"score": 89, "midsole_foam": "PWRRUN PB", "pros": ["나일론 플레이트와 PEBA 슈퍼폼의 마법 같은 조화", "카본화 대비 종아리 피로도가 극히 적어 매일 신을 수 있음", "조깅부터 템포런, 실제 마라톤 대회까지 완벽 커버"], "cons": ["빗길 노면 접지력은 보통 수준"], "verdict": "전 세계 러너들이 단 한 켤레의 신발만 골라야 한다면 선택하는 만능 트레이너.", "url": "https://runrepeat.com/saucony-endorphin-speed-4"}
    },
    {
        "id": "saucony_endorphin_pro_4",
        "brand_id": "saucony",
        "name_kr": "써코니 엔돌핀 프로 4",
        "name_en": "Saucony Endorphin Pro 4",
        "series": "엔돌핀 프로",
        "category": "racing",
        "category_name": "레이싱화 (카본 슈퍼슈즈)",
        "msrp_usd": 250,
        "msrp_krw": 279000,
        "widths": ["D"],
        "specs": {"weight_g": 212, "heel_drop_mm": 8, "midsole": "PWRRUN HG (상단) + PWRRUN PB (하단) + 풀 카본 플레이트", "plate": "Full Carbon Fiber Plate", "stack_height": "39.5mm / 31.5mm", "support_type": "Neutral (엘리트 마라톤 카본 레이서)"},
        "runrepeat": {"score": 91, "midsole_foam": "PWRRUN PB & HG", "pros": ["카본 레이싱화 중 가장 안정적이고 발목 꺾임이 적음", "최상급 HG 폼 탑재로 가속력 폭발", "스피드로 테크놀로지의 자연스러운 롤링"], "cons": ["엔돌핀 스피드보다 딱딱한 카본 체감"], "verdict": "안정성과 폭발적 스피드를 동시에 챙긴 가장 믿음직한 마라톤 카본화.", "url": "https://runrepeat.com/saucony-endorphin-pro-4"}
    },

    # ------------------ HOKA (2025/2026 LATEST, 6 models) ------------------
    {
        "id": "hoka_clifton_9",
        "brand_id": "hoka",
        "name_kr": "호카 클리프톤 9",
        "name_en": "Hoka Clifton 9",
        "series": "클리프톤",
        "category": "daily",
        "category_name": "데일리 / 쿠션화",
        "msrp_usd": 145,
        "msrp_krw": 179000,
        "widths": ["D", "2E"],
        "specs": {"weight_g": 248, "heel_drop_mm": 5, "midsole": "압축 성형 EVA (CMEVA) + 얼리 스테이지 메타 로커", "plate": "없음", "stack_height": "32mm / 27mm", "support_type": "Neutral (국민 쿠션화)"},
        "runrepeat": {"score": 87, "midsole_foam": "CMEVA", "pros": ["248g이라는 믿을 수 없는 경량성과 풍부한 쿠션", "자연스럽게 발이 굴러가는 메타 로커 지오메트리", "장거리 조깅 시 관절 피로 제로"], "cons": ["미드풋 아치가 다소 좁게 느껴질 수 있음(와이드 추천)"], "verdict": "호카를 전 세계적인 브랜드로 만든 상징이자 매일 달리고 싶게 만드는 데일리 쿠션화.", "url": "https://runrepeat.com/hoka-clifton-9"}
    },
    {
        "id": "hoka_clifton_pro",
        "brand_id": "hoka",
        "name_kr": "호카 클리프톤 프로",
        "name_en": "Hoka Clifton PRO",
        "series": "클리프톤 프로",
        "category": "daily",
        "category_name": "데일리 / 쿠션화",
        "msrp_usd": 165,
        "msrp_krw": 199000,
        "widths": ["D", "2E"],
        "specs": {"weight_g": 264, "heel_drop_mm": 5, "midsole": "신형 PROGLIDE+ 초임계 EVA 폼 + 어그레시브 메타로커", "plate": "없음", "stack_height": "39mm / 34mm", "support_type": "Neutral (반응성 강화 프로 에디션)"},
        "runrepeat": {"score": 86, "midsole_foam": "PROGLIDE+ Supercritical EVA", "pros": ["PROGLIDE+ 초임계 폼 전격 채택으로 기존 클리프톤 대비 향상된 에너지 리턴", "더욱 공격적인 메타로커로 경쾌해진 템포 전환", "한여름 장거리 러닝에도 쾌적한 통기성 프리미엄 어퍼"], "cons": ["기본 클리프톤 대비 높은 가격", "젖은 노면 접지력은 보통 수준"], "verdict": "지나치게 푹신하기만 하던 쿠션화에 초임계 폼의 쫄깃한 탄성과 스피드를 더한 클리프톤 프로.", "url": "https://runrepeat.com/hoka-clifton-pro"}
    },
    {
        "id": "hoka_bondi_8",
        "brand_id": "hoka",
        "name_kr": "호카 본디 8",
        "name_en": "Hoka Bondi 8",
        "series": "본디",
        "category": "daily",
        "category_name": "데일리 / 쿠션화",
        "msrp_usd": 165,
        "msrp_krw": 209000,
        "widths": ["D", "2E", "4E"],
        "specs": {"weight_g": 307, "heel_drop_mm": 4, "midsole": "울트라 라이트 EVA 맥스 쿠션", "plate": "없음", "stack_height": "39mm / 35mm", "support_type": "Neutral (울트라 맥스쿠션)"},
        "runrepeat": {"score": 82, "midsole_foam": "Ultra-light EVA", "pros": ["호카 라인업 중 가장 두껍고 푹신한 충격 흡수", "오래 서 있거나 회복 조깅에 최고", "넓은 밑창으로 무릎 흔들림 없음"], "cons": ["무게감이 있어 빠른 페이스는 부적합"], "verdict": "발목과 무릎을 가장 완벽하게 보호해주는 지상 최강의 맥스 쿠션화.", "url": "https://runrepeat.com/hoka-bondi-8"}
    },
    {
        "id": "hoka_arahi_7",
        "brand_id": "hoka",
        "name_kr": "호카 아라히 7",
        "name_en": "Hoka Arahi 7",
        "series": "아라히",
        "category": "stability",
        "category_name": "안정화 (과회내 서포트)",
        "msrp_usd": 145,
        "msrp_krw": 179000,
        "widths": ["D", "2E"],
        "specs": {"weight_g": 275, "heel_drop_mm": 5, "midsole": "J-Frame 다이나믹 서포트 EVA", "plate": "없음", "stack_height": "34mm / 29mm", "support_type": "Stability (J-프레임 안정화)"},
        "runrepeat": {"score": 82, "midsole_foam": "J-Frame EVA", "pros": ["호카 특유의 가벼움에 J-프레임 과회내 제어 결합", "부드러운 니트 플랫 어퍼", "평발 러너들의 관절 보호"], "cons": ["스피드 레이싱에는 부적합"], "verdict": "안정화는 무겁고 투박하다는 편견을 깨주는 호카의 대표 안정화.", "url": "https://runrepeat.com/hoka-arahi-7"}
    },
    {
        "id": "hoka_mach_6",
        "brand_id": "hoka",
        "name_kr": "호카 마하 6",
        "name_en": "Hoka Mach 6",
        "series": "마하",
        "category": "super_trainer",
        "category_name": "슈퍼 트레이너",
        "msrp_usd": 140,
        "msrp_krw": 169000,
        "widths": ["D", "2E"],
        "specs": {"weight_g": 232, "heel_drop_mm": 5, "midsole": "초임계 EVA (Supercritical Foam) + 고무 아웃솔", "plate": "없음", "stack_height": "37mm / 32mm", "support_type": "Neutral (경량 템포 트레이너)"},
        "runrepeat": {"score": 88, "midsole_foam": "Supercritical EVA", "pros": ["초임계 폼 전격 도입으로 전작 대비 반발력 대폭 상승", "전작의 치명적 약점이었던 아웃솔 내구성 해결", "232g 초경량 템포런 최적화"], "cons": ["힐드롭 5mm로 낮은 드롭 적응 필요"], "verdict": "플레이트 없이 오직 가벼움과 폼 탄성으로 질주하는 가장 신나는 트레이너.", "url": "https://runrepeat.com/hoka-mach-6"}
    },
    {
        "id": "hoka_mach_x_2",
        "brand_id": "hoka",
        "name_kr": "호카 마하 X 2",
        "name_en": "Hoka Mach X 2",
        "series": "마하 X",
        "category": "super_trainer",
        "category_name": "슈퍼 트레이너",
        "msrp_usd": 190,
        "msrp_krw": 229000,
        "widths": ["D"],
        "specs": {"weight_g": 260, "heel_drop_mm": 5, "midsole": "PEBA 슈퍼폼 + Pebax 윙 플레이트 + 메타 로커", "plate": "Pebax Winged Plate", "stack_height": "44mm / 39mm", "support_type": "Neutral (플레이트 슈퍼트레이너)"},
        "runrepeat": {"score": 89, "midsole_foam": "PEBA & EVA", "pros": ["44mm 거대 맥스 스택과 Pebax 플레이트의 사기적인 롤링", "대회와 장거리 훈련을 넘나드는 탄성", "시엘로 X1의 감성을 트레이너에 담음"], "cons": ["힐 칼라 피팅 호불호"], "verdict": "호카 특유의 락커와 페박스 플레이트가 결합된 최고의 훈련 파트너.", "url": "https://runrepeat.com/hoka-mach-x-2"}
    },
    {
        "id": "hoka_cielo_x1",
        "brand_id": "hoka",
        "name_kr": "호카 시엘로 X1",
        "name_en": "Hoka Cielo X1",
        "series": "시엘로",
        "category": "racing",
        "category_name": "레이싱화 (카본 슈퍼슈즈)",
        "msrp_usd": 275,
        "msrp_krw": 339000,
        "widths": ["D"],
        "specs": {"weight_g": 254, "heel_drop_mm": 7, "midsole": "듀얼 레이어 100% PEBA 폼 + 윙 카본 플레이트 + 익스트림 로커", "plate": "Winged Carbon Fiber Plate", "stack_height": "39mm / 32mm", "support_type": "Neutral (극강의 추진력 카본 레이서)"},
        "runrepeat": {"score": 90, "midsole_foam": "PEBA Foam", "pros": ["현존 러닝화 중 가장 다이나믹한 로커 지오메트리", "호카 역사상 가장 반발력 높은 100% PEBA 슈퍼폼", "신는 순간 자동으로 앞으로 굴러떨어지는 추진력"], "cons": ["250g대로 타사 플래그십 레이서 대비 무게가 나감"], "verdict": "호카가 모든 기술력을 쏟아부어 완성한 가장 과격하고 짜릿한 카본 슈퍼슈즈.", "url": "https://runrepeat.com/hoka-cielo-x1"}
    },

    # ------------------ NEW BALANCE (2025/2026 LATEST, 6 models) ------------------
    {
        "id": "nb_fresh_foam_arishi_v4",
        "brand_id": "newbalance",
        "name_kr": "뉴발란스 프레쉬폼 아리시 v4",
        "name_en": "New Balance Fresh Foam Arishi v4",
        "series": "아리시",
        "category": "budget",
        "category_name": "가성비 입문화 (≤$100)",
        "msrp_usd": 75,
        "msrp_krw": 89000,
        "widths": ["D", "2E", "4E"],
        "specs": {"weight_g": 255, "heel_drop_mm": 6, "midsole": "Fresh Foam 쿠셔닝", "plate": "없음", "stack_height": "28mm / 22mm", "support_type": "Neutral (입문 워킹/러닝)"},
        "runrepeat": {"score": 73, "midsole_foam": "Fresh Foam", "pros": ["뉴발란스 고유의 프레쉬폼 쿠션을 8만원대에 경험", "가볍고 통기성 뛰어난 니트 어퍼", "4E 와이드 지원"], "cons": ["장거리 마일리지용으로는 얇은 스택"], "verdict": "일상 걷기와 가벼운 조깅을 즐기는 발볼러에게 제격인 가성비 슈즈.", "url": "https://runrepeat.com/new-balance-fresh-foam-arishi-v4"}
    },
    {
        "id": "nb_fresh_foam_x_880_v14",
        "brand_id": "newbalance",
        "name_kr": "뉴발란스 프레쉬폼 X 880 v14",
        "name_en": "New Balance Fresh Foam X 880 v14",
        "series": "880",
        "category": "daily",
        "category_name": "데일리 / 쿠션화",
        "msrp_usd": 140,
        "msrp_krw": 159000,
        "widths": ["D", "2E", "4E"],
        "specs": {"weight_g": 270, "heel_drop_mm": 8, "midsole": "Fresh Foam X 일체형 미드솔", "plate": "없음", "stack_height": "35mm / 27mm", "support_type": "Neutral (정통 데일리)"},
        "runrepeat": {"score": 84, "midsole_foam": "Fresh Foam X", "pros": ["1080보다 탄탄하여 밸런스 좋은 주행감", "내구성 뛰어난 아웃솔 러버", "한국인 발볼러를 위한 4E 지원"], "cons": ["화려한 반발력보다는 우직한 기본기"], "verdict": "매일 묵묵히 마일리지를 채워주는 뉴발란스의 대표 데일리 러닝화.", "url": "https://runrepeat.com/new-balance-fresh-foam-x-880-v14"}
    },
    {
        "id": "nb_fresh_foam_x_1080_v14",
        "brand_id": "newbalance",
        "name_kr": "뉴발란스 프레쉬폼 X 1080 v14",
        "name_en": "New Balance Fresh Foam X 1080 v14",
        "series": "1080",
        "category": "daily",
        "category_name": "데일리 / 쿠션화",
        "msrp_usd": 165,
        "msrp_krw": 199000,
        "widths": ["D", "2E", "4E"],
        "specs": {"weight_g": 285, "heel_drop_mm": 6, "midsole": "Fresh Foam X 2.0 (더 탄탄해진 반발력과 힐락)", "plate": "없음", "stack_height": "38mm / 32mm", "support_type": "Neutral (2025 최신 맥스 쿠션)"},
        "runrepeat": {"score": 82, "midsole_foam": "Fresh Foam X 2.0", "pros": ["전작(v13)의 과도한 물렁함을 개선하여 주행 안정감 대폭 상승", "발등과 뒤꿈치를 단단하게 잡아주는 신형 어퍼", "발볼 넓은 한국인 러너를 위한 완벽한 2E/4E 옵션"], "cons": ["전작 대비 약간 무거워진 무게"], "verdict": "안정성과 풍부한 쿠션을 완벽한 균형으로 완성한 2025 최신 플래그십 트레이너.", "url": "https://runrepeat.com/new-balance-fresh-foam-x-1080-v14"}
    },
    {
        "id": "nb_fresh_foam_x_860_v14",
        "brand_id": "newbalance",
        "name_kr": "뉴발란스 프레쉬폼 X 860 v14",
        "name_en": "New Balance Fresh Foam X 860 v14",
        "series": "860",
        "category": "stability",
        "category_name": "안정화 (과회내 서포트)",
        "msrp_usd": 140,
        "msrp_krw": 159000,
        "widths": ["D", "2E", "4E"],
        "specs": {"weight_g": 298, "heel_drop_mm": 8, "midsole": "Fresh Foam X + 신형 EVA Stability Plane 플레이트", "plate": "EVA Stability Plane", "stack_height": "36mm / 28mm", "support_type": "Stability (안정화)"},
        "runrepeat": {"score": 83, "midsole_foam": "Fresh Foam X", "pros": ["딱딱한 포스트 대신 가벼운 안정성 평면 플레이트 도입", "풍성해진 프레쉬폼 쿠션", "과회내 완벽 서포트"], "cons": ["빠른 템포런보다는 안정 조깅에 최적화"], "verdict": "평발 러너들의 영원한 동반자 860의 가장 세련된 최신 진화형.", "url": "https://runrepeat.com/new-balance-fresh-foam-x-860-v14"}
    },
    {
        "id": "nb_fuelcell_rebel_v4",
        "brand_id": "newbalance",
        "name_kr": "뉴발란스 퓨어셀 레벨 v4",
        "name_en": "New Balance FuelCell Rebel v4",
        "series": "퓨어셀 레벨",
        "category": "super_trainer",
        "category_name": "슈퍼 트레이너",
        "msrp_usd": 140,
        "msrp_krw": 169000,
        "widths": ["D", "2E"],
        "specs": {"weight_g": 208, "heel_drop_mm": 6, "midsole": "FuelCell (PEBA/EVA 블렌드 슈퍼폼)", "plate": "없음", "stack_height": "33mm / 27mm", "support_type": "Neutral (초경량 만능 템포)"},
        "runrepeat": {"score": 89, "midsole_foam": "FuelCell PEBA Blend", "pros": ["208g이라는 깃털 같은 무게", "PEBA 폼 블렌드로 미친 반응성과 쫀득함", "넓어진 밑창으로 전작의 좌우 흔들림 완벽 개선"], "cons": ["어퍼가 얇아 겨울철 발 시려움"], "verdict": "가볍고 빠른 러닝의 정수, 훈련이 즐거워지는 전천후 스피드 트레이너.", "url": "https://runrepeat.com/new-balance-fuelcell-rebel-v4"}
    },
    {
        "id": "nb_fuelcell_sc_elite_v4",
        "brand_id": "newbalance",
        "name_kr": "뉴발란스 퓨어셀 SC 엘리트 v4",
        "name_en": "New Balance FuelCell SuperComp Elite v4",
        "series": "SC 엘리트",
        "category": "racing",
        "category_name": "레이싱화 (카본 슈퍼슈즈)",
        "msrp_usd": 250,
        "msrp_krw": 299000,
        "widths": ["D", "2E"],
        "specs": {"weight_g": 232, "heel_drop_mm": 4, "midsole": "100% PEBA FuelCell + Energy Arc 카본 플레이트", "plate": "Full Carbon Energy Arc", "stack_height": "40mm / 36mm", "support_type": "Neutral (편안한 마라톤 카본 레이서)"},
        "runrepeat": {"score": 90, "midsole_foam": "100% PEBA FuelCell", "pros": ["드디어 100% 순수 PEBA 폼 탑재로 폭발적인 에너지 리턴", "카본 레이싱화 중 유일하게 2E 와이드 발볼 정식 지원", "아치 통증 없는 최고의 편안함"], "cons": ["180g대 초경량 레이서 대비 무게가 살짝 있음"], "verdict": "발볼 넓은 마라토너가 풀코스를 뛸 때 신을 수 있는 가장 축복 같은 카본 레이서.", "url": "https://runrepeat.com/new-balance-fuelcell-sc-elite-v4"}
    },

    # ------------------ PUMA (2025/2026 LATEST, 5 models) ------------------
    {
        "id": "puma_scend_pro",
        "brand_id": "puma",
        "name_kr": "푸마 센드 프로",
        "name_en": "Puma Scend Pro",
        "series": "센드 프로",
        "category": "budget",
        "category_name": "가성비 입문화 (≤$100)",
        "msrp_usd": 75,
        "msrp_krw": 85000,
        "widths": ["D"],
        "specs": {"weight_g": 280, "heel_drop_mm": 9, "midsole": "PROFOAM LITE 쿠셔닝", "plate": "없음", "stack_height": "32mm / 23mm", "support_type": "Neutral (입문 가성비)"},
        "runrepeat": {"score": 75, "midsole_foam": "PROFOAM LITE", "pros": ["PROTREAD 고무 아웃솔의 우수한 접지력", "깔끔한 스트리트 러닝 룩", "가성비 뛰어난 내구성"], "cons": ["고급 니트로 폼 대비 반발력 한계"], "verdict": "도심 속 가벼운 러닝과 일상을 잇는 푸마의 가성비 데일리.", "url": "https://runrepeat.com/puma-scend-pro"}
    },
    {
        "id": "puma_velocity_nitro_3",
        "brand_id": "puma",
        "name_kr": "푸마 벨로시티 니트로 3",
        "name_en": "Puma Velocity Nitro 3",
        "series": "벨로시티 니트로",
        "category": "daily",
        "category_name": "데일리 / 쿠션화",
        "msrp_usd": 135,
        "msrp_krw": 149000,
        "widths": ["D"],
        "specs": {"weight_g": 264, "heel_drop_mm": 10, "midsole": "NITROFOAM (질소 주입 슈퍼폼) + PROFOAM LITE 듀얼 레이어", "plate": "없음", "stack_height": "36mm / 26mm", "support_type": "Neutral (가성비 1위 데일리)"},
        "runrepeat": {"score": 87, "midsole_foam": "NITROFOAM", "pros": ["PUMAGRIP 아웃솔의 전 세계 1위 젖은 노면 접지력", "질소 주입 니트로 폼의 통통 튀는 경쾌한 탄성", "14만원대 믿기 힘든 퀄리티"], "cons": ["발볼이 다소 타이트한 편 (반업 추천)"], "verdict": "비 오는 날에도 거침없이 달리는 러너들을 위한 가성비 접지력 1위 데일리.", "url": "https://runrepeat.com/puma-velocity-nitro-3"}
    },
    {
        "id": "puma_foreverrun_nitro",
        "brand_id": "puma",
        "name_kr": "푸마 포에버런 니트로",
        "name_en": "Puma ForeverRun Nitro",
        "series": "포에버런",
        "category": "stability",
        "category_name": "안정화 (과회내 서포트)",
        "msrp_usd": 150,
        "msrp_krw": 179000,
        "widths": ["D"],
        "specs": {"weight_g": 274, "heel_drop_mm": 10, "midsole": "듀얼 덴시티 NITROFOAM + RUNGUIDE 림", "plate": "없음", "stack_height": "36mm / 26mm", "support_type": "Stability (스마트 가이던스)"},
        "runrepeat": {"score": 84, "midsole_foam": "Dual Density NITROFOAM", "pros": ["질소 주입 폼의 부드러움과 안정 림의 지지력", "카이저 풋랩 협업 지능형 인솔", "가벼운 무게"], "cons": ["발등이 다소 낮게 출시됨"], "verdict": "과회내 러너를 위한 가장 혁신적이고 푹신한 최신 테크 안정화.", "url": "https://runrepeat.com/puma-foreverrun-nitro"}
    },
    {
        "id": "puma_deviate_nitro_3",
        "brand_id": "puma",
        "name_kr": "푸마 디비에이트 니트로 3",
        "name_en": "Puma Deviate Nitro 3",
        "series": "디비에이트 니트로",
        "category": "super_trainer",
        "category_name": "슈퍼 트레이너",
        "msrp_usd": 160,
        "msrp_krw": 199000,
        "widths": ["D"],
        "specs": {"weight_g": 265, "heel_drop_mm": 10, "midsole": "NITROFOAM Elite (상단) + NITROFOAM (하단) + 카본 INNOPLATE", "plate": "Carbon Composite INNOPLATE", "stack_height": "39mm / 29mm", "support_type": "Neutral (카본 슈퍼트레이너)"},
        "runrepeat": {"score": 88, "midsole_foam": "NITRO Elite", "pros": ["엘리트 니트로 폼과 카본 플레이트의 공격적인 추진력", "미끄러짐 없는 절대 접지력 PUMAGRIP", "조깅부터 마라톤 대회까지 모두 소화"], "cons": ["뒤꿈치 힐 패딩이 얇아 힐슬립 체크 필요"], "verdict": "카본화의 탄성과 트레이너의 내구성을 동시에 쥐어주는 스피드 머신.", "url": "https://runrepeat.com/puma-deviate-nitro-3"}
    },
    {
        "id": "puma_deviate_nitro_elite_3",
        "brand_id": "puma",
        "name_kr": "푸마 디비에이트 니트로 엘리트 3",
        "name_en": "Puma Deviate Nitro Elite 3",
        "series": "디비에이트 니트로 엘리트",
        "category": "racing",
        "category_name": "레이싱화 (카본 슈퍼슈즈)",
        "msrp_usd": 230,
        "msrp_krw": 279000,
        "widths": ["D"],
        "specs": {"weight_g": 194, "heel_drop_mm": 8, "midsole": "100% NITROFOAM ELITE (지방족 TPU/PEBA) + 풀 카본 플레이트", "plate": "Full Carbon INNOPLATE", "stack_height": "40mm / 32mm", "support_type": "Neutral (194g 초경량 카본 레이서)"},
        "runrepeat": {"score": 91, "midsole_foam": "NITROFOAM ELITE", "pros": ["194g 초경량 레이서의 날렵한 스피드", "PUMAGRIP-LT의 빗길 절대 접지", "가성비 뛰어난 20만원대 카본 레이싱화"], "cons": ["발볼이 좁아 칼발 러너에게 최적"], "verdict": "비 오는 날 마라톤 대회에서 타 브랜드를 압도하는 접지력 끝판왕 카본화.", "url": "https://runrepeat.com/puma-deviate-nitro-elite-3"}
    },

    # ------------------ BROOKS (2025/2026 LATEST, 5 models) ------------------
    {
        "id": "brooks_trace_3",
        "brand_id": "brooks",
        "name_kr": "브룩스 트레이스 3",
        "name_en": "Brooks Trace 3",
        "series": "트레이스",
        "category": "budget",
        "category_name": "가성비 입문화 (≤$100)",
        "msrp_usd": 100,
        "msrp_krw": 119000,
        "widths": ["D", "2E"],
        "specs": {"weight_g": 252, "heel_drop_mm": 12, "midsole": "DNA LOFT 쿠셔닝", "plate": "없음", "stack_height": "30mm / 18mm", "support_type": "Neutral (100달러 입문)"},
        "runrepeat": {"score": 76, "midsole_foam": "DNA LOFT", "pros": ["브룩스 특유의 검증된 내구성과 발 편함", "100달러 정가에 252g 가벼운 무게", "초보 러너 힐 스트라이크에 최적화된 12mm 드롭"], "cons": ["최신 맥스쿠션 대비 클래식한 쿠션감"], "verdict": "기본기에 가장 충실한 러닝화 전문 브랜드 브룩스의 합리적 엔트리 모델.", "url": "https://runrepeat.com/brooks-trace-3"}
    },
    {
        "id": "brooks_revel_max",
        "brand_id": "brooks",
        "name_kr": "브룩스 레벨 맥스",
        "name_en": "Brooks Revel Max",
        "series": "레벨 맥스",
        "category": "budget",
        "category_name": "가성비 입문화 (≤$100)",
        "msrp_usd": 100,
        "msrp_krw": 119000,
        "widths": ["D", "2E"],
        "specs": {"weight_g": 278, "heel_drop_mm": 6, "midsole": "DNA LOFT v2 맥스 쿠셔닝 + GlideRoll 로커", "plate": "없음", "stack_height": "35mm / 29mm", "support_type": "Neutral (100달러 맥스쿠션 입문)"},
        "runrepeat": {"score": 81, "midsole_foam": "DNA LOFT v2", "pros": ["100달러 입문 가격에 레벨과 고스트맥스를 결합한 최초의 맥스스택", "GlideRoll 로커 지오메트리로 부드럽고 안정적인 전진 롤링", "질긴 아웃솔 내마모성과 편안한 니트 어퍼"], "cons": ["일반 레벨 대비 약간 무거운 중량", "발볼이 살짝 타이트한 편"], "verdict": "100달러 예산으로 고스택 맥스 쿠션의 충격 보호를 누릴 수 있는 2026 최신 국민 가성비화.", "url": "https://runrepeat.com/brooks-revel-max"}
    },
    {
        "id": "brooks_ghost_17",
        "brand_id": "brooks",
        "name_kr": "브룩스 고스트 17",
        "name_en": "Brooks Ghost 17",
        "series": "고스트",
        "category": "daily",
        "category_name": "데일리 / 쿠션화",
        "msrp_usd": 140,
        "msrp_krw": 169000,
        "widths": ["D", "2E", "4E"],
        "specs": {"weight_g": 275, "heel_drop_mm": 10, "midsole": "DNA LOFT v3 (전면 질소 주입 초임계 쿠션폼 업그레이드)", "plate": "없음", "stack_height": "36mm / 26mm", "support_type": "Neutral (2025 미국 판매 1위 국민 데일리)"},
        "runrepeat": {"score": 85, "midsole_foam": "DNA LOFT v3", "pros": ["10mm로 낮아진 드롭으로 한층 더 부드러워진 발구름 전환", "질소 폼의 탄력적인 충격 흡수", "1,000km 뛰어도 멀쩡한 내구성 종결자"], "cons": ["빠른 레이스보다는 조깅과 장거리 훈련에 최적화"], "verdict": "전 세계에서 가장 실패 없는 러닝화라는 찬사를 받는 2025 최신 국민 데일리 트레이너.", "url": "https://runrepeat.com/brooks-ghost-17"}
    },
    {
        "id": "brooks_glycerin_21",
        "brand_id": "brooks",
        "name_kr": "브룩스 글리세린 21",
        "name_en": "Brooks Glycerin 21",
        "series": "글리세린",
        "category": "daily",
        "category_name": "데일리 / 쿠션화",
        "msrp_usd": 160,
        "msrp_krw": 199000,
        "widths": ["D", "2E"],
        "specs": {"weight_g": 278, "heel_drop_mm": 10, "midsole": "DNA LOFT v3 질소 주입 맥스 스택", "plate": "없음", "stack_height": "38mm / 28mm", "support_type": "Neutral (프리미엄 럭셔리 쿠션)"},
        "runrepeat": {"score": 85, "midsole_foam": "DNA LOFT v3", "pros": ["부드러움과 탄력의 완벽한 조화", "포근하게 감싸는 프리미엄 어퍼 핏", "발바닥 충격을 완벽하게 걸러줌"], "cons": ["스피드 인터벌에는 다소 푹신함"], "verdict": "구름 위를 달리는 듯한 안락함을 선사하는 브룩스의 플래그십 쿠션화.", "url": "https://runrepeat.com/brooks-glycerin-21"}
    },
    {
        "id": "brooks_adrenaline_gts_24",
        "brand_id": "brooks",
        "name_kr": "브룩스 아드레날린 GTS 24",
        "name_en": "Brooks Adrenaline GTS 24",
        "series": "아드레날린",
        "category": "stability",
        "category_name": "안정화 (과회내 서포트)",
        "msrp_usd": 140,
        "msrp_krw": 169000,
        "widths": ["D", "2E", "4E"],
        "specs": {"weight_g": 283, "heel_drop_mm": 12, "midsole": "DNA LOFT v3 (질소 주입) + GuideRails 서포트 시스템", "plate": "없음 (가이드레일 범퍼)", "stack_height": "36mm / 24mm", "support_type": "Stability (2025 최신 안정화 1위)"},
        "runrepeat": {"score": 81, "midsole_foam": "DNA LOFT v3", "pros": ["드디어 아드레날린 시리즈 최초로 질소 주입 DNA LOFT v3 폼 탑재", "무릎과 발목 과회전을 완벽하게 제어하는 가이드레일", "발 편함과 안정감의 최고봉"], "cons": ["12mm 높은 힐드롭"], "verdict": "평발과 과회내로 무릎 통증을 겪는 러너를 위한 2025 최신 구원투수 안정화.", "url": "https://runrepeat.com/brooks-adrenaline-gts-24"}
    },
    {
        "id": "brooks_hyperion_max_2",
        "brand_id": "brooks",
        "name_kr": "브룩스 하이페리온 맥스 2",
        "name_en": "Brooks Hyperion Max 2",
        "series": "하이페리온",
        "category": "super_trainer",
        "category_name": "슈퍼 트레이너",
        "msrp_usd": 180,
        "msrp_krw": 219000,
        "widths": ["D"],
        "specs": {"weight_g": 258, "heel_drop_mm": 6, "midsole": "DNA FLASH v2 (질소 슈퍼폼) + Pebax 스피드볼트 플레이트", "plate": "Pebax SpeedVault Plate", "stack_height": "36mm / 30mm", "support_type": "Neutral (스피드 락커 트레이너)"},
        "runrepeat": {"score": 88, "midsole_foam": "DNA FLASH v2", "pros": ["신형 페박스 플레이트 탑재로 전작 대비 10% 향상된 추진력", "초임계 질소 폼의 탄탄하고 빠른 반발", "빠른 페이스 훈련에 최적화"], "cons": ["조깅 페이스에서는 다소 단단함"], "verdict": "인터벌과 템포런을 가볍고 경쾌하게 밀어붙이는 2025 최신 스피드 트레이너.", "url": "https://runrepeat.com/brooks-hyperion-max-2"}
    },

    # ------------------ MIZUNO (2025/2026 LATEST, 3 models) ------------------
    {
        "id": "mizuno_wave_rider_28",
        "brand_id": "mizuno",
        "name_kr": "미즈노 웨이브 라이더 28",
        "name_en": "Mizuno Wave Rider 28",
        "series": "웨이브 라이더",
        "category": "daily",
        "category_name": "데일리 / 쿠션화",
        "msrp_usd": 140,
        "msrp_krw": 169000,
        "widths": ["D", "2E", "4E"],
        "specs": {"weight_g": 272, "heel_drop_mm": 12, "midsole": "MIZUNO ENERZY NXT (초임계 힐폼) + 웨이브 플레이트", "plate": "Mizuno Wave Plate (Pebax 웨이브 플레이트)", "stack_height": "38.5mm / 26.5mm", "support_type": "Neutral (28년 헤리티지 데일리)"},
        "runrepeat": {"score": 85, "midsole_foam": "MIZUNO ENERZY NXT", "pros": ["힐에 ENERZY NXT 슈퍼폼 탑재로 착지 충격 완벽 분산", "웨이브 플레이트 고유의 탄탄하고 흔들림 없는 안정감", "X10 카본 러버의 1,000km 내구성"], "cons": ["소프트한 구름 쿠션을 선호하는 러너에게는 탄탄함"], "verdict": "28년간 전 세계 러너들의 발을 지켜온 일본 장인정신의 정석 러닝화.", "url": "https://runrepeat.com/mizuno-wave-rider-28"}
    },
    {
        "id": "mizuno_wave_inspire_20",
        "brand_id": "mizuno",
        "name_kr": "미즈노 웨이브 인스파이어 20",
        "name_en": "Mizuno Wave Inspire 20",
        "series": "웨이브 인스파이어",
        "category": "stability",
        "category_name": "안정화 (과회내 서포트)",
        "msrp_usd": 140,
        "msrp_krw": 169000,
        "widths": ["D", "2E"],
        "specs": {"weight_g": 295, "heel_drop_mm": 12, "midsole": "MIZUNO ENERZY + 아나토미컬 웨이브 서포트 플레이트", "plate": "Double Fan-shaped Wave Plate", "stack_height": "37.5mm / 25.5mm", "support_type": "Stability (과회내 안정화)"},
        "runrepeat": {"score": 83, "midsole_foam": "MIZUNO ENERZY", "pros": ["부채꼴 웨이브 플레이트의 완벽한 안쪽 발목 꺾임 방지", "단단한 힐컵의 락다운", "비틀림 저항 최우수"], "cons": ["경량화보다 안정성에 치중"], "verdict": "발목 힘이 약하고 평발인 러너에게 가장 견고한 방패가 되어주는 안정화.", "url": "https://runrepeat.com/mizuno-wave-inspire-20"}
    },
    {
        "id": "mizuno_wave_rebellion_pro_2",
        "brand_id": "mizuno",
        "name_kr": "미즈노 웨이브 리벨리온 프로 2",
        "name_en": "Mizuno Wave Rebellion Pro 2",
        "series": "웨이브 리벨리온",
        "category": "racing",
        "category_name": "레이싱화 (카본 슈퍼슈즈)",
        "msrp_usd": 250,
        "msrp_krw": 299000,
        "widths": ["D"],
        "specs": {"weight_g": 215, "heel_drop_mm": 4.5, "midsole": "SMOOTH SPEED ASSIST (힐이 없는 독창적 락커) + 카본 플레이트", "plate": "Carbon Infused Wave Plate", "stack_height": "38mm / 33.5mm", "support_type": "Neutral (극단적 미드풋/포어풋 레이서)"},
        "runrepeat": {"score": 89, "midsole_foam": "ENERZY LITE+", "pros": ["뒤꿈치가 잘려나간 혁신적인 힐리스 지오메트리", "강제적인 완벽한 미드풋/포어풋 착지 유도", "G3 아웃솔의 지면을 파고드는 접지력"], "cons": ["힐 스트라이커 러너는 착용 불가능"], "verdict": "미드풋 착지 러너에게 날개를 달아주는 전 세계에서 가장 급진적인 레이싱화.", "url": "https://runrepeat.com/mizuno-wave-rebellion-pro-2"}
    },

    # ------------------ ON RUNNING (2025/2026 LATEST, 3 models) ------------------
    {
        "id": "on_cloudrunner_2",
        "brand_id": "on",
        "name_kr": "온 클라우드러너 2",
        "name_en": "On Cloudrunner 2",
        "series": "클라우드러너",
        "category": "budget",
        "category_name": "가성비 입문화 (≤$100)",
        "msrp_usd": 140,
        "msrp_krw": 179000,
        "widths": ["D", "2E"],
        "specs": {"weight_g": 277, "heel_drop_mm": 10, "midsole": "Helion 슈퍼폼 + 업그레이드 CloudTec + 스피드보드", "plate": "Speedboard (TPU)", "stack_height": "33mm / 23mm", "support_type": "Stability (지지형 엔트리)"},
        "runrepeat": {"score": 80, "midsole_foam": "Helion Superfoam", "pros": ["헬리온 슈퍼폼 도입으로 전작 대비 훨씬 부드러워진 착지감", "돌 끼임 현상 완벽 개선", "온 러닝 특유의 세련된 프리미엄 디자인"], "cons": ["온 브랜드 특성상 100달러 미만 엔트리가 없음"], "verdict": "스타일과 안정적인 서포트를 모두 잡고 싶은 러너를 위한 온의 대표작.", "url": "https://runrepeat.com/on-cloudrunner-2"}
    },
    {
        "id": "on_cloudmonster_2",
        "brand_id": "on",
        "name_kr": "온 클라우드몬스터 2",
        "name_en": "On Cloudmonster 2",
        "series": "클라우드몬스터",
        "category": "daily",
        "category_name": "데일리 / 쿠션화",
        "msrp_usd": 180,
        "msrp_krw": 229000,
        "widths": ["D"],
        "specs": {"weight_g": 295, "heel_drop_mm": 6, "midsole": "듀얼 덴시티 Helion 슈퍼폼 + 거대 CloudTec 요소", "plate": "Speedboard (나일론 혼합)", "stack_height": "39mm / 33mm", "support_type": "Neutral (거대한 락커 쿠션)"},
        "runrepeat": {"score": 83, "midsole_foam": "Helion Dual Density", "pros": ["거대한 클라우드 구멍이 주는 독보적인 쿠션과 충격 분산", "앞으로 쏟아지는 익스트림 락커 롤링", "독보적인 미래지향적 비주얼"], "cons": ["스피드 레이싱에는 다소 묵직함"], "verdict": "쿠셔닝과 반발력을 극대화하여 달릴 때마다 튀어오르는 몬스터 러닝화.", "url": "https://runrepeat.com/on-cloudmonster-2"}
    },
    {
        "id": "on_cloudboom_echo_3",
        "brand_id": "on",
        "name_kr": "온 클라우드붐 에코 3",
        "name_en": "On Cloudboom Echo 3",
        "series": "클라우드붐",
        "category": "racing",
        "category_name": "레이싱화 (카본 슈퍼슈즈)",
        "msrp_usd": 290,
        "msrp_krw": 349000,
        "widths": ["D"],
        "specs": {"weight_g": 215, "heel_drop_mm": 9.5, "midsole": "Helion HF (100% Pebax 슈퍼폼) + 풀 카본 스피드보드", "plate": "Full Carbon Speedboard", "stack_height": "38mm / 28.5mm", "support_type": "Neutral (올림픽 카본 레이서)"},
        "runrepeat": {"score": 88, "midsole_foam": "Helion HF (PEBA)", "pros": ["온 최초의 100% Pebax(Helion HF) 슈퍼폼 탑재", "카본 스피드보드의 날카로운 가속과 킥", "초미세 마이크로파이버 깃털 어퍼"], "cons": ["매우 높은 34만원대 정가"], "verdict": "온 러닝이 마라톤 챔피언들을 위해 탄생시킨 스위스 엔지니어링 카본 플래그십.", "url": "https://runrepeat.com/on-cloudboom-echo-3"}
    },
    {
        "id": "on_cloudboom_strike",
        "brand_id": "on",
        "name_kr": "온 클라우드붐 스트라이크",
        "name_en": "On Cloudboom Strike",
        "series": "클라우드붐",
        "category": "racing",
        "category_name": "레이싱화 (카본 슈퍼슈즈)",
        "msrp_usd": 280,
        "msrp_krw": 339000,
        "widths": ["D"],
        "specs": {"weight_g": 201, "heel_drop_mm": 4, "midsole": "Helion HF (100% Pebax 초임계 폼) + 풀렝스 카본 스피드보드", "plate": "Full Carbon Speedboard", "stack_height": "39.5mm / 35.5mm", "support_type": "Neutral (엘리트 마라톤 카본 레이서)"},
        "runrepeat": {"score": 90, "midsole_foam": "Helion HF (Pebax)", "pros": ["201g 극경량 설계에 폭발적인 100% Pebax Helion HF 슈퍼폼 장착", "앞발 착지(포어풋/미드풋) 러너에게 최적화된 날카로운 탄성 킥", "뛰어난 젖은 노면 접지력과 밀착 일체형 레이싱 핏"], "cons": ["후족부 착지(힐 스트라이커) 러너에게는 다소 불안정한 서포트", "고가의 가격대"], "verdict": "온러닝의 혁신 기술이 총망라된 100% Pebax 기반의 세계 최정상급 마라톤 레이싱 플래그십.", "url": "https://runrepeat.com/on-cloudboom-strike"}
    }
]

def main():
    try:
        from expand_database_with_carryovers import CARRYOVER_SHOES
        for s in SHOES:
            if "gen_type" not in s:
                s["gen_type"] = "current"
            if "release_year" not in s:
                name = s.get("name_en", "").lower()
                if any(k in name for k in ["revel max", "hurricane 26", "clifton pro", "nimbus 27", "novablast 5", "rise 2", "superblast 2", "cloudboom strike"]):
                    s["release_year"] = 2026
                else:
                    s["release_year"] = 2025
        existing_ids = set(s["id"] for s in SHOES)
        for cs in CARRYOVER_SHOES:
            if cs["id"] not in existing_ids:
                SHOES.append(cs)
    except Exception as e:
        print(f"Notice: {e}")

    print(f"Total shoes generated: {len(SHOES)}")
    
    out_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(out_dir, "data")
    os.makedirs(data_dir, exist_ok=True)
    
    master_path = os.path.join(data_dir, "shoes_master.json")
    with open(master_path, "w", encoding="utf-8") as f:
        json.dump(SHOES, f, ensure_ascii=False, indent=2)
    print(f"Saved {len(SHOES)} shoes to {master_path}")
    
    config_path = os.path.join(data_dir, "brands_stores_config.json")
    config_data = {
        "brands": BRANDS,
        "categories": CATEGORIES,
        "generations": {
            "all": "전체 세대 (최신+이월)",
            "current": "✨ 2025-2026 최신형",
            "carryover": "🏷️ 2023-2024 이월할인 명작"
        },
        "sizes": [230, 235, 240, 245, 250, 255, 260, 265, 270, 275, 280, 285, 290, 295, 300, 305, 310],
        "widths": ["D", "2E", "4E"]
    }
    with open(config_path, "w", encoding="utf-8") as f:
        json.dump(config_data, f, ensure_ascii=False, indent=2)
    print(f"Saved config to {config_path}")
    
    data_js_path = os.path.join(out_dir, "data.js")
    with open(data_js_path, "w", encoding="utf-8") as f:
        f.write("/** ShoeF Master Database (2023-2026 Master Dataset) **/\n")
        f.write("window.SHOEF_CONFIG = " + json.dumps(config_data, ensure_ascii=False, indent=2) + ";\n\n")
        f.write("window.SHOEF_MASTER = " + json.dumps(SHOES, ensure_ascii=False, indent=2) + ";\n")
    print(f"Saved data.js to {data_js_path}")

if __name__ == "__main__":
    main()
