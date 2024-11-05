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
    "usa": "https://music.apple.com/us/playlist/top-100-usa/pl.606afcbb70264d2eb2b51d8dbcfa6a12",
    "uk": "https://music.apple.com/us/playlist/top-100-uk/pl.c2273b7e89b44121b3093f67228918e7",
    "canada": "https://music.apple.com/us/playlist/top-100-canada/pl.79bac9045a2540e0b195e983df8ba569",
    "japan": "https://music.apple.com/us/playlist/top-100-japan/pl.043a2c9876114d95a4659988497567be",
    "australia": "https://music.apple.com/us/playlist/top-100-australia/pl.18be1cf04dfd4ffb9b6b0453e8fae8f1",
    "france": "https://music.apple.com/us/playlist/top-100-france/pl.6e8cfd81d51042648fa36c9df5236b8d",
    "germany": "https://music.apple.com/us/playlist/top-100-germany/pl.c10a2c113db14685a0b09fa5834d8e8b",
    "china": "https://music.apple.com/us/playlist/top-100-china/pl.fde851dc95ce4ffbb74028dfd254ced5",
    "india": "https://music.apple.com/us/playlist/top-100-india/pl.c0e98d2423e54c39b3df955c24df3cc5",
    "italy": "https://music.apple.com/us/playlist/top-100-italy/pl.737e067787df485a8062e2c4927d94db",
    "thailand": "https://music.apple.com/us/playlist/top-100-thailand/pl.c509137d97214632a087129ece060a3d",
    "vietnam": "https://music.apple.com/us/playlist/top-100-vietnam/pl.550110ec6feb4ae0aff364bcde6d1372",
    "singapore": "https://music.apple.com/us/playlist/top-100-singapore/pl.4d763fa1cf15433b9994a14be6a46164"
}

# 웹드라이버 설정
options = ChromeOptions()
options.add_argument("--headless")
browser = webdriver.Chrome(options=options)

for country, url in countries.items():
    print(f"Processing data for {country}...")

    # 폴더 및 파일 이름 설정
    folder_path = f"apple{country.capitalize()}"
    file_name = f"{folder_path}/{folder_path}100_{current_date}.json"
    os.makedirs(folder_path, exist_ok=True)

    # 페이지 로드
    browser.get(url)

    # 페이지가 완전히 로드될 때까지 대기
    try:
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "songs-list"))
        )
        print(f"{country} 페이지가 완전히 로드되었습니다.")
        time.sleep(3)
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
        album = track.select_one(".songs-list__col--tertiary div span a").text.strip() if track.select_one(".songs-list__col--tertiary div span a") else None
        image = track.select_one(".artwork-component source")["srcset"].split(",")[1].strip().split(" ")[0] if track.select_one(".artwork-component source") else None
        length = track.select_one(".songs-list-row__length").text.strip() if track.select_one(".songs-list-row__length") else None

        # 수집된 정보를 딕셔너리에 저장
        chart_data.append({
            "ranking": ranking,
            "title": title,
            "artist": artist,
            "album": album,
            "image": image,
            "length": length
        })

    # 추출된 데이터를 JSON 파일로 저장
    with open(file_name, 'w', encoding='utf-8') as f:
        json.dump(chart_data, f, ensure_ascii=False, indent=4)
        print(f"{country} 데이터가 '{file_name}' 파일에 저장되었습니다.")

# 브라우저 종료
browser.quit()
