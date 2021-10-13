# observability-cluster

1 - Observability cluster using Microk8s

## Basic setup

```sh
sudo snap install microk8s --classic --channel=1.21
sudo usermod -a -G microk8s $USER
sudo chown -f -R $USER ~/.kube
newgrp microk8s
microk8s status
microk8s enable dns helm3 host-access metrics-server storage
microk8s config > cluster.config
sudo snap alias microk8s.kubectl k
sudo snap alias microk8s.helm3 helm
```

## Minio Setup

```
helm repo add minio https://operator.min.io/
helm repo update
helm install --namespace minio-operator --create-namespace --set tenants.servers=4 --generate-name minio/minio-operator
helm install --namespace minio-operator --create-namespace --set tenants.servers="4" --set tenants.servers.storageClassName="microk8s-hostpath" --generate-name minio/minio-operator
```

## Ansible setup

```
sudo apt-get install python-software-properties
sudo apt-add-repository -y ppa:ansible/ansible
sudo apt-get update
sudo apt-get install -y ansible
ansible --version
```

2 - Observability cluster using a Server-based with Ansible