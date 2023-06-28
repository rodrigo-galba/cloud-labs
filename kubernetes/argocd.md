# ArgoCD

## Setup

```
sudo snap alias microk8s.kubectl kubectl
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "NodePort"}}'
kubectl get svc argocd-server -n argocd -o yaml | yq '.spec.ports[0].nodePort'
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
argocd app create guestbook --repo https://github.com/rodrigo-galba/argocd-example-apps.git --path helm-guestbook --dest-server https://kubernetes.default.svc --dest-namespace default
```

# Prometheus


- Edit Prometheus configmap:
```
kubectl edit configmap/prometheus-server
```
```yaml
- job_name: argocd-metrics
     metrics_path: /metrics
     scheme: http
     static_configs:
     - targets: 
       - argocd-metrics.argocd.svc.cluster.local:8082
- job_name: argocd-server-metrics
     metrics_path: /metrics
     scheme: http
     static_configs:
     - targets: 
       - argocd-server-metrics.argocd.svc.cluster.local:8083
```
- Reload prometheus config
```
curl -X POST http://192.168.50.143:31646/-/reload
```