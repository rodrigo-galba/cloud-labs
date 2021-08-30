# Creating a Kubernetes Cluster

On this lab, a Kubernetes cluster consisting of 1 master and 2 nodes will be created.

## Part 1 - Install Docker and Kubernetes on all servers

1. Elevate privileges using sudo:  
```sh
sudo su
```

2. Disable SELinux:
```sh
setenforce 0
sed -i --follow-symlinks 's/SELINUX=enforcing/SELINUX=disabled/g' /etc/sysconfig/selinux
```

3. Enable the br_netfilter module for cluster communication:
```sh
modprobe br_netfilter
echo '1' > /proc/sys/net/bridge/bridge-nf-call-iptables
```

4. Ensure that the Docker dependencies are satisfied:
```
yum install -y yum-utils device-mapper-persistent-data lvm2
```

5. Add the Docker repo and install Docker:
```
yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
yum install -y docker-ce
```

6. Set the cgroup driver for Docker to systemd, reload systemd, then enable and start Docker:
```sh
sed -i '/^ExecStart/ s/$/ --exec-opt native.cgroupdriver=systemd/' /usr/lib/systemd/system/docker.service
systemctl daemon-reload
systemctl enable docker --now
```

7. Add the Kubernetes repo:
```
cat << EOF > /etc/yum.repos.d/kubernetes.repo
[kubernetes]
name=Kubernetes
baseurl=https://packages.cloud.google.com/yum/repos/kubernetes-el7-x86_64
enabled=1
gpgcheck=0
repo_gpgcheck=0
gpgkey=https://packages.cloud.google.com/yum/doc/yum-key.gpg
  https://packages.cloud.google.com/yum/doc/rpm-package-key.gpg
EOF
```

8. Install Kubernetes:
```
yum install -y kubelet kubeadm kubectl
```

9. Enable the kubelet service. The kubelet service will fail to start until the cluster is initialized, this is expected:
```
systemctl enable kubelet
```

## Part 2 - Initialize the cluster on the master node only

1. Initialize the cluster using the IP range for Flannel:
```
$ kubeadm init --pod-network-cidr=10.244.0.0/16
Your Kubernetes control-plane has initialized successfully!

To start using your cluster, you need to run the following as a regular user:

  mkdir -p $HOME/.kube
  sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
  sudo chown $(id -u):$(id -g) $HOME/.kube/config

Alternatively, if you are the root user, you can run:

  export KUBECONFIG=/etc/kubernetes/admin.conf

You should now deploy a pod network to the cluster.
Run "kubectl apply -f [podnetwork].yaml" with one of the options listed at:
  https://kubernetes.io/docs/concepts/cluster-administration/addons/

Then you can join any number of worker nodes by running the following on each as root:

kubeadm join 10.0.1.100:6443 --token i3kkhx.2zkfzocc07f15ig0 \
        --discovery-token-ca-cert-hash sha256:40d377912a45686c87ef84ad58da36099126edc3735ec8b9c9744e0b2b22cfbf
```

2. Copy the kubeadmn join command that is in the output. We will need this later.
3. Exit sudo, copy the admin.conf to your home directory, and take ownership.
```sh
mkdir -p $HOME/.kube
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```
4. Deploy Flannel:
```sh
kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml
```
5. Check the cluster state:
```
kubectl get pods --all-namespaces
```

## Part 3 - Configure the nodes (don't run it on master)

1. Run the `join` command that you copied earlier as sudo:
```
sudo kubeadm join 10.0.1.100:6443 --token i3kkhx.2zkfzocc07f15ig0 \
        --discovery-token-ca-cert-hash sha256:40d377912a45686c87ef84ad58da36099126edc3735ec8b9c9744e0b2b22cfbf
```

## Part 4 - Create and Scale a Deployment Using kubectl

> These commands will only be run on the master node.

1. Check the nodes are `Ready`:
```
kubectl get no
NAME        STATUS   ROLES                  AGE    VERSION
k8smaster   Ready    control-plane,master   7m3s   v1.22.1
k8snode1    Ready    <none>                 56s    v1.22.1
k8snode2    Ready    <none>                 101s   v1.22.1
```

2. Create a simple deployment:
```
kubectl create deployment nginx --image=nginx
```

3. Inspect the pod:
```
kubectl get pods
```