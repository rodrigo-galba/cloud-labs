# Keycloak

## Docker

```
docker run -e KEYCLOAK_ADMIN=admin -e KEYCLOAK_ADMIN_PASSWORD=admin -p 8080:8080 --name mykeycloak quay.io/keycloak/keycloak start-dev
```


## Deployment on Kubernetes (Helm)

- https://artifacthub.io/packages/helm/bitnami/keycloak