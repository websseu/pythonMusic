import json
import re
from collections import defaultdict

# 괄호와 공백을 제거하고 소문자로 변환하는 함수
def normalize(text):
    return re.sub(r'\([^)]*\)', '', text).replace(' ', '').lower()

# 3개의 파일에서 데이터를 읽어오기
files = ['listAppleMusic.json', 'listSpotifyMusic.json', 'listYoutubeMusic.json']
merged_data = defaultdict(lambda: {"title": None, "artist": None, "ids": []})

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        data = json.load(f)
        for song in data:
            title = song['title']
            artist = song['artist']
            song_id = song['id']
            
            # Normalize title and artist
            normalized_key = (normalize(title), normalize(artist))
            
            # 통합 데이터에 추가
            if not merged_data[normalized_key]["title"]:
                merged_data[normalized_key]["title"] = title
                merged_data[normalized_key]["artist"] = artist
            merged_data[normalized_key]["ids"].append(song_id)

# 결과를 리스트 형태로 변환
result = [{"title": item["title"], "artist": item["artist"], "ids": item["ids"]} for item in merged_data.values()]

# 결과 저장
with open('merged_music_list.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)

print("통합 완료! 결과는 merged_music_list.json에 저장되었습니다.")
