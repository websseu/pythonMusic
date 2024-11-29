from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from datetime import datetime
from bs4 import BeautifulSoup
import os
import json
import time

# Spotify 로그인 정보
SPOTIFY_USERNAME = "richclub9@naver.com"
SPOTIFY_PASSWORD = "Forever8888!s"

# 오늘 날짜 계산
today = datetime.now().strftime("%Y-%m-%d")

# 한국 차트 URL
url = "https://charts.spotify.com/charts/view/regional-kr-daily/latest"

# 웹드라이버 설정
options = ChromeOptions()
options.add_argument("--headless")
browser = webdriver.Chrome(options=options)

try:
    # Spotify 차트 페이지로 이동
    browser.get("https://charts.spotify.com/home")
    print("Spotify 차트 페이지에 접속했습니다.")

    # Log in 버튼 대기 및 클릭
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

    # 데이터 저장 경로 설정
    folder_path = "korea/spotify"
    file_name = f"{folder_path}/spotifyTop100_{today}.json"

    # 폴더 생성
    os.makedirs(folder_path, exist_ok=True)

    # 한국 차트 URL로 이동
    browser.get(url)
    print("한국 차트 페이지에 접속했습니다.")

    # 페이지 로딩 대기
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "table"))
    )
    print("한국 차트 테이블이 로드되었습니다.")

    # 페이지 소스 파싱
    soup = BeautifulSoup(browser.page_source, "html.parser")
    print("한국 데이터 수집 시작...")

    # 테이블 행 추출
    table = soup.find("table")
    if not table:
        print("한국: 테이블을 찾을 수 없습니다.")
    else:
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
                    "spotifyID": spotify_id,
                })
            except AttributeError as e:
                # 데이터가 누락된 경우 처리
                print(f"데이터 추출 중 오류 발생: {e}")
                continue

        # JSON 파일로 저장
        with open(file_name, "w", encoding="utf-8") as f:
            json.dump(chart_data, f, ensure_ascii=False, indent=4)

        print(f"한국 차트 데이터가 {file_name}에 저장되었습니다.")

except TimeoutException as e:
    print(f"오류 발생: {str(e)}")

finally:
    # 브라우저 닫기
    browser.quit()
