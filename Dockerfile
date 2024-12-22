FROM ubuntu

# Installer Git
RUN apt-get update && apt-get install -y \ 
            git \
            python3 \
            python3-venv \
            python3-pip \
            python3-tk \
            libx11-6 \
            && apt-get clean

# Définir le répertoire de travail dans le conteneur
WORKDIR /

# Cloner le repository en utilisant le token du secret 
# juste pour tester car le token reste dans l'environnement git pour pouvoir y accéder
RUN --mount=type=secret,id=GITHUB_TOKEN git clone  https://$(cat /run/secrets/GITHUB_TOKEN)@github.com/jlv91/PYTHON.git

WORKDIR /PYTHON 

# git config local
ARG USER_NAME
ARG USER_EMAIL
RUN git config user.name $USER_NAME
RUN git config user.email $USER_EMAIL

# Python Virtual Env
ENV VIRTUAL_ENV=/.venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install -r requirements.txt

CMD ["bash"]