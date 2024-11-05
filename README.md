# 파이썬을 이용한 뮤직 데이터 수집하기

파이썬을 이용하여 뮤직 순위정보를 수집하여 사이트를 만들겠습니다.

## 뮤직 챠트 수집하기

애플 뮤직 코리아 순위 100 : [https://music.apple.com/kr/new](https://music.apple.com/kr/playlist/%EC%98%A4%EB%8A%98%EC%9D%98-top-100-%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD/pl.d3d10c32fbc540b38e266367dc8cb00c)  
멜론 뮤직 순위 100 : [https://www.melon.com/chart/index.htm](https://www.melon.com/chart/index.htm)  
지니 뮤직 순위 100 : [https://www.genie.co.kr/chart/top200](https://www.genie.co.kr/chart/top200?ditc=D&ymd=20241105&hh=10&rtm=Y&pg=1)  
벅스 뮤직 순위 100 : [https://music.bugs.co.kr/chart](https://music.bugs.co.kr/chart)  
플로 뮤직 순위 100 : [https://www.music-flo.com/browse](https://www.music-flo.com/browse)  
바이브 뮤직 순위 100 : [https://vibe.naver.com/chart/total](https://vibe.naver.com/chart/total)

빌보드 핫 뮤직 순위 100 : [https://www.billboard.com/charts/hot-100/](https://www.billboard.com/charts/hot-100/)  
빌보드 글로벌 뮤직 순위 100 : [https://www.billboard.com/charts/billboard-global-200/](https://www.billboard.com/charts/billboard-global-200/)  
애플 뮤직 글로벌 순위 100 : [https://music.apple.com/us/playlist/top-100-global](https://music.apple.com/us/playlist/top-100-global/pl.d25f5d1181894928af76c85c967f8f31)  
애플 뮤직 🇺🇸 미국 순위 100 : [https://music.apple.com/us/playlist/top-100-usa](https://music.apple.com/us/playlist/top-100-usa/pl.606afcbb70264d2eb2b51d8dbcfa6a12)  
애플 뮤직 🇬🇧 영국 순위 100 : [https://music.apple.com/us/playlist/top-100-uk](https://music.apple.com/us/playlist/top-100-uk/pl.c2273b7e89b44121b3093f67228918e7)  
애플 뮤직 🇨🇦 캐나다 순위 100 : [https://music.apple.com/us/playlist/top-100-canada](https://music.apple.com/us/playlist/top-100-canada/pl.79bac9045a2540e0b195e983df8ba569)  
애플 뮤직 🇯🇵 일본 순위 100 : [https://music.apple.com/us/playlist/top-100-japan](https://music.apple.com/us/playlist/top-100-japan/pl.043a2c9876114d95a4659988497567be)

### Requests

HTTP 요청을 쉽게 할 수 있도록 해주는 라이브러리입니다. 이를 통해 웹 API와의 상호작용, 웹 페이지 데이터 수집 등 다양한 HTTP 작업을 간편하게 수행할 수 있습니다

```bash
pip install requests
```

### Selenium

Selenium은 웹 브라우저를 자동화하는 도구로, 웹 애플리케이션을 테스트하거나 데이터를 수집하는 데 많이 사용됩니다.

```bash
pip install selenium
```

### BeautifulSoup

BeautifulSoup은 HTML이나 XML 파일을 파싱하여 원하는 정보를 쉽게 추출할 수 있게 해주는 도구입니다. BeautifulSoup은 웹 크롤링과 스크래핑 작업에서 많이 사용되며, HTML 문서 구조를 파싱하여 특정 태그, 속성, 클래스 등을 통해 데이터를 추출할 수 있습니다.

```bash
pip install beautifulsoup4
```
