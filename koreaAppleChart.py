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
import re

def generate_title_id(title, appleID):
    # 1. 괄호를 제거하고 괄호 안의 내용은 유지
    title = re.sub(r'\(|\)', '', title)
    # 2. 제목을 소문자로 변환
    title = title.lower()
    # 3. 앰퍼샌드(&)를 하이픈(-)으로 변환
    title = title.replace('&', '-')
    # 4. 빈칸을 '-'로 대체
    title = title.replace(' ', '-')
    # 5. 허용된 문자(영숫자, 하이픈)만 남기기
    title = re.sub(r'[^\w\-]', '', title)
    # 6. 연속된 하이픈을 단일 하이픈으로 변경
    title = re.sub(r'-+', '-', title)
    # 7. 제목과 ID를 "/"로 결합
    return f"{title}/{appleID}"

# 현재 날짜를 문자열로 저장
current_date = datetime.now().strftime("%Y-%m-%d")

# 파일 이름 설정
folder_path = "korea/apple"
file_name = f"{folder_path}/appleTop100_{current_date}.json"

# 폴더가 없으면 생성
os.makedirs(folder_path, exist_ok=True)

# 웹드라이버 백그라운드 설정 및 페이지 로드
options = ChromeOptions()
options.add_argument("--headless")
browser = webdriver.Chrome(options=options)
browser.get("https://music.apple.com/kr/playlist/%EC%98%A4%EB%8A%98%EC%9D%98-top-100-%EB%8C%80%ED%95%9C%EB%AF%BC%EA%B5%AD/pl.d3d10c32fbc540b38e266367dc8cb00c")

# 페이지가 완전히 로드될 때까지 대기
try:
    WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "songs-list"))
    )
    print("페이지가 완전히 로드되었습니다.")
    time.sleep(3)
except TimeoutException:
    print("요소를 찾는 데 실패했습니다. 페이지가 완전히 로드되지 않았습니다.")
    browser.quit()
    exit()

# 업데이트된 페이지 소스를 변수에 저장
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
    song_link = track.select_one(".songs-list-row__song-name-wrapper a")["href"] if track.select_one(".songs-list-row__song-name-wrapper a") else None
    appleID = song_link.split("/")[-1] if song_link else None

    # 제목과 ID를 규칙에 따라 변환
    title_id = generate_title_id(title, appleID) if title and appleID else None


    # 수집된 정보를 딕셔너리에 저장
    chart_data.append({
        "ranking": ranking,
        "title": title,
        "artist": artist,
        "image": image,
        "appleID": title_id
    })

# 추출된 데이터를 JSON 파일로 저장
with open(file_name, 'w', encoding='utf-8') as f:
    json.dump(chart_data, f, ensure_ascii=False, indent=4)
    print(f"데이터가 '{file_name}' 파일에 저장되었습니다.")
  
# 브라우저 종료
browser.quit()
