from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from datetime import datetime, timedelta
from bs4 import BeautifulSoup
import os
import json
import time

# Spotify 로그인 정보
SPOTIFY_USERNAME = "richclub9@naver.com"
SPOTIFY_PASSWORD = "Forever8879!s"

# 이틀 전 날짜 계산
two_days_ago = (datetime.now() - timedelta(days=2)).strftime("%Y-%m-%d")

# 국가별 URL 설정
countries = {
    "global": f"https://charts.spotify.com/charts/view/regional-global-daily/{two_days_ago}",
    "argentina": f"https://charts.spotify.com/charts/view/regional-ar-daily/{two_days_ago}",
    "australia": f"https://charts.spotify.com/charts/view/regional-au-daily/{two_days_ago}",
    "austria": f"https://charts.spotify.com/charts/view/regional-at-daily/{two_days_ago}",
    "belarus": f"https://charts.spotify.com/charts/view/regional-by-daily/{two_days_ago}",
    "belgium": f"https://charts.spotify.com/charts/view/regional-be-daily/{two_days_ago}",
    "bolivia": f"https://charts.spotify.com/charts/view/regional-bo-daily/{two_days_ago}",
    "brazil": f"https://charts.spotify.com/charts/view/regional-br-daily/{two_days_ago}",
    "bulgaria": f"https://charts.spotify.com/charts/view/regional-bg-daily/{two_days_ago}",
    "canada": f"https://charts.spotify.com/charts/view/regional-ca-daily/{two_days_ago}",
    "chile": f"https://charts.spotify.com/charts/view/regional-cl-daily/{two_days_ago}",
    "colombia": f"https://charts.spotify.com/charts/view/regional-co-daily/{two_days_ago}",
    "costa-rica": f"https://charts.spotify.com/charts/view/regional-cr-daily/{two_days_ago}",
    "czech-republic": f"https://charts.spotify.com/charts/view/regional-cz-daily/{two_days_ago}",
    "denmark": f"https://charts.spotify.com/charts/view/regional-dk-daily/{two_days_ago}",
    "dominican Republic": f"https://charts.spotify.com/charts/view/regional-do-daily/{two_days_ago}",
    "ecuador": f"https://charts.spotify.com/charts/view/regional-ec-daily/{two_days_ago}",
    "egypt": f"https://charts.spotify.com/charts/view/regional-eg-daily/{two_days_ago}",
    "el-salvador": f"https://charts.spotify.com/charts/view/regional-sv-daily/{two_days_ago}",
    "estonia": f"https://charts.spotify.com/charts/view/regional-ee-daily/{two_days_ago}",
    "finland": f"https://charts.spotify.com/charts/view/regional-fi-daily/{two_days_ago}",
    "france": f"https://charts.spotify.com/charts/view/regional-fr-daily/{two_days_ago}",
    "germany": f"https://charts.spotify.com/charts/view/regional-de-daily/{two_days_ago}",
    "greece": f"https://charts.spotify.com/charts/view/regional-gr-daily/{two_days_ago}",
    "guatemala": f"https://charts.spotify.com/charts/view/regional-gt-daily/{two_days_ago}",
    "honduras": f"https://charts.spotify.com/charts/view/regional-hn-daily/{two_days_ago}",
    "hong-kong": f"https://charts.spotify.com/charts/view/regional-hk-daily/{two_days_ago}",
    "hungary": f"https://charts.spotify.com/charts/view/regional-hu-daily/{two_days_ago}",
    "hungary": f"https://charts.spotify.com/charts/view/regional-hu-daily/{two_days_ago}",
    "iceland": f"https://charts.spotify.com/charts/view/regional-is-daily/{two_days_ago}",
    "israel": f"https://charts.spotify.com/charts/view/regional-il-daily/{two_days_ago}",
    "italy": f"https://charts.spotify.com/charts/view/regional-it-daily/{two_days_ago}",
    "japan": f"https://charts.spotify.com/charts/view/regional-jp-daily/{two_days_ago}",
    "kazakhstan": f"https://charts.spotify.com/charts/view/regional-kz-daily/{two_days_ago}",
    "latvia": f"https://charts.spotify.com/charts/view/regional-lv-daily/{two_days_ago}",
    "lithuania": f"https://charts.spotify.com/charts/view/regional-lt-daily/{two_days_ago}",
    "luxembourg": f"https://charts.spotify.com/charts/view/regional-lu-daily/{two_days_ago}",
    "malaysia": f"https://charts.spotify.com/charts/view/regional-my-daily/{two_days_ago}",
    "mexico": f"https://charts.spotify.com/charts/view/regional-mx-daily/{two_days_ago}",
    "morocco": f"https://charts.spotify.com/charts/view/regional-ma-daily/{two_days_ago}",
    "netherlands": f"https://charts.spotify.com/charts/view/regional-nl-daily/{two_days_ago}",
    "new-zealand": f"https://charts.spotify.com/charts/view/regional-nz-daily/{two_days_ago}",
    "nicaragua": f"https://charts.spotify.com/charts/view/regional-ni-daily/{two_days_ago}",
    "nicaragua": f"https://charts.spotify.com/charts/view/regional-ni-daily/{two_days_ago}",
    "norway": f"https://charts.spotify.com/charts/view/regional-no-daily/{two_days_ago}",
    "pakistan": f"https://charts.spotify.com/charts/view/regional-pk-daily/{two_days_ago}",
    "panama": f"https://charts.spotify.com/charts/view/regional-pa-daily/{two_days_ago}",
    "paraguay": f"https://charts.spotify.com/charts/view/regional-py-daily/{two_days_ago}",
    "peru": f"https://charts.spotify.com/charts/view/regional-pe-daily/{two_days_ago}",
    "philippines": f"https://charts.spotify.com/charts/view/regional-ph-daily/{two_days_ago}",
    "poland": f"https://charts.spotify.com/charts/view/regional-pl-daily/{two_days_ago}",
    "portugal": f"https://charts.spotify.com/charts/view/regional-pt-daily/{two_days_ago}",
    "romania": f"https://charts.spotify.com/charts/view/regional-ro-daily/{two_days_ago}",
    "saudi-arabia": f"https://charts.spotify.com/charts/view/regional-sa-daily/{two_days_ago}",
    "singapore": f"https://charts.spotify.com/charts/view/regional-sg-daily/{two_days_ago}",
    "slovakia": f"https://charts.spotify.com/charts/view/regional-sk-daily/{two_days_ago}",
    "south-africa": f"https://charts.spotify.com/charts/view/regional-za-daily/{two_days_ago}",
    "south-korea": f"https://charts.spotify.com/charts/view/regional-kr-daily/{two_days_ago}",
    "spain": f"https://charts.spotify.com/charts/view/regional-es-daily/{two_days_ago}",
    "sweden": f"https://charts.spotify.com/charts/view/regional-se-daily/{two_days_ago}",
    "switzerland": f"https://charts.spotify.com/charts/view/regional-ch-daily/{two_days_ago}",
    "taiwan": f"https://charts.spotify.com/charts/view/regional-tw-daily/{two_days_ago}",
    "thailand": f"https://charts.spotify.com/charts/view/regional-th-daily/{two_days_ago}",
    "turkey": f"https://charts.spotify.com/charts/view/regional-tr-daily/{two_days_ago}",
    "united-arab-emirates": f"https://charts.spotify.com/charts/view/regional-ae-daily/{two_days_ago}",
    "ukraine": f"https://charts.spotify.com/charts/view/regional-ua-daily/{two_days_ago}",
    "uk": f"https://charts.spotify.com/charts/view/regional-gb-daily/{two_days_ago}",
    "uruguay": f"https://charts.spotify.com/charts/view/regional-uy-daily/{two_days_ago}",
    "usa": f"https://charts.spotify.com/charts/view/regional-us-daily/{two_days_ago}",
    "venezuela": f"https://charts.spotify.com/charts/view/regional-ve-daily/{two_days_ago}",
    "vietnam": f"https://charts.spotify.com/charts/view/regional-vn-daily/{two_days_ago}",
}

# 웹드라이버 설정
# browser = webdriver.Chrome()

options = ChromeOptions()
options.add_argument("--headless")
browser = webdriver.Chrome(options=options)

try:
    # Spotify 차트 페이지로 이동
    browser.get("https://charts.spotify.com/home")
    print("Spotify 차트 페이지에 접속했습니다.")

    # `Log in` 버튼 대기 및 클릭
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//a[@data-testid='charts-login']"))
    )
    login_button = browser.find_element(By.XPATH, "//a[@data-testid='charts-login']")
    login_button.click()
    print("Log in 버튼을 클릭했습니다.")

    # Spotify 로그인 페이지 대기
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "login-username"))
    )
    print("Spotify 로그인 페이지로 이동했습니다.")

    # 사용자 이름 입력
    username_field = browser.find_element(By.ID, "login-username")
    username_field.send_keys(SPOTIFY_USERNAME)

    # 비밀번호 입력
    password_field = browser.find_element(By.ID, "login-password")
    password_field.send_keys(SPOTIFY_PASSWORD)

    # 로그인 버튼 클릭
    login_button = browser.find_element(By.ID, "login-button")
    login_button.click()
    print("로그인 버튼을 클릭했습니다.")

    # 로그인 후 차트 페이지 대기
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.XPATH, "//div[@data-testid='overview-body']"))
    )
    print("차트 페이지로 성공적으로 이동했습니다.")
    time.sleep(2)

    # 국가별 데이터 수집
    for country, url in countries.items():
        try:
            # 국가별 폴더 및 파일 경로 설정
            folder_path = f"spotify/{country}"
            file_name = f"{folder_path}/{country}Top100_{two_days_ago}.json"

            # 폴더 생성
            os.makedirs(folder_path, exist_ok=True)

            # 해당 국가의 URL로 이동
            browser.get(url)
            print(f"{country} 페이지에 접속했습니다.")

            # 페이지 로딩 대기
            WebDriverWait(browser, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "table"))
            )
            print(f"{country} 차트 테이블이 로드되었습니다.")

            # 페이지 소스 파싱
            soup = BeautifulSoup(browser.page_source, "html.parser")
            print(f"{country} 데이터 수집 시작...")

            # 테이블 행 추출
            table = soup.find("table")
            if not table:
                print(f"{country}: 테이블을 찾을 수 없습니다.")
                continue
            rows = table.find_all("tr")

            # 데이터 저장할 리스트
            chart_data = []

            for row in rows[1:101]:  # 상위 100개만 처리
                try:
                    # 순위 추출
                    ranking = row.select_one("td:nth-child(2) span[aria-label='Current position']").text.strip()

                    # 타이틀 추출
                    title = row.select_one("td:nth-child(3) > div > div:nth-child(2) > a > div > span > span > div > span").text.strip()

                    # 아티스트 추출
                    artist = row.select_one("td:nth-child(3) > div > div:nth-child(2) > div > span > span > div > div > p").text.strip()

                    # 이미지 추출
                    image = row.select_one("td:nth-child(3) > div > div:nth-child(1) > img")["src"]

                    # 아이디 추출
                    spotify_url = row.select_one("td:nth-child(3) > div > div:nth-child(2) > a")["href"]
                    spotify_id = spotify_url.split("/")[-1]

                    # Peak 추출
                    peak = row.select_one("td:nth-child(4)").text.strip()

                    # Prev 추출
                    prev = row.select_one("td:nth-child(5) > span").text.strip()

                    # Streak 추출
                    streak = row.select_one("td:nth-child(6)").text.strip()

                    # Streams 추출
                    streams = row.select_one("td:nth-child(7)").text.strip()

                    # 데이터 추가
                    chart_data.append({
                        "ranking": ranking,
                        "title": title,
                        "artist": artist,
                        "image": image,
                        "peak": peak,
                        "prev": prev,
                        "streak": streak,
                        "streams": streams,
                        "spotifyID": spotify_id
                    })
                except AttributeError as e:
                    # 데이터가 누락된 경우 처리
                    print(f"{country}: 데이터 추출 중 오류 발생: {e}")
                    continue

            # JSON 파일로 저장
            with open(file_name, "w", encoding="utf-8") as f:
                json.dump(chart_data, f, ensure_ascii=False, indent=4)

            print(f"{country} 차트 데이터가 {file_name}에 저장되었습니다.")

        except TimeoutException as e:
            print(f"{country} 오류 발생: {str(e)}")

finally:
    # 브라우저 닫기
    browser.quit()
