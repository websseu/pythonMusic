import requests
from bs4 import BeautifulSoup
from datetime import datetime
import json
import os

# 현재 날짜를 문자열로 저장
current_date = datetime.now().strftime("%Y-%m-%d")

# 파일 이름 설정
folder_path = "melon"
file_name = f"{folder_path}/{folder_path}100_{current_date}.json"

# 폴더가 없으면 생성
os.makedirs(folder_path, exist_ok=True)

# 웹 페이지로부터 데이터 요청 및 수신(웹 서버가 자동 스크립트를 막아놓은 경우 우회할 때 사용)
head = {'User-Agent' : 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
res = requests.get("https://www.melon.com/chart/index.htm", headers=head)
soup = BeautifulSoup(res.text, "lxml")

# print(res.text)
# print(res.status_code) 

# 데이터 선택
ranking = soup.select("tbody .wrap.t_center > .rank")
title = soup.select("tbody .wrap_song_info .ellipsis.rank01 span > a")
artist = soup.select("tbody .wrap_song_info .ellipsis.rank02 span > a:nth-child(1)")
image = soup.select("tbody .image_typeAll > img")
album = soup.select("tbody .wrap_song_info .ellipsis.rank03 > a")

# print(len(title))

# 데이터 저장
rankings = [r.text.strip() for r in ranking]
titles = [t.text.strip() for t in title]
artists = [a.text.strip() for a in artist]
images = [i.get('src') for i in image]
albums = [a.text.strip() for a in album]

# 데이터 프레임 생성
chart_data = []
for ranking, title, artist, image_url, album in zip(rankings, titles, artists, images, albums):
    chart_data.append({
        "ranking": ranking,
        "title": title,
        "artist": artist,
        "imageURL": image_url,
        "album": album
    })

# 추출된 데이터를 JSON 파일로 저장
with open(file_name, 'w', encoding='utf-8') as f:
    json.dump(chart_data, f, ensure_ascii=False, indent=4)
    print(f"데이터가 '{file_name}' 파일에 저장되었습니다.")