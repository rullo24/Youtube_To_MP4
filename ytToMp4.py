from pytube import YouTube
import pathlib


def downloadVideo(url):

    # Create a YouTube object
    yt = YouTube(url)

    # Use the filter method to specify the download format of the video
    ytDownloadFormat = yt.streams.filter(file_extension="mp4")

    # Get the video you want by specifying the resolution
    mp4ResolutionDef = ytDownloadFormat.get_highest_resolution()

    # Getting the location of user's downloads folder
    downloadsPath = pathlib.Path.home() / "Downloads"

    # Save the downloaded video to the local file system
    mp4ResolutionDef.download(downloadsPath)