import json
import os
import glob
import re

# 파일 경로 설정
file1_path = "apple/totalAppleMusic.json"
base_folder_path = "apple"  # apple 폴더를 기준으로 모든 하위 폴더 처리

# 표준화 함수: 공백 제거, 소문자 변환, 특수 문자 제거
def standardize(text):
    if not text:
        return ""
    # ()와 그 안의 내용을 제거, 이후 특수 문자와 공백 제거, 소문자 변환
    text = re.sub(r"\([^)]*\)", "", text)  # ()와 그 안의 내용을 제거
    return re.sub(r"[&,. ]+", "", text).lower()  # 공백 및 다른 특수 문자 제거

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
        (standardize(item.get("title")), standardize(item.get("artist"))): item.get("youtubeID")
        for item in data1
        if "youtubeID" in item and item["youtubeID"]
    }

    # apple 폴더 안의 모든 하위 폴더의 JSON 파일 처리
    json_files = glob.glob(os.path.join(base_folder_path, "**", "*.json"), recursive=True)

    if not json_files:
        print(f"{base_folder_path} 폴더에 JSON 파일이 없습니다.")
    else:
        print(f"{len(json_files)}개의 JSON 파일 발견!")

    for file_path in json_files:
        print(f"처리 중: {file_path}")

        # JSON 파일 로드
        with open(file_path, "r", encoding="utf-8") as file:
            data2 = json.load(file)

        # 두 번째 파일에서 동일한 title과 artist를 가진 항목에 youtubeID 추가
        updated_data = []
        for item in data2:
            title_artist = (standardize(item.get("title")), standardize(item.get("artist")))
            if title_artist in youtube_id_map:
                item["youtubeID"] = youtube_id_map[title_artist]
            updated_data.append(item)

        # 업데이트된 데이터를 해당 파일에 저장
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(updated_data, file, ensure_ascii=False, indent=4)
        print(f"{file_path} 파일에 youtubeID가 추가되었습니다!")

except Exception as e:
    print(f"파일을 처리하는 중 오류 발생: {e}")
