import os
import json
import re

# JSON 파일 경로
input_folder = "json"
youtube_file = os.path.join(input_folder, "youtubeChange.json")
spotify_file = os.path.join(input_folder, "spotifyChange.json")
apple_file = os.path.join(input_folder, "appleChange.json")
output_file = os.path.join(input_folder, "totalChange.json")

# 불필요한 텍스트 제거 및 소문자로 변환 함수
def clean_text(text):
    return re.sub(r"\(.*?\)", "", text).strip().lower()

# 아티스트 이름 정규화
def normalize_artist(artist):
    # ,와 &를 쉼표로 변환, and도 쉼표로 변환
    artist = re.sub(r"\s*[&and]\s*", ",", artist, flags=re.IGNORECASE)
    # 쉼표로 나눈 뒤 개별 이름을 소문자로 정렬
    artist_list = sorted([name.strip().lower() for name in artist.split(",")])
    return ",".join(artist_list)

# JSON 파일 읽기
def load_json(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

# 데이터 병합
def merge_data(youtube_data, spotify_data, apple_data):
    combined_data = {}

    # 유튜브 데이터 우선 추가
    for item in youtube_data:
        key = (clean_text(item["title"]), normalize_artist(item["artist"]))
        combined_data[key] = {
            "title": item["title"],
            "artist": item["artist"],
            "image": item["image"],
            "youtubeID": item["youtubeID"],
            "spotifyID": "",
            "appleID": "",
        }

    # Spotify 데이터 병합
    for item in spotify_data:
        key = (clean_text(item["title"]), normalize_artist(item["artist"]))
        if key not in combined_data:
            combined_data[key] = {
                "title": item["title"],
                "artist": item["artist"],
                "image": "",  # 유튜브 데이터가 없으므로 이미지 없음
                "youtubeID": "",
                "spotifyID": item["spotifyID"],
                "appleID": "",
            }
        else:
            combined_data[key]["spotifyID"] = item["spotifyID"]

    # Apple 데이터 병합
    for item in apple_data:
        key = (clean_text(item["title"]), normalize_artist(item["artist"]))
        if key not in combined_data:
            combined_data[key] = {
                "title": item["title"],
                "artist": item["artist"],
                "image": "",  # 유튜브 데이터가 없으므로 이미지 없음
                "youtubeID": "",
                "spotifyID": "",
                "appleID": item["appleID"],
            }
        else:
            combined_data[key]["appleID"] = item["appleID"]

    return list(combined_data.values())

# JSON 파일 저장
def save_json(data, file_path):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

# 실행
def main():
    # JSON 파일 로드
    youtube_data = load_json(youtube_file)
    spotify_data = load_json(spotify_file)
    apple_data = load_json(apple_file)

    # 데이터 병합
    merged_data = merge_data(youtube_data, spotify_data, apple_data)

    # 결과 저장
    save_json(merged_data, output_file)

    print(f"Merged data saved to: {output_file}")
    print(f"Total entries after merging: {len(merged_data)}")

if __name__ == "__main__":
    main()
