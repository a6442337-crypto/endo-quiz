# 내분비학 기출 퀴즈

2020–2025 내분비학 복원 기출(2026 담당 교수님 기준으로 정리) 200문항과 예상 변형 45문항을 푸는 정적 웹페이지입니다. 정답과 해설은 26 학습부 기준으로 다시 판단했습니다.

## 구조
- `index.html` — 배포용 페이지(빌드 결과, GitHub Pages가 바로 서비스)
- `data/past.json` — 기출 문항 (장·소단원, 지문 HTML, 선지, 정답 인덱스, 해설, 근거)
- `data/variants.json` — 예상 변형 문항
- `figs/` — 문항 그림
- `src/template.html` — 퀴즈 UI 템플릿 (`__DATA__` 자리에 데이터가 들어감)
- `tools/build.py` — `python3 tools/build.py` 로 index.html 재생성

## 문항 데이터 형식
```json
{"id":"23-01","keys":["23-01"],"ch":11,"g":"소단원","stem":"<div>…</div>","o":["…"],"a":3,"A":"④","E":"해설","B":"근거","N":"비고","img":["figs/23-01.jpg"],"v":false}
```
`a`는 0부터 시작하는 정답 인덱스, `v`가 true이면 변형 문항입니다.
