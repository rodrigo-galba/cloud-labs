# Minikube

minikube quickly sets up a local Kubernetes cluster on macOS, Linux, and Windows. We proudly focus on helping application developers and new Kubernetes users.

## Highlights


- Supports the latest Kubernetes release (+6 previous minor versions)
- Cross-platform (Linux, macOS, Windows)
- Deploy as a VM, a container, or on bare-metal
- Multiple container runtimes (CRI-O, containerd, docker)
- Direct API endpoint for blazing fast image load and build
- Advanced features such as LoadBalancer, filesystem mounts, FeatureGates, and network policy
- Addons for easily installed Kubernetes applications
- Supports common CI environments

## Linux setup

To install:
```
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
```

To start:
```
minikube start
```

References

- https://minikube.sigs.k8s.io/docs/
