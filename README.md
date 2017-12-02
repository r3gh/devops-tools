# devops-tools
Coleção de ferramentas de DevOps

## Instalar Vagrant Virtual Box:
- (mac) `brew cask install vagrant virtualbox`
- (ubuntu) `apt-get install vagrant virtualbox`

```
cd devops-tools
vagrant up
vagrant ssh
```

## Para Criar instância:

(Dentro da VM local):
```
python3 tools/criar-instancia.py 
```
A saída vai listar o IP na nuvem. Pegue esse IP.


Primeiro, consertar as permissões:
```
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys 
chmod 644 ~/.ssh/known_hosts 

cd /home/ubuntu/devops-tools
chmod 755 .ssh
chmod 600 .ssh/id_rsa
chmod 644 .ssh/id_rsa.pub 
```

