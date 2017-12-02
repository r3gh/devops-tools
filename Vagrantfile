# -*- mode: ruby -*-
# vi: set ft=ruby :

required_plugins = %w( vagrant-vbguest )
required_plugins.each do |plugin|
  system "vagrant plugin install #{plugin}" unless Vagrant.has_plugin? plugin
end

Vagrant.configure("2") do |config|
  # You can search for boxes at https://atlas.hashicorp.com/search
  config.vm.box = "ubuntu/xenial64"
  config.ssh.forward_agent = true
  config.ssh.forward_x11 = true

  config.vm.synced_folder ".", "/vagrant", disabled: true
  config.vm.synced_folder ".", "/home/ubuntu/devops-tools"

  config.vm.provider "virtualbox" do |vb|
    vb.name = "devops-tools"
    vb.gui = false
    vb.memory = "1024"
    vb.cpus = "1"
  end

  config.vm.provision "shell", inline: <<-SHELL

    # Setting up bash environment
    echo "cd ~/devopss-tools"                                                        >> /etc/profile
    echo "source ~/devops-tools/openrc.sh"                                           >> /etc/profile
    alias get-ip="python3 -c \"import shade; cloud = shade.openstack_cloud(cloud='envvars'); \
                               print(dict(cloud.list_floating_ips()[0])['floating_ip_address'])\""
                                                                                     >> /etc/profile
    alias sshcloud="ssh -i .ssh/id_rsa -l ubuntu \$(get-ip)"                         >> /etc/profile

    # Install simulator dependencies
    echo "Installing dependencies..."
    apt-get update
    apt-get install -y python3 python3-pip python3-dev build-essential
    pip3 install --upgrade pip setuptools
    pip3 install --upgrade -r /home/ubuntu/devops-tools/requirements.txt
  SHELL
end
