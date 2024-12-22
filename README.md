# Developper avec Python dans un container Docker

Le Dockerfile part d'une image Ubuntu (et non Python).
<br>Il installe  git, python3, python3-venv, python3-pip, python3-tk, libx11-6.

Il clone le repo Git, et le configure.
Il crée un environnement virtuel et installe les dépendances de requirements.txt.

Pour créer le container:
<br>
<code>docker build --secret id=GITHUB_TOKEN,src=GITHUB_TOKEN --build-arg USER_NAME=$USER_NAME --build-arg USER_EMAIL=$USER_EMAIL -t python-dev .</code>



Pour exécuter le container:
<br>
<code>docker run -it --rm -e DISPLAY=192.168.1.148:0.0 python-dev</code>
<li>Le serveur X doit être lancé pour afficher les fenêtres matplotlib.
<li>Attacher VsCode au container
<li>Laisser VsCode installer les extensions nécessaires au développement Python comme Jupyter, Pylance
