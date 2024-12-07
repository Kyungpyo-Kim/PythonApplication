import re

import requests
from bs4 import BeautifulSoup


def extract_mp3_urls_from_soup(soup):
    print(soup)
    page_text = str(soup)
    prefix_name = "podbbag"
    if "mp3" in page_text:
        print("mp3!!")
        title_tag = soup.find("meta", property="og:title")
        if title_tag and title_tag.get("content"):
            prefix_name = title_tag["content"]
            prefix_name = prefix_name.replace(" ", "_")
    else:
        print(page_text)
    mp3_url = re.findall(r'https:[^"]+\.mp3', page_text)
    return mp3_url, prefix_name


def find_mp3_links(url):
    try:
        # 요청을 보내고 페이지 소스 가져오기
        response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()
        html_content = response.text
        # BeautifulSoup로 HTML 파싱
        soup = BeautifulSoup(html_content, "html.parser")
        return extract_mp3_urls_from_soup(soup)

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []


def download_mp3(url, save_path):
    try:
        # 파일 다운로드 요청
        response = requests.get(url, stream=True)
        response.raise_for_status()  # 요청에 오류가 있는지 확인
        # 다운로드한 파일을 저장
        with open(save_path, "wb") as file:
            for chunk in response.iter_content(
                chunk_size=8192
            ):  # 데이터를 청크 단위로 읽음
                if chunk:
                    file.write(chunk)
        print(f"File downloaded successfully: {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")


# 테스트 URL
url = (
    "https://www.podbbang.com/channels/7210/episodes/24414229"  # 여기에 원하는 URL 입력
)
mp3_files, name = find_mp3_links(url)

if mp3_files:
    print("MP3 Files found:")
    print(mp3_files)

    for i, f in enumerate(mp3_files):
        f = f.replace("\\u002F", "/")
        print(f)
        download_mp3(f, f"{name}_{i}.mp3")
else:
    print("No MP3 files found.")
