import os
import json

# Apple 폴더의 경로를 지정하세요.
apple_folder = "apple"

# 병합된 데이터를 저장할 폴더와 파일 경로
output_folder = "json"
output_file = os.path.join(output_folder, "appleChange.json")

# 병합 데이터를 저장할 리스트
merged_data = []

# 폴더 생성 (존재하지 않으면 생성)
os.makedirs(output_folder, exist_ok=True)

# 모든 JSON 파일을 처리
for country in os.listdir(apple_folder):
    country_folder = os.path.join(apple_folder, country)

    if os.path.isdir(country_folder):  # 나라별 폴더만 처리
        for json_file in os.listdir(country_folder):
            if json_file.endswith(".json"):
                input_path = os.path.join(country_folder, json_file)

                # JSON 파일 읽기
                with open(input_path, "r", encoding="utf-8") as f:
                    data = json.load(f)

                # 데이터 변환 및 병합
                transformed_data = [
                    {
                        "title": item.get("title", ""),
                        "artist": item.get("artist", ""),
                        "image": item.get("image", ""),
                        "youtubeID": "",  # Apple 데이터에 youtubeID가 없으므로 빈 값 설정
                        "spotifyID": "",  # 추가 데이터가 없으므로 빈 값 설정
                        "appleID": item.get("appleID", "")
                    }
                    for item in data
                ]
                merged_data.extend(transformed_data)

# 중복 제거
unique_data = {}
for item in merged_data:
    key = (item["title"], item["artist"])
    if key not in unique_data:  # 새로운 (title, artist) 조합만 추가
        unique_data[key] = item

# 중복이 제거된 데이터를 리스트로 변환
deduplicated_data = list(unique_data.values())

# 병합된 데이터를 하나의 JSON 파일로 저장
with open(output_file, "w", encoding="utf-8") as f:
    json.dump(deduplicated_data, f, ensure_ascii=False, indent=4)

print(f"Deduplicated data saved to: {output_file}")
print(f"Total entries after deduplication: {len(deduplicated_data)}")
