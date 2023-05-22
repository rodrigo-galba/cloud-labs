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


References
- https://www.youtube.com/watch?v=qWEzbfb9qgQ