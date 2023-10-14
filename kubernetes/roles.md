# K8s Role and ClusterRole

- An RBAC Role or ClusterRole contains rules that represent a set of permissions. 
- Permissions are purely additive (there are no "deny" rules).
- A Role always sets permissions within a particular namespace; when you create a Role, you have to specify the namespace it belongs in.

ClusterRole, by contrast, is a non-namespaced resource. The resources have different names (Role and ClusterRole) because a Kubernetes object always has to be either namespaced or not namespaced; it can't be both.

ClusterRoles have several uses. You can use a ClusterRole to:

    define permissions on namespaced resources and be granted access within individual namespace(s)
    define permissions on namespaced resources and be granted access across all namespaces
    define permissions on cluster-scoped resources

If you want to define a role within a namespace, use a Role; if you want to define a role cluster-wide, use a ClusterRole.

```
kubectl apply -f ckad/role.yaml
kubectl apply -f ckad/role-binding.yaml
```

- https://kubernetes.io/docs/reference/access-authn-authz/rbac/