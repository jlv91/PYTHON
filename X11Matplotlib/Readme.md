# Utiliser un serveur X

<br>Installer VcXsrv, lancer le serveurt X
<br>docker build -t matplotlib .
<br>docker run -it --rm -e DISPLAY=192.168.1.148:0.0  matplotlib

Le plot doit s'afficher.