from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from bs4 import BeautifulSoup
from datetime import datetime
import os
import json
import time

# 현재 날짜를 문자열로 저장
current_date = datetime.now().strftime("%Y-%m-%d")

# 한국 차트 URL 설정
url = "https://charts.youtube.com/charts/TopSongs/kr/weekly"

# 파일 저장 경로 설정
folder_path = "korea/youtube"
os.makedirs(folder_path, exist_ok=True)
json_file_name = os.path.join(folder_path, f"youtubeTop100_{current_date}.json")

# 웹드라이버 설정
options = ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_experimental_option("prefs", {"intl.accept_languages": "en-US,en"})
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
browser = webdriver.Chrome(options=options)

try:
    print(f"Processing YouTube Korea chart...")

    # 브라우저로 URL 열기
    browser.get(url)
    time.sleep(10)  # 페이지 로드 대기

    # HTML 데이터 파싱
    soup = BeautifulSoup(browser.page_source, 'html.parser')

    # 데이터 추출
    data = []
    rows = soup.find_all('ytmc-entry-row')  # 각 row를 선택

    for row in rows:
        # 랭킹 추출
        rank_element = row.find('span', {'id': 'rank'})
        ranking = rank_element.text.strip() if rank_element else None

        # 제목 추출
        title_element = row.find('div', {'id': 'entity-title'})
        title = title_element.text.strip() if title_element else None

        # 가수 추출
        artist_element = row.select_one("div#artist-names > span[hidden]")
        artist = artist_element.text.strip() if artist_element else None

        # 이미지 URL 추출
        img_element = row.select_one("div.thumbnail-container > img#thumbnail")
        image = img_element['src'] if img_element else None

        # 지난주 랭킹 추출
        prev_element = row.select_one("div.data-table-container > div:nth-child(4)")
        prev = prev_element.text.strip() if prev_element else None

        # 지속 기간 추출
        streak_element = row.select_one("div.data-table-container > div:nth-child(5)")
        streak = streak_element.text.strip() if streak_element else None

        # 주간 조회수 추출
        streams_element = row.select_one("div.data-table-container > div:nth-child(6)")
        streams = streams_element.text.strip() if streams_element else None

        # YouTube ID 추출
        youtube_element = row.select_one("div.thumbnail-container > img#thumbnail")
        if youtube_element and "endpoint" in youtube_element.attrs:
            # endpoint 속성에서 URL을 추출
            endpoint = youtube_element["endpoint"]
            # watch?v= 이후의 값을 추출
            youtubeID = endpoint.split("watch?v=")[-1].split('"')[0] if "watch?v=" in endpoint else None
        else:
            youtubeID = None

        # 데이터 저장
        data.append({
            "ranking": ranking,
            "title": title,
            "artist": artist,
            "image": image,
            "prev": prev,
            "streak": streak,
            "streams": streams,
            "youtubeID": youtubeID,
        })

    # JSON 파일로 저장
    with open(json_file_name, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

    # JSON 저장 완료 메시지
    print(f"Data saved in {json_file_name}")

except Exception as e:
    print(f"Error occurred: {e}")

finally:
    # 브라우저 닫기
    browser.quit()
