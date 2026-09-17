@echo off
chcp 65001 > nul
setlocal enabledelayedexpansion

echo ========================================================
echo   [ShoeF] 러닝화 위키 & 다나와 최저가 배포기
echo   서비스 주소: https://shoef.runanalyz.com
echo   원격 저장소: https://github.com/chicstory/shoef.git
echo ========================================================

cd /d "%~dp0"

echo [1/4] 데이터 무결성 검증 수행 중...
python test_data_integrity.py
if errorlevel 1 (
    echo [ERROR] 데이터 무결성 검증에 실패했습니다. 배포를 중단합니다.
    pause
    exit /b 1
)

echo.
echo [2/4] 정적 데이터 동기화 및 렌더링 검증...
python test_browser_render.py > nul 2>&1

echo.
echo [3/4] 변경 사항 명시적 스테이징 (GEMINI 보안 수칙 준수)...
git add index.html style.css app.js data.js CNAME README.md .gitignore run_shoef_daily.bat test_data_integrity.py test_browser_render.py build_verified_data.py data/shoes_master.json data/brands_stores_config.json

for /f "tokens=1-3 delims=- " %%a in ('date /t') do (
    set TODAY=%%a-%%b-%%c
)

echo.
echo [4/4] GitHub shoef(main) 브랜치로 배포 중...
git commit -m "feat(shoef): daily price update & wiki sync %TODAY%"
git push origin main

echo.
echo ========================================================
echo   [COMPLETE] ShoeF 배포가 완료되었습니다!
echo   접속 주소: https://shoef.runanalyz.com
echo ========================================================
echo.
timeout /t 5
