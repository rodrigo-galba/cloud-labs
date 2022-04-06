# API Registry

> The Registry API allows teams to track and manage machine-readable descriptions of APIs. 

https://github.com/apigee/registry

## How to build an image

Building `registry-server`:
```shell
git clone https://github.com/apigee/registry
cd registry/
docker build -f containers/registry-server/Dockerfile -t registry-server .
docker tag registry-server rogal/apigee-registry
docker push rogal/apigee-registry:latest
```

Building `registry-tools`
```shell
cd registry/
docker build -f containers/registry-tools/Dockerfile -t rogal/apigee-registry-tools .
docker push rogal/apigee-registry-tools:latest
```

## How to run server

```shell
docker-compose up
```

## How to run client

TBD  

## Data model

![Registry data model](./assets/database-registry-diagram.png)

### References
- https://graspingtech.com/docker-compose-postgresql/
