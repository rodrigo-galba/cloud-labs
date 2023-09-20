# Microk8s

## Setup

Create a basic VM:
```
multipass launch -n devbox --disk 20G -m 4G
multipass shell devbox
```

## Install Microk8s

```
sudo apt update
sudo apt upgrade
sudo snap install microk8s --classic
sudo usermod -a -G microk8s ubuntu
sudo chown -f -R ubuntu ~/.kube
newgrp microk8s
```

## Install addons

```
microk8s enable dns rbac storage
microk8s enable metrics-server
```

## Get Microk8s config

```
microk8s config view
microk8s enable observability
```

## Private Registry

1- Configure docker daemon to accept unsecure registry
```
sudo vim /etc/docker/daemon.json
{
  "insecure-registries" : ["192.168.50.130:32000"]
}
sudo systemctl restart docker
```

```
sudo docker pull nginx
sudo docker tag nginx localhost:32000/nginx
sudo docker push localhost:32000/nginx
kubectl apply -f deployment-nginx.yml
```

Reference
- https://microk8s.io/docs/registry-private
