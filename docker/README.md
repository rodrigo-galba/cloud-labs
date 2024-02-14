# Docker

## Ubuntu setup
```
sudo snap install docker
sudo groupadd docker
sudo snap restart docker
sudo chmod 666 /var/run/docker.sock
```

```
sudo systemctl list-unit-files --type service --all
```

- https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user