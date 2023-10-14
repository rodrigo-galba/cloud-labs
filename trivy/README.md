# Trivy

Scan vulnerabilities and misconfiguration.

```
docker run --name trivy aquasec/trivy repo https://github.com/rodrigo-galba/cloud-labs -o report.txt
docker cp trivy:report.txt report.txt
```

References
- [Trivy doc](https://aquasecurity.github.io/trivy/v0.42/)

## kynerno

- Kubernetes Native Policy Management
https://kyverno.io/