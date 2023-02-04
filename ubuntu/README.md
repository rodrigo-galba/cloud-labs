# Ubuntu 

## Python setup

```
sudo apt install python3.10 -y
sudo apt install python3.10-dev python3.10-venv python3.10-distutils python3.10-lib2to3 python3.10-gdbm python3.10-tk -y
```

## Microk8s

```
sudo iptables -P FORWARD ACCEPT
```

Configure Docker after install microk8s:
```
sudo vim /etc/docker/daemon.json
```

```json
{
    "insecure-registries" : ["localhost:32000"]
}
```

```
sudo systemctl restart docker
```

Configure cgroups