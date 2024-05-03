# K3d Documentation

## What is K3d?

K3d is a lightweight wrapper to run Kubernetes clusters in Docker. It allows you to easily create, manage, and delete Kubernetes clusters using Docker containers.

## Installation

To install K3d, follow these steps:

1. Install Docker on your machine if you haven't already.
2. Run the following command to install K3d:

    ```shell
    curl -s https://raw.githubusercontent.com/rancher/k3d/main/install.sh | bash
    ```

3. Verify the installation by running `k3d version` in your terminal.

## Windows Installation

To install K3d on Windows, follow these steps:

1. Install Docker Desktop for Windows if you haven't already. You can download it from the [Docker website](https://www.docker.com/products/docker-desktop).

2. Open a command prompt or PowerShell window.

3. Run the following command to install K3d:

    ```shell
    curl -s https://raw.githubusercontent.com/rancher/k3d/main/install.sh | bash
    ```

4. Verify the installation by running `k3d version` in your command prompt or PowerShell window.


## License

K3d is licensed under the Apache License 2.0. For more details, please refer to the [LICENSE](https://github.com/rancher/k3d/blob/main/LICENSE) file.

## Creating a Cluster with 2 Agents

To create a Kubernetes cluster with 2 agents using K3d, follow these steps:

1. Open your terminal.
2. Run the following command to create a new cluster named "my-cluster" with 2 agents:

    ```shell
    k3d cluster create my-cluster --agents 1 -p "8000:80@loadbalancer"
    ```

   This will create a new Kubernetes cluster with 2 agents using K3d.

3. Verify the cluster creation by running `kubectl get nodes` in your terminal. You should see the nodes of your newly created cluster.

## Updating K3d

To update K3d to the latest version, you can use the following command:
```bash
curl -s https://raw.githubusercontent.com/rancher/k3d/main/install.sh | bash
```

Verify the update by running k3d version in your terminal.

## Removing K3d

Run the following command to remove K3d:

```bash
curl -s https://raw.githubusercontent.com/rancher/k3d/main/uninstall.sh | bash
```
## Differences between K3s and Kind

K3s and Kind are two popular tools for running Kubernetes clusters, but they have some key differences. Here are the main differences between K3s and Kind:

1. **Size and Resource Usage**: K3s is designed to be lightweight and optimized for resource-constrained environments, making it a good choice for edge computing or IoT devices. Kind, on the other hand, is more resource-intensive and is typically used for local development and testing.

2. **Installation and Setup**: K3s is easy to install and can be set up with a single command. It comes bundled with all the necessary components, including the Kubernetes control plane and container runtime. Kind, on the other hand, requires Docker to be installed and relies on Docker containers to run the Kubernetes nodes.

3. **Cluster Management**: K3s provides a simple command-line interface for managing clusters, allowing you to easily create, scale, and delete clusters. It also supports features like high availability and load balancing. Kind, on the other hand, is primarily focused on local development and testing, and does not provide advanced cluster management features.

4. **Compatibility**: K3s aims to be fully compatible with standard Kubernetes, which means you can use the same tools and configurations that you would use with a regular Kubernetes cluster. Kind, on the other hand, is designed to be a lightweight alternative for local development and testing, and may not support all Kubernetes features or configurations.

5. **Use Cases**: K3s is well-suited for scenarios where resource usage and footprint are critical, such as edge computing, IoT, or running Kubernetes on low-powered devices. Kind, on the other hand, is ideal for local development and testing, providing an easy way to spin up Kubernetes clusters on your development machine.

Overall, the choice between K3s and Kind depends on your specific use case and requirements. If you need a lightweight and resource-efficient solution, K3s is a good choice. If you primarily need a tool for local development and testing, Kind is a better fit.

## Cluster backup

Backing up a K3d cluster involves backing up the etcd data, which is the data store that Kubernetes uses to store all its data. Here's how you can do it:

1. First, identify the server container for your K3d cluster. You can do this with the following command:

```bash
sudo docker ps -a | grep k3d-my-cluster-server-0
```
Look for the container with "server" in its name.

2. Once you've identified the server container, you can use the docker exec command to run the etcd snapshot save command inside the container. Here's an example:

```bash
sudo docker exec -it k3d-my-cluster-server-0 sh -c 'ETCDCTL_API=3 etcdctl snapshot save /var/lib/rancher/k3s/server/db/snapshot.db --endpoints=https://localhost:2379 --cacert=/var/lib/rancher/k3s/server/tls/etcd/server-ca.crt --cert=/var/lib/rancher/k3s/server/tls/etcd/server-client.crt --key=/var/lib/rancher/k3s/server/tls/etcd/server-client.key'
```
Replace "k3d-my-cluster-server-0" with the name of your server container.

3. The above command will create a snapshot of the etcd data and save it inside the server container. To copy the snapshot file to your local machine, you can use the docker cp command. Here's an example:

```bash
docker cp k3d-my-cluster-server-0:/var/lib/rancher/k3s/server/db/snapshot.db ./snapshot.db`
```
Replace "k3d-my-cluster-server-0" with the name of your server container.

After running these commands, you should have a file named "snapshot.db" on your local machine. This file is a backup of your K3d cluster's etcd data.

