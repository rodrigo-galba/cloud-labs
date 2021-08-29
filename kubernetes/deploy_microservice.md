# Deploying a Microservice Application to Kubernetes

## Deploy the Stan's Robot Shop app to the cluster

Clone sample app from github:  
```
cd ~/
git clone https://github.com/linuxacademy/robot-shop.git
```

Create required resources:  
```
kubectl create namespace robot-shop
kubectl -n robot-shop create -f ~/robot-shop/K8s/descriptors/
kubectl get pods -n robot-shop
curl http://$kube_master_public_ip:30080
```

Scaling mongodb to 3 replicas:  
```
kubectl scale deployment/mongodb -n robot-shop --replicas=2
```