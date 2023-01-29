# Performing a Kubernetes upgrade with kubeadm

> When you are managing Kubernetes in the real world, it is essential that you are able to keep your cluster up to date. This lab will allow you to practice the process of upgrading a Kubernetes cluster to a newer Kubernetes version using kubeadm. This will ensure you are comfortable with the upgrade process and ready to manage real-world Kubernetes clusters.

## Solution

- Log in to the control plane server using the credentials provided.
## Upgrade the controle plane

1. Upgrade kubeadm
```
[cloud_user@k8s-control]$ sudo apt-get update && \
sudo apt-get install -y --allow-change-held-packages kubeadm=1.22.2-00
```

2. MAke sure it upgraded correctly
```
[cloud_user@k8s-control]$ kubeadm version
```

3. Deain the control plane node
```
[cloud_user@k8s-control]$ kubectl drain k8s-control --ignore-daemonsetsc
```

4. Plan the upgrade
```
[cloud_user@k8s-control]$ kubectl drain k8s-control --ignore-daemonsets
```

5. Upgrade the control plane components
```
[cloud_user@k8s-control]$ sudo kubeadm upgrade apply v1.22.2
```

6. Upgrade kubelet and kubectl on the control plane node
```
[cloud_user@k8s-control]$ sudo apt-get update && \
sudo apt-get install -y --allow-change-held-packages kubelet=1.22.2-00 kubectl=1.22.2-00
```

7. Restart kubelet
```
[cloud_user@k8s-control]$ sudo systemctl daemon-reload
[cloud_user@k8s-control]$ sudo systemctl restart kubelet
```

8. Uncordon the control plane node
```
[cloud_user@k8s-control]$ kubectl uncordon k8s-control
```

9. Verify the control plane is working
```
[cloud_user@k8s-control]$ kubectl get nodes
```

# Upgrade the Worker Nodes

1. Run the following on the control plane node to drain worker node 1:
```
[cloud_user@k8s-control]$ kubectl drain k8s-worker1 --ignore-daemonsets --force
```

2. In a new terminal window, log in to worker node 1:
```
ssh cloud_user@<WORKER_1_PUBLIC_IP_ADDRESS>
```

3. Upgrade kubeadm on worker node 1:
```
[cloud_user@k8s-worker1]$ sudo apt-get update && \
sudo apt-get install -y --allow-change-held-packages kubeadm=1.22.2-00
[cloud_user@k8s-worker1]$ kubeadm version
```

4. Back on worker node 1, upgrade the kubelet configuration on the worker node:
```
[cloud_user@k8s-worker1]$ sudo kubeadm upgrade node
```

5. Upgrade kubelet and kubectl on worker node 1:
```
[cloud_user@k8s-worker1]$ sudo apt-get update && \
sudo apt-get install -y --allow-change-held-packages kubelet=1.22.2-00 kubectl=1.22.2-00
```

6. Restart kubelet:
```
[cloud_user@k8s-worker1]$ sudo systemctl daemon-reload
[cloud_user@k8s-worker1]$ sudo systemctl restart kubelet
```

7. From the control plane node, uncordon worker node 1:
```
[cloud_user@k8s-control]$ kubectl uncordon k8s-worker1
```

## Worker node 2

1. From the control plane node, drain worker node 2:
```
[cloud_user@k8s-control]$ kubectl drain k8s-worker2 --ignore-daemonsets --force
```

2. In a new terminal window, log in to worker node 2:
```
ssh cloud_user@<WORKER_2_PUBLIC_IP_ADDRESS>
```

3. Upgrade kubeadm
```
[cloud_user@k8s-worker2]$ sudo apt-get update && \
sudo apt-get install -y --allow-change-held-packages kubeadm=1.22.2-00
[cloud_user@k8s-worker2]$ kubeadm version
```

4. Back on worker node 2, perform the upgrade:
```
[cloud_user@k8s-worker2]$ sudo kubeadm upgrade node
[cloud_user@k8s-worker2]$ sudo apt-get update && \
sudo apt-get install -y --allow-change-held-packages kubelet=1.22.2-00 kubectl=1.22.2-00
[cloud_user@k8s-worker2]$ sudo systemctl daemon-reload
[cloud_user@k8s-worker2]$ sudo systemctl restart kubelet
```

5. From the control plane node, uncordong worker node 2
```
[cloud_user@k8s-control]$ kubectl uncordon k8s-worker2
```

6. Still in the control plane, verify the cluster is upgraded and working:
```
[cloud_user@k8s-control]$ kubectl get nodes
```
