# 파이썬을 이용한 뮤직 데이터 수집하기

파이썬을 이용하여 뮤직 순위정보를 수집하여 사이트를 만들겠습니다.

## 뮤직 챠트 수집하기

애플 뮤직 코리아 순위 100 : [https://music.apple.com/kr/new](https://music.apple.com/kr/playlist/%EC%98%A4%EB%8A%98%EC%9D%98-top-100-%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD/pl.d3d10c32fbc540b38e266367dc8cb00c)   
빌보드 뮤직 순위 100 : [https://www.billboard.com/charts/billboard-200/](https://www.billboard.com/charts/billboard-200/)

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
