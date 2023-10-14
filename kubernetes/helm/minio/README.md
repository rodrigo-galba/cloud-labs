```
wget https://dl.min.io/client/mc/release/linux-amd64/mc
chmod +x minio
mc alias set myminio/ http://192.168.50.143:31628 JTTUHe73iYPR8gQveFdz QIe0e2Cqdp6YuCfTE28oxKkZ95JjKBrchAOxCla0
```

```
docker run quay.io/thanos/thanos:v0.31.0 sidecar --log.level=debug --prometheus.url="http://192.168.50.143:32053"
```

# Prometheus scrapper

- Edit Prometheus configmap:
```
kubectl edit configmap/prometheus-server
```
```yaml
- job_name: minio-job
     metrics_path: /minio/v2/metrics/cluster
     scheme: http
     static_configs:
     - targets: 
       - minio:9000
```
- Reload prometheus config
```
curl -X POST http://prometheus-server/-/reload
```