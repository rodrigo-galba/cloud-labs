## Regarding kubernetes deployment, Define a Deployment YAML manifest to create a scalable application.

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
```

Here's a breakdown of the manifest:

- apiVersion, kind, and metadata are standard Kubernetes fields that specify the API version to use, the kind of resource to create, and the metadata of the resource respectively.
- spec is where you define the desired state of the resource. For a Deployment, this includes the number of replicas, the selector to identify the Pods to manage, and the template for creating new Pods.
- replicas specifies the desired number of Pods. Kubernetes will ensure that this number of Pods always exists.
- selector specifies the labels that the Pods should have. Only Pods that match the selector will be managed by the Deployment.
- template specifies the template for creating new Pods. This includes the metadata and the spec of the Pods. The spec of the Pods includes the containers to run in the Pods. In this case, it's a single nginx container.


## Set environment variables and resource limits

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80
        env:
        - name: ENV_VAR_NAME
          value: "env_var_value"
        resources:
          limits:
            cpu: "1"
            memory: "500Mi"
          requests:
            cpu: "0.5"
            memory: "200Mi"
```

In this updated manifest:

- env is a list of environment variables to set in the container. Each environment variable is specified as a name-value pair.
- resources specifies the resource requirements and limits for the container. limits specifies the maximum amount of each resource that the container can use. requests specifies the amount of each resource that the system should reserve for the container. In this case, the container is limited to use 1 CPU and 500Mi of memory, and the system will reserve 0.5 CPU and 200Mi of memory for the container.

The information about setting environment variables and resource limits in a Kubernetes Deployment can be found in the official Kubernetes documentation. Here are the relevant links:

For setting environment variables, you can refer to the Define Environment Variables for a Container section. https://kubernetes.io/docs/tasks/inject-data-application/define-environment-variable-container/

For setting resource limits, you can refer to the Assign Memory Resources to Containers and Pods and Assign CPU Resources to Containers and Pods sections. https://kubernetes.io/docs/tasks/configure-pod-container/assign-memory-resource/
https://kubernetes.io/docs/tasks/configure-pod-container/assign-cpu-resource/
