# K3s

## What is K3s

K3s is a lightweight distribution of Kubernetes. It is designed to be easy to install and use, making it a good choice for local development, CI/CD, and edge computing. It is fully compliant with Kubernetes, but removes some less commonly used features to reduce its footprint.

K3s includes only what is necessary to run Kubernetes, including:

- A Kubernetes server, an agent, and kubectl.
- A container runtime (containerd).
- Networking (Flannel).
- A load balancing service (Traefik).
- Basic local storage (hostPath).

K3s is developed and maintained by Rancher Labs.

## License

K3s is licensed under the Apache License, Version 2.0. You can find the full text of the license [here](https://www.apache.org/licenses/LICENSE-2.0).

## Installation

To install K3s, follow these steps:

1. Download the K3s binary from the official website or GitHub repository. You can use the following command to download the binary:
    ```bash
    curl -LO https://github.com/k3s-io/k3s/releases/latest/download/k3s
    ```

2. Make the binary executable by running the following command:
    ```bash
    chmod +x k3s
    # Disable system memory swap
    sudo swapoff -a
    sudo chmod 644 /etc/rancher/k3s/k3s.yaml
    export KUBECONFIG=/etc/rancher/k3s/k3s.yaml
    ```

3. Run the installation script by executing the following command:
    ```bash
    curl -sfL https://get.k3s.io | sh -
    ```

4. Wait for the installation process to complete.

5. Verify the installation by running the following command:
    ```bash
    k3s check-config
    ```

# Configure kubectl for K3s (In case you use Microk8s)
1. Copy the K3s kubeconfig file to the default location:
    ```bash
    sudo cp /etc/rancher/k3s/k3s.yaml ~/.kube/config
    ```

2. Set the correct permissions for the kubeconfig file:
    ```bash
    sudo chown $(id -u):$(id -g) ~/.kube/config
    ```

3. Test the configuration by running the following command:
    ```bash
    kubectl get nodes
    ```
    You should see the list of nodes in your K3s cluster.

## Installation using Docker

To install K3s using Docker Compose, follow these steps:

1. Create a `docker-compose.yml` file with the following content:

    ```yaml
    version: '3'
    services:
      k3s-server:
        image: rancher/k3s:latest
        command: server
        privileged: true
        volumes:
          - k3s-server:/var/lib/rancher/k3s
        environment:
          - K3S_KUBECONFIG_OUTPUT=/output/kubeconfig.yaml
          - K3S_KUBECONFIG_MODE=666
        volumes:
          - ./kubeconfig.yaml:/output/kubeconfig.yaml

      k3s-agent1:
        image: rancher/k3s:latest
        command: agent
        privileged: true
        environment:
          - K3S_URL=ws://k3s-server:6443
          - K3S_TOKEN=secret

      k3s-agent2:
        image: rancher/k3s:latest
        command: agent
        privileged: true
        environment:
          - K3S_URL=ws://k3s-server:6443
          - K3S_TOKEN=secret

    volumes:
      k3s-server:
    ```

2. Run the following command to start the K3s server and agents:

    ```bash
    docker-compose up -d
    ```

3. You can then interact with the K3s server using `kubectl` by setting the `KUBECONFIG` environment variable to point to the `kubeconfig.yaml` file:

    ```bash
    export KUBECONFIG=./kubeconfig.yaml
    ```

Please note that running K3s in Docker is not officially supported and should only be done for testing or development purposes.

## Updating K3s

K3s provides a simple and straightforward way to update the Kubernetes cluster. Here are the steps to update K3s:

1. Check the current version of K3s by running the following command:
    ```bash
    k3s --version
    ```

2. Download the latest version of K3s binary from the official website or GitHub repository. You can use the following command to download the binary:
    ```bash
    curl -LO https://github.com/k3s-io/k3s/releases/latest/download/k3s
    ```

3. Make the binary executable by running the following command:
    ```bash
    chmod +x k3s
    ```

4. Stop the existing K3s server and agents by running the following command:
    ```bash
    sudo systemctl stop k3s
    ```

5. Replace the existing K3s binary with the new version by running the following command:
    ```bash
    sudo mv k3s /usr/local/bin/k3s
    ```

6. Start the K3s server and agents using the new version by running the following command:
    ```bash
    sudo systemctl start k3s
    ```

7. Verify the updated version of K3s by running the following command:
    ```bash
    k3s --version
    ```

Please note that updating K3s may require additional steps depending on your specific setup and configuration. It is recommended to refer to the official documentation for more detailed instructions on updating K3s.

## Disabling K3s

To disable K3s, you can use the following steps:

1. Stop the K3s server and agents by running the following command:
    ```bash
    sudo systemctl stop k3s
    ```

2. Disable the K3s service from starting automatically on system boot by running the following command:
    ```bash
    sudo systemctl disable k3s
    ```

3. Remove the K3s binary from the system by running the following command:
    ```bash
    sudo rm /usr/local/bin/k3s
    ```

4. Remove the K3s configuration directory by running the following command:
    ```bash
    sudo rm -rf /etc/rancher/k3s
    ```

5. Remove the K3s data directory by running the following command:
    ```bash
    sudo rm -rf /var/lib/rancher/k3s
    ```

After completing these steps, K3s will be fully disabled and removed from your system.

Please note that disabling K3s will stop all Kubernetes-related services and remove all associated data. Make sure to backup any important data before disabling K3s.