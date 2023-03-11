from yt_downloader.downloader import YouTubeDownloader
from subprocess import check_output
import click
import re

@click.command(help='A simple CLI application to download video and audio from YouTube.')
@click.argument('url')
@click.option('-a', '--audio', is_flag=True, help='Download audio')
@click.option('-r', '--resolution', default=None, type=int, help='Enter resolution')
def main(url, audio, resolution):
    DOWNLOAD_PATH = check_output(['xdg-user-dir', 'DOWNLOAD']).decode('utf-8').strip()
    youtube_regex = r'^((?:https?:)?\/\/)?((?:www|m)\.)?((?:youtube(-nocookie)?\.com|youtu.be))(\/(?:[\w\-]+\?v=|embed\/|v\/)?)([\w\-]+)(\S+)?$'
    youtube_match = re.match(youtube_regex, url)
    if youtube_match:
        if audio and resolution:
            raise click.BadOptionUsage(option_name='', message='Invalid combination of options.')
        youtube = YouTubeDownloader(url, resolution, DOWNLOAD_PATH)
        if audio:
            youtube.download_audio()
        else:
            youtube.download_video()
    else:
        raise click.BadArgumentUsage(message='Invalid URL.')

if __name__ == '__main__':
    main()