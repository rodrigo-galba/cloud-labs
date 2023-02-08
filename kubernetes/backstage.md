# Backstage.io

## Deployment On Kubernetes (Helm)

```
helm repo add backstage https://backstage.github.io/charts
$ helm install \
--set postgresql.auth.existingSecret=postgresql \
--set service.type=NodePort \
backstage \
backstage/backstage
```

- https://backstage.io/docs/deployment/k8s
- https://github.com/backstage/charts
- https://github.com/backstage/charts/tree/main/charts/backstage
