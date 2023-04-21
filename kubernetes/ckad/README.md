# Certificate Kubernetes Administrator

## Setup a cluster

- Create a local vm using multipass
- Set mappings on hosts among them
- Install Kubeadm


```bash
multipass launch -n k8s-control --disk 10G -m 4G
multipass launch -n k8s-worker1 --disk 10G -m 4G
multipass launch -n k8s-worker2 --disk 10G -m 4G
```

