# Multipass boxes

> Get an instant Ubuntu VM with a single command. Multipass can launch and run virtual machines and configure them with cloud-init like a public cloud. Prototype your cloud launches locally for free.  

[Official page](https://multipass.run/)

## Launch a box

Launch an instance (by default you get the current Ubuntu LTS) named `cloudbox` with 4GB in RAM:  
```bash
multipass launch -n cloudbox -m 4G -d 10G --clout-init cloudbox-config.yaml
multipass launch -n devbox -m 4G
```

## Run commands

Run commands in that instance, try running bash (logout or ctrl-d to quit)  
```bash
multipass exec foo -- lsb_release -a
```

## Cloud-init on launch

Pass a cloud-init metadata file to an instance on launch. See using [cloud-init](https://ubuntu.com/blog/using-cloud-init-with-multipass) with multipass for more details:

```bash
multipass launch -n bar --cloud-init cloud-config.yaml
```

## To start and stop

To start an existent box:  
```bash
multipass start cloudbox
multipass stop cloudbox
```

## To access a box

To connect an existent box:  
```bash
multipass shell cloudbox
```

## List instances

```bash
multipass list
```

## Delete and clean up

```bash
multipass delete cloudbox
multipass purge
```

## Ansible integration

TBD  

## SSH setup

- TBD
- https://cloudinit.readthedocs.io/en/latest/topics/examples.html#configure-instances-ssh-keys

## Cloud-config

- https://cloudinit.readthedocs.io/en/latest/
- https://www.digitalocean.com/community/tutorials/how-to-use-cloud-config-for-your-initial-server-setup
