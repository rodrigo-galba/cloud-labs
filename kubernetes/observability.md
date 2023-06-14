# Observability stack

## Prometheus

Helm chart:
- https://artifacthub.io/packages/helm/prometheus-community/prometheus

Values:  

```yaml
persistentVolume.storageClass: microk8s-hostpath
alertmanager.enabled: false
prometheus-pushgateway.enabled: false
kube-state-metrics.enabled: false
```


- https://github.com/prometheus-community/helm-charts/tree/main/charts/prometheus

## Thanos.io

#### sidecar
Configure external_labels for Prometheus
```
global:
  external_labels:
    cluster: z2-g3
    replica: "0"
```

```
#$ docker run quay.io/thanos/thanos:v0.20.0 sidecar --prometheus.url "http://192.168.50.143:30535"
$ docker run docker.io/bitnami/thanos:0.31.0-scratch-r5 sidecar --prometheus.url "http://192.168.50.143:30535"
level=info ts=2023-06-06T22:02:09.8531671Z caller=sidecar.go:123 msg="no supported bucket was configured, uploads will be disabled"
level=info ts=2023-06-06T22:02:09.8532358Z caller=options.go:26 protocol=gRPC msg="disabled TLS, key and cert must be set to enable"
level=info ts=2023-06-06T22:02:09.8537634Z caller=sidecar.go:363 msg="starting sidecar"
level=info ts=2023-06-06T22:02:09.8549547Z caller=intrumentation.go:75 msg="changing probe status" status=healthy
level=info ts=2023-06-06T22:02:09.8552898Z caller=http.go:73 service=http/server component=sidecar msg="listening for requests and metrics" address=0.0.0.0:10902
level=info ts=2023-06-06T22:02:09.8555784Z caller=tls_config.go:232 service=http/server component=sidecar msg="Listening on" address=[::]:10902
level=info ts=2023-06-06T22:02:09.8556241Z caller=tls_config.go:235 service=http/server component=sidecar msg="TLS is disabled." http2=false address=[::]:10902
level=info ts=2023-06-06T22:02:09.8553257Z caller=reloader.go:199 component=reloader msg="nothing to be watched"
level=info ts=2023-06-06T22:02:09.8553682Z caller=intrumentation.go:56 msg="changing probe status" status=ready
level=info ts=2023-06-06T22:02:09.8561638Z caller=grpc.go:131 service=gRPC/server component=sidecar msg="listening for serving gRPC" address=0.0.0.0:10901
level=info ts=2023-06-06T22:02:09.9463288Z caller=sidecar.go:179 msg="successfully loaded prometheus version"
level=info ts=2023-06-06T22:02:09.9534511Z caller=sidecar.go:201 msg="successfully loaded prometheus external labels" external_labels="{cluster=\"z2-g3\", replica=\"0\"}"
```


- https://thanos.io/tip/operating/troubleshooting.md/#description-1
- https://artifacthub.io/packages/helm/bitnami/thanos
