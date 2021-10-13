# Encrypting K8s secrets with Sealed Secrets

## Sealed secrets deployment

```sh
helm repo add sealed-secrets https://bitnami-labs.github.io/sealed-secrets
helm install sealed-secrets --namespace kube-system --version 1.13.2 sealed-secrets/sealed-secrets
```

Install `kubeseal` CLI tool:

```sh
wget https://github.com/bitnami-labs/sealed-secrets/releases/download/v0.13.1/kubeseal-linux-amd64 -O kubeseal
sudo install -m 755 kubeseal /usr/local/bin/kubeseal
kubeseal --help
```
> The kubeseal CLI uses the current kubectl context to access the cluster.

## Creating a sealed secret

The kubeseal CLI takes a Kubernetes Secret manifest as an input, encrypts it and outputs a SealedSecret manifest.  
Create the secret manifest as the `secret.yml` file:  

```yaml
apiVersion: v1
kind: Secret
metadata:
  creationTimestamp: null
  name: my-secret
data:
  password: YmFy # base64
  username: Zm9v # base64
```

Now, encrypt it:  

```sh
cat /vagrant/templates/sealed-secrets/secret.yml | kubeseal \
    --controller-namespace kube-system \
    --controller-name sealed-secrets \
    --format yaml \
    > /vagrant/templates/sealed-secrets/sealed-secret.yml
```

The content of the `sealed-secret.yaml` file should look like this:  

```yaml
apiVersion: bitnami.com/v1alpha1
kind: SealedSecret
metadata:
  creationTimestamp: null
  name: my-secret
  namespace: default
spec:
  encryptedData:
    password: AgA...
    username: AgA...
  template:
    metadata:
      creationTimestamp: null
      name: my-secret
      namespace: default
```

```
kubectl apply -f /vagrant/templates/sealed-secrets/sealed-secret.yml
```

--------------

References

[Sealed secrets tutorial](https://www.arthurkoziel.com/encrypting-k8s-secrets-with-sealed-secrets/)