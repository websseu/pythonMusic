import json
import re

# 정규화 함수
def normalize_text(text):
    text = text.lower()  # 소문자로 변환
    text = re.sub(r'[\s,&,]', '', text)  # 공백, &, 쉼표 제거
    text = re.sub(r'\(.*?\)', '', text)  # 괄호 및 괄호 안 내용 제거
    return text.strip()

# 특정 파일의 ID 매핑 생성
def create_id_mapping(file_path, id_field):
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    mapping = {}
    for item in data:
        title_artist_key = normalize_text(item['title'] + item['artist'])
        mapping[title_artist_key] = item.get(id_field)
    return mapping

# koreaMusicList.json 파일 로드
with open('korea/koreaMusicList.json', 'r', encoding='utf-8') as f:
    korea_music_list = json.load(f)

# Apple, YouTube, Spotify ID 매핑 생성
apple_id_mapping = create_id_mapping('korea/koreaMusicListApple.json', 'appleID')
youtube_id_mapping = create_id_mapping('korea/koreaMusicListYoutube.json', 'youtubeID')
spotify_id_mapping = create_id_mapping('korea/koreaMusicListSpotify.json', 'spotifyID')

# koreaMusicList.json 업데이트
for item in korea_music_list:
    title_artist_key = normalize_text(item['title'] + item['artist'])
    
    # Apple ID 추가
    if title_artist_key in apple_id_mapping:
        item['appleID'] = apple_id_mapping[title_artist_key]
    
    # YouTube ID 추가
    if title_artist_key in youtube_id_mapping:
        item['youtubeID'] = youtube_id_mapping[title_artist_key]
    
    # Spotify ID 추가
    if title_artist_key in spotify_id_mapping:
        item['spotifyID'] = spotify_id_mapping[title_artist_key]

# 업데이트된 koreaMusicList.json 저장
with open('korea/koreaMusicList.json', 'w', encoding='utf-8') as f:
    json.dump(korea_music_list, f, ensure_ascii=False, indent=4)

print("appleID, youtubeID, spotifyID 추가 작업 완료!")
