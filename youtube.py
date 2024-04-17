from pytube import YouTube

#very basic 2d graphics, build into python
import tkinter as tk
from tkinter import filedialog

def download_video(url,save_path):
    try:
        yt = YouTube(url)
        # get the stas about the video

        # download on highest resolution
        streams = yt.streams.filter(progressive = True, file_extension = 'mp4')
        highest_res_stream = streams.get_highest_resolution()
        highest_res_stream.download(output_path = save_path)
        print("Video downloaded Successfully!")

    except Exception as e:
        print(e)

# url = "https://www.youtube.com/watch?v=Rw1r5GRKpqY&list=RDRw1r5GRKpqY&index=1"
# save_path = "C:\yt_vid_download"

# download_video(url,save_path)

# user friendly, dont ahve to type the url and path
def open_file_dialog():
    folder = filedialog.askdirectory()
    if folder:
        print(f"Selected folder: {folder}")
    return folder



if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()

    video_url = input("Please enter a youtube url: ")

    # switch if you want to change the directory
    # save_dir = open_file_dialog()

    # directory to hard disk
    # save_dir = "D:\yt_vid_download"

    # direcotry to the project in laptop
    # save_dir = r"C:\Users\jovin\Desktop\pythonProj\yt_Vid_downloader\ytVidDownloader"

    if not save_dir:
        print("Invalid location ...")
    else:
        print("Started downloading video")
        download_video(video_url,save_dir)