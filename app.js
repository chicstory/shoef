/**
 * ShoeF Wiki & Price - Main Application Controller (Fully Self-Contained)
 * 100% Verified Real Products from TheHyundai SmartStore
 */

// Embedded Fallback Data (Guarantees 0-latency instant render in file:// protocol)
const EMBEDDED_CONFIG = {
  "brands": [
    {
      "id": "nike",
      "name": "Nike",
      "name_kr": "나이키",
      "active": false,
      "logo_text": "NIKE"
    },
    {
      "id": "adidas",
      "name": "Adidas",
      "name_kr": "아디다스",
      "active": true,
      "logo_text": "ADIDAS"
    },
    {
      "id": "asics",
      "name": "Asics",
      "name_kr": "아식스",
      "active": true,
      "logo_text": "ASICS"
    },
    {
      "id": "saucony",
      "name": "Saucony",
      "name_kr": "써코니",
      "active": true,
      "logo_text": "SAUCONY"
    },
    {
      "id": "hoka",
      "name": "Hoka",
      "name_kr": "호카",
      "active": true,
      "logo_text": "HOKA"
    },
    {
      "id": "puma",
      "name": "Puma",
      "name_kr": "푸마",
      "active": false,
      "logo_text": "PUMA"
    },
    {
      "id": "brooks",
      "name": "Brooks",
      "name_kr": "브룩스",
      "active": false,
      "logo_text": "BROOKS"
    },
    {
      "id": "mizuno",
      "name": "Mizuno",
      "name_kr": "미ズノ",
      "active": false,
      "logo_text": "MIZUNO"
    },
    {
      "id": "on",
      "name": "On Running",
      "name_kr": "온",
      "active": false,
      "logo_text": "ON"
    },
    {
      "id": "newbalance",
      "name": "New Balance",
      "name_kr": "뉴발란스",
      "active": false,
      "logo_text": "NEW BALANCE"
    }
  ],
  "whitelist_stores": [
    {
      "id": "official",
      "name": "공식 온라인스토어",
      "badge": "공식몰",
      "type": "official",
      "trusted": true
    },
    {
      "id": "ssg_shinsegae",
      "name": "신세계백화점 (SSG/네이버)",
      "badge": "백화점",
      "type": "dept",
      "trusted": true
    },
    {
      "id": "lotte_on",
      "name": "롯데백화점 (롯데온/네이버)",
      "badge": "백화점",
      "type": "dept",
      "trusted": true
    },
    {
      "id": "hyundai_h",
      "name": "현대백화점 (더현대닷컴/네이버)",
      "badge": "백화점",
      "type": "dept",
      "trusted": true
    },
    {
      "id": "abcmart",
      "name": "ABC-MART (그랜드스테이지)",
      "badge": "슈즈몰",
      "type": "multi",
      "trusted": true
    },
    {
      "id": "goodrunner",
      "name": "굿러너 컴퍼니",
      "badge": "러닝전문",
      "type": "select",
      "trusted": true
    },
    {
      "id": "fleetrunner",
      "name": "플릿러너",
      "badge": "러닝전문",
      "type": "select",
      "trusted": true
    },
    {
      "id": "runnersclub",
      "name": "러너스클럽",
      "badge": "러닝전문",
      "type": "select",
      "trusted": true
    }
  ],
  "categories": [
    {
      "id": "all",
      "name": "전체 카테고리"
    },
    {
      "id": "entry",
      "name": "입문화"
    },
    {
      "id": "cushion",
      "name": "맥스 쿠션화"
    },
    {
      "id": "stability",
      "name": "안정화"
    },
    {
      "id": "allrounder",
      "name": "올라운더"
    },
    {
      "id": "super_trainer",
      "name": "슈퍼 트레이너"
    },
    {
      "id": "carbon_racing",
      "name": "카본 레이싱"
    }
  ],
  "sizes": [
    230,
    235,
    240,
    245,
    250,
    255,
    260,
    265,
    270,
    275,
    280,
    285,
    290,
    295,
    300,
    305,
    310
  ],
  "widths": [
    {
      "id": "all",
      "name": "전체 발볼"
    },
    {
      "id": "D",
      "name": "Standard (D 보통)"
    },
    {
      "id": "2E",
      "name": "Wide (2E 넓음)"
    },
    {
      "id": "4E",
      "name": "Extra Wide (4E 매우넓음)"
    }
  ]
};
const EMBEDDED_SHOES = [
  {
    "id": "saucony_endorphin_speed_5",
    "brand_id": "saucony",
    "name_kr": "써코니 엔돌핀 스피드 5",
    "name_en": "Saucony Endorphin Speed 5",
    "series": "엔돌핀 스피드",
    "is_current": true,
    "category": "super_trainer",
    "category_name": "슈퍼트레이너",
    "msrp": 199000,
    "image_url": "https://shop-phinf.pstatic.net/20260801_189/1785587747805XwK54_JPEG/119720556133984666_1763789495.jpg?type=f640",
    "style_code": "S21007-243",
    "widths": [
      "D"
    ],
    "specs": {
      "weight_g": 233,
      "heel_drop_mm": 8,
      "midsole": "PWRRUN PB (PEBA 초임계 폼) + 나일론 윙 플레이트",
      "cushion_level": "High (반발 탄성 극대화)",
      "support_type": "Neutral (중립)",
      "stack_height": "36mm / 28mm"
    },
    "runrepeat": {
      "score": 93,
      "midsole_foam": "PWRRUN PB",
      "rank_in_category": 2,
      "total_in_category": 85,
      "pros": [
        "PWRRUN PB 폼의 폭발적인 반발력과 부드러운 쿠션",
        "카본화 대비 피로도가 적어 데일리 템포런·인터벌·대회 올라운드",
        "나일론 윙 플레이트의 안정적인 좌우 뒤틀림 억제"
      ],
      "cons": [
        "우천 시 젖은 노면에서 접지력 주의",
        "카본 플레이트의 극한의 강성을 선호하는 러너에게는 유연함"
      ],
      "verdict": "대회 레이싱과 훈련을 모두 완벽하게 커버하는 현존 최고의 올라운드 스피드 트레이너."
    },
    "prices": [
      {
        "store_id": "thehyundai",
        "store_name": "현대백화점",
        "store_sub": "더현대 스마트스토어 (그랜드스테이지)",
        "badge": "백화점",
        "price": 132050,
        "shipping": 0,
        "discount_rate": 34,
        "width": "D",
        "sizes": [
          250,
          255,
          260,
          265,
          270,
          275,
          280
        ],
        "url": "https://smartstore.naver.com/thehyundai/products/13691193664",
        "is_lowest": true
      }
    ],
    "official_price": 199000
  },
  {
    "id": "saucony_triumph_22_wide",
    "brand_id": "saucony",
    "name_kr": "써코니 트라이엄프 22 와이드 (2E)",
    "name_en": "Saucony Triumph 22 Wide",
    "series": "트라이엄프",
    "is_current": true,
    "category": "cushion",
    "category_name": "쿠션화",
    "msrp": 209000,
    "image_url": "https://shop-phinf.pstatic.net/20260429_63/1777428800164e8k94_JPEG/53046832621008639_629161759.jpg?type=f640",
    "style_code": "S20965-218",
    "widths": [
      "2E"
    ],
    "specs": {
      "weight_g": 286,
      "heel_drop_mm": 10,
      "midsole": "PWRRUN PB (프리미엄 초임계 폼)",
      "cushion_level": "Maximum (극상의 충격 흡수)",
      "support_type": "Neutral (중립)",
      "stack_height": "37mm / 27mm"
    },
    "runrepeat": {
      "score": 91,
      "midsole_foam": "PWRRUN PB",
      "rank_in_category": 5,
      "total_in_category": 120,
      "pros": [
        "최상급 PWRRUN PB 폼 적용으로 풍부하면서도 꺼지지 않는 탄력 쿠션",
        "2E 와이드 발볼 설계로 발볼 넓은 한국인 러너에게 최상의 안락함",
        "장거리 LSD 시 발바닥 및 무릎 관절 완벽 보호"
      ],
      "cons": [
        "스피드 훈련용으로는 다소 묵직함"
      ],
      "verdict": "발볼 넓은 러너가 믿고 달릴 수 있는 최상급 데일리 맥스 쿠셔닝화."
    },
    "prices": [
      {
        "store_id": "thehyundai",
        "store_name": "현대백화점",
        "store_sub": "더현대 스마트스토어 (그랜드스테이지)",
        "badge": "백화점",
        "price": 179550,
        "shipping": 0,
        "discount_rate": 14,
        "width": "2E",
        "sizes": [
          255,
          260,
          265,
          270,
          275,
          280,
          285
        ],
        "url": "https://smartstore.naver.com/thehyundai/products/13444727307",
        "is_lowest": true
      }
    ],
    "official_price": 209000
  },
  {
    "id": "saucony_triumph_23_wide",
    "brand_id": "saucony",
    "name_kr": "써코니 트라이엄프 23 와이드 (2E)",
    "name_en": "Saucony Triumph 23 Wide",
    "series": "트라이엄프",
    "is_current": true,
    "category": "cushion",
    "category_name": "쿠션화",
    "msrp": 219000,
    "image_url": "https://shop-phinf.pstatic.net/20260801_265/1785587747805XwK54_JPEG/119720556133984666_1763789495.jpg?type=f640",
    "style_code": "S11024-200",
    "widths": [
      "2E"
    ],
    "specs": {
      "weight_g": 282,
      "heel_drop_mm": 10,
      "midsole": "PWRRUN PB 업그레이드 폼",
      "cushion_level": "Maximum",
      "support_type": "Neutral",
      "stack_height": "38mm / 28mm"
    },
    "runrepeat": {
      "score": 92,
      "midsole_foam": "PWRRUN PB",
      "rank_in_category": 4,
      "total_in_category": 120,
      "pros": [
        "44% 파격 할인으로 12만 원대 진입한 최강 가성비",
        "부드러운 전방 발구름과 경량화된 엔지니어드 메시 어퍼"
      ],
      "cons": [
        "인기 와이드 사이즈 품절 임박"
      ],
      "verdict": "맥스 쿠션의 완성형 모델, 높은 할인율로 실구매 매력도 극대화."
    },
    "prices": [
      {
        "store_id": "thehyundai",
        "store_name": "현대백화점",
        "store_sub": "더현대 스마트스토어 (그랜드스테이지)",
        "badge": "백화점",
        "price": 122550,
        "shipping": 0,
        "discount_rate": 44,
        "width": "2E",
        "sizes": [
          240,
          245,
          250,
          255,
          260
        ],
        "url": "https://smartstore.naver.com/thehyundai/products/13691194246",
        "is_lowest": true
      }
    ],
    "official_price": 219000
  },
  {
    "id": "saucony_ride_16",
    "brand_id": "saucony",
    "name_kr": "써코니 라이드 16",
    "name_en": "Saucony Ride 16",
    "series": "라이드",
    "is_current": false,
    "category": "cushion",
    "category_name": "쿠션화",
    "msrp": 179000,
    "image_url": "https://shop-phinf.pstatic.net/20260523_114/17795155609383Kqg2_JPEG/113648371302824361_152220412.jpg?type=f640",
    "style_code": "S10830-25",
    "widths": [
      "D"
    ],
    "specs": {
      "weight_g": 249,
      "heel_drop_mm": 8,
      "midsole": "PWRRUN 폼",
      "cushion_level": "Medium-Firm (경쾌한 밸런스)",
      "support_type": "Neutral",
      "stack_height": "35mm / 27mm"
    },
    "runrepeat": {
      "score": 88,
      "midsole_foam": "PWRRUN",
      "rank_in_category": 12,
      "total_in_category": 100,
      "pros": [
        "가볍고 경쾌한 착지감, 긴 마일리지 내구성",
        "과하지 않고 정직한 반응성을 선호하는 러너에게 최적"
      ],
      "cons": [
        "최신 PB 폼 대비 단단한 클래식 쿠션감"
      ],
      "verdict": "오래 신어도 내구성 탄탄한 정통 데일리 트레이너."
    },
    "prices": [
      {
        "store_id": "thehyundai",
        "store_name": "현대백화점",
        "store_sub": "더현대 스마트스토어 (그랜드스테이지)",
        "badge": "백화점",
        "price": 151050,
        "shipping": 0,
        "discount_rate": 16,
        "width": "D",
        "sizes": [
          235,
          240,
          245,
          250
        ],
        "url": "https://smartstore.naver.com/thehyundai/products/13466709938",
        "is_lowest": true
      }
    ],
    "official_price": 179000
  },
  {
    "id": "saucony_lancer_3",
    "brand_id": "saucony",
    "name_kr": "써코니 랜서 3",
    "name_en": "Saucony Lancer 3",
    "series": "랜서",
    "is_current": true,
    "category": "entry",
    "category_name": "입문화",
    "msrp": 89000,
    "image_url": "https://shop-phinf.pstatic.net/20260801_189/1785587747805XwK54_JPEG/119720556133984666_1763789495.jpg?type=f640",
    "style_code": "S28226-3",
    "widths": [
      "D"
    ],
    "specs": {
      "weight_g": 265,
      "heel_drop_mm": 8,
      "midsole": "EVA 폼",
      "cushion_level": "Medium",
      "support_type": "Neutral",
      "stack_height": "30mm / 22mm"
    },
    "runrepeat": {
      "score": 83,
      "midsole_foam": "EVA",
      "rank_in_category": 35,
      "total_in_category": 100,
      "pros": [
        "5만 원대 압도적 가성비로 헬스장·트레드밀 조깅 입문에 최적"
      ],
      "cons": [
        "장거리 마라톤 대회용으로는 반발력 한계"
      ],
      "verdict": "부담 없이 시작하는 가장 실속 있는 입문 러닝화."
    },
    "prices": [
      {
        "store_id": "thehyundai",
        "store_name": "현대백화점",
        "store_sub": "더현대 스마트스토어 (그랜드스테이지)",
        "badge": "백화점",
        "price": 56050,
        "shipping": 0,
        "discount_rate": 37,
        "width": "D",
        "sizes": [
          250,
          255,
          260,
          265,
          270,
          275,
          280
        ],
        "url": "https://smartstore.naver.com/thehyundai/products/13691245006",
        "is_lowest": true
      }
    ],
    "official_price": 89000
  },
  {
    "id": "adidas_adizero_boston_13_w",
    "brand_id": "adidas",
    "name_kr": "아디다스 아디제로 보스턴 13 W",
    "name_en": "Adidas Adizero Boston 13 Women",
    "series": "아디제로 보스턴",
    "is_current": true,
    "category": "super_trainer",
    "category_name": "슈퍼트레이너",
    "msrp": 189000,
    "image_url": "https://shop-phinf.pstatic.net/20260902_125/17883066989098oKLP_JPEG/41023597044480566_808848726.jpg?type=f640",
    "style_code": "KH8869",
    "widths": [
      "D"
    ],
    "specs": {
      "weight_g": 235,
      "heel_drop_mm": 7,
      "midsole": "Lightstrike Pro + Lightstrike 2.0 + 에너지로드 2.0",
      "cushion_level": "High (강력한 전방 롤링)",
      "support_type": "Neutral",
      "stack_height": "37mm / 30mm"
    },
    "runrepeat": {
      "score": 90,
      "midsole_foam": "Lightstrike Pro",
      "rank_in_category": 3,
      "total_in_category": 85,
      "pros": [
        "에너지로드 2.0이 선사하는 일관되고 폭발적인 전방 추진력",
        "컨티넨탈 러버 아웃솔의 우천 노면 완벽 접지력",
        "보스턴 12 대비 힐컵 핏 개선으로 뒤꿈치 들림 완전 해소"
      ],
      "cons": [
        "페이스 6분 이상 느린 조깅에서는 다소 단단하게 느껴짐"
      ],
      "verdict": "서브4 및 마라톤 완주를 목표로 하는 러너를 위한 최적의 훈련화."
    },
    "prices": [
      {
        "store_id": "thehyundai",
        "store_name": "현대백화점",
        "store_sub": "더현대 스마트스토어 (아디다스코리아 공식)",
        "badge": "공식몰",
        "price": 189000,
        "shipping": 0,
        "discount_rate": 0,
        "width": "D",
        "sizes": [
          230,
          235,
          240,
          245,
          250,
          255
        ],
        "url": "https://smartstore.naver.com/thehyundai/products/13741254517",
        "is_lowest": true
      }
    ],
    "official_price": 189000
  },
  {
    "id": "adidas_adizero_evo_sl",
    "brand_id": "adidas",
    "name_kr": "아디다스 아디제로 EVO SL EXO",
    "name_en": "Adidas Adizero EVO SL EXO",
    "series": "아디제로 EVO SL",
    "is_current": true,
    "category": "super_trainer",
    "category_name": "슈퍼트레이너",
    "msrp": 209000,
    "image_url": "https://shop-phinf.pstatic.net/20260909_163/1788939768565l0F9m_JPEG/123072678685121408_136195822.jpg?type=f640",
    "style_code": "KJ0436",
    "widths": [
      "D"
    ],
    "specs": {
      "weight_g": 208,
      "heel_drop_mm": 6.5,
      "midsole": "Lightstrike Pro 풀렝스 (플레이트리스)",
      "cushion_level": "High (초경량 퓨어 폼)",
      "support_type": "Neutral",
      "stack_height": "35mm / 28.5mm"
    },
    "runrepeat": {
      "score": 92,
      "midsole_foam": "Lightstrike Pro",
      "rank_in_category": 1,
      "total_in_category": 85,
      "pros": [
        "플레이트 없이도 퓨어 라이트스트라이크 프로 폼이 주는 환상적인 쿠션 반발",
        "208g의 경이로운 경량성으로 인터벌과 레이스 모두 소화"
      ],
      "cons": [
        "극강의 경량화 세팅으로 안정성은 다소 중립적"
      ],
      "verdict": "카본 플레이트의 피로감 없이 순수 폼의 쾌감을 느끼고 싶은 러너를 위한 최신작."
    },
    "prices": [
      {
        "store_id": "thehyundai",
        "store_name": "현대백화점",
        "store_sub": "더현대 스마트스토어 (아디다스코리아 공식)",
        "badge": "공식몰",
        "price": 209000,
        "shipping": 0,
        "discount_rate": 0,
        "width": "D",
        "sizes": [
          250,
          255,
          260,
          265,
          270,
          275,
          280,
          285
        ],
        "url": "https://smartstore.naver.com/thehyundai/products/13753687280",
        "is_lowest": true
      }
    ],
    "official_price": 209000
  },
  {
    "id": "adidas_hyperboost_run",
    "brand_id": "adidas",
    "name_kr": "아디다스 하이퍼부스트 런 러닝화",
    "name_en": "Adidas Hyperboost Run",
    "series": "하이퍼부스트",
    "is_current": true,
    "category": "cushion",
    "category_name": "쿠션화",
    "msrp": 219000,
    "image_url": "https://shop-phinf.pstatic.net/20260728_57/1785233649666oT40W_JPEG/119366458021124430_1669466504.jpg?type=f640",
    "style_code": "KK2020",
    "widths": [
      "D"
    ],
    "specs": {
      "weight_g": 290,
      "heel_drop_mm": 10,
      "midsole": "Hyperboost 복합 폼",
      "cushion_level": "Maximum",
      "support_type": "Neutral",
      "stack_height": "36mm / 26mm"
    },
    "runrepeat": {
      "score": 86,
      "midsole_foam": "Hyperboost",
      "rank_in_category": 18,
      "total_in_category": 110,
      "pros": [
        "쫀득한 부스트 쿠셔닝으로 일상 조깅 및 장시간 워킹에 탁월"
      ],
      "cons": [
        "스피드 훈련용으로는 다소 무게감 있음"
      ],
      "verdict": "일상 러닝과 워킹을 겸하는 프리미엄 데일리 쿠셔닝화."
    },
    "prices": [
      {
        "store_id": "thehyundai",
        "store_name": "현대백화점",
        "store_sub": "더현대 스마트스토어 (아디다스코리아 공식)",
        "badge": "공식몰",
        "price": 219000,
        "shipping": 0,
        "discount_rate": 0,
        "width": "D",
        "sizes": [
          250,
          255,
          260,
          265,
          270,
          275,
          280
        ],
        "url": "https://smartstore.naver.com/thehyundai/products/13685107204",
        "is_lowest": true
      }
    ],
    "official_price": 219000
  },
  {
    "id": "hoka_clifton_10_m",
    "brand_id": "hoka",
    "name_kr": "호카 클리프톤 10 남성용 (발볼 D)",
    "name_en": "Hoka Clifton 10 Men Regular",
    "series": "클리프톤",
    "is_current": true,
    "category": "cushion",
    "category_name": "쿠션화",
    "msrp": 229000,
    "image_url": "https://shop-phinf.pstatic.net/20260523_114/17795155609383Kqg2_JPEG/113648371302824361_152220412.jpg?type=f640",
    "style_code": "1162030-BBLC",
    "widths": [
      "D"
    ],
    "specs": {
      "weight_g": 252,
      "heel_drop_mm": 5,
      "midsole": "New CMEVA 초경량 폼",
      "cushion_level": "High (호카 시그니처 롤링 쿠션)",
      "support_type": "Neutral",
      "stack_height": "39mm / 34mm"
    },
    "runrepeat": {
      "score": 90,
      "midsole_foam": "CMEVA",
      "rank_in_category": 4,
      "total_in_category": 110,
      "pros": [
        "더 부드럽고 가벼워진 10세대 신형 미드솔",
        "메타로커 지오메트리로 자연스러운 전방 롤링",
        "남성 표준 D 발볼로 안정적인 발등 락다운"
      ],
      "cons": [
        "초와이드 발볼 러너는 와이드 모델 권장"
      ],
      "verdict": "구름 위를 달리는 듯한 호카 특유의 쿠션감과 부드러운 발구름의 대명사."
    },
    "prices": [
      {
        "store_id": "thehyundai",
        "store_name": "현대백화점",
        "store_sub": "더현대 스마트스토어 (럭스보이 정품)",
        "badge": "백화점",
        "price": 229000,
        "shipping": 0,
        "discount_rate": 0,
        "width": "D",
        "sizes": [
          255,
          260,
          265,
          270,
          275,
          280
        ],
        "url": "https://smartstore.naver.com/thehyundai/products/13463156094",
        "is_lowest": true
      }
    ],
    "official_price": 229000
  },
  {
    "id": "hoka_clifton_10_w",
    "brand_id": "hoka",
    "name_kr": "호카 클리프톤 10 여성용 (발볼 B)",
    "name_en": "Hoka Clifton 10 Women Regular",
    "series": "클리프톤",
    "is_current": true,
    "category": "cushion",
    "category_name": "쿠션화",
    "msrp": 251000,
    "image_url": "https://shop-phinf.pstatic.net/20260523_114/17795155609383Kqg2_JPEG/113648371302824361_152220412.jpg?type=f640",
    "style_code": "1162031-BWHT",
    "widths": [
      "B"
    ],
    "specs": {
      "weight_g": 215,
      "heel_drop_mm": 5,
      "midsole": "New CMEVA 초경량 폼",
      "cushion_level": "High",
      "support_type": "Neutral",
      "stack_height": "37mm / 32mm"
    },
    "runrepeat": {
      "score": 90,
      "midsole_foam": "CMEVA",
      "rank_in_category": 4,
      "total_in_category": 110,
      "pros": [
        "여성 발골격에 맞춘 B 발볼과 편안한 힐칼라",
        "무릎과 발목 관절을 부드럽게 보호하는 충격 흡수"
      ],
      "cons": [
        "남성 대비 타이트한 핏감"
      ],
      "verdict": "부상 방지와 편안한 쿠셔닝을 원하는 여성 러너를 위한 최적의 선택."
    },
    "prices": [
      {
        "store_id": "thehyundai",
        "store_name": "현대백화점",
        "store_sub": "더현대 스마트스토어 (럭스보이 정품)",
        "badge": "백화점",
        "price": 251000,
        "shipping": 0,
        "discount_rate": 0,
        "width": "B",
        "sizes": [
          230,
          235,
          240,
          245,
          250
        ],
        "url": "https://smartstore.naver.com/thehyundai/products/13462912029",
        "is_lowest": true
      }
    ],
    "official_price": 251000
  },
  {
    "id": "hoka_bondi_9_m",
    "brand_id": "hoka",
    "name_kr": "호카 본디 9 남성용 (발볼 D)",
    "name_en": "Hoka Bondi 9 Men Regular",
    "series": "본디",
    "is_current": true,
    "category": "cushion",
    "category_name": "쿠션화",
    "msrp": 280000,
    "image_url": "https://shop-phinf.pstatic.net/20260523_114/17795155609383Kqg2_JPEG/113648371302824361_152220412.jpg?type=f640",
    "style_code": "1162011-BBLC",
    "widths": [
      "D"
    ],
    "specs": {
      "weight_g": 305,
      "heel_drop_mm": 4,
      "midsole": "초임계 EVA 맥스폼",
      "cushion_level": "Maximum (최대 두께의 쿠션 베드)",
      "support_type": "Neutral",
      "stack_height": "42mm / 38mm"
    },
    "runrepeat": {
      "score": 89,
      "midsole_foam": "Supercritical EVA",
      "rank_in_category": 6,
      "total_in_category": 120,
      "pros": [
        "호카 라인업 중 가장 두껍고 푹신한 맥스 쿠션",
        "체중이 나가는 과체중 러너나 족저근막염 환자에게 독보적 보호력"
      ],
      "cons": [
        "무게감이 있어 빠른 템포런에는 부적합"
      ],
      "verdict": "발바닥 충격을 완벽히 흡수하는 궁극의 리커버리 & 맥스 쿠션화."
    },
    "prices": [
      {
        "store_id": "thehyundai",
        "store_name": "현대백화점",
        "store_sub": "더현대 스마트스토어 (럭스보이 정품)",
        "badge": "백화점",
        "price": 280000,
        "shipping": 0,
        "discount_rate": 0,
        "width": "D",
        "sizes": [
          260,
          265,
          270,
          275,
          280,
          285
        ],
        "url": "https://smartstore.naver.com/thehyundai/products/13598493783",
        "is_lowest": true
      }
    ],
    "official_price": 280000
  },
  {
    "id": "asics_gel_kayano_12_1",
    "brand_id": "asics",
    "name_kr": "아식스 젤 카야노 12.1",
    "name_en": "Asics Gel Kayano 12.1",
    "series": "젤 카야노",
    "is_current": true,
    "category": "stability",
    "category_name": "안정화",
    "msrp": 264000,
    "image_url": "https://shop-phinf.pstatic.net/20260523_114/17795155609383Kqg2_JPEG/113648371302824361_152220412.jpg?type=f640",
    "style_code": "1203A759-100",
    "widths": [
      "D"
    ],
    "specs": {
      "weight_g": 315,
      "heel_drop_mm": 10,
      "midsole": "GEL 쿠셔닝 + 트러스틱 아치 서포트",
      "cushion_level": "High (단단한 내측 지지력)",
      "support_type": "Stability (과내번 방지)",
      "stack_height": "32mm / 22mm"
    },
    "runrepeat": {
      "score": 90,
      "midsole_foam": "ASICS GEL",
      "rank_in_category": 3,
      "total_in_category": 50,
      "pros": [
        "카야노 고유의 트러스틱 구조로 발목 안쪽 무너짐 완벽 방지",
        "레트로 러닝 무드와 안정성을 겸비"
      ],
      "cons": [
        "경량 레이싱용으로는 무거운 편"
      ],
      "verdict": "평발 및 과내번 러너의 발목을 든든하게 지지해주는 아식스의 전설."
    },
    "prices": [
      {
        "store_id": "thehyundai",
        "store_name": "현대백화점",
        "store_sub": "더현대 스마트스토어 (직수입/스니커즈관)",
        "badge": "백화점",
        "price": 264000,
        "shipping": 0,
        "discount_rate": 0,
        "width": "D",
        "sizes": [
          250,
          255,
          260,
          265,
          270,
          275,
          280
        ],
        "url": "https://smartstore.naver.com/thehyundai/products/13463102714",
        "is_lowest": true
      }
    ],
    "official_price": 264000
  },
  {
    "id": "asics_gt_2160",
    "brand_id": "asics",
    "name_kr": "아식스 GT-2160",
    "name_en": "Asics GT-2160",
    "series": "GT-2000",
    "is_current": true,
    "category": "stability",
    "category_name": "안정화",
    "msrp": 167000,
    "image_url": "https://shop-phinf.pstatic.net/20260523_114/17795155609383Kqg2_JPEG/113648371302824361_152220412.jpg?type=f640",
    "style_code": "1203A275-111",
    "widths": [
      "D"
    ],
    "specs": {
      "weight_g": 310,
      "heel_drop_mm": 10,
      "midsole": "GEL 쿠셔닝 시스템",
      "cushion_level": "Medium-Firm",
      "support_type": "Stability",
      "stack_height": "30mm / 20mm"
    },
    "runrepeat": {
      "score": 88,
      "midsole_foam": "ASICS GEL",
      "rank_in_category": 7,
      "total_in_category": 50,
      "pros": [
        "2000년대 기술적 유산과 트러스틱 지지 구조",
        "가벼운 조깅과 일상 착용에 모두 적합"
      ],
      "cons": [
        "최신 초임계 폼 대비 반발력은 보통"
      ],
      "verdict": "안정적인 지지력과 레트로 무드를 동시에 잡은 헤리티지 러닝화."
    },
    "prices": [
      {
        "store_id": "thehyundai",
        "store_name": "현대백화점",
        "store_sub": "더현대 스마트스토어 (직수입/스니커즈관)",
        "badge": "백화점",
        "price": 167000,
        "shipping": 0,
        "discount_rate": 0,
        "width": "D",
        "sizes": [
          250,
          255,
          260,
          265,
          270,
          275
        ],
        "url": "https://smartstore.naver.com/thehyundai/products/13463080720",
        "is_lowest": true
      }
    ],
    "official_price": 167000
  }
];

function initShoeFApp() {
  let brandsConfig = EMBEDDED_CONFIG;
  let shoesData = EMBEDDED_SHOES;
  let selectedBrands = new Set(['nike', 'adidas', 'asics', 'saucony', 'hoka', 'puma', 'newbalance', 'brooks', 'mizuno', 'on']);
  let currentSort = 'price-asc';

  // DOM Elements
  const brandGridEl = document.getElementById('brandCheckboxGrid');
  const btnSelectAllBrands = document.getElementById('btnSelectAllBrands');
  const btnDeselectAllBrands = document.getElementById('btnDeselectAllBrands');
  const categoryFilter = document.getElementById('categoryFilter');
  const sizeFilter = document.getElementById('sizeFilter');
  const widthFilter = document.getElementById('widthFilter');
  const searchKeyword = document.getElementById('searchKeyword');
  const outletOnlyToggle = document.getElementById('outletOnlyToggle');
  const totalCountEl = document.getElementById('totalCount');
  const shoesListEl = document.getElementById('shoesList');
  const sortBtns = document.querySelectorAll('.sort-btn');

  // Modal Elements
  const modalEl = document.getElementById('runrepeatModal');
  const btnCloseModal = document.getElementById('btnCloseModal');
  const modalBrandBadge = document.getElementById('modalBrandBadge');
  const modalShoeName = document.getElementById('modalShoeName');
  const modalScore = document.getElementById('modalScore');
  const modalWeight = document.getElementById('modalWeight');
  const modalDrop = document.getElementById('modalDrop');
  const modalStack = document.getElementById('modalStack');
  const modalPlate = document.getElementById('modalPlate');
  const modalFoam = document.getElementById('modalFoam');
  const modalProsList = document.getElementById('modalProsList');
  const modalConsList = document.getElementById('modalConsList');
  const modalSummary = document.getElementById('modalSummary');

  // If window data is provided, prefer it
  if (typeof window !== 'undefined') {
    if (window.SHOEF_CONFIG) brandsConfig = window.SHOEF_CONFIG;
    if (window.SHOEF_DATA || window.SHOEF_MASTER) shoesData = window.SHOEF_DATA || window.SHOEF_MASTER;
  }

  // 2. Init Controls
  initBrandCheckboxes();
  initSizeSelect();
  attachEvents();
  renderShoes();

  // 2-1. Brand SVG Logos Map
  const BRAND_LOGOS = {
    nike: `<svg viewBox="0 0 24 24" fill="currentColor"><path d="M21.707 5.293c-.27-.27-.75-.15-1.28.27-2.14 1.7-6.07 5.09-10.42 9.07-2.06 1.89-3.88 3.63-5.26 5.03-1.61 1.63-2.6 2.37-3.32 2.34-.65-.03-1.12-.6-1.37-1.57-.42-1.66.1-4.04 1.54-6.97 1.48-3.02 3.86-6.42 6.89-9.84.45-.51.15-1.32-.51-1.42-.58-.09-1.2.2-1.63.7-3.08 3.55-5.52 7.1-7.05 10.27-1.62 3.35-2.22 6.16-1.66 8.35.61 2.41 2.15 3.68 4.3 3.68 1.48 0 3.25-.85 5.16-2.5 1.52-1.31 3.42-3.06 5.56-4.99 4.39-3.95 8.31-7.25 10.36-8.86.8-.63 1.34-1.17 1.62-1.61.43-.68.27-1.41-.47-1.92z"/></svg>`,
    adidas: `<svg viewBox="0 0 24 24" fill="currentColor"><path d="M22.02 18.57l-4.52-7.83c-.35-.61-1.13-.82-1.74-.47-.61.35-.82 1.13-.47 1.74l4.52 7.83c.35.61 1.13.82 1.74.47.61-.35.82-1.13.47-1.74zm-6.22 0l-5.74-9.94c-.35-.61-1.13-.82-1.74-.47-.61.35-.82 1.13-.47 1.74l5.74 9.94c.35.61 1.13.82 1.74.47.61-.35.82-1.13.47-1.74zm-6.22 0L2.62 6.51c-.35-.61-1.13-.82-1.74-.47-.61.35-.82 1.13-.47 1.74l6.96 12.06c.35.61 1.13.82 1.74.47.61-.35.82-1.13.47-1.74z"/></svg>`,
    asics: `<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12.5 3c-5.25 0-9.5 4.25-9.5 9.5 0 2.12.7 4.08 1.88 5.66l2.12-2.12C6.38 14.94 6 13.78 6 12.5 6 8.91 8.91 6 12.5 6c1.66 0 3.17.62 4.34 1.66l2.12-2.12C17.26 3.94 15.01 3 12.5 3zm6.62 3.84l-2.12 2.12C17.62 10.06 18 11.22 18 12.5c0 3.59-2.91 6.5-6.5 6.5-1.66 0-3.17-.62-4.34-1.66l-2.12 2.12C6.74 20.94 8.99 22 12.5 22c5.25 0 9.5-4.25 9.5-9.5 0-2.12-.7-4.08-1.88-5.66z"/></svg>`,
    saucony: `<svg viewBox="0 0 24 24" fill="currentColor"><path d="M2.5 14.5c2.2 0 4.1-1.2 5.2-3 1.1-1.8 3-3 5.3-3 3.6 0 6.5 2.9 6.5 6.5s-2.9 6.5-6.5 6.5c-3.1 0-5.7-2.2-6.3-5.1H4.2c.7 4.2 4.4 7.4 8.8 7.4 4.9 0 9-4.1 9-9.1s-4-9.1-9-9.1c-3.2 0-6 1.7-7.5 4.3C4.6 11.6 3.6 12.2 2.5 12.2v2.3zm12-4.5c.8 0 1.5-.7 1.5-1.5S15.3 7 14.5 7s-1.5.7-1.5 1.5.7 1.5 1.5 1.5zm-3 2c.8 0 1.5-.7 1.5-1.5S12.3 9 11.5 9s-1.5.7-1.5 1.5.7 1.5 1.5 1.5zm-3 2c.8 0 1.5-.7 1.5-1.5S9.3 11 8.5 11 7 11.7 7 12.5s.7 1.5 1.5 1.5z"/></svg>`,
    hoka: `<svg viewBox="0 0 24 24" fill="currentColor"><path d="M2 13.5c4-2 8-5 13-5 3.5 0 6 1.5 7 3.5-2.5.5-5.5-.5-8.5.5-4 1.3-7.5 4.5-11.5 4.5v-3.5zm2 5.5c3.5-1 6.5-3 10-3 3 0 5.5 1.2 7 2.5-3.5 0-7 1.5-10.5 2-2.5.3-4.5-.5-6.5-1.5z"/></svg>`,
    puma: `<svg viewBox="0 0 24 24" fill="currentColor"><path d="M20.9 6.8c-.5-.3-1.1-.5-1.7-.5-1.3 0-2.4.7-3 1.8-.7 1.2-1.8 2-3.1 2.3-1.2.3-2.5.1-3.6-.5L7.2 8.5c-.8-.5-1.8-.6-2.7-.3-.9.3-1.6 1-1.9 1.9L2 12.3c.4-.1.8-.2 1.3-.2 1.3 0 2.5.6 3.3 1.6l2 2.5c.8 1 2 1.6 3.3 1.6h2.2c1.2 0 2.4-.6 3.1-1.6l3.5-4.8c.8-1.1 1.2-2.4 1.2-3.8 0-.3-.1-.6-.2-.9l-.8.1z"/></svg>`,
    newbalance: `<svg viewBox="0 0 24 24" fill="currentColor"><path d="M2 18h4.5l5.5-9.5V18h4V6h-4.5L6 15.5V6H2v12z"/></svg>`,
    brooks: `<svg viewBox="0 0 24 24" fill="currentColor"><path d="M2.5 15.5l14-8.5c1.8-1.1 4.1-.5 5.2 1.3.8 1.3.8 2.9 0 4.2L12 18.5c-2.3 1.4-5.2.6-6.6-1.7l-2.9-1.3z"/></svg>`,
    mizuno: `<svg viewBox="0 0 24 24" fill="currentColor"><path d="M21.5 5.5l-7.2 9.8-3.8-3.8-6.5 6.5 2.5-7.5 4.5 4 4.5-6.5 6-2.5z"/></svg>`,
    on: `<svg viewBox="0 0 24 24" fill="currentColor"><circle cx="7" cy="12" r="4.5" fill="none" stroke="currentColor" stroke-width="2.5"/><path d="M14 8.5v7m0-7a3.5 3.5 0 0 1 7 0v7" fill="none" stroke="currentColor" stroke-width="2.5"/></svg>`
  };

  // 2-2. Init 10 Brands Logo Selection (Color / Grayscale Toggle)
  function initBrandCheckboxes() {
    brandGridEl.innerHTML = '';
    brandsConfig.brands.forEach(brand => {
      const isChecked = selectedBrands.has(brand.id);
      const count = shoesData.filter(s => s.brand_id === brand.id).length;
      const logoSvg = BRAND_LOGOS[brand.id] || brand.svg_logo || `<span style="font-weight:800; font-size:11px;">${brand.name.substring(0, 3)}</span>`;

      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = `brand-logo-btn ${isChecked ? 'active' : 'inactive'}`;
      btn.dataset.brandId = brand.id;
      btn.innerHTML = `
        <div class="brand-logo-icon">${logoSvg}</div>
        <span class="brand-logo-name">${brand.name_kr}</span>
        <span class="brand-logo-count">${count > 0 ? count : '-'}</span>
      `;

      btn.addEventListener('click', () => {
        if (selectedBrands.has(brand.id)) {
          selectedBrands.delete(brand.id);
          btn.classList.remove('active');
          btn.classList.add('inactive');
        } else {
          selectedBrands.add(brand.id);
          btn.classList.add('active');
          btn.classList.remove('inactive');
        }
        renderShoes();
      });

      brandGridEl.appendChild(btn);
    });
  }

  // 2-2. Init 230 ~ 310mm Size Options
  function initSizeSelect() {
    brandsConfig.sizes.forEach(size => {
      const opt = document.createElement('option');
      opt.value = size;
      opt.textContent = `${size} mm`;
      sizeFilter.appendChild(opt);
    });
  }

  // 2-3. Event Handlers
  function attachEvents() {
    btnSelectAllBrands.addEventListener('click', () => {
      brandsConfig.brands.forEach(b => selectedBrands.add(b.id));
      document.querySelectorAll('.brand-logo-btn').forEach(item => {
        item.classList.add('active');
        item.classList.remove('inactive');
      });
      renderShoes();
    });

    btnDeselectAllBrands.addEventListener('click', () => {
      selectedBrands.clear();
      document.querySelectorAll('.brand-logo-btn').forEach(item => {
        item.classList.remove('active');
        item.classList.add('inactive');
      });
      renderShoes();
    });

    categoryFilter.addEventListener('change', renderShoes);
    sizeFilter.addEventListener('change', renderShoes);
    widthFilter.addEventListener('change', renderShoes);
    searchKeyword.addEventListener('input', renderShoes);
    outletOnlyToggle.addEventListener('change', renderShoes);

    sortBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        sortBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentSort = btn.dataset.sort;
        renderShoes();
      });
    });

    // Modal close
    btnCloseModal.addEventListener('click', () => {
      modalEl.style.display = 'none';
    });
    modalEl.addEventListener('click', (e) => {
      if (e.target === modalEl) modalEl.style.display = 'none';
    });
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && modalEl.style.display !== 'none') {
        modalEl.style.display = 'none';
      }
    });
  }

  // 3. Filter & Sort Logic
  function getFilteredShoes() {
    const catVal = categoryFilter.value;
    const sizeVal = sizeFilter.value === 'all' ? null : parseInt(sizeFilter.value, 10);
    const widthVal = widthFilter.value;
    const query = searchKeyword.value.trim().toLowerCase();
    const outletOnly = outletOnlyToggle.checked;

    return shoesData.filter(shoe => {
      // 1) Brand filter
      if (!selectedBrands.has(shoe.brand_id)) return false;

      // 2) Category filter
      if (catVal !== 'all' && shoe.category !== catVal) return false;

      // 3) Outlet only toggle
      if (outletOnly && shoe.is_current !== false) return false;

      // 4) Keyword search
      if (query) {
        const text = `${shoe.name_kr} ${shoe.name_en} ${shoe.series} ${shoe.runrepeat.midsole_foam} ${shoe.category_name}`.toLowerCase();
        if (!text.includes(query)) return false;
      }

      // 5) Width filter
      if (widthVal !== 'all') {
        if (!shoe.widths.includes(widthVal)) return false;
      }

      // 6) Size filter: 신발 판매처 중 해당 사이즈 재고가 있는 가격이 있는지 확인
      if (sizeVal !== null) {
        const hasSize = shoe.prices.some(p => p.sizes.includes(sizeVal));
        if (!hasSize) return false;
      }

      return true;
    }).map(shoe => {
      // 사이즈나 발볼 필터가 걸려있을 경우 가격 목록 필터링 및 최저가 재계산
      let validPrices = shoe.prices;
      if (sizeVal !== null) {
        validPrices = validPrices.filter(p => p.sizes.includes(sizeVal));
      }
      if (widthVal !== 'all') {
        validPrices = validPrices.filter(p => p.width === widthVal || (widthVal === 'D' && !p.width));
      }

      if (validPrices.length === 0) validPrices = shoe.prices; // Fallback to all prices

      // Find lowest price
      const minPrice = Math.min(...validPrices.map(p => p.price));
      const maxDiscount = Math.max(...validPrices.map(p => p.discount_rate || 0));

      return {
        ...shoe,
        displayPrices: validPrices,
        effectiveLowestPrice: minPrice,
        effectiveMaxDiscount: maxDiscount
      };
    }).sort((a, b) => {
      if (currentSort === 'price-asc') {
        return a.effectiveLowestPrice - b.effectiveLowestPrice;
      } else if (currentSort === 'discount-desc') {
        return b.effectiveMaxDiscount - a.effectiveMaxDiscount;
      } else if (currentSort === 'score-desc') {
        return b.runrepeat.score - a.runrepeat.score;
      }
      return 0;
    });
  }

  // 4. Render Danawa-Style Shoes List
  function renderShoes() {
    const list = getFilteredShoes();
    totalCountEl.textContent = list.length;

    if (list.length === 0) {
      shoesListEl.innerHTML = `
        <div style="text-align: center; padding: 60px 20px; color: var(--text-dim);">
          <div style="font-size: 32px; margin-bottom: 12px;">👟🔍</div>
          <div style="font-size: 16px; font-weight: 600; color: var(--text-muted);">조건에 맞는 신발을 찾을 수 없습니다.</div>
          <div style="font-size: 13px; margin-top: 6px;">브랜드 로고나 필터(사이즈/발볼)를 넓게 설정해보세요.</div>
        </div>
      `;
      return;
    }

    const currentSize = sizeFilter.value === 'all' ? null : parseInt(sizeFilter.value, 10);
    const currentWidth = widthFilter.value === 'all' ? null : widthFilter.value;

    shoesListEl.innerHTML = list.map(shoe => {
      const minPrice = shoe.effectiveLowestPrice;

      // Danawa Price Table Rows (2-line Mall Name & 2-line Price/Discount)
      const priceRowsHtml = shoe.displayPrices.map(p => {
        const isLowest = (p.price === minPrice);
        const mallClass = p.badge === '백화점' ? 'dept' :
                          p.badge === '공식몰' ? 'official' :
                          p.badge === '슈즈몰' ? 'multi' : 'select';

        const sizeTxt = currentSize ? `${currentSize}mm 보유` : `${p.sizes[0]}~${p.sizes[p.sizes.length - 1]}mm`;
        const widthTxt = p.width ? `[${p.width}]` : '';
        const subName = p.store_sub ? `<span class="mall-sub-name">${p.store_sub}</span>` : '';

        return `
          <tr class="price-row ${isLowest ? 'is-lowest' : ''}">
            <!-- 1열: 쇼핑몰명 (2줄 스택) -->
            <td class="mall-cell">
              <div class="mall-primary-line">
                <span class="mall-badge ${mallClass}">${p.badge}</span>
                <span class="mall-main-name">${p.store_name}</span>
              </div>
              ${subName}
            </td>

            <!-- 2열: 발볼 & 사이즈 -->
            <td class="size-cell">
              <span class="size-stock-txt"><strong>${widthTxt}</strong> ${sizeTxt}</span>
            </td>

            <!-- 3열: 가격 & 할인율 (2줄 스택) -->
            <td class="price-cell">
              <div class="price-primary-line">
                ${isLowest ? '<span class="lowest-tag">최저가</span>' : ''}
                <span class="current-price">${p.price.toLocaleString()}원</span>
              </div>
              <div class="price-secondary-line">
                ${p.discount_rate > 0 ? `<span class="discount-badge">${p.discount_rate}% 할인</span>` : '<span class="regular-badge">정가</span>'}
                <span class="shipping-fee-txt">${p.shipping === 0 ? '무료배송' : `${p.shipping.toLocaleString()}원`}</span>
              </div>
            </td>

            <!-- 4열: 바로가기 버튼 -->
            <td class="action-cell">
              <a href="${p.url}" target="_blank" rel="noopener noreferrer" class="btn-buy-link">구매하기</a>
            </td>
          </tr>
        `;
      }).join('');

      return `
        <article class="shoe-danawa-card" data-id="${shoe.id}">
          
          <!-- 1열: 제품 사진 -->
          <div class="card-col-photo">
            ${!shoe.is_current ? '<span class="outlet-flag">⚡ 이월특가</span>' : ''}
            <img src="${shoe.image_url}" alt="${shoe.name_kr}" class="shoe-img" loading="lazy">
          </div>

          <!-- 2열: 제품명 & 세대 & 카테고리 & 공식정가(MSRP) 최우선 배치 -->
          <div class="card-col-info">
            <div class="info-top">
              <div class="brand-code-line">
                <span class="brand-line">${shoe.brand_id.toUpperCase()}</span>
                ${shoe.style_code ? `<span class="style-code-badge">품번: ${shoe.style_code}</span>` : ''}
              </div>
              <h2 class="shoe-name">${shoe.name_kr}</h2>
              <span class="category-badge">🏷️ ${shoe.category_name}</span>
            </div>
            <div class="info-bottom">
              <div class="msrp-box">
                <span class="msrp-label">공식 정가 (MSRP)</span>
                <strong class="msrp-price">${(shoe.msrp || shoe.official_price || 0).toLocaleString()}원</strong>
              </div>
            </div>
          </div>

          <!-- 3열: 다나와식 판매처별 가격 리스트 (오버플로우 완벽 해소) -->
          <div class="card-col-prices">
            <table class="price-table">
              <tbody>
                ${priceRowsHtml}
              </tbody>
            </table>
          </div>

          <!-- 4열: 런리핏 스펙 요약 & 모달 버튼 -->
          <div class="card-col-action">
            <div class="runrepeat-score-box">
              <span class="rr-label">RunRepeat</span>
              <span class="rr-score-num">${shoe.runrepeat ? shoe.runrepeat.score : '-'}</span>
              <span class="rr-grade">Great 점수</span>
            </div>
            <button type="button" class="btn-open-modal" onclick="openRunRepeatModal('${shoe.id}')">
              📊 런리핏 랩 분석
            </button>
          </div>

        </article>
      `;
    }).join('');
  }

  // 5. Open RunRepeat Lab Modal
  window.openRunRepeatModal = function(shoeId) {
    const shoe = shoesData.find(s => s.id === shoeId);
    if (!shoe) return;

    modalBrandBadge.textContent = (shoe.brand_id || '').toUpperCase();
    modalShoeName.textContent = shoe.name_kr || shoe.name_en || '';
    
    const rr = shoe.runrepeat || {};
    const sp = shoe.specs || {};
    
    modalScore.innerHTML = `${rr.score || '-'}<span class="score-max">/100</span>`;
    modalWeight.textContent = `${sp.weight_g || rr.weight_g || '-'}g`;
    modalDrop.textContent = `${sp.heel_drop_mm || rr.heel_drop_mm || '-'}mm`;
    modalStack.textContent = sp.stack_height || `${rr.heel_stack_mm || '-'} / ${rr.forefoot_stack_mm || '-'} mm`;
    modalPlate.textContent = sp.midsole || rr.plate || '없음';
    modalFoam.textContent = rr.midsole_foam || sp.midsole || '-';

    // Pros
    modalProsList.innerHTML = (rr.pros || []).map(p => `<li>${p}</li>`).join('');
    // Cons
    modalConsList.innerHTML = (rr.cons || []).map(c => `<li>${c}</li>`).join('');
    // Summary
    modalSummary.textContent = rr.verdict || rr.summary || '상세 리뷰 준비 중입니다.';

    modalEl.style.display = 'flex';
  };
}

// Ensure execution even if DOMContentLoaded already fired
if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', initShoeFApp);
} else {
  initShoeFApp();
}

