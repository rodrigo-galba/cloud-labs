# ETCD - Kubernetes store

> Question: EXAM TASK The cluster k8s has been misconfigured and needs to be restored from a backup located at /tmp/c02dkjs0-001.db. Perform the restore and verify that the DaemonSet kube-proxy has been restored to the cluster.

```
# etcd needs to be set for V3
apt update; apt install -y etcd-client
export ETCDCTL_API=3
$ etcdctl -v
```

## Backup

```shell
$ etcdctl snapshot save snapshotdb \
  --cacert /etc/kubernetes/pki/etcd/ca.crt \
  --cert /etc/kubernetes/pki/etcd/server.crt \
  --key /etc/kubernetes/pki/etcd/server.key
{"level":"info","ts":1708042312.339988,"caller":"snapshot/v3_snapshot.go:119","msg":"created temporary db file","path":"snapshotdb.part"}
{"level":"info","ts":"2024-02-16T00:11:52.361Z","caller":"clientv3/maintenance.go:200","msg":"opened snapshot stream; downloading"}
{"level":"info","ts":1708042312.3612556,"caller":"snapshot/v3_snapshot.go:127","msg":"fetching snapshot","endpoint":"127.0.0.1:2379"}
{"level":"info","ts":"2024-02-16T00:11:52.399Z","caller":"clientv3/maintenance.go:208","msg":"completed snapshot read; closing"}
{"level":"info","ts":1708042312.4050689,"caller":"snapshot/v3_snapshot.go:142","msg":"fetched snapshot","endpoint":"127.0.0.1:2379","size":"2.2 MB","took":0.064912329}
{"level":"info","ts":1708042312.4051971,"caller":"snapshot/v3_snapshot.go:152","msg":"saved","path":"snapshotdb"}
Snapshot saved at snapshotdb  
```

## Getting data

To get data from an ETCD **snapshotdb** file:
```
etcdctl snapshot status snapshotdb --write-out=table
```

## Restoring ETCD

To simulate something to restore, delete the DaemonSet that was created for our kube-proxy service, which will allow us to verify that our restore operation was successful after we restore it. To delete the DaemonSet, perform the command:
```
$ kubectl delete ds kube-proxy -n kube-system
daemonset.apps "kube-proxy" deleted
$ kubectl get ds -A
NAMESPACE     NAME      DESIRED   CURRENT   READY   UP-TO-DATE   AVAILABLE   NODE SELECTOR            AGE
kube-system   kindnet   3         3         3       3            3           kubernetes.io/os=linux   25h
# There is no kube-proxy running
```

1 - Preparing the file **snapshotdb** to be restored which will be used by Kubernetes:
```
$ etcdctl snapshot restore snapshotdb --data-dir /var/lib/etcd-restore
{"level":"info","ts":1708042653.7333221,"caller":"snapshot/v3_snapshot.go:296","msg":"restoring snapshot","path":"snapshotdb","wal-dir":"/var/lib/etcd-restore/member/wal","data-dir":"/var/lib/etcd-restore","snap-dir":"/var/lib/etcd-restore/member/snap"}
{"level":"info","ts":1708042653.7519042,"caller":"mvcc/kvstore.go:388","msg":"restored last compact revision","meta-bucket-name":"meta","meta-bucket-name-key":"finishedCompactRev","restored-compact-revision":134325}
{"level":"info","ts":1708042653.7579575,"caller":"membership/cluster.go:392","msg":"added member","cluster-id":"cdf818194e3a8c32","local-member-id":"0","added-peer-id":"8e9e05c52164694d","added-peer-peer-urls":["http://localhost:2380"]}
{"level":"info","ts":1708042653.7698069,"caller":"snapshot/v3_snapshot.go:309","msg":"restored snapshot","path":"snapshotdb","wal-dir":"/var/lib/etcd-restore/member/wal","data-dir":"/var/lib/etcd-restore","snap-dir":"/var/lib/etcd-restore/member/snap"}
```

2 - Change the location where Kubernetes looks for the etcd data. This can be changed in the YAML specification for the API server, which will always be located on the control plane node in the **/etc/kubernetes/manifests** directory.  Any YAML files that you place in this directory will automatically schedule the Kubernetes resources within.
2.1 - Edit the file `/etc/kubernetes/manifests/etcd.yaml` and change the path for the volume from `/var/lib/etcd` to `/var/lib/etcd-restore`:

```yaml
# vim /etc/kubernetes/manifests/etcd.yaml
  volumes:
  - hostPath:
      path: /etc/kubernetes/pki/etcd
      type: DirectoryOrCreate
    name: etcd-certs
  - hostPath:
      path: /var/lib/etcd-restore
      type: DirectoryOrCreate
    name: etcd-data
status: {} 
```
