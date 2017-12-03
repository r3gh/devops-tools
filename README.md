# devops-tools
Coleção de ferramentas de DevOps

## Ambiente de DevOps
Para facilitar a definição das credenciais de acesso a nuvem criamos uma máquina virtual local para
uso de todos os desenvolvedores.

Usamos **Vagrant** e **VirtualBox** como provisionadores desta VM local, conforme especificado no `Vagrantfile`.

Em `.ssh/` se encontram as chaves de acesso SSH a nuvem.
Esta chave foi criada **dentro** da máquina de DevOps para não comprometer as chaves SSH dos desenvolvedores.

### Instalação:
- No **macOS**: `brew cask install vagrant virtualbox`
- No **Ubuntu**: `apt-get install vagrant virtualbox`

```
user@laptop: devops-tools $> vagrant up    (levanta a VM de DevOps)
user@laptop: devops-tools $> vagrant ssh   (se conecta na VM de DevOps)
```

### Criação da instância na nuvem
```
ubuntu@ubuntu-xenial:~/devops-tools$ python3 tools/criar-instancia.py
```
A saída vai listar o IP da instância na nuvem. Pegue esse IP.

### Conexão com instância na nuvem
```
ubuntu@ubuntu-xenial:~/devops-tools$ sshcloud IP_DA_INSTANCIA

```

### Caso o comando `sshcloud` não funcione...
```
chmod 700 ~/.ssh
chmod 600 ~/.ssh/authorized_keys
chmod 644 ~/.ssh/known_hosts
chmod 755 .ssh
chmod 600 .ssh/id_rsa
chmod 644 .ssh/id_rsa.pub
```

