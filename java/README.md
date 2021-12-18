# Java apps on cloud native environments

## Building a Java image

- https://docs.docker.com/language/java/build-images/

### Build docker image

```sh
mvn package
docker build -t cloudlabs/java-app .
```

### Run docker image

```sh
docker run -p 8080:8080 cloudlabs/java-app
```