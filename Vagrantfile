# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  # You can search for boxes at https://atlas.hashicorp.com/search
  config.vm.box = "ubuntu/xenial64"
  config.ssh.forward_agent = true
  config.ssh.forward_x11 = true

  config.vm.synced_folder ".", "/vagrant", disabled: true
  config.vm.synced_folder ".", "/home/vagrant/devops-tools"

  config.vm.provider "virtualbox" do |vb|
    vb.name = "devops-tools"
    vb.gui = false
    vb.memory = "1024"
    vb.cpus = "1"
  end

  config.vm.provision "shell", inline: <<-SHELL

    # Setting up bash environment
    echo "cd ~/devops-tools" >> /etc/profile

    # Install simulator dependencies
    # echo "Installing dependencies..."
    apt-get update
    apt-get install -y python3 python3-pip python3-dev build-essentials
    pip3 install --upgrade pip setuptools
    pip3 install --upgrade -r /home/vagrant/devops-tools/requirements.txt
  SHELL
end
