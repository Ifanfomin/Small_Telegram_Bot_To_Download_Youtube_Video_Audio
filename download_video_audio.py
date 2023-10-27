import yt_dlp
import asyncio
import time


async def download_video(url):
    ydl_opts = {
        'format': 'mp4',
        "quiet": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        ydl.process_info(info_dict)
        video_file = ydl.prepare_filename(info_dict)
    return video_file


async def download_audio(url):
    ydl_opts = {
        'format': 'mp3/bestaudio/best',
        # ℹ️ See help(yt_dlp.postprocessor) for a list of available Postprocessors and their arguments
        'postprocessors': [{  # Extract audio using ffmpeg
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
        }]
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=False)
        ydl.process_info(info_dict)
        audio_file = ydl.prepare_filename(info_dict)
    return audio_file

if __name__ == '__main__':

    name = asyncio.run(download_video("https://www.youtube.com/watch?v=XcOHiGonWwU"))
    print(name)
    print("Спимzzzzzzzzzzzzzzzzzzzzzzzz")
    time.sleep(10)
