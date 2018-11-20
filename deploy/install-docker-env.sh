# localt test env
# ip:192.168.96.156
# user: sinobot
# password: sinobot

# https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04
# https://www.digitalocean.com/community/tutorials/how-to-install-docker-compose-on-ubuntu-18-04

#### install Docker
sudo apt update
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu bionic stable"
sudo apt update
apt-cache policy docker-ce
sudo apt install -y docker-ce
sudo usermod -aG docker $USER
# verfiy docker info
docker version
sudo docker info

### install Docker Compose
sudo curl -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
docker-compose --version

# prepare host directory for container
sudo mkdir -p /var/log/sinyi
sudo chown -R $USER:$USER /var/log/sinyi
sudo chmod -R 755 /media/data 

sudo apt-get install -y cifs-utils
sudo mkdir -p /media/data
sudo chown -R $USER:$USER /media/data
sudo chmod -R 755 /media/data 
#### test mount 
#### sudo mount -t cifs -o username=administrator,password=password123\!\#,uid=$USER,gid=$USER //192.168.96.136/Users/Administrator/Documents/xypdf  /media/data
#### echo "//192.168.96.136/Users/Administrator/Documents/xypdf /media/data cifs username=administrator,password=password123!# 0 0" >> /etc/fstab


