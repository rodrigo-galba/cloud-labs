# kind

> Kind is a tool for running local Kubernetes clusters using Docker container “nodes”.

## Setup

Windows
- Download kind binary
- Install Docker desktop
- Install (Lens 4.2 (optional))[https://github.com/lensapp/lens/releases/tag/v4.2.3]

## Creating a cluster

```
$ kind create cluster
rogal@hp-z8:~/cloud-labs/kind$ kind create cluster
Creating cluster "kind" ...
 ✓ Ensuring node image (kindest/node:v1.27.3) 🖼 
 ✓ Preparing nodes 📦  
 ✓ Writing configuration 📜 
 ✓ Starting control-plane 🕹️ 
 ✓ Installing CNI 🔌 
 ✓ Installing StorageClass 💾 
Set kubectl context to "kind-kind"
You can now use your cluster with:

kubectl cluster-info --context kind-kind

Have a nice day! 👋
```
```
kubectl cluster-info --context kind-kind
kubectl get po --all-namespaces
```

## Get cluster config

```
kubectl config view --raw > kind-config
```


references
- https://kind.sigs.k8s.io/
