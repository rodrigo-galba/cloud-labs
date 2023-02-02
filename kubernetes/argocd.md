# ArgoCD

## Setup

```
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "NodePort"}}'
ngrok http 32316 --basic-auth 'ngrok:issecure'
```

## Install CLI

```
curl -sSL -o argocd-linux-amd64 https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64
sudo install -m 555 argocd-linux-amd64 /usr/local/bin/argocd
rm argocd-linux-amd64
argocd login localhost:32316
```

## Create app from git repo

```
kubectl config set-context --current --namespace=argocd
argocd app create guestbook --repo https://github.com/rodrigo-galba/argocd-example-apps.git --path guestbook --dest-server https://kubernetes.default.svc --dest-namespace default
```