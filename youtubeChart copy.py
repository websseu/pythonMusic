from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from datetime import datetime
from bs4 import BeautifulSoup
import os
import json
import time

# 현재 날짜를 문자열로 저장
current_date = datetime.now().strftime("%Y-%m-%d")

# 파일 이름 설정
folder_path = "youtube"
file_name = f"{folder_path}/youtubeTop100_{current_date}.json"

# 폴더가 없으면 생성
os.makedirs(folder_path, exist_ok=True)

# 웹드라이버 백그라운드 설정 및 페이지 로드
options = ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--disable-infobars")
options.add_argument("--disable-notifications")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36")

browser = webdriver.Chrome(options=options)
browser.get("https://charts.youtube.com/charts/TopSongs/kr/weekly")

# 요소가 로드될 때까지 기다림
try:
    WebDriverWait(browser, 20).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, 'chart-table-container'))
    )
except TimeoutException:
    print("페이지 로드 시간 초과")

# 페이지 소스 다운
detail_page_html = browser.page_source
soup = BeautifulSoup(detail_page_html, 'html.parser')

# # 타이틀 찾기 및 텍스트 추출
# titles = soup.find_all(class_='title style-scope ytmc-entry-row')
# entry_texts = [{"title": entry.get_text(strip=True)} for entry in titles]

# 타이틀 찾기 및 텍스트 추출
titles = soup.find_all(class_='title style-scope ytmc-entry-row')
entry_texts = [{"title": entry.get_text(strip=True)} for entry in titles]


# JSON 파일로 데이터 저장
with open(file_name, 'w', encoding='utf-8') as json_file:
    json.dump(entry_texts, json_file, ensure_ascii=False, indent=4)

print(f"Data saved to {file_name}")

# 브라우저 닫기
browser.quit()
