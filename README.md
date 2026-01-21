# YT-MP3 CLI

De URLs de YouTube a MP3 utilizando 'yt-dlp'

## Instalación

```bash
git clone https://github.com/TuUsuario/yt_mp3_CLI.git
cd yt_mp3_CLI

python3 -m venv myenv
source myenv/bin/activate

pip install -r requirements.txt
```

***Nota***: Necesitas `ffmpeg` instalado en el sistema

En ubuntu
~~~bash
sudo apt install ffmpeg
~~~

## Configuración previa
En el archivo `yt_mp3.py` cambia la ubicación donde desees que se descarguen los MP3 editanto la variable `output_folder`

~~~bash
output_folder = "/ruta/deseada"
~~~

## Uso
### Opción 1 - Ejecutarlo directamente

Una vez descargadas las dependencias en el entorno virtual se puede desactivar sin problema y ejecutar el programa con:
~~~bash
python3 yt_mp3.py
~~~

### Opción 2 - Ejecutarlo como comando global
Para ejecutarlo desde cualquier parte del sistema, se crea un wrapper para sistema. Ej:
~~~bash
sudo nano /usr/local/bin/ytmp3
~~~
***Nota***: El nombre al final es como se va a llamar el comando con el que llamaremos la herramienta, puedes ponerle como gustes :DD

Y Dentro del archivo va lo siguiente:
~~~bash
#!/bin/bash
/ruta/absoluta/.../yt_mp3_CLI/yt_mp3.py "$@"
~~~
**`Tip`**: puedes obtener la ruta absoluta con `pwd`

Finalmente le das permisos de ejecución:
~~~bash
sudo chmod +x /usr/local/bin/ytmp3
~~~

Con esto ya puedes ejecutar ytmp3 (O el nombre que hayas elegido) desde cualquier lugar (;