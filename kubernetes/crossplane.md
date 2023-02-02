# Crossplane.io

```
sudo snap alias microk8s.kubectl kubectl
sudo snap alias microk8s.helm3 helm
# Step 1: Create target namespace 
kubectl create namespace crossplane-system
# Step 2: Add crossplane stable repo to helm and update 
helm repo add crossplane-stable https://charts.crossplane.io/stable
helm repo update
# Step 3: Install Crossplane
helm install crossplane --namespace crossplane-system crossplane-stable/crossplane
```

Install crossplane CLI
```
curl -sL https://raw.githubusercontent.com/crossplane/crossplane/master/install.sh | sh
sudo mv kubectl-crossplane /snap/bin
kubectl crossplane --help
```