# 파이썬을 이용한 뮤직 데이터 수집하기

파이썬을 이용하여 뮤직 순위정보를 수집합니다.

## 📋 데이터 사용하기

데이터는 다음과 같이 사용할 수 있습니다.

```js
https://websseu.github.io/pythonMusic/korea/apple/appleTop100_2024-11-06.json
https://websseu.github.io/pythonMusic/korea/bugs/bugsTop100_2024-11-06.json
https://websseu.github.io/pythonMusic/korea/flo/floTop100_2024-11-06.json
https://websseu.github.io/pythonMusic/korea/genie/genieTop100_2024-11-06.json
https://websseu.github.io/pythonMusic/korea/melon/melonTop100_2024-11-06.json
https://websseu.github.io/pythonMusic/korea/vibe/vibeTop100_2024-11-06.json
```

## 🇰🇷 한국 노래 챠트 수집하기

애플(apple) 뮤직 코리아 순위 100 : [https://music.apple.com/kr/new](https://music.apple.com/kr/playlist/%EC%98%A4%EB%8A%98%EC%9D%98-top-100-%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD/pl.d3d10c32fbc540b38e266367dc8cb00c)  
멜론(melon) 뮤직 순위 100 : [https://www.melon.com/chart/index.htm](https://www.melon.com/chart/index.htm)  
지니(genie) 뮤직 순위 100 : [https://www.genie.co.kr/chart/top200](https://www.genie.co.kr/chart/top200?ditc=D&ymd=20241105&hh=10&rtm=Y&pg=1)  
벅스(bugs) 뮤직 순위 100 : [https://music.bugs.co.kr/chart](https://music.bugs.co.kr/chart)  
플로(flo) 뮤직 순위 100 : [https://www.music-flo.com/browse](https://www.music-flo.com/browse)  
바이브(vibe) 뮤직 순위 100 : [https://vibe.naver.com/chart/total](https://vibe.naver.com/chart/total)

```js
https://websseu.github.io/pythonMusic/korea/[이름]/[이름]Top100_[날짜].json
```

## 💸 빌보드 챠트 수집하기

```js
https://websseu.github.io/pythonMusic/billboard/grobal/grobalTop100_[날짜].json
https://websseu.github.io/pythonMusic/billboard/hot/hotTop100_[날짜].json

```

빌보드 핫 뮤직 순위 100 : [https://www.billboard.com/charts/hot-100/](https://www.billboard.com/charts/hot-100/)  
빌보드 글로벌 뮤직 순위 100 : [https://www.billboard.com/charts/billboard-global-200/](https://www.billboard.com/charts/billboard-global-200/)

## 📹 유튜브 뮤직 전세계 챠트 수집하기

```js
https://websseu.github.io/pythonMusic/youtube/[나라이름]/[나라이름]Top100_[날짜].json
```

유튜브 뮤직 🌏 글로벌(global) 순위 100 : [https://charts.youtube.com/charts/TopSongs/global/weekly](https://charts.youtube.com/charts/TopSongs/global/weekly)  
유튜브 뮤직 🇦🇷 아르헨티나(ar) 순위 100 : [https://charts.youtube.com/charts/TopSongs/ar/weekly](https://charts.youtube.com/charts/TopSongs/ar/weekly)  
유튜브 뮤직 🇦🇺 호주(au) 순위 100 : [https://charts.youtube.com/charts/TopSongs/au/weekly](https://charts.youtube.com/charts/TopSongs/au/weekly)  
유튜브 뮤직 🇦🇹 오스트리아(at) 순위 100 : [https://charts.youtube.com/charts/TopSongs/at/weekly](https://charts.youtube.com/charts/TopSongs/at/weekly)  
유튜브 뮤직 🇧🇴 볼리비아(bo) 순위 100 : [https://charts.youtube.com/charts/TopSongs/bo/weekly](https://charts.youtube.com/charts/TopSongs/bo/weekly)  
유튜브 뮤직 🇧🇷 브라질(br) 순위 100 : [https://charts.youtube.com/charts/TopSongs/br/weekly](https://charts.youtube.com/charts/TopSongs/br/weekly)  
유튜브 뮤직 🇨🇦 캐나다(ca) 순위 100 : [https://charts.youtube.com/charts/TopSongs/ca/weekly](https://charts.youtube.com/charts/TopSongs/ca/weekly)  
유튜브 뮤직 🇨🇱 칠레(cl) 순위 100 : [https://charts.youtube.com/charts/TopSongs/cl/weekly](https://charts.youtube.com/charts/TopSongs/cl/weekly)  
유튜브 뮤직 🇨🇴 콜롬비아(co) 순위 100 : [https://charts.youtube.com/charts/TopSongs/co/weekly](https://charts.youtube.com/charts/TopSongs/co/weekly)  
유튜브 뮤직 🇨🇷 코스타리카(cr) 순위 100 : [https://charts.youtube.com/charts/TopSongs/cr/weekly](https://charts.youtube.com/charts/TopSongs/cr/weekly)  
유튜브 뮤직 🇨🇿 체코(cr) 순위 100 : [https://charts.youtube.com/charts/TopSongs/cz/weekly](https://charts.youtube.com/charts/TopSongs/cz/weekly)  
유튜브 뮤직 🇩🇰 덴마크(dk) 순위 100 : [https://charts.youtube.com/charts/TopSongs/dk/weekly](https://charts.youtube.com/charts/TopSongs/dk/weekly)  
유튜브 뮤직 🇩🇴 도미니카 공화국(do) 순위 100 : [https://charts.youtube.com/charts/TopSongs/do/weekly](https://charts.youtube.com/charts/TopSongs/do/weekly)  
유튜브 뮤직 🇪🇨 에콰도르(ec) 순위 100 : [https://charts.youtube.com/charts/TopSongs/ec/weekly](https://charts.youtube.com/charts/TopSongs/ec/weekly)  
유튜브 뮤직 🇪🇬 이집트(eg) 순위 100 : [https://charts.youtube.com/charts/TopSongs/eg/weekly](https://charts.youtube.com/charts/TopSongs/eg/weekly)  
유튜브 뮤직 🇸🇻 엘살바도르(sv) 순위 100 : [https://charts.youtube.com/charts/TopSongs/sv/weekly](https://charts.youtube.com/charts/TopSongs/sv/weekly)  
유튜브 뮤직 🇪🇪 에스토니아(ee) 순위 100 : [https://charts.youtube.com/charts/TopSongs/ee/weekly](https://charts.youtube.com/charts/TopSongs/ee/weekly)  
유튜브 뮤직 🇫🇮 핀란드(fi) 순위 100 : [https://charts.youtube.com/charts/TopSongs/fi/weekly](https://charts.youtube.com/charts/TopSongs/fi/weekly)  
유튜브 뮤직 🇫🇷 프랑스(fr) 순위 100 : [https://charts.youtube.com/charts/TopSongs/fr/weekly](https://charts.youtube.com/charts/TopSongs/fr/weekly)  
유튜브 뮤직 🇩🇪 독일(de) 순위 100 : [https://charts.youtube.com/charts/TopSongs/de/weekly](https://charts.youtube.com/charts/TopSongs/de/weekly)  
유튜브 뮤직 🇬🇹 과테말라(gt) 순위 100 : [https://charts.youtube.com/charts/TopSongs/gt/weekly](https://charts.youtube.com/charts/TopSongs/gt/weekly)  
유튜브 뮤직 🇬🇹 온두라스(hn) 순위 100 : [https://charts.youtube.com/charts/TopSongs/hn/weekly](https://charts.youtube.com/charts/TopSongs/hn/weekly)  
유튜브 뮤직 🇭🇺 헝가리(hn) 순위 100 : [https://charts.youtube.com/charts/TopSongs/hu/weekly](https://charts.youtube.com/charts/TopSongs/hu/weekly)  
유튜브 뮤직 🇮🇸 아이슬란드(is) 순위 100 : [https://charts.youtube.com/charts/TopSongs/is/weekly](https://charts.youtube.com/charts/TopSongs/is/weekly)  
유튜브 뮤직 🇮🇳 인도(in) 순위 100 : [https://charts.youtube.com/charts/TopSongs/in/weekly](https://charts.youtube.com/charts/TopSongs/in/weekly)  
유튜브 뮤직 🇮🇩 인도네시아(id) 순위 100 : [https://charts.youtube.com/charts/TopSongs/id/weekly](https://charts.youtube.com/charts/TopSongs/id/weekly)  
유튜브 뮤직 🇮🇱 이스라엘(il) 순위 100 : [https://charts.youtube.com/charts/TopSongs/il/weekly](https://charts.youtube.com/charts/TopSongs/il/weekly)  
유튜브 뮤직 🇮🇹 이탈리아(it) 순위 100 : [https://charts.youtube.com/charts/TopSongs/it/weekly](https://charts.youtube.com/charts/TopSongs/it/weekly)  
유튜브 뮤직 🇯🇵 일본(jp) 순위 100 : [https://charts.youtube.com/charts/TopSongs/jp/weekly](https://charts.youtube.com/charts/TopSongs/jp/weekly)  
유튜브 뮤직 🇰🇪 케냐(ke) 순위 100 : [https://charts.youtube.com/charts/TopSongs/ke/weekly](https://charts.youtube.com/charts/TopSongs/ke/weekly)  
유튜브 뮤직 🇱🇺 룩셈부르크(lu) 순위 100 : [https://charts.youtube.com/charts/TopSongs/lu/weekly](https://charts.youtube.com/charts/TopSongs/lu/weekly)  
유튜브 뮤직 🇲🇽 멕시코(lu) 순위 100 : [https://charts.youtube.com/charts/TopSongs/mx/weekly](https://charts.youtube.com/charts/TopSongs/mx/weekly)  
유튜브 뮤직 🇳🇱 네덜란드(lu) 순위 100 : [https://charts.youtube.com/charts/TopSongs/nl/weekly](https://charts.youtube.com/charts/TopSongs/nl/weekly)  
유튜브 뮤직 🇳🇿 뉴질랜드(nz) 순위 100 : [https://charts.youtube.com/charts/TopSongs/nz/weekly](https://charts.youtube.com/charts/TopSongs/nz/weekly)  
유튜브 뮤직 🇳🇮 니카라과(ni) 순위 100 : [https://charts.youtube.com/charts/TopSongs/ni/weekly](https://charts.youtube.com/charts/TopSongs/ni/weekly)  
유튜브 뮤직 🇳🇬 나이지리아(ng) 순위 100 : [https://charts.youtube.com/charts/TopSongs/ng/weekly](https://charts.youtube.com/charts/TopSongs/ng/weekly)  
유튜브 뮤직 🇳🇴 노르웨이(no) 순위 100 : [https://charts.youtube.com/charts/TopSongs/no/weekly](https://charts.youtube.com/charts/TopSongs/no/weekly)  
유튜브 뮤직 🇵🇦 파나마(no) 순위 100 : [https://charts.youtube.com/charts/TopSongs/pa/weekly](https://charts.youtube.com/charts/TopSongs/pa/weekly)  
유튜브 뮤직 🇵🇾 파라과이(no) 순위 100 : [https://charts.youtube.com/charts/TopSongs/py/weekly](https://charts.youtube.com/charts/TopSongs/py/weekly)  
유튜브 뮤직 🇵🇾 페루(pe) 순위 100 : [https://charts.youtube.com/charts/TopSongs/pe/weekly](https://charts.youtube.com/charts/TopSongs/pe/weekly)  
유튜브 뮤직 🇵🇱 폴란드(pl) 순위 100 : [https://charts.youtube.com/charts/TopSongs/pl/weekly](https://charts.youtube.com/charts/TopSongs/pl/weekly)  
유튜브 뮤직 🇵🇹 포르투갈(pt) 순위 100 : [https://charts.youtube.com/charts/TopSongs/pt/weekly](https://charts.youtube.com/charts/TopSongs/pt/weekly)  
유튜브 뮤직 🇷🇴 루마니아(ro) 순위 100 : [https://charts.youtube.com/charts/TopSongs/ro/weekly](https://charts.youtube.com/charts/TopSongs/ro/weekly)  
유튜브 뮤직 🇷🇺 러시아(ru) 순위 100 : [https://charts.youtube.com/charts/TopSongs/ru/weekly](https://charts.youtube.com/charts/TopSongs/ru/weekly)  
유튜브 뮤직 🇸🇦 사우디아라비아(ru) 순위 100 : [https://charts.youtube.com/charts/TopSongs/sa/weekly](https://charts.youtube.com/charts/TopSongs/sa/weekly)  
유튜브 뮤직 🇷🇸 세르비아(rs) 순위 100 : [https://charts.youtube.com/charts/TopSongs/rs/weekly](https://charts.youtube.com/charts/TopSongs/rs/weekly)  
유튜브 뮤직 🇿🇦 남아프리카 공화국(za) 순위 100 : [https://charts.youtube.com/charts/TopSongs/za/weekly](https://charts.youtube.com/charts/TopSongs/za/weekly)  
유튜브 뮤직 🇰🇷 대한민국(kr) 순위 100 : [https://charts.youtube.com/charts/TopSongs/kr/weekly](https://charts.youtube.com/charts/TopSongs/kr/weekly)  
유튜브 뮤직 🇪🇸 스페인(es) 순위 100 : [https://charts.youtube.com/charts/TopSongs/es/weekly](https://charts.youtube.com/charts/TopSongs/es/weekly)  
유튜브 뮤직 🇸🇪 스웨덴(se) 순위 100 : [https://charts.youtube.com/charts/TopSongs/se/weekly](https://charts.youtube.com/charts/TopSongs/se/weekly)  
유튜브 뮤직 🇨🇭 스위스(ch) 순위 100 : [https://charts.youtube.com/charts/TopSongs/ch/weekly](https://charts.youtube.com/charts/TopSongs/ch/weekly)  
유튜브 뮤직 🇹🇿 탄자니아(ch) 순위 100 : [https://charts.youtube.com/charts/TopSongs/tz/weekly](https://charts.youtube.com/charts/TopSongs/tz/weekly)  
유튜브 뮤직 🇹🇷 튀르키예(tr) 순위 100 : [https://charts.youtube.com/charts/TopSongs/tr/weekly](https://charts.youtube.com/charts/TopSongs/tr/weekly)  
유튜브 뮤직 🇺🇬 우간다(tr) 순위 100 : [https://charts.youtube.com/charts/TopSongs/ug/weekly](https://charts.youtube.com/charts/TopSongs/ug/weekly)  
유튜브 뮤직 🇺🇦 우크라이나(ua) 순위 100 : [https://charts.youtube.com/charts/TopSongs/ua/weekly](https://charts.youtube.com/charts/TopSongs/ua/weekly)  
유튜브 뮤직 🇦🇪 아랍에미리트(ae) 순위 100 : [https://charts.youtube.com/charts/TopSongs/ae/weekly](https://charts.youtube.com/charts/TopSongs/ae/weekly)  
유튜브 뮤직 🇬🇧 영국(gb) 순위 100 : [https://charts.youtube.com/charts/TopSongs/gb/weekly](https://charts.youtube.com/charts/TopSongs/gb/weekly)  
유튜브 뮤직 🇺🇸 미국(us) 순위 100 : [https://charts.youtube.com/charts/TopSongs/us/weekly](https://charts.youtube.com/charts/TopSongs/us/weekly)  
유튜브 뮤직 🇺🇾 우루과이(uy) 순위 100 : [https://charts.youtube.com/charts/TopSongs/uy/weekly](https://charts.youtube.com/charts/TopSongs/uy/weekly)  
유튜브 뮤직 🇿🇼 짐바브웨(zw) 순위 100 : [https://charts.youtube.com/charts/TopSongs/zw/weekly](https://charts.youtube.com/charts/TopSongs/zw/weekly)

## 🍎 애플 뮤직 전세계 챠트 수집하기

```js
https://websseu.github.io/pythonMusic/apple/[나라이름]/[나라이름]Top100_[날짜].json
```

애플 뮤직 🌏 글로벌(global) 순위 100 : [https://music.apple.com/us/playlist/top-100-global](https://music.apple.com/us/playlist/top-100-global/pl.d25f5d1181894928af76c85c967f8f31)  
애플 뮤직 🇺🇸 미국(usa) 순위 100 : [https://music.apple.com/us/playlist/top-100-usa](https://music.apple.com/us/playlist/top-100-usa/pl.606afcbb70264d2eb2b51d8dbcfa6a12)  
애플 뮤직 🇬🇧 영국(uk) 순위 100 : [https://music.apple.com/us/playlist/top-100-uk](https://music.apple.com/us/playlist/top-100-uk/pl.c2273b7e89b44121b3093f67228918e7)  
애플 뮤직 🇲🇽 멕시코(mexico) 순위 100 : [https://music.apple.com/us/playlist/top-100-mexico](https://music.apple.com/us/playlist/top-100-mexico/pl.df3f10ca27b1479087de2cd3f9f6716b)  
애플 뮤직 🇦🇺 호주 순위 100 : [https://music.apple.com/us/playlist/top-100-australia](https://music.apple.com/us/playlist/top-100-australia/pl.18be1cf04dfd4ffb9b6b0453e8fae8f1)  
애플 뮤직 🇯🇵 일본 순위 100 : [https://music.apple.com/us/playlist/top-100-japan](https://music.apple.com/us/playlist/top-100-japan/pl.043a2c9876114d95a4659988497567be)  
애플 뮤직 🇪🇸 스페인 순위 100 : [https://music.apple.com/us/playlist/top-100-spain](https://music.apple.com/us/playlist/top-100-spain/pl.0d656d7feae64198bc5fb1b02786ed75)  
애플 뮤직 🇫🇷 프랑스 순위 100 : [https://music.apple.com/us/playlist/top-100-australia](https://music.apple.com/us/playlist/top-100-france/pl.6e8cfd81d51042648fa36c9df5236b8d)  
애플 뮤직 🇩🇪 독일 순위 100 : [https://music.apple.com/us/playlist/top-100-germany](https://music.apple.com/us/playlist/top-100-germany/pl.c10a2c113db14685a0b09fa5834d8e8b)  
애플 뮤직 🇰🇷 한국 순위 100 : [https://music.apple.com/us/playlist/top-100-south-korea](https://music.apple.com/us/playlist/top-100-south-korea/pl.d3d10c32fbc540b38e266367dc8cb00c)  
애플 뮤직 🇦🇬 앤티가 바부다 순위 100 : [https://music.apple.com/us/playlist/top-100-antigua-and-barbuda](https://music.apple.com/us/playlist/top-100-antigua-and-barbuda/pl.cca0d50798424e4e871820a03719e841)  
애플 뮤직 🇦🇷 아르헨티나 순위 100 : [https://music.apple.com/us/playlist/top-100-argentina](https://music.apple.com/us/playlist/top-100-argentina/pl.7ae8594e422f44658e58212d876d9323)  
애플 뮤직 🇦🇲 아르메니아 순위 100 : [https://music.apple.com/us/playlist/top-100-armenia](https://music.apple.com/us/playlist/top-100-armenia/pl.42abb2144d594137a8fb4d37a9f35b42)  
애플 뮤직 🇦🇺 호주 순위 100 : [https://music.apple.com/us/playlist/top-100-austria](https://music.apple.com/us/playlist/top-100-austria/pl.f34430d010a843128337927bba98048b)  
애플 뮤직 🇦🇿 아제르바이잔 순위 100 : [https://music.apple.com/us/playlist/top-100-azerbaijan](https://music.apple.com/us/playlist/top-100-azerbaijan/pl.ccc31c81303c405baddaaf0f5328b7f3)  
애플 뮤직 🇧🇭 바레인 순위 100 : [https://music.apple.com/us/playlist/top-100-bahrain](https://music.apple.com/us/playlist/top-100-bahrain/pl.02a8276fa4ca40b19ac248fda4725fbb)  
애플 뮤직 🇧🇧 바베이도스 순위 100 : [https://music.apple.com/us/playlist/top-100-barbados](https://music.apple.com/us/playlist/top-100-barbados/pl.13743dcd86174ea5b4cb6b2534637e23)  
애플 뮤직 🇧🇾 벨라루스 순위 100 : [https://music.apple.com/us/playlist/top-100-belarus](https://music.apple.com/us/playlist/top-100-belarus/pl.50c1747c37404a9aa07acc39316f6873)  
애플 뮤직 🇧🇪 벨기에 순위 100 : [https://music.apple.com/us/playlist/top-100-belgium](https://music.apple.com/us/playlist/top-100-belgium/pl.cefe84f7916b4cae8b21b0a78e948380)  
애플 뮤직 🇧🇧 벨리즈 순위 100 : [https://music.apple.com/us/playlist/top-100-belize](https://music.apple.com/us/playlist/top-100-belize/pl.c6d8b5dcf6814168a4b0262628d3a317)  
애플 뮤직 🇧🇴 볼리비아 순위 100 : [https://music.apple.com/us/playlist/top-100-bolivia](https://music.apple.com/us/playlist/top-100-bolivia/pl.cfcd547b034d47648a16fb8e2df0623f)  
애플 뮤직 🇧🇼 보츠와나 순위 100 : [https://music.apple.com/us/playlist/top-100-botswana](https://music.apple.com/us/playlist/top-100-botswana/pl.73bb3593281444fb8ab21d58ccab4600)  
애플 뮤직 🇧🇷 브라질 순위 100 : [https://music.apple.com/us/playlist/top-100-brazil](https://music.apple.com/us/playlist/top-100-brazil/pl.11ac7cc7d09741c5822e8c66e5c7edbb)  
애플 뮤직 🇧🇬 불가리아 순위 100 : [https://music.apple.com/us/playlist/top-100-bulgaria](https://music.apple.com/us/playlist/top-100-bulgaria/pl.040cf0b4c7e9467eb9eed2d33e7a29d6)  
애플 뮤직 🇰🇭 캄보디아 순위 100 : [https://music.apple.com/us/playlist/top-100-cambodia](https://music.apple.com/us/playlist/top-100-cambodia/pl.9d9ee12c7734402ab5ab0dc81911822c)  
애플 뮤직 🇨🇻 카보베르데 순위 100 : [https://music.apple.com/us/playlist/top-100-cape-verde](https://music.apple.com/us/playlist/top-100-cape-verde/pl.917f294713a34cdeb46e67ad2a137067)  
애플 뮤직 🇨🇱 칠레 순위 100 : [https://music.apple.com/us/playlist/top-100-cape-chile](https://music.apple.com/us/playlist/top-100-chile/pl.81015bbbefdd46758b2c8c7065f0863e)  
애플 뮤직 🇨🇳 중국 순위 100 : [https://music.apple.com/us/playlist/top-100-cape-china](https://music.apple.com/us/playlist/top-100-china/pl.fde851dc95ce4ffbb74028dfd254ced5)  
애플 뮤직 🇨🇴 콜로비아 순위 100 : [https://music.apple.com/us/playlist/top-100-colombia](https://music.apple.com/us/playlist/top-100-colombia/pl.d116fa6286734b74acff3d38a740fe0d)  
애플 뮤직 🇨🇷 코스타리카 순위 100 : [https://music.apple.com/us/playlist/top-100-costa-rica](https://music.apple.com/us/playlist/top-100-costa-rica/pl.7771c20fc0354f64a723ae9c11a4d5f5)  
애플 뮤직 🇨🇾 키프로스 순위 100 : [https://music.apple.com/us/playlist/top-100-cyprus](https://music.apple.com/us/playlist/top-100-cyprus/pl.a5ae21745d1d45edacb68971746d31ae)  
애플 뮤직 🇨🇿 체코 순위 100 : [https://music.apple.com/us/playlist/top-100-czechia](https://music.apple.com/us/playlist/top-100-czechia/pl.e447d9ba54254130a76143bf6fdfa65c)  
애플 뮤직 🇩🇰 덴마크 순위 100 : [https://music.apple.com/us/playlist/top-100-denmark](https://music.apple.com/us/playlist/top-100-denmark/pl.d08496850bc840a4874e877177a69f9f)  
애플 뮤직 🇩🇲 도미니카 순위 100 : [https://music.apple.com/us/playlist/top-100-dominica](https://music.apple.com/us/playlist/top-100-dominica/pl.68e6ad675521400487ea78463b39899d)  
애플 뮤직 🇩🇴 도미니카 공화국 순위 100 : [https://music.apple.com/us/playlist/top-100-dominican-republic](https://music.apple.com/us/playlist/top-100-dominican-republic/pl.deec8b036583481782c40a2a05554b0b)  
애플 뮤직 🇪🇨 에콰도르 순위 100 : [https://music.apple.com/us/playlist/top-100-ecuador](https://music.apple.com/us/playlist/top-100-ecuador/pl.41b0d399afea495699dbc7660994a96c)  
애플 뮤직 🇪🇬 이집트 순위 100 : [https://music.apple.com/us/playlist/top-100-egypt](https://music.apple.com/us/playlist/top-100-egypt/pl.a0b3d0b9a2764646b59ccacdf82e3544)  
애플 뮤직 🇸🇻 엘살바도르 순위 100 : [https://music.apple.com/us/playlist/top-100-salvador](https://music.apple.com/us/playlist/top-100-el-salvador/pl.9a175d1e9b1e4c81bfa7c63f28c1a79e)  
애플 뮤직 🇪🇪 에스토니아 순위 100 : [https://music.apple.com/us/playlist/top-100-estonia](https://music.apple.com/us/playlist/top-100-estonia/pl.054734b06c7742a985805f45a283bcb4)  
애플 뮤직 🇫🇲 미크로네시아 순위 100 : [https://music.apple.com/us/playlist/top-100-micronesia](https://music.apple.com/us/playlist/top-100-micronesia/pl.bee910bc105b43c28eed7d20e4e09a8c)  
애플 뮤직 🇫🇯 피지 순위 100 : [https://music.apple.com/us/playlist/top-100-fiji](https://music.apple.com/us/playlist/top-100-fiji/pl.1e2c1286034c49b78139d2b4ff499a94)  
애플 뮤직 🇫🇮 핀란드 순위 100 : [https://music.apple.com/us/playlist/top-100-finland](https://music.apple.com/us/playlist/top-100-finland/pl.acea41a017664a8ebcd5aa1622aecc88)  
애플 뮤직 🇬🇲 감비아 순위 100 : [https://music.apple.com/us/playlist/top-100-gambia](https://music.apple.com/us/playlist/top-100-gambia/pl.62e12ecd522d47858321846adcaac43d)  
애플 뮤직 🇬🇭 가나 순위 100 : [https://music.apple.com/us/playlist/top-100-ghana](https://music.apple.com/us/playlist/top-100-ghana/pl.78f1974e882d4952b26ebfb8e017c933)  
애플 뮤직 🇬🇷 그리스 순위 100 : [https://music.apple.com/us/playlist/top-100-greece](https://music.apple.com/us/playlist/top-100-greece/pl.0f15f3a8ba014979b9fdd7a0ef906dca)  
애플 뮤직 🇬🇩 그레나다 순위 100 : [https://music.apple.com/us/playlist/top-100-grenada](https://music.apple.com/us/playlist/top-100-grenada/pl.b14c0257c1744d2686f88d05ab1efb4c)  
애플 뮤직 🇬🇹 과테말라 순위 100 : [https://music.apple.com/us/playlist/top-100-guatemala](https://music.apple.com/us/playlist/top-100-guatemala/pl.7235b4236ee241f083f8026d372cc2d8)  
애플 뮤직 🇬🇼 기니비사우 순위 100 : [https://music.apple.com/us/playlist/top-100-bissau](https://music.apple.com/us/playlist/top-100-guinea-bissau/pl.ac455234996b468b9f58e573752ab05c)  
애플 뮤직 🇭🇳 온두라스 순위 100 : [https://music.apple.com/us/playlist/top-100-honduras](https://music.apple.com/us/playlist/top-100-honduras/pl.ec6d493f976349dfb0cba8f6c2f7e937)  
애플 뮤직 🇭🇰 홍콩 순위 100 : [https://music.apple.com/us/playlist/top-100-hong-kong](https://music.apple.com/us/playlist/top-100-hong-kong/pl.7f35cffa10b54b91aab128ccc547f6ef)  
애플 뮤직 🇭🇺 헝가리 순위 100 : [https://music.apple.com/us/playlist/top-100-hungary](https://music.apple.com/us/playlist/top-100-hungary/pl.cee165c3a51e466481bde5de75d6dee3)  
애플 뮤직 🇭🇺 헝가리 순위 100 : [https://music.apple.com/us/playlist/top-100-hungary](https://music.apple.com/us/playlist/top-100-hungary/pl.cee165c3a51e466481bde5de75d6dee3)  
애플 뮤직 🇮🇳 인도 순위 100 : [https://music.apple.com/us/playlist/top-100-china](https://music.apple.com/us/playlist/top-100-india/pl.c0e98d2423e54c39b3df955c24df3cc5)  
애플 뮤직 🇮🇩 인도네시아 순위 100 : [https://music.apple.com/us/playlist/top-100-indonesia](https://music.apple.com/us/playlist/top-100-indonesia/pl.2b7e089dc9ef4dd7a18429df9c6e26a3)  
애플 뮤직 🇮🇱 이스라엘 순위 100 : [https://music.apple.com/us/playlist/top-100-israel](https://music.apple.com/us/playlist/top-100-israel/pl.0c9765e5330048af96c2336fa7bc3525)  
애플 뮤직 🇮🇹 이탈리아 순위 100 : [https://music.apple.com/us/playlist/top-100-china](https://music.apple.com/us/playlist/top-100-italy/pl.737e067787df485a8062e2c4927d94db)  
애플 뮤직 🇯🇴 요르단 순위 100 : [https://music.apple.com/us/playlist/top-100-jordan](https://music.apple.com/us/playlist/top-100-jordan/pl.5adf310412994d9483918fcd8e091fc5)  
애플 뮤직 🇰🇿 카자흐스탄 순위 100 : [https://music.apple.com/us/playlist/top-100-kazakhstan](https://music.apple.com/us/playlist/top-100-kazakhstan/pl.27d3c4d63b0e41f29f79c98bb5a090e1)  
애플 뮤직 🇰🇪 케냐 순위 100 : [https://music.apple.com/us/playlist/top-100-kenya](https://music.apple.com/us/playlist/top-100-kenya/pl.0b36ea82865d4adeb9d1d62207aab172)  
애플 뮤직 🇰🇬 키르기스스탄 순위 100 : [https://music.apple.com/us/playlist/top-100-kyrgyzstan](https://music.apple.com/us/playlist/top-100-kyrgyzstan/pl.5318aa72adb84bcfac803ecaf6156325)  
애플 뮤직 🇱🇦 라오스 순위 100 : [https://music.apple.com/us/playlist/top-100-laos](https://music.apple.com/us/playlist/top-100-laos/pl.42b3fe9c75a947ab84a80019e7bcd704)  
애플 뮤직 🇱🇻 라트비아 순위 100 : [https://music.apple.com/us/playlist/top-100-latvia](https://music.apple.com/us/playlist/top-100-latvia/pl.5ac047a9ada144aebb9b2f16f5bc8c1d)  
애플 뮤직 🇱🇧 레바논 순위 100 : [https://music.apple.com/us/playlist/top-100-lebanon](https://music.apple.com/us/playlist/top-100-lebanon/pl.838a4daba8924c42969ca7162fdc74da)  
애플 뮤직 🇱🇹 리투아니아 순위 100 : [https://music.apple.com/us/playlist/top-100-lithuania](https://music.apple.com/us/playlist/top-100-lithuania/pl.e96de57d836e42dca30f7da24c64bbea)  
애플 뮤직 🇱🇺 룩셈부르크 순위 100 : [https://music.apple.com/us/playlist/top-100-luxembourg](https://music.apple.com/us/playlist/top-100-luxembourg/pl.2f85377267d74a13be02a53882a5b488)  
애플 뮤직 🇲🇾 말레이시아 순위 100 : [https://music.apple.com/us/playlist/top-100-malaysia](https://music.apple.com/us/playlist/top-100-malaysia/pl.a165defeeccb4b17a59bb5c85637b9b7)  
애플 뮤직 🇲🇹 몰타 순위 100 : [https://music.apple.com/us/playlist/top-100-malta](https://music.apple.com/us/playlist/top-100-malta/pl.06ab782ba2324ae49317d6bde84eef56)  
애플 뮤직 🇲🇺 모리셔스 순위 100 : [https://music.apple.com/us/playlist/top-100-mauritius](https://music.apple.com/us/playlist/top-100-mauritius/pl.5e6efed969354b378770c2ea6f2fed6b)  
애플 뮤직 🇲🇳 몽골 순위 100 : [https://music.apple.com/us/playlist/top-100-mongolia](https://music.apple.com/us/playlist/top-100-mongolia/pl.71c450d15a9e4440ac5d24c174958225)  
애플 뮤직 🇳🇵 네팔 순위 100 : [https://music.apple.com/us/playlist/top-100-nepal](https://music.apple.com/us/playlist/top-100-nepal/pl.9032e70a644e442688f120a829c636cd)  
애플 뮤직 🇳🇱 네덜란드 순위 100 : [https://music.apple.com/us/playlist/top-100-netherlands](https://music.apple.com/us/playlist/top-100-netherlands/pl.26fb1998d54a4b3192be548529a97f8e)  
애플 뮤직 🇳🇿 뉴질랜드 순위 100 : [https://music.apple.com/us/playlist/top-100-new-zealand](https://music.apple.com/us/playlist/top-100-new-zealand/pl.d8742df90f43402ba5e708eefd6d949a)  
애플 뮤직 🇳🇮 니카라과 순위 100 : [https://music.apple.com/us/playlist/top-100-nicaragua](https://music.apple.com/us/playlist/top-100-nicaragua/pl.2249e0cc6edb46f4ae64de2c937a4f41)  
애플 뮤직 🇳🇪 니제르 순위 100 : [https://music.apple.com/us/playlist/top-100-niger](https://music.apple.com/us/playlist/top-100-niger/pl.cd4a09b0acde49cda246819d9421b26b)  
애플 뮤직 🇳🇬 나이지리아 순위 100 : [https://music.apple.com/us/playlist/top-100-nigeriar](https://music.apple.com/us/playlist/top-100-nigeria/pl.2fc68f6d68004ae993dadfe99de83877)  
애플 뮤직 🇳🇴 노르웨이 순위 100 : [https://music.apple.com/us/playlist/top-100-norway](https://music.apple.com/us/playlist/top-100-norway/pl.05a67957c3974729aac67c01247e55b6)  
애플 뮤직 🇴🇲 오만 순위 100 : [https://music.apple.com/us/playlist/top-100-oman](https://music.apple.com/us/playlist/top-100-oman/pl.d4ca5698caf04a9f873861c3659aeeca)  
애플 뮤직 🇵🇦 파나마 순위 100 : [https://music.apple.com/us/playlist/top-100-panama](https://music.apple.com/us/playlist/top-100-panama/pl.9d5ee7c72f804dbab97163616c7a8399)  
애플 뮤직 🇵🇬 파푸아뉴기니 순위 100 : [https://music.apple.com/us/playlist/top-100-papua-new-guinea](https://music.apple.com/us/playlist/top-100-papua-new-guinea/pl.30fbe54afbf846edabdbe00e90095d04)  
애플 뮤직 🇵🇾 파라과이 순위 100 : [https://music.apple.com/us/playlist/top-100-paraguay](https://music.apple.com/us/playlist/top-100-paraguay/pl.0843e61953c1430287162e5a36dff52b)  
애플 뮤직 🇵🇪 페루 순위 100 : [https://music.apple.com/us/playlist/top-100-peru](https://music.apple.com/us/playlist/top-100-peru/pl.569a0034bcc64db68bb13afa8171a687)  
애플 뮤직 🇵🇭 필리핀 순위 100 : [https://music.apple.com/us/playlist/top-100-philippines](https://music.apple.com/us/playlist/top-100-philippines/pl.b9eb00f9d195440e8b0bdf19b8db7f34)  
애플 뮤직 🇵🇱 폴란드 순위 100 : [https://music.apple.com/us/playlist/top-100-poland](https://music.apple.com/us/playlist/top-100-poland/pl.8c91cbb0ef4e48308dbbba4238135eaf)  
애플 뮤직 🇵🇹 포르투갈 순위 100 : [https://music.apple.com/us/playlist/top-100-portugal](https://music.apple.com/us/playlist/top-100-portugal/pl.5437c1490ac74e9e9505fc7d1f201655)  
애플 뮤직 🇲🇩 몰도바 순위 100 : [https://music.apple.com/us/playlist/top-100-moldova](https://music.apple.com/us/playlist/top-100-moldova/pl.e4dcd4663130419bb03b80216dee9f57)  
애플 뮤직 🇷🇴 루마니아 순위 100 : [https://music.apple.com/us/playlist/top-100-romania](https://music.apple.com/us/playlist/top-100-romania/pl.0c6bea611ad54c79b854299bc515a5a6)  
애플 뮤직 🇸🇦 사우디아라비아 순위 100 : [https://music.apple.com/us/playlist/top-100-saudi-arabia](https://music.apple.com/us/playlist/top-100-saudi-arabia/pl.a5365fa3b6ec4a34994339ca100801ae)  
애플 뮤직 🇸🇬 싱가포르 순위 100 : [https://music.apple.com/us/playlist/top-100-singapore](https://music.apple.com/us/playlist/top-100-singapore/pl.4d763fa1cf15433b9994a14be6a46164)  
애플 뮤직 🇸🇰 슬로바키아 순위 100 : [https://music.apple.com/us/playlist/top-100-slovakia](https://music.apple.com/us/playlist/top-100-slovakia/pl.2e50996a5bf44ab78cbb5c34b1992701)  
애플 뮤직 🇸🇮 슬로베니아 순위 100 : [https://music.apple.com/us/playlist/top-100-slovenia](https://music.apple.com/us/playlist/top-100-slovenia/pl.e7374de32aec446c92136234d5bcae2f)  
애플 뮤직 🇿🇦 남아프리카 공화국 순위 100 : [https://music.apple.com/us/playlist/top-100-south-africa](https://music.apple.com/us/playlist/top-100-south-africa/pl.447bd05172824b89bd745628f7f54c18)  
애플 뮤직 🇱🇰 스리랑카 공화국 순위 100 : [https://music.apple.com/us/playlist/top-100-sri-lanka](https://music.apple.com/us/playlist/top-100-sri-lanka/pl.cd9b6c35086b43b193ecc3d32882a41e)  
애플 뮤직 🇰🇳 세인트키츠 네비스 공화국 순위 100 : [https://music.apple.com/us/playlist/top-100-st-kitts-and-nevis](https://music.apple.com/us/playlist/top-100-st-kitts-and-nevis/pl.be7b2d63abaf4d25918ef41187f88be4)  
애플 뮤직 🇸🇿 에스와티니 순위 100 : [https://music.apple.com/us/playlist/top-100-eswatini](https://music.apple.com/us/playlist/top-100-eswatini/pl.046c3e297666475aa84c12159a954596)  
애플 뮤직 🇸🇪 스웨덴 순위 100 : [https://music.apple.com/us/playlist/top-100-sweden](https://music.apple.com/us/playlist/top-100-sweden/pl.5876877c387b4ffb8860ac3ea2c244c3)  
애플 뮤직 🇨🇭 스위스 순위 100 : [https://music.apple.com/us/playlist/top-100-switzerland](https://music.apple.com/us/playlist/top-100-switzerland/pl.bb1f5218a0f04de3877c4f9ccd63d260)  
애플 뮤직 🇹🇼 대만 순위 100 : [https://music.apple.com/us/playlist/top-100-taiwan](https://music.apple.com/us/playlist/top-100-taiwan/pl.741ff34016704547853b953ec5181d83)  
애플 뮤직 🇹🇯 타지키스탄 순위 100 : [https://music.apple.com/us/playlist/top-100-tajikistan](https://music.apple.com/us/playlist/top-100-tajikistan/pl.ea75568dc0524a479b818d551a7b3c35)  
애플 뮤직 🇹🇭 태국 순위 100 : [https://music.apple.com/us/playlist/top-100-thailand](https://music.apple.com/us/playlist/top-100-thailand/pl.c509137d97214632a087129ece060a3d)  
애플 뮤직 🇹🇹 트리니다드 토바고 순위 100 : [https://music.apple.com/us/playlist/top-100-trinidad-and-tobago](https://music.apple.com/us/playlist/top-100-trinidad-and-tobago/pl.f1495be1a9774341ab8a1eceb7011579)  
애플 뮤직 🇹🇷 튀르키예 순위 100 : [https://music.apple.com/us/playlist/top-100-t%C3%BCrkiye](https://music.apple.com/us/playlist/top-100-t%C3%BCrkiye/pl.f3e0d6ef238542609572c18b0de1513b9)  
애플 뮤직 🇹🇲 투르크메니스탄 순위 100 : [https://music.apple.com/us/playlist/top-100-turkmenistan](https://music.apple.com/us/playlist/top-100-turkmenistan/pl.f783d8aec4df401583434a2454adbc3d)  
애플 뮤직 🇺🇬 우간다 순위 100 : [https://music.apple.com/us/playlist/top-100-uganda](https://music.apple.com/us/playlist/top-100-uganda/pl.b9e553253ed24c2a829c9c08209e5f67)  
애플 뮤직 🇺🇦 우크라이나 순위 100 : [https://music.apple.com/us/playlist/top-100-ukraine](https://music.apple.com/us/playlist/top-100-ukraine/pl.815f78effb3844909a8259d759ecbddb)  
애플 뮤직 🇦🇪 아랍에미리트 순위 100 : [https://music.apple.com/us/playlist/top-100-united-arab-emirates](https://music.apple.com/us/playlist/top-100-united-arab-emirates/pl.7b5e51f09aee4733958e23ea97dda459)  
애플 뮤직 🇺🇿 우즈베키스탄 순위 100 : [https://music.apple.com/us/playlist/top-100-uzbekistan](https://music.apple.com/us/playlist/top-100-uzbekistan/pl.90ad69a600ed4d10b00d158eea68cad7)  
애플 뮤직 🇻🇪 베네수엘라 순위 100 : [https://music.apple.com/us/playlist/top-100-venezuela](https://music.apple.com/us/playlist/top-100-venezuela/pl.617da0e0bbb74461b607cad435b1e941)  
애플 뮤직 🇻🇳 베트남 순위 100 : [https://music.apple.com/us/playlist/top-100-vietnam](https://music.apple.com/us/playlist/top-100-vietnam/pl.550110ec6feb4ae0aff364bcde6d1372)  
애플 뮤직 🇿🇼 짐바브웨 순위 100 : [https://music.apple.com/us/playlist/top-100-Zimbabwe](https://music.apple.com/us/playlist/top-100-zimbabwe/pl.ad37160bb16c4c70a1d83d3670e96c1a)
