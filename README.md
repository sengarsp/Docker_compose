# Docker_compose
this project works on docker-compose as if the server will get disconnected then it will take to launch the new webserver so, docker can launch within 1 sec and it has MYsql to storage of the data permanent 



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
python3 docker__project.py
```
![alt text](https://github.com/sengarsp/Docker_compose/blob/master/docker__project.PNG)
>now everything is set up
> choose your option to launch your desired web server

![alt text](https://github.com/sengarsp/Docker_compose/blob/master/web1.PNG)
![alt text](https://github.com/sengarsp/Docker_compose/blob/master/web4.PN
## BUILT WITH
RHEL-8 Runing in Virtual Box
Docker 
Docker_compose 
Docker images:
       mysql
       wordpress
       joomla
## Author 
Shyamendra Pratan Singh Sengar
