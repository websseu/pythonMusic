from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup
from datetime import datetime
import os
import json

# 현재 날짜 가져오기
current_date = datetime.now().strftime("%Y-%m-%d")

# 파일 이름 설정
folder_path = "appleKorea"
filename = f"{folder_path}/{folder_path}100_{current_date}.json"

# 폴더가 없으면 생성
os.makedirs(folder_path, exist_ok=True)

# 웹드라이버 설정 및 페이지 로드
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
except TimeoutException:
    print("요소를 찾는 데 실패했습니다. 페이지가 완전히 로드되지 않았습니다.")
    browser.quit()
    exit()

# 업데이트된 페이지 소스를 변수에 저장
html_source_updated = browser.page_source
soup = BeautifulSoup(html_source_updated, 'html.parser')

# 노래 정보를 추출
song_data = []
songs_list = soup.find_all('div', class_='songs-list-row', role='row')
for song in songs_list:
    ranking = song.find('div', class_='songs-list-row__rank')
    title = song.find('div', class_='songs-list-row__song-name')
    artist_tag = song.find_all('a', {'data-testid': 'click-action'})
    
    # 요소가 존재하는지 확인 후 데이터 추출
    ranking_text = ranking.text.strip() if ranking else "No ranking"
    title_text = title.text.strip() if title else "No title"
    artist_text = artist_tag[0].text.strip() if artist_tag else "No artist"
    album_text = artist_tag[1].text.strip() if len(artist_tag) > 1 else "No album"
    
    # 이미지 URL 추출
    img_tag = song.find('picture').find('source', type="image/webp") if song.find('picture') else None
    if img_tag:
        image_sources = img_tag.get('srcset', "")
        image_url = next((src.split(' ')[0] for src in image_sources.split(',') if '80x80bb.webp' in src), "No image available")
    else:
        image_url = "No image available"
    
    song_data.append({
        'ranking': ranking_text,
        'title': title_text,
        'artist': artist_text,
        'album': album_text,
        'image_url': image_url
    })

# 추출된 데이터를 JSON 파일로 저장
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(song_data, f, ensure_ascii=False, indent=4)
    print(f"데이터가 '{filename}' 파일에 저장되었습니다.")
  
# 브라우저 종료
browser.quit()
