# Troubleshooting

## Kubectl not responding

1-Check status and get its output:
```
$ microk8s status
```

```
$ microk8s inspect
Inspecting system
Inspecting Certificates
Inspecting services
  Service snap.microk8s.daemon-cluster-agent is running
  Service snap.microk8s.daemon-containerd is running
  Service snap.microk8s.daemon-kubelite is running
  Service snap.microk8s.daemon-k8s-dqlite is running
  Service snap.microk8s.daemon-apiserver-kicker is running
  Copy service arguments to the final report tarball
Inspecting AppArmor configuration
Gathering system information
  Copy processes list to the final report tarball
  Copy disk usage information to the final report tarball
  Copy memory usage information to the final report tarball
  Copy server uptime to the final report tarball
  Copy openSSL information to the final report tarball
  Copy snap list to the final report tarball
  Copy VM name (or none) to the final report tarball
  Copy current linux distribution to the final report tarball
  Copy network configuration to the final report tarball
Inspecting kubernetes cluster
  Inspect kubernetes cluster
Inspecting dqlite
  Inspect dqlite  
WARNING:  The memory cgroup is not enabled. 
The cluster may not be functioning properly. Please ensure cgroups are enabled 
See for example: https://microk8s.io/docs/install-alternatives#heading--arm 
Building the report tarball
  Report tarball is at /var/snap/microk8s/6254/inspection-report-20240214_131458.tar.gz  
```