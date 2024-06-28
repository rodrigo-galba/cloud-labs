## Kubernetes developer - Application Deployment

> Give me examples of the application deployment section for the Kubernetes developer exam.

Certainly! In the **Application Deployment** section of the **Certified Kubernetes Application Developer (CKAD)** exam, you'll work with various Kubernetes resources to deploy and manage applications. Here are some examples:

1. **Deployments**:
    - Create a simple web application deployment using a Deployment manifest.
    - Specify the desired number of replicas, container images, and ports.
    - Update the deployment to a new version of the application.

2. **StatefulSets**:
    - Deploy a stateful application (e.g., a database) using a StatefulSet.
    - Configure persistent storage for StatefulSets.
    - Understand ordered pod creation and deletion.

3. **DaemonSets**:
    - Use a DaemonSet to ensure a specific pod runs on every node.
    - Deploy monitoring agents or log collectors as DaemonSets.

4. **ConfigMaps and Secrets**:
    - Create a ConfigMap to store configuration data (e.g., environment variables).
    - Define a Secret for sensitive information (e.g., API keys, passwords).

5. **Pod Design**:
    - Create pods directly (not recommended) and understand when to use controllers (like Deployments).
    - Set pod affinity and anti-affinity rules.

6. **Init Containers**:
    - Design an init container to perform setup tasks before the main container starts.
    - Use init containers for database schema migrations or configuration checks.

7. **Multi-Container Pods**:
    - Deploy pods with multiple containers sharing the same network namespace.
    - Examples include sidecar containers for logging or monitoring.

8. **Resource Requests and Limits**:
    - Specify CPU and memory requests and limits in pod definitions.
    - Understand how resource constraints affect scheduling and performance.

9. **Pod Lifecycle Hooks**:
    - Use lifecycle hooks (preStart, postStart, preStop) for actions during pod startup and shutdown.

10. **Application Autoscaling**:
    - Set up Horizontal Pod Autoscaling (HPA) based on CPU or custom metrics.
    - Observe how the cluster scales the application based on demand.

Remember to practice creating and managing these resources in a Kubernetes cluster. Hands-on experience is crucial for success in the CKAD exam. Good luck with your preparation! 🌟🚀

------
1. Create a Deployment: You might be asked to create a Deployment for a specific application, ensuring that a certain number of replicas are always available.
```
kubectl create deployment nginx --image=nginx:1.14.2
```
2. Update a Deployment: You might need to update the version of the application in a Deployment and then verify that the update was successful.
```
kubectl set image deployment/nginx nginx=nginx:1.16.1 --record
kubectl rollout status deployment/nginx
```
3. Rollback a Deployment: If an update goes wrong, you might need to rollback a Deployment to a previous version.
```
kubectl rollout undo deployment/nginx
```
4. Scale a Deployment: You might be asked to scale a Deployment up or down based on load.
```
kubectl scale deployment/nginx --replicas=3
```
5. Create a Job or a CronJob: You might need to create a Job or a CronJob that runs a specific task at a certain time or interval.
```
kubectl create job my-job --image=busybox -- echo "Hello World"
```
6. Create a ConfigMap or a Secret and use it in a Pod: You might need to create a ConfigMap or a Secret and then modify a Pod to use it.
```
kubectl create configmap app-config --from-literal=key=value
```
7. Create a multi-container Pod: You might be asked to create a Pod that runs multiple containers.
------

## Configmaps

- create a configmap to keep all nginx configurations.

To create a ConfigMap to store Nginx configurations, you can use the kubectl create configmap command. If you have a configuration file, for example nginx.conf, you can create a ConfigMap from that file:

```
kubectl create configmap nginx-config --from-file=nginx.conf
```

This command creates a ConfigMap named nginx-config with the content of the nginx.conf file.

Then, you can mount this ConfigMap into a Pod so that Nginx can use it. Here's an example of how to do this in a Pod configuration:
```
apiVersion: v1
kind: Pod
metadata:
  name: nginx
spec:
  containers:
  - name: nginx
    image: nginx
    volumeMounts:
    - name: config-volume
      mountPath: /etc/nginx/nginx.conf
      subPath: nginx.conf
  volumes:
  - name: config-volume
    configMap:
      name: nginx-config
```
This configuration creates a Pod that runs the Nginx server. The nginx-config ConfigMap is mounted as a volume to the path /etc/nginx/nginx.conf in the container. The subPath field is used to specify the exact file to mount from the ConfigMap.


- in the volumemounts section, why the mountpath has the same subpath nginx.conf value?

The mountPath and subPath properties in the volumeMounts section of a Kubernetes Pod specification serve different purposes:

mountPath is the path inside the container where the volume is mounted.
subPath is used to share a specific file or directory of the volume to that mountPath.
In the context of a ConfigMap, if you have multiple files in the ConfigMap and you only want to use one of them in a specific location, you can use subPath to specify that file.

In your case, mountPath: /etc/nginx/nginx.conf means that the volume is mounted at /etc/nginx/nginx.conf inside the container. The subPath: nginx.conf means that only the nginx.conf file from the ConfigMap is mounted at that location.

So, the nginx.conf file from the ConfigMap replaces the nginx.conf file inside the container at /etc/nginx/nginx.conf. This is useful when you want to override the default configuration file of Nginx (or any other application) with your own configuration.


-----

For more detailed examples and tutorials, you can explore resources like the [DEV Community guide](https://dev.to/pavanbelagatti/deploying-an-application-on-kubernetes-a-complete-guide-1cj6) or the [Google Kubernetes Engine tutorial](https://cloud.google.com/kubernetes-engine/docs/tutorials/hello-app) ¹³.

Source: Conversation with Bing, 3/25/2024
(1) Deploying an Application on Kubernetes: A Complete Guide!. https://dev.to/pavanbelagatti/deploying-an-application-on-kubernetes-a-complete-guide-1cj6.
(2) Deploying a containerized web application | Kubernetes Engine | Google .... https://cloud.google.com/kubernetes-engine/docs/tutorials/hello-app.
(3) Kubernetes Online Test | TestDome. https://www.testdome.com/tests/kubernetes-online-test/176.
(4) Kubernetes: A Detailed Example of Deployment of a Stateful Application .... https://betterprogramming.pub/kubernetes-a-detailed-example-of-deployment-of-a-stateful-application-de3de33c8632.