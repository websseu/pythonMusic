from datetime import datetime
from bs4 import BeautifulSoup
import os
import requests
import json

# 현재 날짜를 문자열로 저장
current_date = datetime.now().strftime("%Y-%m-%d")

# 파일 이름 설정
folder_path = "billboard/global"
file_name = f"{folder_path}/globalTop100_{current_date}.json"

# 폴더가 없으면 생성
os.makedirs(folder_path, exist_ok=True)

# 웹 페이지로부터 데이터 요청 및 수신
res = requests.get("https://www.billboard.com/charts/billboard-global-200/")
soup = BeautifulSoup(res.text, "lxml")

# print(res.text)
# print(res.status_code)

# 데이터 선택
ranking = soup.select(".o-chart-results-list-row-container > ul > li.o-chart-results-list__item:nth-child(1) > span.c-label:nth-child(1)")
title = soup.select(".o-chart-results-list-row-container > ul > li.lrv-u-width-100p > ul > li:nth-child(1) > h3.c-title")
artist = soup.select(".o-chart-results-list-row-container > ul > li.lrv-u-width-100p > ul > li:nth-child(1) > span.c-label")
image = soup.select(".o-chart-results-list-row-container ul > li:nth-child(2) .c-lazy-image > div > img")

# print(len(title))

# 데이터 저장
rankings = [r.text.strip() for r in ranking]
titles = [t.text.strip() for t in title]
artists = [a.text.strip() for a in artist]
images = [img.get('data-src') or img.get('data-lazy-src') or img.get('src') for img in image]

# 데이터 프레임 생성
chart_data = []
for ranking, title, artist, image_url in zip(rankings, titles, artists, images):
    chart_data.append({
        "ranking": ranking,
        "title": title,
        "artist": artist,
        "imageURL": image_url
    })

# 추출된 데이터를 JSON 파일로 저장
with open(file_name, 'w', encoding='utf-8') as f:
    json.dump(chart_data, f, ensure_ascii=False, indent=4)
    print(f"데이터가 '{file_name}' 파일에 저장되었습니다.")