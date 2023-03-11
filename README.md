# YouTube Downloader

Aplicación de terminal para descargar video y audio de YouTube.

## Instalación

La aplicación es para sistemas UNIX y usa FFmpeg para procesamiento de video y audio.

Para instalar FFmpeg en distribuciones basadas en Debian:

```bash
sudo apt update
sudo apt install ffmpeg
```

Para distribuciones basadas en arch:

```bash
pacman -Syu
pacman -S ffmpeg
```

Ejecutar setup.py e instalar el paquete con PIP.

## Sintaxis

Descargar video:

```bash
ytd https://www.youtube.com/watch?v=dQw4w9WgXcQ
```

Descargar audio:

```bash
ytd https://www.youtube.com/watch?v=dQw4w9WgXcQ -a
```

Descargar video con resolución especifica:

```bash
ytd https://www.youtube.com/watch?v=dQw4w9WgXcQ -r 1080
```