# Certificate Kubernetes Administrator

## Setup a cluster using Kubeadm

- Create a local vm using multipass
- Set mappings on hosts among them
- Install Kubeadm


```bash
multipass launch -n k8s-control --disk 10G -m 4G
multipass launch -n k8s-worker1 --disk 10G -m 4G
multipass launch -n k8s-worker2 --disk 10G -m 4G
```

## Create multi node cluster using Kind

```shell
cd kind
kind create cluster --config 3-nodes-cluster.yaml
docker exec -it kind-control-plane  bash
$ kubectl get no
NAME                 STATUS   ROLES           AGE    VERSION
kind-control-plane   Ready    control-plane   3d9h   v1.29.1
kind-worker          Ready    <none>          3d9h   v1.29.1
kind-worker2         Ready    <none>          3d9h   v1.29.1
```

## First take

Questions not completed
- Create a cluster role
- Use of sidecar container
- Do ETCD backup
- Upgrade K8s version on master node only
- Network policy creation
