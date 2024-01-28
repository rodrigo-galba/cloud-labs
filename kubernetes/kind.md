# Local cluster with Kind

> kind is a tool for running local Kubernetes clusters using Docker container “nodes”.
> kind was primarily designed for testing Kubernetes itself, but may be used for local development or CI.

## Findings

Kubernetes cluster.

A cluster has many different components, including two main parts: a control plane, which is handled by the control plane nodes, and the worker nodes, which are responsible for running the workloads (i.e., the containerized applications running on top of Kubernetes).

Linux system services are important in Kubernetes because they are responsible for keeping Kubernetes running on the host itself.

You can access the cluster in two ways, programmatically or using a tool called kubectl, which both require a certificate to authenticate. This certificate is common in a PKI (public key infrastructure) system that checks in with the CA (certificate authority) to ensure that the certificate is valid and that communication can happen between components in the Kubernetes cluster.

Kubernetes was built with microservices in mind, meaning that large microservice applications can run more efficiently in Kubernetes, being that each service is decoupled from the overall application.

Running Services on Kubernetes is more efficient via a declarative approach. This way, we can describe what we want the end state to be, as opposed to running a set of imperative commands to achieve the same result.

## General questions

```
Perform the command to list all API resources in your Kubernetes cluster. Save the output to a file named resources.csv.

List the services on your Linux operating system that are associated with Kubernetes. Save the output to a file named services.csv.

List the status of the kubelet service running on the Kubernetes node, output the result to a file named kubelet-status.txt, and save the file in the /tmp directory.

Use the declarative syntax to create a Pod from a YAML file in Kubernetes. Save the YAML file as chap1-pod.yaml. Use the kubectl create command to create the Pod.

Using the kubectl CLI tool, list all the Services created in your Kubernetes cluster across all namespaces. Save the output of the command to a file named all-k8s-services.txt.
```

> EXAM TASK There’s a need for company X to upgrade the Kubernetes controller to version 1.24 or higher, due to a bug that affects Pod scheduling. Perform the update with minimal downtime and loss of service.

reference
- [Kind K8s](https://kind.sigs.k8s.io/)
- [Life of a packet in Kubernete system](https://youtu.be/0Omvgd7Hg1I)
- [Star Wars API](https://swapi.dev/)
