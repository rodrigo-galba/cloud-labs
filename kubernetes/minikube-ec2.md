# Minikube on EC2

Run it as user data:
```bash
#!bin/bash
sudo apt update
sudo apt upgrade -y
sudo hostnamectl set-hostname minikube
sudo apt-get install -y apt-transport-https ca-certificates curl
sudo apt-get update -y &&  sudo apt-get install -y docker.io
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
snap install kubectl --classic
sudo apt install conntrack -y
```

references
- https://www.fosstechnix.com/how-to-install-minikube-on-ubuntu-22-04-lts/