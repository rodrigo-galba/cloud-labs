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
