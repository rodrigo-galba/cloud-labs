# Installing Istio using Helm

## Setup and Verify

```
curl -L https://git.io/getLatestIstio | ISTIO_VERSION=1.11.1 sh -
cd istio-1.11.1
export PATH=$PWD/bin:$PATH
istioctl install --set profile=demo -y
kubectl label namespace default istio-injection=enabled
kubectl apply -f samples/bookinfo/platform/kube/bookinfo.yaml
kubectl get services
kubectl get pods
kubectl exec "$(kubectl get pod -l app=ratings -o jsonpath='{.items[0].metadata.name}')" -c ratings -- curl -sS productpage:9080/productpage | grep -o "<title>.*</title>"
kubectl apply -f samples/bookinfo/networking/bookinfo-gateway.yaml
export INGRESS_HOST=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')
export INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="http2")].port}')
export SECURE_INGRESS_PORT=$(kubectl -n istio-system get service istio-ingressgateway -o jsonpath='{.spec.ports[?(@.name=="https")].port}')
export GATEWAY_URL=$INGRESS_HOST:$INGRESS_PORT
echo "$GATEWAY_URL"
echo "http://$GATEWAY_URL/productpage"
```

## Kiali deployment

```
export  KUBECONFIG=/vagrant/eks-kube-config
kubectl apply -f samples/addons
kubectl rollout status deployment/kiali -n istio-system
cd istio-1.11.1
export PATH=$PWD/bin:$PATH
istioctl dashboard kiali
```

## Install Istio

```
kubectl create namespace istio-system
```
[Istio lab](https://github.com/rgalba/Kubernetes-Service-Mesh-with-Istio/blob/master/Section-1/video-1.5.md)