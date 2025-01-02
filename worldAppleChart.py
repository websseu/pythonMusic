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

# 현재 날짜를 문자열로 저장
current_date = datetime.now().strftime("%Y-%m-%d")

# 국가별 URL 및 폴더 설정
countries = {
    "global": "https://music.apple.com/kr/playlist/top-100-global/pl.d25f5d1181894928af76c85c967f8f31",
    "antigua-and-barbuda": "https://music.apple.com/kr/playlist/top-100-antigua-and-barbuda/pl.cca0d50798424e4e871820a03719e841",
    
}

# 웹드라이버 설정
options = ChromeOptions()
options.add_argument("--headless")
browser = webdriver.Chrome(options=options)

# 최상위 apple 폴더 생성
base_folder_path = "apple"
os.makedirs(base_folder_path, exist_ok=True)

for country, url in countries.items():
    print(f"{country} 데이터를 처리하고 있습니다.")

    # 나라별 하위 폴더 생성
    country_folder_path = os.path.join(base_folder_path, country)
    os.makedirs(country_folder_path, exist_ok=True)

    # 파일 이름 설정
    file_name = f"{country_folder_path}/{country}Top100_{current_date}.json"

    # 페이지 로드
    browser.get(url)

    # 페이지가 완전히 로드될 때까지 대기
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "songs-list"))
        )
        print(f"{country} 페이지가 완전히 로드되었습니다.")
        time.sleep(10)
    except TimeoutException:
        print(f"{country} 페이지가 완전히 로드되지 않았습니다.")
        continue  # 다음 나라로 넘어가기

    # BeautifulSoup으로 페이지 소스 파싱
    html_source_updated = browser.page_source
    soup = BeautifulSoup(html_source_updated, 'html.parser')

    # 차트 정보를 저장할 리스트
    chart_data = []

    # 데이터 추출
    tracks = soup.select(".songs-list-row")

    for track in tracks:
        # 순위, 제목, 아티스트, 앨범 정보 추출
        ranking = track.select_one(".songs-list-row__rank").text.strip() if track.select_one(".songs-list-row__rank") else None
        title = track.select_one(".songs-list-row__song-name").text.strip() if track.select_one(".songs-list-row__song-name") else None
        artist = track.select_one(".songs-list__col--secondary div span a").text.strip() if track.select_one(".songs-list__col--secondary div span a") else None
        image = track.select_one(".artwork-component source")["srcset"].split(",")[1].strip().split(" ")[0] if track.select_one(".artwork-component source") else None
        appleID = (
            track.find("a", {"class": "click-action"})["href"].split("song/")[-1]
            if track.find("a", {"class": "click-action"})
            else None
        )

        # 수집된 정보를 딕셔너리에 저장
        chart_data.append({
            "ranking": ranking,
            "title": title,
            "artist": artist,
            "image": image,
            "appleID": appleID
        })

    # 추출된 데이터를 JSON 파일로 저장
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(chart_data, f, ensure_ascii=False, indent=4)
        print(f"{country} 데이터가 '{file_name}' 파일에 저장되었습니다.")

# 브라우저 종료
browser.quit()
