## Lambda base image

```
<!-- docker run -it --rm --entrypoint /bin/bash -v /tmp:/mnt amazon/aws-lambda-python:3.8 -->
cd cloud-labs\aws\lambda\bash-lambda
docker build -t bash-lambda .
```

References

- https://gallery.ecr.aws/?operatingSystems=Linux&page=1