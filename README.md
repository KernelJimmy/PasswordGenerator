# PasswordGenerator for linux
<h1>Pasos para poder crear la imagen y correr el contenedor</h1>
<ul>
  <li><p>Crea una carpeta en tu sistema linux con el nombre que desees. Allí pasarás todos los ficheros de este proyecto.</p></li>
    <p>Ejecuta este comando en tu sistema:</p>
    <p><i>xhost +</i></p>
    <p>, que retornará;</p>
    <p><i>access control disabled, clients can connect from any host.</i></p>
    <p>Se necesita para conectarse al servidor gráfico desde otro host.</p>
  <li><h2>Descargar el fichero de python</h2></li>
  <p>Descarga el fichero passGen.py y examinaló por si no te fias. Si quieres pega el código en chatGPT y que te diga lo que hace.</p>
</ul>
<p>Una vez que te has descargado el Dockerfile en tu sistema. Puedes correrlo con;</p>
<p><i>$docker build -t [algún_nombre] . </i></p>
<p>Una vez construida la imagen corre el contenedor con el comando;</p>
<p><i>docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -e XAUTHORITY=/Xauthority-file-path def_pyper</i></p>

