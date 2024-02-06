# Kubernetes

## Productivity

- Kubectx
- krew (krew is a kubectl plugin manager)

## Krew

Install: https://krew.sigs.k8s.io/docs/user-guide/setup/install/  
For BASH or Zsh shell:

```bash
sudo apt install git curl vim -y
(
  set -x; cd "$(mktemp -d)" &&
  OS="$(uname | tr '[:upper:]' '[:lower:]')" &&
  ARCH="$(uname -m | sed -e 's/x86_64/amd64/' -e 's/\(arm\)\(64\)\?.*/\1\2/' -e 's/aarch64$/arm64/')" &&
  KREW="krew-${OS}_${ARCH}" &&
  curl -fsSLO "https://github.com/kubernetes-sigs/krew/releases/latest/download/${KREW}.tar.gz" &&
  tar zxvf "${KREW}.tar.gz" &&
  ./"${KREW}" install krew
)
```

```
vim ~/.bashrc
export PATH="${KREW_ROOT:-$HOME/.krew}/bin:$PATH"
```

Check configuration by running:
```
kubectl krew
```

## Helm

TBD


### Cloud shell as a pod

```
kubectl run cloud-shell --rm -i --tty --image ubuntu -- bash
apt update && apt install -y lsb-core lsb-release wget  && apt-get clean all
echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list
wget -qO- https://www.postgresql.org/media/keys/ACCC4CF8.asc | sudo tee /etc/apt/trusted.gpg.d/pgdg.asc &>/dev/null
apt install postgresql postgresql-client -y
```
where:
- my-shell: This ends up being the name of the Deployment that is created. Your pod name will typically be this plus a unique hash or ID at the end.
- --rm: Delete any resources we've created once we detach. When you exit out of your session, this cleans up the Deployment and Pod.
- -i/--tty: The combination of these two are what allows us to attach to an interactive session. 
- --: Delimits the end of the kubectl run options from the positional arg (bash).
- bash: Overrides the container's CMD. In this case, we want to launch bash as our container's command.


## DNS troubleshoot

Restart coreDNS
```
kubectl -n kube-system rollout restart deployment coredns
```

#### References
- https://www.youtube.com/watch?v=qWEzbfb9qgQ
- https://stackoverflow.com/questions/45805483/kubernetes-pods-cant-resolve-hostnames