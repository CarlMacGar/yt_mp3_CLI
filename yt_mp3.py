#!/usr/bin/env python3

""" 
Por si acaso
No quise mover el archivo al bin, sino que hice un wrapper en bin quedando
    /usr/local/bin/ytmp3 <-- (Este es un archivo y el comando)
    Se edita (sudo nano /usr/local/bin/ytmp3)
    y sólo queda con estas dos líneas
        #!/bin/bash
        ~/yt_mp3/yt_mp3.py "$@" <-- Poner la ruta absoluta (Ej: /home/user/escritorio/cositas/yt_mp3/yt_mp3.py "$@")
    Y ya, con eso poniendo en la terminal ytmp3 ya corre

    NOTA: Si quiere cambiar el folder donde descarga, cambiar output_folder
"""

import os
import sys

script_dir = os.path.dirname(__file__)
venv_python = os.path.join(script_dir, "myenv", "bin", "python3")
venv_bin = os.path.join(script_dir, "myenv", "bin")

# relanzar con python del venv si hace falta
if sys.executable != venv_python and os.path.exists(venv_python):
    os.execv(venv_python, [venv_python] + sys.argv)

# añadir binarios del venv al PATH
os.environ["PATH"] = venv_bin + os.pathsep + os.environ.get("PATH", "")

import subprocess
from pathlib import Path

def main():
    print("De YT a MP3")

    yt_url = input("URL de YT: ").strip()

    output_folder = os.path.expanduser("/suite/Music")

    Path(output_folder).mkdir(parents=True, exist_ok=True)

    print(f"Guardando en: {output_folder}")
    print("Descargando...")
    print("Presiona cualquier tecla para cancelar la descarga")

    try:
        command = [
            "yt-dlp",
            "-x", # Obtener audio
            "--audio-format", "mp3", # Formato (MP3)
            "--audio-quality", "0", # 0 - 9 (0 mejor, 9 malita)
            "--embed-thumbnail", # Portada
            "--add-metadata", # Metadatos
            "--output", f'{output_folder}/%(title)s.%(ext)s',
            yt_url
        ]

        result = subprocess.run(command)

        if result.returncode == 0:
            print("Descarga exitosa")
        else:
            print("Error en la descarga") 

    except KeyboardInterrupt:
        print("\nDescarga cancelada")
    except Exception as e:
        print(f'Error: {e}')

if __name__ == "__main__":
    try:
        subprocess.run(["yt-dlp", "--version"],
                        capture_output=True,
                        check=True)
        
        main()
    
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("yt-dlp no está instalado.")
        print("\nPara instalar en Ubuntu:")
        print("1. Opción recomendada (pip):")
        print("   sudo apt update")
        print("   sudo apt install python3-pip ffmpeg")
        print("   pip install yt-dlp")
        print("\n2. Con apt:")
        print("   sudo apt update")
        print("   sudo apt install yt-dlp ffmpeg")
        sys.exit(1)

""" Aquí hay uno que es para descargar playlist de spotify """

# # windows
# import os, subprocess, sys

# yt_url = input("URL de YouTube: ").strip()

# output_folder = os.path.expanduser("/suite/Music/Prueba")
# os.makedirs(output_folder, exist_ok=True)

# command = f'yt-dlp -x --audio-format mp3 --audio-quality 0 --embed-thumbnail --add-metadata --outpput "{output_folder}/%(title)s.%(ext)s" {yt_url}'
# print("Descargando...")
# os.system(command)
# print("Listo")

# # python -m pip install spotdl
# # winget install Gyan.FFmpeg