import subprocess


def download_mp3(url):
    try:
        # yt-dlp 명령어 설정
        command = [
            "yt-dlp",
            "-x",  # 오디오만 추출
            "--audio-format",
            "mp3",  # 오디오 포맷을 MP3로 설정
            "--audio-quality",
            "0",
            url,  # 다운로드할 URL
        ]

        # 명령어 실행
        subprocess.run(command, check=True)
        print(f"MP3 파일이 성공적으로 다운로드되었습니다: {url}")

    except subprocess.CalledProcessError as e:
        print(f"다운로드 중 오류가 발생했습니다: {e}")


# 사용 예시
youtube_url = "https://www.youtube.com/watch?v=1Z_5O2Y6NGM"
download_mp3(youtube_url)
