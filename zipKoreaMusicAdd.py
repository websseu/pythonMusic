import os
import json
import re

# 정규화 함수
def normalize_text(text):
    text = text.lower()  # 소문자로 변환
    text = re.sub(r'[\s,&,]', '', text)  # 공백, &, 쉼표 제거
    text = re.sub(r'\(.*?\)', '', text)  # 괄호 및 괄호 안 내용 제거
    return text.strip()

# koreaMusicList.json 로드 및 매핑 생성
with open('korea/koreaMusicList.json', 'r', encoding='utf-8') as f:
    korea_music_list = json.load(f)

# koreaMusicList.json을 기반으로 매핑 생성
id_mapping = {}
for item in korea_music_list:
    title_artist_key = normalize_text(item['title'] + item['artist'])
    id_mapping[title_artist_key] = {
        'youtubeID': item.get('youtubeID'),
        'spotifyID': item.get('spotifyID'),
        'appleID': item.get('appleID'),
    }

# korea 하위 폴더의 JSON 파일 업데이트
korea_subfolders = [os.path.join('korea', folder) for folder in os.listdir('korea') if os.path.isdir(os.path.join('korea', folder))]

for folder in korea_subfolders:
    for file_name in os.listdir(folder):
        if file_name.endswith('.json'):
            file_path = os.path.join(folder, file_name)
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)

            # 파일 내 항목 업데이트
            for item in data:
                title_artist_key = normalize_text(item['title'] + item['artist'])
                if title_artist_key in id_mapping:
                    # koreaMusicList.json에서 ID 추가
                    for key, value in id_mapping[title_artist_key].items():
                        if value:  # 값이 존재하는 경우만 추가
                            item[key] = value
            
            # 업데이트된 데이터를 JSON 파일에 저장
            with open(file_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)

print("하위 폴더 JSON 파일에 ID 추가 완료!")
