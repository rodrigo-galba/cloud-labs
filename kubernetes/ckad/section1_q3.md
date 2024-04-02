# Design a DaemonSet to ensure a pod runs on every node.

```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
    name: fluentd
    namespace: kube-system
    labels:
        k8s-app: fluentd-logging
spec:
    selector:
        matchLabels:
            name: fluentd
    template:
        metadata:
            labels:
                name: fluentd
        spec:
            containers:
            - name: fluentd
                image: fluent/fluentd:v1.11-debian-1
                resources:
                    limits:
                        memory: 200Mi
                    requests:
                        cpu: 100m
                        memory: 200Mi
            terminationGracePeriodSeconds: 30
```

This YAML file creates a DaemonSet named fluentd in the kube-system namespace. The fluent/fluentd:v1.11-debian-1 image is used for the pods. The spec.selector.matchLabels field is used to select the pods that belong to this DaemonSet.

```
kubectl apply -f fluentd-daemonset.yaml
```

This will create a Fluentd pod on every node in your cluster. If new nodes are added to the cluster, the DaemonSet will ensure that the Fluentd pod is also added to the new nodes.

# Use cases for daemonsets

DaemonSets are useful for running a specific type of Pod on all or certain nodes in a Kubernetes cluster. Here are some common use cases:

Node Monitoring: You can use a DaemonSet to run a Pod on every node that collects and reports system metrics, such as CPU usage, memory usage, network IO, disk IO, etc. Examples of such tools include Prometheus Node Exporter, cAdvisor, and Datadog.

Log Collection: DaemonSets are often used to deploy log collection agents on each node. These agents can collect and forward logs from the node and the containers running on it to a central logging solution. Examples include Fluentd, Logstash, and Filebeat.

Network Overlays: Some network plugins, like Calico or Flannel, use DaemonSets to ensure that each node has a Pod running that can handle the network overlay for container communication across nodes.

Storage: Some types of storage solutions, like Rook, use DaemonSets to manage the storage on each node.

Security: DaemonSets can be used to deploy security agents on each node to monitor and enforce security policies. Examples include Falco and Sysdig.

Node Maintenance: DaemonSets can be used to run tasks like cleaning up disk space or managing updates across all nodes.

Remember, the key characteristic of a DaemonSet is that it ensures that a copy of a Pod is running on all (or some) nodes in a cluster. This makes it ideal for system-wide tasks like monitoring, logging, and network configuration.
