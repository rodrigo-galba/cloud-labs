# Deploying a Pod to a Node with a Label in Kubernetes

> You have been tasked with creating a pod named nginx, which needs to use the nginx image. This pod needs to run on a node that has solid state drives (SSD). Luckily, the nodes have already been labeled with the disk type. You must find the node with the label disk=ssd from within the provided Kubernetes cluster. Then, you will create the pod YAML which will force the pod to use the node with that label. Finally, you will apply the YAML to the Kubernetes cluster and verify that the pod is running on the correct node.

1. List all the nodes in the cluster.
```
kubectl get nodes
```

2. List all the pods in all namespaces.
```
kubectl get pods --all-namespaces
```

3. List all the namespaces in the cluster.
```
kubectl get namespaces
```

4. List the labels for all nodes in the cluster
```
kubectl get no --show-labels | grep disk=ssd
```

> We should see the label `disk=ssd` for one of the nodes.

5. Create the pod YAML that will run on the node labeled `disk=ssd`
```sh
cat << EOF > pod.yaml
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
    - name: nginx
      image: nginx
  nodeSelector:
    disk: ssd
EOF
```

Apply the `pod.yaml` file for that Pod:
```
kubectl apply -f pod.yaml
```

6. Verify that the pod is running on the correct node
```sh
kubectl get po -o wide
```