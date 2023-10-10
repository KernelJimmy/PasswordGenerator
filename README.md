# PasswordGenerator for linux
<p>Antes de buildear este Dockerfile en vuestra máquina linux tebdréis que correr este comando;</p>
<p><i>xhost +</i></p>
<p>, que retornará;</p>
<p><i>access control disabled, clients can connect from any host.</i></p>
<p>Se necesita para conectarse al servidor gráfico desde otro host.</p>
<p>Descarga el fichero passGen.py y examinaló por si no te fias.</p>

<p>Una vez que te has descargado el Dockerfile en tu sistema. Puedes correrlo con;</p>
<p><i>$docker build -t <algún_nombre> . </i></p>
<p>Una vez construida la imagen corre el contenedor con el comando;</p>
<p><i>docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -e XAUTHORITY=/Xauthority-file-path def_pyper</i></p>

