<div>
  <center>
  <img src="docker.png" width="200px" height="200px"><img src="phyton.png" width="200px" height="200px">
  </center>
</div>
# PasswordGenerator for linux
<h2>Pasos para poder crear la imagen y correr el contenedor</h2>
<ul>
  <li><p>Crea una carpeta en tu sistema linux con el nombre que desees. Allí pasarás todos los ficheros de este proyecto.</p></li>
    <p>Ejecuta este comando en tu sistema:</p>
    <p><i>xhost +</i></p>
    <p>, que retornará;</p>
    <p><i>access control disabled, clients can connect from any host.</i></p>
    <p>Se necesita para conectarse al servidor gráfico desde otro host.</p>
  <li>Descarga el fichero passGen.py y examinaló por si no te fias. Si quieres pega el código en chatGPT y que te diga lo que hace.</li>
  <li>Descargar el fichero Dockerfile que como puedes ver no tiene nada raro. Haz lo mismo en chatGPT con este fichero.</li>
  <li>Cuando este todo descargado y en la misma carpeta corre la imagen del Dockerfile con:</li>
  <p>$docker build -t [nombre_que_quieras]</p>
  <li>Una vez que la imagen se ha creado ya puedes correr el contenedor con:</li>
  <p><i>docker run -it --rm -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -e XAUTHORITY=/Xauthority-file-path def_pyper</i></p>
  <p>Ya podrás interactuar con el contenedor y crear tus contraseñas a medida y con la función de dejar copiada la contraseña para guardarla en tu gestor de contraseñas       como por ejemplo Bitwarden.</p>
  <p>https://bitwarden.com/download/</p>
  <li>Disfruta y dame las gracias.</li>
</ul>
