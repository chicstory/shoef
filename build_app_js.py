"""
Build modern, robust, fully self-contained app.js for ShoeF Wiki.
Integrates:
- 51 shoes master dataset embedded
- 5 Categories (Budget <= $100, Daily, Stability, Super Trainer, Racing)
- 1:1 and 1:N Comparison System with sticky floating bar
- Anonymous Runner Shoutbox (ownerMemoSection from engines with math captcha & cooldown)
- RunRepeat Lab Spec Wiki Cards (isolated block rows for 360px zero-overflow)
- Direct RunRepeat review link buttons
"""

import json
import os

def build():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    data_dir = os.path.join(base_dir, "data")
    
    with open(os.path.join(data_dir, "shoes_master.json"), "r", encoding="utf-8") as f:
        shoes = json.load(f)
        
    with open(os.path.join(data_dir, "brands_stores_config.json"), "r", encoding="utf-8") as f:
        config = json.load(f)
        
    shoes_json = json.dumps(shoes, ensure_ascii=False, indent=2)
    config_json = json.dumps(config, ensure_ascii=False, indent=2)

    js_template = f'''/**
 * ShoeF - Global Running Shoe Lab Wiki & Comparison Platform
 * RunRepeat Verified Lab Specs & 1:1 Comparison & Runner Shoutbox
 */

// 1. Embedded Master Data
const EMBEDDED_CONFIG = {config_json};
const EMBEDDED_SHOES = {shoes_json};

(function initShoeF() {{
  let brandsConfig = EMBEDDED_CONFIG;
  let shoesData = EMBEDDED_SHOES;

  if (typeof window !== 'undefined') {{
    if (window.SHOEF_CONFIG) brandsConfig = window.SHOEF_CONFIG;
    if (window.SHOEF_MASTER || window.SHOEF_DATA) shoesData = window.SHOEF_MASTER || window.SHOEF_DATA;
  }}

  // Comparison Tray State (Set of shoe IDs, max 4)
  const compareTray = new Set();

  // Active Selected Brands (All active initially)
  const selectedBrands = new Set(brandsConfig.brands.map(b => b.id));

  // Current Sort Mode
  let currentSort = 'score-desc';

  // DOM Elements
  const brandGridEl = document.getElementById('brandCheckboxGrid');
  const btnSelectAllBrands = document.getElementById('btnSelectAllBrands');
  const btnDeselectAllBrands = document.getElementById('btnDeselectAllBrands');
  const categoryFilter = document.getElementById('categoryFilter');
  const widthFilter = document.getElementById('widthFilter');
  const searchKeyword = document.getElementById('searchKeyword');
  const totalCountEl = document.getElementById('totalCount');
  const shoesListEl = document.getElementById('shoesList');
  const sortBtns = document.querySelectorAll('.sort-btn');

  // Compare Tray & Modal DOM
  const compareBar = document.getElementById('compareFloatingBar');
  const compareCountTxt = document.getElementById('compareCountTxt');
  const compareChipsContainer = document.getElementById('compareChips');
  const btnOpenCompare = document.getElementById('btnOpenCompare');
  const btnClearCompare = document.getElementById('btnClearCompare');
  const compareModal = document.getElementById('compareModal');
  const btnCloseCompareModal = document.getElementById('btnCloseCompareModal');
  const compareModalTableBody = document.getElementById('compareModalTableBody');

  // Memo Modal DOM
  const memoModal = document.getElementById('memoModal');
  const btnCloseMemoModal = document.getElementById('btnCloseMemoModal');
  const memoShoeTitle = document.getElementById('memoShoeTitle');
  const memoShoeSubtitle = document.getElementById('memoShoeSubtitle');
  const commentsList = document.getElementById('commentsList');
  const memoForm = document.getElementById('memoForm');
  const commentAuthor = document.getElementById('commentAuthor');
  const commentText = document.getElementById('commentText');
  const mathQuizLabel = document.getElementById('mathQuizLabel');
  const mathAnswer = document.getElementById('mathAnswer');
  const hpUrlCheck = document.getElementById('hp_url_check');

  let currentActiveMemoShoeId = null;
  let numA = 3, numB = 4, correctSum = 7;

  // Brand SVG Logos Map
  const BRAND_LOGOS = {{
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
  }};

  // 2. Initialize Brand Buttons
  function initBrandButtons() {{
    brandGridEl.innerHTML = '';
    brandsConfig.brands.forEach(brand => {{
      const isChecked = selectedBrands.has(brand.id);
      const count = shoesData.filter(s => s.brand_id === brand.id).length;
      const logoSvg = BRAND_LOGOS[brand.id] || `<span style="font-weight:800; font-size:11px;">${{brand.name.substring(0, 3)}}</span>`;

      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = `brand-logo-btn ${{isChecked ? 'active' : 'inactive'}}`;
      btn.dataset.brandId = brand.id;
      btn.innerHTML = `
        <div class="brand-logo-icon">${{logoSvg}}</div>
        <span class="brand-logo-name">${{brand.name_kr}}</span>
        <span class="brand-logo-count">${{count > 0 ? count : '-'}}</span>
      `;

      btn.addEventListener('click', () => {{
        if (selectedBrands.has(brand.id)) {{
          selectedBrands.delete(brand.id);
          btn.classList.remove('active');
          btn.classList.add('inactive');
        }} else {{
          selectedBrands.add(brand.id);
          btn.classList.add('active');
          btn.classList.remove('inactive');
        }}
        renderShoes();
      }});

      brandGridEl.appendChild(btn);
    }});
  }}

  // Dynamic Category Option Counts Sync (Never hardcode counts)
  function updateCategoryOptionCounts() {{
    if (!categoryFilter) return;
    const counts = {{
      all: shoesData.length,
      budget: shoesData.filter(s => s.category === 'budget').length,
      daily: shoesData.filter(s => s.category === 'daily').length,
      stability: shoesData.filter(s => s.category === 'stability').length,
      super_trainer: shoesData.filter(s => s.category === 'super_trainer').length,
      racing: shoesData.filter(s => s.category === 'racing').length,
    }};

    const labels = {{
      all: `전체 카테고리 (${{counts.all}}종)`,
      budget: `🌱 가성비 입문화 (${{counts.budget}}종)`,
      daily: `☁️ 데일리 / 쿠션화 (${{counts.daily}}종)`,
      stability: `🛡️ 안정화 (${{counts.stability}}종)`,
      super_trainer: `⚡ 슈퍼 트레이너 (${{counts.super_trainer}}종)`,
      racing: `🏆 레이싱화 (${{counts.racing}}종)`,
    }};

    Array.from(categoryFilter.options).forEach(opt => {{
      if (labels[opt.value]) {{
        opt.textContent = labels[opt.value];
      }}
    }});
  }}

  // 3. Filter & Sort Logic
  function getFilteredShoes() {{
    const catVal = categoryFilter.value;
    const widthVal = widthFilter.value;
    const query = searchKeyword.value.trim().toLowerCase();

    return shoesData.filter(shoe => {{
      // 1) Brand filter
      if (!selectedBrands.has(shoe.brand_id)) return false;

      // 2) Category filter
      if (catVal !== 'all' && shoe.category !== catVal) return false;

      // 3) Width filter
      if (widthVal !== 'all') {{
        if (!shoe.widths || !shoe.widths.includes(widthVal)) return false;
      }}

      // 4) Keyword search
      if (query) {{
        const text = `${{shoe.name_kr}} ${{shoe.name_en}} ${{shoe.series}} ${{shoe.specs.midsole}} ${{shoe.specs.plate}} ${{shoe.category_name}}`.toLowerCase();
        if (!text.includes(query)) return false;
      }}

      return true;
    }}).sort((a, b) => {{
      if (currentSort === 'score-desc') {{
        return b.runrepeat.score - a.runrepeat.score;
      }} else if (currentSort === 'price-asc') {{
        return a.msrp_krw - b.msrp_krw;
      }} else if (currentSort === 'price-desc') {{
        return b.msrp_krw - a.msrp_krw;
      }} else if (currentSort === 'weight-asc') {{
        return a.specs.weight_g - b.specs.weight_g;
      }}
      return 0;
    }});
  }}

  // 4. Shoutbox (Memo) LocalStorage Helpers
  function getShoeMemos(shoeId) {{
    try {{
      const data = localStorage.getItem(`shoef_memo_${{shoeId}}`);
      return data ? JSON.parse(data) : [];
    }} catch(e) {{
      return [];
    }}
  }}

  function refreshMathQuiz() {{
    numA = Math.floor(Math.random() * 8) + 2;
    numB = Math.floor(Math.random() * 8) + 1;
    correctSum = numA + numB;
    if (mathQuizLabel) {{
      mathQuizLabel.textContent = `${{numA}} + ${{numB}} =`;
    }}
  }}

  function escapeHtml(str) {{
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#039;');
  }}

  function renderCommentsList(shoeId) {{
    const memos = getShoeMemos(shoeId);
    if (memos.length === 0) {{
      commentsList.innerHTML = `
        <div style="text-align:center; padding:2rem 1rem; color:var(--text-dim); font-size:0.9rem;">
          👟 아직 등록된 러너 실전 팁이 없습니다.<br>
          <span style="font-size:0.8rem; color:var(--text-muted);">실제 착화감, 발볼 팁, 마일리지 후기를 첫 번째로 공유해보세요!</span>
        </div>
      `;
      return;
    }}

    commentsList.innerHTML = memos.slice().reverse().map(m => `
      <div class="memo-comment-row">
        <div class="memo-comment-left">
          <div class="memo-author-line">
            <strong class="memo-comment-author">${{escapeHtml(m.author)}}</strong>
            <span class="memo-comment-time">${{escapeHtml(m.time)}}</span>
          </div>
          <p class="memo-comment-text">${{escapeHtml(m.text)}}</p>
        </div>
      </div>
    `).join('');
  }}

  function openMemoModal(shoeId) {{
    const shoe = shoesData.find(s => s.id === shoeId);
    if (!shoe) return;

    currentActiveMemoShoeId = shoeId;
    memoShoeTitle.textContent = shoe.name_kr;
    memoShoeSubtitle.textContent = `${{shoe.name_en}} · 정가 ${{shoe.msrp_krw.toLocaleString()}}원`;

    commentText.value = '';
    mathAnswer.value = '';
    refreshMathQuiz();
    renderCommentsList(shoeId);

    memoModal.style.display = 'flex';
  }}

  // 5. Compare Tray Management
  function updateCompareTrayUI() {{
    const count = compareTray.size;
    compareCountTxt.textContent = `${{count}}/4`;

    if (count > 0) {{
      compareBar.classList.add('show');
    }} else {{
      compareBar.classList.remove('show');
    }}

    compareChipsContainer.innerHTML = Array.from(compareTray).map(id => {{
      const shoe = shoesData.find(s => s.id === id);
      if (!shoe) return '';
      return `
        <span class="compare-chip">
          <span class="chip-name">${{shoe.name_kr}}</span>
          <button type="button" class="btn-remove-chip" data-id="${{shoe.id}}" aria-label="삭제">&times;</button>
        </span>
      `;
    }}).join('');

    // Attach chip delete events
    compareChipsContainer.querySelectorAll('.btn-remove-chip').forEach(btn => {{
      btn.addEventListener('click', (e) => {{
        e.stopPropagation();
        const id = btn.dataset.id;
        compareTray.delete(id);
        updateCompareTrayUI();
        renderShoes();
      }});
    }});
  }}

  function toggleCompare(shoeId) {{
    if (compareTray.has(shoeId)) {{
      compareTray.delete(shoeId);
    }} else {{
      if (compareTray.size >= 4) {{
        alert('신발 비교는 한 번에 최대 4개까지만 가능합니다.');
        return;
      }}
      compareTray.add(shoeId);
    }}
    updateCompareTrayUI();
    renderShoes();
  }}

  // 6. Open Compare Modal & Render Matrix
  function openCompareMatrix() {{
    if (compareTray.size < 1) {{
      alert('비교할 신발을 최소 1개 이상 선택해주세요.');
      return;
    }}

    const selectedShoes = Array.from(compareTray).map(id => shoesData.find(s => s.id === id)).filter(Boolean);

    // Build side-by-side table rows
    const specsItems = [
      {{ label: '신발 정보', render: s => `<div class="comp-shoe-head"><strong class="comp-shoe-name">${{s.name_kr}}</strong><span class="comp-shoe-en">${{s.name_en}}</span></div>` }},
      {{ label: '런리핏 평점', render: s => `<div class="comp-score"><span class="score-num">${{s.runrepeat.score}}</span><span class="score-den">/100점</span></div>` }},
      {{ label: '카테고리', render: s => `<span class="category-badge cat-${{s.category}}">${{s.category_name}}</span>` }},
      {{ label: '출시 정가 (MSRP)', render: s => `<strong>${{s.msrp_krw.toLocaleString()}}원</strong><br><span style="color:var(--text-dim); font-size:0.75rem;">$${{s.msrp_usd}}</span>` }},
      {{ label: '실측 무게 (270mm)', render: s => `<strong>${{s.specs.weight_g}}g</strong>` }},
      {{ label: '힐드롭 (Heel Drop)', render: s => `<strong>${{s.specs.heel_drop_mm}}mm</strong>` }},
      {{ label: '스택 높이 (힐/앞발)', render: s => `${{s.specs.stack_height}}` }},
      {{ label: '미드솔 폼 소재', render: s => `<strong>${{s.specs.midsole}}</strong>` }},
      {{ label: '플레이트 유무', render: s => `${{s.specs.plate}}` }},
      {{ label: '발볼 옵션', render: s => `${{s.widths.join(', ')}}` }},
      {{ label: '서포트 타입', render: s => `${{s.specs.support_type}}` }},
      {{ label: '핵심 장점 (Pros)', render: s => `<ul class="comp-list pros">${{s.runrepeat.pros.map(p => `<li>${{p}}</li>`).join('')}}</ul>` }},
      {{ label: '주의/단점 (Cons)', render: s => `<ul class="comp-list cons">${{s.runrepeat.cons.map(c => `<li>${{c}}</li>`).join('')}}</ul>` }},
      {{ label: '런리핏 총평', render: s => `<p class="comp-verdict">"${{s.runrepeat.verdict}}"</p>` }},
      {{ label: '공식 랩 분석', render: s => `<a href="${{s.runrepeat.url}}" target="_blank" rel="noopener noreferrer" class="btn-rr-link">🔬 런리핏 원문 리포트</a>` }}
    ];

    let html = '';
    specsItems.forEach(item => {{
      html += `
        <tr>
          <th class="spec-label-col">${{item.label}}</th>
          ${{selectedShoes.map(s => `<td class="spec-val-col">${{item.render(s)}}</td>`).join('')}}
        </tr>
      `;
    }});

    compareModalTableBody.innerHTML = html;
    compareModal.style.display = 'flex';
  }}

  // 7. Render Shoes List Cards (Wiki Style with Pure Lab Specs & Isolated Blocks for 360px)
  function renderShoes() {{
    const list = getFilteredShoes();
    totalCountEl.textContent = list.length;

    if (list.length === 0) {{
      shoesListEl.innerHTML = `
        <div style="text-align: center; padding: 60px 20px; color: var(--text-dim);">
          <div style="font-size: 36px; margin-bottom: 12px;">👟🔍</div>
          <div style="font-size: 16px; font-weight: 600; color: var(--text-muted);">조건에 맞는 러닝화를 찾을 수 없습니다.</div>
          <div style="font-size: 13px; margin-top: 6px;">브랜드나 필터 설정을 넓게 선택해보세요.</div>
        </div>
      `;
      return;
    }}

    shoesListEl.innerHTML = list.map(shoe => {{
      const isCompared = compareTray.has(shoe.id);
      const memos = getShoeMemos(shoe.id);
      const memoCount = memos.length;

      return `
        <article class="shoe-wiki-card" data-id="${{shoe.id}}">
          
          <!-- 카드 상단: 브랜드 & 모델명 & 비교 체크 토글 -->
          <div class="card-top-row">
            <div class="card-brand-model">
              <span class="card-brand-badge">${{shoe.brand_id.toUpperCase()}}</span>
              <h2 class="card-title-kr">${{shoe.name_kr}}</h2>
              <span class="card-title-en">${{shoe.name_en}}</span>
            </div>
            <button type="button" class="btn-compare-toggle ${{isCompared ? 'active' : ''}}" data-id="${{shoe.id}}">
              ${{isCompared ? '✓ 비교함 담김' : '+ 비교함 담기'}}
            </button>
          </div>

          <!-- 독립 블록 1: 런리핏 평점 & 카테고리 태그 (360px 오버플로우 방지) -->
          <div class="card-score-row">
            <div class="rr-score-badge">
              <span class="rr-score-icon">🟢</span>
              <span class="rr-score-val">${{shoe.runrepeat.score}}</span>
              <span class="rr-score-max">/100</span>
              <span class="rr-score-label">RunRepeat Score</span>
            </div>
            <span class="category-badge cat-${{shoe.category}}">${{shoe.category_name}}</span>
          </div>

          <!-- 독립 블록 2: 공식 정가 및 발볼 정보 -->
          <div class="card-price-row">
            <div class="price-box">
              <span class="price-label">공식 출시가 (MSRP)</span>
              <span class="price-val">${{shoe.msrp_krw.toLocaleString()}}원 <span class="usd-val">($${{shoe.msrp_usd}})</span></span>
            </div>
            <div class="widths-box">
              <span class="widths-label">발볼 옵션:</span>
              <span class="widths-val">${{shoe.widths.join(', ')}}</span>
            </div>
          </div>

          <!-- 독립 블록 3: 4대 핵심 랩 실측 수치 그리드 -->
          <div class="card-specs-grid">
            <div class="spec-cell">
              <span class="spec-cell-label">실측 무게 (270mm)</span>
              <strong class="spec-cell-val">${{shoe.specs.weight_g}}g</strong>
            </div>
            <div class="spec-cell">
              <span class="spec-cell-label">힐드롭</span>
              <strong class="spec-cell-val">${{shoe.specs.heel_drop_mm}}mm</strong>
            </div>
            <div class="spec-cell">
              <span class="spec-cell-label">스택 높이</span>
              <strong class="spec-cell-val">${{shoe.specs.stack_height}}</strong>
            </div>
            <div class="spec-cell">
              <span class="spec-cell-label">미드솔 폼 / 플레이트</span>
              <strong class="spec-cell-val">${{shoe.specs.midsole}} · ${{shoe.specs.plate}}</strong>
            </div>
          </div>

          <!-- 독립 블록 4: 런리핏 랩 핵심 장단점 요약 -->
          <div class="card-verdict-box">
            <p class="verdict-txt">"${{shoe.runrepeat.verdict}}"</p>
            <div class="pros-cons-list">
              <div class="pros-group">
                <span class="pros-title">👍 핵심 장점</span>
                <ul>${{shoe.runrepeat.pros.map(p => `<li>${{p}}</li>`).join('')}}</ul>
              </div>
              <div class="cons-group">
                <span class="cons-title">⚠️ 체크 포인트</span>
                <ul>${{shoe.runrepeat.cons.map(c => `<li>${{c}}</li>`).join('')}}</ul>
              </div>
            </div>
          </div>

          <!-- 독립 블록 5: 액션 버튼 바 (런리핏 원문 리포트 & 러너 메모장) -->
          <div class="card-action-row">
            <a href="${{shoe.runrepeat.url}}" target="_blank" rel="noopener noreferrer" class="btn-rr-direct">
              🔬 런리핏 랩 실측 리포트 보기
            </a>
            <button type="button" class="btn-memo-open" data-id="${{shoe.id}}">
              💬 러너 실전 팁 (${{memoCount}})
            </button>
          </div>

        </article>
      `;
    }}).join('');

    // Attach Compare Buttons
    shoesListEl.querySelectorAll('.btn-compare-toggle').forEach(btn => {{
      btn.addEventListener('click', () => {{
        toggleCompare(btn.dataset.id);
      }});
    }});

    // Attach Memo Buttons
    shoesListEl.querySelectorAll('.btn-memo-open').forEach(btn => {{
      btn.addEventListener('click', () => {{
        openMemoModal(btn.dataset.id);
      }});
    }});
  }}

  // 8. Attach Global Events
  function attachEvents() {{
    btnSelectAllBrands.addEventListener('click', () => {{
      brandsConfig.brands.forEach(b => selectedBrands.add(b.id));
      document.querySelectorAll('.brand-logo-btn').forEach(item => {{
        item.classList.add('active');
        item.classList.remove('inactive');
      }});
      renderShoes();
    }});

    btnDeselectAllBrands.addEventListener('click', () => {{
      selectedBrands.clear();
      document.querySelectorAll('.brand-logo-btn').forEach(item => {{
        item.classList.remove('active');
        item.classList.add('inactive');
      }});
      renderShoes();
    }});

    categoryFilter.addEventListener('change', renderShoes);
    widthFilter.addEventListener('change', renderShoes);
    searchKeyword.addEventListener('input', renderShoes);

    sortBtns.forEach(btn => {{
      btn.addEventListener('click', () => {{
        sortBtns.forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentSort = btn.dataset.sort;
        renderShoes();
      }});
    }});

    // Floating Compare Bar Events
    btnOpenCompare.addEventListener('click', openCompareMatrix);
    btnClearCompare.addEventListener('click', () => {{
      compareTray.clear();
      updateCompareTrayUI();
      renderShoes();
    }});

    // Compare Modal Close
    btnCloseCompareModal.addEventListener('click', () => {{
      compareModal.style.display = 'none';
    }});
    compareModal.addEventListener('click', (e) => {{
      if (e.target === compareModal) compareModal.style.display = 'none';
    }});

    // Memo Modal Close
    btnCloseMemoModal.addEventListener('click', () => {{
      memoModal.style.display = 'none';
    }});
    memoModal.addEventListener('click', (e) => {{
      if (e.target === memoModal) memoModal.style.display = 'none';
    }});

    // Memo Submit Logic (with math captcha & 10s cooldown)
    memoForm.addEventListener('submit', (e) => {{
      e.preventDefault();

      if (!currentActiveMemoShoeId) return;

      // 1. Honeypot check
      if (hpUrlCheck.value !== '') return;

      // 2. Math Captcha check
      const userAns = parseInt(mathAnswer.value, 10);
      if (userAns !== correctSum) {{
        alert('스팸 방지 산수 문제의 정답이 올바르지 않습니다.');
        return;
      }}

      // 3. Cooldown check (10 seconds)
      const lastPost = localStorage.getItem('last_shoef_memo_time');
      const now = Date.now();
      if (lastPost && now - parseInt(lastPost, 10) < 10000) {{
        alert('도배 방지를 위해 10초 후에 다시 작성하실 수 있습니다.');
        return;
      }}

      const author = commentAuthor.value.trim() || '익명 러너';
      const text = commentText.value.trim();
      if (!text) {{
        alert('러너 실전 팁 내용을 입력해주세요.');
        return;
      }}

      const d = new Date();
      const timeStr = `${{d.getMonth()+1}}/${{d.getDate()}} ${{String(d.getHours()).padStart(2,'0')}}:${{String(d.getMinutes()).padStart(2,'0')}}`;

      const memos = getShoeMemos(currentActiveMemoShoeId);
      memos.push({{ author, text, time: timeStr }});
      localStorage.setItem(`shoef_memo_${{currentActiveMemoShoeId}}`, JSON.stringify(memos));
      localStorage.setItem('last_shoef_memo_time', now.toString());

      commentText.value = '';
      mathAnswer.value = '';
      refreshMathQuiz();
      renderCommentsList(currentActiveMemoShoeId);
      renderShoes(); // Update memo count badge on card
    }});

    // ESC key close
    document.addEventListener('keydown', (e) => {{
      if (e.key === 'Escape') {{
        compareModal.style.display = 'none';
        memoModal.style.display = 'none';
      }}
    }});
  }}

  // Start Application
  initBrandButtons();
  updateCategoryOptionCounts();
  attachEvents();
  renderShoes();
}})();
'''
    
    app_js_path = os.path.join(base_dir, "app.js")
    with open(app_js_path, "w", encoding="utf-8") as f:
        f.write(js_template)
    print(f"Successfully generated clean app.js at {app_js_path} ({len(js_template)} bytes)")

if __name__ == "__main__":
    build()
