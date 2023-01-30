cloud_user@k8s-control:~$ sudo apt-get install -y --allow-change-held-packages kubeadm=1.22.2-00
Reading package lists... Done
Building dependency tree
Reading state information... Done
The following held packages will be changed:
  kubeadm
The following packages will be upgraded:
  kubeadm
1 upgraded, 0 newly installed, 0 to remove and 114 not upgraded.
Need to get 8718 kB of archives.
After this operation, 0 B of additional disk space will be used.
Get:1 https://packages.cloud.google.com/apt kubernetes-xenial/main amd64 kubeadm amd64 1.22.2-00 [8718 kB]
Fetched 8718 kB in 0s (21.8 MB/s)
(Reading database ... 120921 files and directories currently installed.)
Preparing to unpack .../kubeadm_1.22.2-00_amd64.deb ...
Unpacking kubeadm (1.22.2-00) over (1.22.0-00) ...
Setting up kubeadm (1.22.2-00) ...

cloud_user@k8s-control:~$ kubeadm version
kubeadm version: &version.Info{Major:"1", Minor:"22", GitVersion:"v1.22.2", GitCommit:"8b5a19147530eaac9476b0ab82980b4088bbc1b2", GitTreeState:"clean", BuildDate:"2021-09-15T21:37:34Z", GoVersion:"go1.16.8", Compiler:"gc", Platform:"linux/amd64"}

cloud_user@k8s-control:~$ kubectl get no
NAME          STATUS                     ROLES                  AGE   VERSION
k8s-control   Ready,SchedulingDisabled   control-plane,master   43m   v1.22.0
k8s-worker1   Ready                      <none>                 42m   v1.22.0
k8s-worker2   Ready                      <none>                 42m   v1.22.0

cloud_user@k8s-control:~$ sudo kubeadm upgrade plan v1.22.2
[upgrade/config] Making sure the configuration is correct:
[upgrade/config] Reading configuration from the cluster...
[upgrade/config] FYI: You can look at this config file with 'kubectl -n kube-system get cm kubeadm-config -o yaml'
[preflight] Running pre-flight checks.
[upgrade] Running cluster health checks
[upgrade] Fetching available versions to upgrade to
[upgrade/versions] Cluster version: v1.22.0
[upgrade/versions] kubeadm version: v1.22.2
[upgrade/versions] Target version: v1.22.2
[upgrade/versions] Latest version in the v1.22 series: v1.22.2

Components that must be upgraded manually after you have upgraded the control plane with 'kubeadm upgrade apply':
COMPONENT   CURRENT       TARGET
kubelet     3 x v1.22.0   v1.22.2

Upgrade to the latest version in the v1.22 series:

COMPONENT                 CURRENT   TARGET
kube-apiserver            v1.22.0   v1.22.2
kube-controller-manager   v1.22.0   v1.22.2
kube-scheduler            v1.22.0   v1.22.2
kube-proxy                v1.22.0   v1.22.2
CoreDNS                   v1.8.4    v1.8.4
etcd                      3.5.0-0   3.5.0-0

You can now apply the upgrade by executing the following command:

        kubeadm upgrade apply v1.22.2

_____________________________________________________________________


The table below shows the current state of component configs as understood by this version of kubeadm.
Configs that have a "yes" mark in the "MANUAL UPGRADE REQUIRED" column require manual config upgrade or
resetting to kubeadm defaults before a successful upgrade can be performed. The version to manually
upgrade to is denoted in the "PREFERRED VERSION" column.

API GROUP                 CURRENT VERSION   PREFERRED VERSION   MANUAL UPGRADE REQUIRED
kubeproxy.config.k8s.io   v1alpha1          v1alpha1            no
kubelet.config.k8s.io     v1beta1           v1beta1             no
_____________________________________________________________________

cloud_user@k8s-control:~$ sudo kubeadm upgrade apply v1.22.2
[upgrade/config] Making sure the configuration is correct:
[upgrade/config] Reading configuration from the cluster...
[upgrade/config] FYI: You can look at this config file with 'kubectl -n kube-system get cm kubeadm-config -o yaml'
[preflight] Running pre-flight checks.
[upgrade] Running cluster health checks
[upgrade/version] You have chosen to change the cluster version to "v1.22.2"
[upgrade/versions] Cluster version: v1.22.0
[upgrade/versions] kubeadm version: v1.22.2
[upgrade/confirm] Are you sure you want to proceed with the upgrade? [y/N]: Y
[upgrade/prepull] Pulling images required for setting up a Kubernetes cluster
[upgrade/prepull] This might take a minute or two, depending on the speed of your internet connection
[upgrade/prepull] You can also perform this action in beforehand using 'kubeadm config images pull'
[upgrade/apply] Upgrading your Static Pod-hosted control plane to version "v1.22.2"...
Static pod: kube-apiserver-k8s-control hash: 0e966c09b16f5767fc4863773307b8cc
Static pod: kube-controller-manager-k8s-control hash: 09a2fa2090ba4338877f0de49f30f3d2
Static pod: kube-scheduler-k8s-control hash: b297569a40d892bac14f0dbfeca80e7f
[upgrade/etcd] Upgrading to TLS for etcd
Static pod: etcd-k8s-control hash: e8d7f17803b7dcd1acd054424f8705ee
[upgrade/staticpods] Preparing for "etcd" upgrade
[upgrade/staticpods] Current and new manifests of etcd are equal, skipping upgrade
[upgrade/etcd] Waiting for etcd to become available
[upgrade/staticpods] Writing new Static Pod manifests to "/etc/kubernetes/tmp/kubeadm-upgraded-manifests607986081"
[upgrade/staticpods] Preparing for "kube-apiserver" upgrade
[upgrade/staticpods] Renewing apiserver certificate
[upgrade/staticpods] Renewing apiserver-kubelet-client certificate
[upgrade/staticpods] Renewing front-proxy-client certificate
[upgrade/staticpods] Renewing apiserver-etcd-client certificate
[upgrade/staticpods] Moved new manifest to "/etc/kubernetes/manifests/kube-apiserver.yaml" and backed up old manifest to "/etc/kubernetes/tmp/kubeadm-backup-manifests-2023-01-28-22-02-54/kube-apiserver.yaml"
[upgrade/staticpods] Waiting for the kubelet to restart the component
[upgrade/staticpods] This might take a minute or longer depending on the component/version gap (timeout 5m0s)
Static pod: kube-apiserver-k8s-control hash: 0e966c09b16f5767fc4863773307b8cc
Static pod: kube-apiserver-k8s-control hash: 0e966c09b16f5767fc4863773307b8cc
Static pod: kube-apiserver-k8s-control hash: 0e966c09b16f5767fc4863773307b8cc
Static pod: kube-apiserver-k8s-control hash: e37c6f2a631786070e9bd9f45650fc6a
[apiclient] Found 1 Pods for label selector component=kube-apiserver
[upgrade/staticpods] Component "kube-apiserver" upgraded successfully!
[upgrade/staticpods] Preparing for "kube-controller-manager" upgrade
[upgrade/staticpods] Renewing controller-manager.conf certificate
[upgrade/staticpods] Moved new manifest to "/etc/kubernetes/manifests/kube-controller-manager.yaml" and backed up old manifest to "/etc/kubernetes/tmp/kubeadm-backup-manifests-2023-01-28-22-02-54/kube-controller-manager.yaml"
[upgrade/staticpods] Waiting for the kubelet to restart the component
[upgrade/staticpods] This might take a minute or longer depending on the component/version gap (timeout 5m0s)
Static pod: kube-controller-manager-k8s-control hash: 09a2fa2090ba4338877f0de49f30f3d2
Static pod: kube-controller-manager-k8s-control hash: 0ecf51e212a51c91e23a2b78e6d9402f
[apiclient] Found 1 Pods for label selector component=kube-controller-manager
[upgrade/staticpods] Component "kube-controller-manager" upgraded successfully!
[upgrade/staticpods] Preparing for "kube-scheduler" upgrade
[upgrade/staticpods] Renewing scheduler.conf certificate
[upgrade/staticpods] Moved new manifest to "/etc/kubernetes/manifests/kube-scheduler.yaml" and backed up old manifest to "/etc/kubernetes/tmp/kubeadm-backup-manifests-2023-01-28-22-02-54/kube-scheduler.yaml"
[upgrade/staticpods] Waiting for the kubelet to restart the component
[upgrade/staticpods] This might take a minute or longer depending on the component/version gap (timeout 5m0s)
Static pod: kube-scheduler-k8s-control hash: b297569a40d892bac14f0dbfeca80e7f
Static pod: kube-scheduler-k8s-control hash: 5ed270d5546ab2757c00c9c027fa3e0d
[apiclient] Found 1 Pods for label selector component=kube-scheduler
[upgrade/staticpods] Component "kube-scheduler" upgraded successfully!
[upgrade/postupgrade] Applying label node-role.kubernetes.io/control-plane='' to Nodes with label node-role.kubernetes.io/master='' (deprecated)
[upload-config] Storing the configuration used in ConfigMap "kubeadm-config" in the "kube-system" Namespace
[kubelet] Creating a ConfigMap "kubelet-config-1.22" in namespace kube-system with the configuration for the kubelets in the cluster
[kubelet-start] Writing kubelet configuration to file "/var/lib/kubelet/config.yaml"
[bootstrap-token] configured RBAC rules to allow Node Bootstrap tokens to get nodes
[bootstrap-token] configured RBAC rules to allow Node Bootstrap tokens to post CSRs in order for nodes to get long term certificate credentials
[bootstrap-token] configured RBAC rules to allow the csrapprover controller automatically approve CSRs from a Node Bootstrap Token
[bootstrap-token] configured RBAC rules to allow certificate rotation for all node client certificates in the cluster
[addons] Applied essential addon: CoreDNS
[addons] Applied essential addon: kube-proxy

[upgrade/successful] SUCCESS! Your cluster was upgraded to "v1.22.2". Enjoy!

[upgrade/kubelet] Now that your control plane is upgraded, please proceed with upgrading your kubelets if you haven't already done so.
cloud_user@k8s-control:~$