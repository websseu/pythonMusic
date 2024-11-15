import json
import os
import glob

# 파일 경로 설정
file1_path = "korea/totalKoreaMusic.json"
folder_paths = ["korea/apple", "korea/bugs", "korea/flo", "korea/genie", "korea/melon", "korea/vibe"]

try:
    # 첫 번째 파일 로드
    data1 = []
    if os.path.exists(file1_path):
        with open(file1_path, "r", encoding="utf-8") as file1:
            data1 = json.load(file1)
        print(f"{file1_path} 로드 성공! 데이터 개수: {len(data1)}")
    else:
        print(f"{file1_path} 파일이 존재하지 않습니다.")
        data1 = []

    # 첫 번째 파일의 title, artist, youtubeID 매핑 생성
    youtube_id_map = {
        (item.get("title"), item.get("artist")): item.get("youtubeID")
        for item in data1
        if "youtubeID" in item and item["youtubeID"]
    }

    # 여러 폴더 내 모든 JSON 파일 처리
    for folder_path in folder_paths:
        print(f"처리 중인 폴더: {folder_path}")
        json_files = glob.glob(os.path.join(folder_path, "*.json"))

        if not json_files:
            print(f"{folder_path} 폴더에 JSON 파일이 없습니다.")
            continue

        for file_path in json_files:
            print(f"처리 중: {file_path}")

            # JSON 파일 로드
            with open(file_path, "r", encoding="utf-8") as file:
                data2 = json.load(file)

            # 두 번째 파일에서 동일한 title과 artist를 가진 항목에 youtubeID 추가
            updated_data = []
            for item in data2:
                title_artist = (item.get("title"), item.get("artist"))
                if title_artist in youtube_id_map:
                    item["youtubeID"] = youtube_id_map[title_artist]
                updated_data.append(item)

            # 업데이트된 데이터를 해당 파일에 저장
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(updated_data, file, ensure_ascii=False, indent=4)
            print(f"{file_path} 파일에 youtubeID가 추가되었습니다!")

except Exception as e:
    print(f"파일을 처리하는 중 오류 발생: {e}")
