#!/usr/bin/env bash
echo "nameserver 9.9.9.9" >> /etc/resolv.conf;

echo "Clonando o repositório..."
git clone git@github.com:r3gh/hackathonRioHeatMap.git
cd ~/hackathonRioHeatMap

echo "Instalando dependências do sistema..."
apt-get update
apt-get install -y python3 python3-pip python3-dev build-essential postgresql-9.6

echo "Instalando dependências do Python..."
pip3 install --upgrade pip setuptools
pip3 install --upgrade -r requirements.txt
pip3 install --upgrade -r ott-crawler/requirements.txt

echo "Iniciando componentes..."
./run.sh