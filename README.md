# Docker_compose

## Docker Installation

Yum configuration for adding docker repo
using "https://download.docker.com/linux/centos/docker-ce.repo" put this link in the file in /etc/yum.repos.d/

!

## Start Docker
``` html
systemctl start docker
```
## Installing Docker Compose
``` html
url -L https://github.com/docker/compose/releases/download/1.21.2/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
chmod +x /usr/local/bin/docker-compose
```

# Cloning this project
``` html
git clone https://github.com/sengarsp/Docker_compose.git
```
## Run Python file
``` html
python3 docker_
