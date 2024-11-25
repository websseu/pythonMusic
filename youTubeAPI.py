import json
from googleapiclient.discovery import build
import os

# API 키 설정
# YOUTUBE_API_KEY = 'AIzaSyDY-NgoHIzYgtpSpeXfGuMqsvFx4XoiNQk'
YOUTUBE_API_KEY = 'AIzaSyDXH12UjWwEep8Qj4LNC2BPp3ZsdxqU_l4'
youtube = build('youtube', 'v3', developerKey=YOUTUBE_API_KEY)

def get_youtube_video_id(title, artist):
    """제목과 아티스트로 YouTube 영상 ID 검색"""
    query = f"{title} {artist}"
    response = youtube.search().list(
        q=query,
        part="id,snippet",
        maxResults=1,
        type="video"
    ).execute()
    
    # 검색 결과가 없을 경우 None 반환
    if not response["items"]:
        return None

    # 첫 번째 검색 결과의 videoId 반환
    return response["items"][0]["id"]["videoId"]

def add_youtube_ids_to_json(file_path):
    """JSON 파일에서 타이틀과 아티스트 및 YouTube ID만 추가하여 새 파일 저장"""
    try:
        # 파일 읽기
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        # 새로운 데이터 리스트 생성 (타이틀, 아티스트, YouTube ID만 포함)
        new_data = []
        for entry in data:
            title = entry.get("title")
            artist = entry.get("artist")
            if title and artist:
                youtube_id = get_youtube_video_id(title, artist)
                new_entry = {
                    "title": title,
                    "artist": artist,
                    "youtubeID": youtube_id
                }
                new_data.append(new_entry)

        # 새로운 파일 경로 설정 (상위 폴더에 저장)
        output_file_path = os.path.join(os.path.dirname(file_path), "../totalAppleMusic.json")
        output_file_path = os.path.normpath(output_file_path)
        
        # 파일 저장
        with open(output_file_path, 'w', encoding='utf-8') as file:
            json.dump(new_data, file, ensure_ascii=False, indent=4)
        
        print(f"Updated JSON saved to {output_file_path}")
        return output_file_path

    except Exception as e:
        print(f"Error: {e}")
        return None

# 실행 예제
output_file = add_youtube_ids_to_json("apple/australia/australiaTop100_2024-11-24.json")

if output_file:
    print(f"작업이 완료되었습니다! 결과 파일: {output_file}")
