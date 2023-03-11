from setuptools import setup, find_packages

DESCRIPTION = 'A simple CLI application to download video and audio from YouTube.'

setup(
    name='yt-downloader',
    version='0.0.1',
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        'click==8.1.3',
        'pytube==12.1.2'
    ],
    keywords=['python',' youtube', 'video', 'audio'],
    classifiers=[
        'Operating System :: Unix',
        'Programming Language :: Python :: 3'
    ],
    entry_points={
        'console_scripts': [
            'ytd = yt_downloader.main:main'
        ]
    }
)