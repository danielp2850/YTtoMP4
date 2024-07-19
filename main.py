import yt_dlp
import sys


def download_video(url, download_path):
    ydl_opts = {
        'format': 'best',
        'outtmpl': f'{download_path}/%(title)s.%(ext)s',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download successful!")
    except yt_dlp.utils.DownloadError as e:
        print(f"Error: Failed to download video - {e}")
    except Exception as e:
        print(f"Error: An unexpected error occurred - {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <YouTube URL>")
    else:
        url = sys.argv[1]
        download_path = r"C:\YTDOWNLOADS"
        download_video(url, download_path)
