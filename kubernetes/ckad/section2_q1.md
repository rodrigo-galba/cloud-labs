# give an example of a statefulset for an stateful application on Kubernetes.

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: mongo
spec:
  serviceName: "mongo"
  replicas: 3
  selector:
    matchLabels:
      app: mongo
  template:
    metadata:
      labels:
        app: mongo
    spec:
      terminationGracePeriodSeconds: 10
      containers:
      - name: mongo
        image: mongo
        command:
          - mongod
          - "--replSet"
          - rs0
          - "--bind_ip"
          - "0.0.0.0"
        ports:
        - containerPort: 27017
        volumeMounts:
        - name: mongo-persistent-storage
          mountPath: /data/db
  volumeClaimTemplates:
  - metadata:
      name: mongo-persistent-storage
    spec:
      accessModes: [ "ReadWriteOnce" ]
      resources:
        requests:
          storage: 1Gi
```

## Understand how StatefulSets handle ordered pod creation and deletion

StatefulSets in Kubernetes are designed to manage stateful applications, and they handle pod creation and deletion in a specific order to maintain the state and identity of each pod.

Ordered Pod Creation:

When a StatefulSet is created, pods are created sequentially in order from {0...N-1} where N is the number of replicas specified. For example, if you have a StatefulSet with 3 replicas, the pods will be created in the order pod-0, pod-1, pod-2. The next pod (say pod-1) will not be created until the previous pod (say pod-0) is running and ready.

**Ordered Pod Deletion**:

When a StatefulSet is deleted, pods are deleted in reverse order from {N-1...0}. Using the previous example, if you delete the StatefulSet, the pods will be deleted in the order pod-2, pod-1, pod-0. The next pod (say pod-1) will not be deleted until the previous pod (say pod-2) is fully terminated.

**Stable Network Identity**:

Each pod in a StatefulSet derives its hostname from the name of the StatefulSet and the ordinal of the pod. The pattern is {statefulset-name}-{ordinal}. This ensures that each pod has a unique, stable network identity.

**Stable Storage**:

StatefulSets use Persistent Volumes (PV) and Persistent Volume Claims (PVC) to provide stable storage. When a StatefulSet is deleted, the PVCs of the pods are not deleted. This ensures that the state is preserved.

These features make StatefulSets suitable for running stateful applications like databases in a Kubernetes cluster.

## How can I scale the number of replicas in a StatefulSet using kubectl?

You can scale the number of replicas in a StatefulSet using the kubectl scale command. Here's the syntax:

```yaml
kubectl scale statefulsets <statefulset-name> --replicas=<number-of-replicas>
```

## Given a statefulset with 3 replicas that uses 3 persistent volume claims. Then it scales to 2 replicas. What happens with the persistent volume claims?

When you scale down a StatefulSet in Kubernetes, the corresponding Pods are deleted, but the Persistent Volume Claims (PVCs) are not. This means that the data on the volumes associated with the PVCs is preserved.

In your example, if you have a StatefulSet with 3 replicas and each replica has its own PVC, when you scale down the StatefulSet to 2 replicas, the pod-2 will be deleted (as the deletion happens in reverse order), but the PVC for pod-2 will not be deleted. The data on the volume associated with the PVC for pod-2 will still be there.

If you later scale the StatefulSet back up to 3 replicas, pod-2 will be recreated and it will reattach to its original PVC, and thus have access to its original data. This is one of the key features of StatefulSets that makes them suitable for stateful applications.

## How to remove a PVC managed by a statefulset?

To remove a Persistent Volume Claim (PVC) that is managed by a StatefulSet, you need to first scale down the StatefulSet to ensure that no pods are using the PVC. Then, you can delete the PVC using the kubectl delete pvc command.

Here are the steps:

1. Scale down the StatefulSet:
```
kubectl scale statefulsets <statefulset-name> --replicas=0
```
Replace <statefulset-name> with the name of your StatefulSet.

2. Delete the PVC:
```
kubectl delete pvc <pvc-name>
```
Replace <pvc-name> with the name of the PVC you want to delete.

Please note that deleting a PVC will also delete the associated Persistent Volume (PV) if the Reclaim Policy of the PV is set to Delete. If the Reclaim Policy is set to Retain, the PV will not be deleted, but it will become available for other PVCs to claim.

Also, be aware that deleting a PVC will permanently delete all data stored on the associated PV, so make sure to backup any important data before deleting a PVC.
