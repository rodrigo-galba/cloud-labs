# Ansible

Tool for configuration management.

## How to run
```
sudo apt insall sshpass
ansible-vault create secret # input ansible_sudo_pass: value
ansible-playbook -i inventory.ini playbook.yaml -k --ask-vault-pass -b -e users=$USER
```

Reference
- https://stackoverflow.com/questions/21870083/specify-sudo-password-for-ansible
- https://www.digitalocean.com/community/tutorials/how-to-use-ansible-to-install-and-set-up-docker-on-ubuntu-20-04
