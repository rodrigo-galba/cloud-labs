# Users and Groups

## Giving permission to a User

1- Generate a private key for a given user `carol`:
```
openssl genrsa -out carol.key 2048
```

2. create a certificate-signing request file, using the private key we just created,
```
openssl req -new -key carol.key -subj "/CN=carol/O=developers" -out carol.csr
```

3. Store the file in an environment var
```
export REQUEST=$(cat carol.csr | base64 -w 0)
```

4. Create a CertificateSigningRequest
https://kubernetes.io/docs/reference/access-authn-authz/certificate-signing-requests/#create-certificatessigningrequest
```
cat <<EOF | kubectl apply -f -
apiVersion: certificates.k8s.io/v1
kind: CertificateSigningRequest
metadata:
  name: carol
spec:
  request: $REQUEST
  signerName: kubernetes.io/kube-apiserver-client
  usages:
  - client auth
EOF
```

5. Approve the request
```
$ k certificate approve carol
root@kind-control-plane:/# k get csr
NAME    AGE   SIGNERNAME                            REQUESTOR          REQUESTEDDURATION   CONDITION
carol   26s   kubernetes.io/kube-apiserver-client   kubernetes-admin   <none>              Pending
root@kind-control-plane:/# k certificate approve carol
certificatesigningrequest.certificates.k8s.io/carol approved
root@kind-control-plane:/# k get csr
NAME    AGE   SIGNERNAME                            REQUESTOR          REQUESTEDDURATION   CONDITION
carol   61s   kubernetes.io/kube-apiserver-client   kubernetes-admin   <none>              Approved,Issued
```

6. Extract and decode to a `crt` file
```
kubectl get csr carol -o jsonpath='{.status.certificate}' | base64 -d > carol.crt
```

7. Embed the certificate key values infot the file:
```
$ kubectl config set-credentials carol --client-key=carol.key --client-certificate=carol.crt --embed-certs
User "carol" set.
```

8. See the credentials
```
kubectl config view
```

9. Add new user to the context:
```
$ k config set-context carol --user=carol --cluster=kind
Context "carol" created.
```

10. Get the context created:
```
kubectl config get-contexts
```

11. Run a pod to be viewed by the user:
```
kubect run nginx --image nginx
```

12. Set the context for new user
```
kubectl config use-context carol
```

13. Get a pod an try to delete it
```
root@kind-control-plane:/# k get po
NAME    READY   STATUS    RESTARTS   AGE
nginx   1/1     Running   0          82s
root@kind-control-plane:/# k delete pod nginx
Error from server (Forbidden): pods "nginx" is forbidden: User "carol" cannot delete resource "pods" in API group "" in the namespace "default"
```

14. Double check user permission for pod deletion
```
root@kind-control-plane:/# k auth can-i delete pod
no
```

## Giving permission to a Group

1. Assume the admin user:
```
kubectl config use-context kubernetes-admin@kind
```

2. Delete rolebinding bound to the user:
```
kubectl delete rolebinding pod-reader-binding
```

3. Create a new Role binding to the group `developers`
```
kubectl create rolebinding pod-reader-bind --role=pod-reader --group=developers
```

4. Switch back to user context
```
kubectl config use-context carol
```

5. Get the pod
```
k get po
```

6. Double check user permission for pod deletion
```
k auth can-i delete pod
no
```
