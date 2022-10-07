# kind

> Kind is a tool for running local Kubernetes clusters using Docker container “nodes”.

## Setup

Windows
- Download kind binary
- Install Docker desktop
- Install (Lens 4.2 (optional))[https://github.com/lensapp/lens/releases/tag/v4.2.3]

## Creating a cluster

```
kind create cluster
kubectl cluster-info --context kind-kind
kubectl get po --all-namespaces
```

## Get cluster config

```
kubectl config view --raw
```


references
- https://kind.sigs.k8s.io/
