# -*- mode: ruby -*-
# vi: set ft=ruby :

# Vagrantfile API/syntax version. Don't touch unless you know what you're doing!
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|


config.vm.define "entbus" do |entbus|

      entbus.vm.box = "centos-6.4-x86_64"
      entbus.vm.box_url = "https://dl.dropboxusercontent.com/u/97268835/boxes/centos-6.4-x86_64.box"
      entbus.vm.hostname = "entbus.example.com"
      entbus.vm.network "private_network", ip: "192.168.50.3"
      entbus.vm.network :forwarded_port, guest: 7001, host: 7001, auto_correct: true
      
      
      entbus.vm.synced_folder ".", "/vagrant", :mount_options => ["dmode=777","fmode=777"]
      
      
      entbus.vm.provider :virtualbox do |vb|
          vb.customize ["modifyvm", :id, "--memory", "2048"]
      end
       
      entbus.vm.provision :puppet do |puppet|
        puppet.manifests_path = "puppet/manifests"
        puppet.module_path = "puppet/modules"
        puppet.manifest_file  = "site_osb.pp"
        puppet.options = "--verbose"
      end

  end 
     

   config.vm.define "erpbus" do |erpbus|

      erpbus.vm.box = "centos-6.4-x86_64"
      
      erpbus.vm.box_url = "https://dl.dropboxusercontent.com/u/97268835/boxes/centos-6.4-x86_64.box"
      erpbus.vm.hostname = "erpbus.example.com"
      erpbus.vm.network "private_network", ip: "192.168.50.4"
      erpbus.vm.network :forwarded_port, guest: 7001, host: 7001, auto_correct: true
      
      
      erpbus.vm.synced_folder ".", "/vagrant", :mount_options => ["dmode=777","fmode=777"]
      
      
      erpbus.vm.provider :virtualbox do |vb|
          vb.customize ["modifyvm", :id, "--memory", "2048"]
      end
       
      erpbus.vm.provision :puppet do |puppet|
        puppet.manifests_path = "puppet/manifests"
        puppet.module_path = "puppet/modules"
        puppet.manifest_file  = "site_osb.pp"
        puppet.options = "--verbose"
      end

  end

  config.vm.define "xe11g" do |xe11g|


    xe11g.vm.box = "centos-6.4-x86_64"
    xe11g.vm.box_url = "https://dl.dropboxusercontent.com/u/97268835/boxes/centos-6.4-x86_64.box"
    xe11g.vm.hostname = "xe11g.example.com"
    xe11g.vm.network "private_network", ip: "192.168.50.5"
    xe11g.vm.network "forwarded_port", guest:22, host: 2200, auto_correct: true
    xe11g.vm.network "forwarded_port", guest: 8080, host: 8080
    xe11g.vm.network "forwarded_port", guest: 1521, host: 1521

    xe11g.vm.synced_folder ".", "/vagrant", :mount_options => ["dmode=777","fmode=777"]

    xe11g.vm.provider :virtualbox do |vb|
      vb.customize ["modifyvm", :id, "--memory", "512"]
    end
    
    xe11g.vm.provision :puppet do |puppet|
      puppet.manifests_path = "puppet/manifests"
      puppet.module_path = "puppet/modules"
      puppet.manifest_file  = "site_xe11g.pp"
      puppet.options = "--verbose"
    end

  end

 
end
