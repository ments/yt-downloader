from subprocess import Popen, PIPE, run
from tempfile import NamedTemporaryFile
from pytube import YouTube
from io import BytesIO
import os

class YouTubeDownloader():

    def __init__(
        self,
        url: str,
        resolution: int,
        path: str
    ):
        self.youtube_video: object = YouTube(url)
        self.resolution: int = resolution
        self.path: str = path
    
    def download_video(self) -> None:
        if self.resolution:
            stream = self.get_stream()
            if stream is not None:
                if not stream.is_progressive:
                    self.merge_streams(stream)
                    return None
            else:
                return None
        else:
            stream = self.youtube_video.streams.get_highest_resolution()
        stream.download(self.path, filename=f'{self.youtube_video.title}.mp4')
    
    def get_stream(self) -> object or None:
        streams = self.youtube_video.streams.filter(res=f'{self.resolution}p', mime_type='video/mp4')
        if streams:
            progressive_streams = streams.filter(progressive=True)
            if progressive_streams:
                return progressive_streams.first()
            else:
                dash_stream = streams.filter(progressive=False).first()
                return dash_stream
        else:
            return None
    
    def merge_streams(self, stream: object) -> None:
        video_buffer = BytesIO()
        stream.stream_to_buffer(video_buffer)
        audio_bytes = self.convert_to_mp3()

        with NamedTemporaryFile(suffix='.mp4') as video_tmp_file, NamedTemporaryFile(suffix='.mp3') as audio_tmp_file:
            video_tmp_file.write(video_buffer.getvalue())
            audio_tmp_file.write(audio_bytes)
            command = [
                'ffmpeg',
                '-i', video_tmp_file.name,
                '-i', audio_tmp_file.name,
                '-loglevel', 'quiet',
                '-c:v', 'copy',
                '-c:a', 'aac',
                os.path.join(self.path, f'{self.youtube_video.title}.mp4')
            ]
            run(command)

    def convert_to_mp3(self) -> bytes or None:
        stream = self.youtube_video.streams.get_lowest_resolution()
        buffer = BytesIO()
        stream.stream_to_buffer(buffer)
        buffer.seek(0)

        command = [
            'ffmpeg',
            '-i', 'pipe:0',
            '-f', 'mp3',
            '-'
        ]
        process = Popen(command, stdin=PIPE, stdout=PIPE, stderr=PIPE)
        output, error = process.communicate(input=buffer.read())

        if process.returncode == 0:
            return output
    
    def download_audio(self) -> None:
        audio_bytes = self.convert_to_mp3()
        with open(os.path.join(self.path, f'{self.youtube_video.title}.mp3'), mode='wb') as f:
            f.write(audio_bytes)