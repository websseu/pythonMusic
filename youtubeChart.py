from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from bs4 import BeautifulSoup
import os
import json
import time
from datetime import datetime

# 현재 날짜를 문자열로 저장
current_date = datetime.now().strftime("%Y-%m-%d")

# 파일 이름 설정
folder_path = "youtube"
html_file_name = f"{folder_path}/youtubeTop100_{current_date}.html"
json_file_name = f"{folder_path}/youtubeTop100_{current_date}.json"

# 폴더가 없으면 생성
os.makedirs(folder_path, exist_ok=True)

# 웹드라이버 설정 및 페이지 로드
options = ChromeOptions()
options.add_argument("--headless")  # 백그라운드 실행
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# 크롬 웹드라이버로 YouTube 차트 페이지 열기
browser = webdriver.Chrome(options=options)
browser.get("https://charts.youtube.com/charts/TopSongs/kr/weekly")
time.sleep(20)  # 페이지가 로드될 때까지 대기

# 페이지 소스를 HTML 파일로 저장
with open(html_file_name, 'w', encoding='utf-8') as file:
    file.write(browser.page_source)

# 브라우저 닫기
browser.quit()

print(f"HTML 파일이 {html_file_name}로 저장되었습니다.")

# 저장된 HTML 파일을 열어 BeautifulSoup으로 파싱
with open(html_file_name, 'r', encoding='utf-8') as file:
    soup = BeautifulSoup(file, 'html.parser')

# 순위, 제목, 가수 정보 추출
songs = []

# 각 곡 정보를 담고 있는 요소를 찾기
entries = soup.find_all('ytmc-entry-row')  # 예시로 작성된 코드입니다. 실제 태그와 클래스를 확인해 수정해야 합니다.

# 실제 HTML 구조를 확인하고 맞는 태그와 클래스로 수정해주세요
for entry in entries:
    rank_tag = entry.find('span', {'id': 'rank'})  # 순위 태그 확인 필요
    title_tag = entry.find('span', {'class': 'title'})  # 제목 태그 확인 필요
    artist_tag = entry.find('span', {'class': 'subtitle'})  # 가수 태그 확인 필요

    rank = rank_tag.get_text(strip=True) if rank_tag else None
    title = title_tag.get_text(strip=True) if title_tag else None
    artist = artist_tag.get_text(strip=True) if artist_tag else None

    # 모든 정보가 있는 경우 리스트에 추가
    if rank and title and artist:
        songs.append({
            'rank': rank,
            'title': title,
            'artist': artist
        })

# 결과를 JSON 파일로 저장
with open(json_file_name, 'w', encoding='utf-8') as json_file:
    json.dump(songs, json_file, ensure_ascii=False, indent=4)

print(f"Top 100 songs saved to {json_file_name}")
