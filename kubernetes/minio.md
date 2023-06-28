# Minio

## Kubernetes (helm)

```
helm install \
--set global.storageClass=microk8s-hostpath \
--set livenessProbe.initialDelaySeconds=60 \
--set readinessProbe.initialDelaySeconds=60 \
minio \
bitnami/minio
```

output:
```
NAME: minio
LAST DEPLOYED: Mon Jan 30 21:08:04 2023
NAMESPACE: default
STATUS: deployed
REVISION: 1
TEST SUITE: None
NOTES:
CHART NAME: minio
CHART VERSION: 12.1.1
APP VERSION: 2023.1.25


To connect to your MinIO&reg; server using a client:

- Run a MinIO&reg; Client pod and append the desired command (e.g. 'admin info'):

   kubectl run --namespace default minio-client \
     --rm --tty -i --restart='Never' \
     --env MINIO_SERVER_ROOT_USER=$ROOT_USER \
     --env MINIO_SERVER_ROOT_PASSWORD=$ROOT_PASSWORD \
     --env MINIO_SERVER_HOST=minio \
     --image docker.io/bitnami/minio-client:2023.1.11-debian-11-r4 -- admin info minio

To access the MinIO&reg; web UI:

- Get the MinIO&reg; URL:

   export NODE_PORT=$(kubectl get --namespace default -o jsonpath="{.spec.ports[0].nodePort}" services minio)
   export NODE_IP=$(kubectl get nodes --namespace default -o jsonpath="{.items[0].status.addresses[0].address}")
   echo "MinIO&reg; web URL: http://$NODE_IP:$NODE_PORT/minio"
```

#### Sample user

```
f7lWCc0oFNyyP7Hc
WJ8Eqjg8bX4JennmbWF43Qa0ZnXIJx4F
```
