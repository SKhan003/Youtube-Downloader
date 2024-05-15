from pytube import YouTube
import os

link = input("Enter Your Link Here: ")
check = input("Press 1 for video and 2 for audio: ")

def get_download_path():
    download_path = input("Enter the path where you want to download: ")
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    return download_path

if check == "1":
    youtube_1 = YouTube(link)
    videos = youtube_1.streams.filter(progressive=True)
    vid = list(enumerate(videos))
    for i in vid:
        print(i)
    strm = int(input("Please provide which stream you want to download: "))
    download_path = get_download_path()
    videos[strm].download(download_path)
    print("Video successfully downloaded.")

elif check == "2":
    youtube_1 = YouTube(link)
    audio = youtube_1.streams.filter(only_audio=True)
    aud = list(enumerate(audio))
    for i in aud:
        print(i)
    strm = int(input("Please provide which stream you want to download audio: "))
    download_path = get_download_path()
    audio[strm].download(download_path)
    print("Audio successfully downloaded.")

else:
    print("Invalid choice. Please choose 1 for video or 2 for audio.")

