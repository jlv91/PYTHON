FROM python:3.10-slim

# Installer les dépendances
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-tk \
    libx11-6 \
    && apt-get clean

# Installer matplotlib
RUN pip install matplotlib

# Définir le répertoire de travail
WORKDIR /app

# Copier le code source
COPY TestMatplotlibX11.py  .

# Commande par défaut
CMD ["python", "TestMatplotlibX11.py"]
