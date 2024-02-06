# Kubernetes test tool

Kuttl
- https://kuttl.dev/
- https://youtu.be/ZSTQQNu4laY

## What is KUTTL?

The KUbernetes Test TooL (KUTTL) is a toolkit that makes it easy to test Kubernetes Operators

(opens new window), just using YAML.

It provides a way to inject an operator (subject under test) during the TestSuite setup and allows tests to be standard YAML files. Test assertions are often partial YAML documents which assert the state defined is true.

It is also possible to have KUTTL automate the setup of a cluster.

```
kubectl kuttl test test/
```