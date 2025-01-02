import os
import json

# 기본 폴더 경로 및 파일 설정
base_folders = {
    "apple": "./apple",
    "youtube": "./youtube",
    "spotify": "./spotify"
}
output_files = {
    "apple": "listAppleMusic.json",
    "youtube": "listYoutubeMusic.json",
    "spotify": "listSpotifyMusic.json"
}

def process_folder(folder_path, output_file):
    unique_songs = set()  # 중복 제거를 위한 세트
    result_list = []      # 최종 결과 리스트

    # 폴더 내 하위 폴더 순회
    for sub_folder in os.listdir(folder_path):
        sub_folder_path = os.path.join(folder_path, sub_folder)
        if os.path.isdir(sub_folder_path):  # 폴더인지 확인
            # 하위 폴더 내 JSON 파일 순회
            for json_file in os.listdir(sub_folder_path):
                if json_file.endswith(".json"):
                    json_file_path = os.path.join(sub_folder_path, json_file)
                    with open(json_file_path, "r", encoding="utf-8") as file:
                        try:
                            data = json.load(file)
                            for item in data:
                                # 고유한 키 생성 (title, artist, appleID/spotifyID/youtubeID 조합)
                                unique_key = (
                                    item["title"], 
                                    item["artist"], 
                                    item.get("appleID") or item.get("spotifyID") or item.get("youtubeID")
                                )
                                if unique_key not in unique_songs:
                                    unique_songs.add(unique_key)
                                    result_list.append({
                                        "title": item["title"],
                                        "artist": item["artist"],
                                        "id": item.get("appleID") or item.get("spotifyID") or item.get("youtubeID")
                                    })
                        except json.JSONDecodeError as e:
                            print(f"Error reading {json_file_path}: {e}")

    # 결과를 JSON 파일로 저장
    with open(output_file, "w", encoding="utf-8") as outfile:
        json.dump(result_list, outfile, ensure_ascii=False, indent=4)
    print(f"{output_file} 파일이 성공적으로 생성되었습니다!")

# 각 폴더를 처리
for platform, folder_path in base_folders.items():
    if os.path.exists(folder_path):
        process_folder(folder_path, output_files[platform])
    else:
        print(f"{folder_path} 폴더를 찾을 수 없습니다.")
