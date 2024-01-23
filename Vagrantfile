Vagrant.configure("2") do |config|

  config.vm.define "scriptbox" do |scriptbox|
    scriptbox.vm.box = "ubuntu/bionic64"
	scriptbox.vm.hostname = "scriptbox"
	scriptbox.vm.network "private_network", ip: "192.168.10.2"
  end
  
end
