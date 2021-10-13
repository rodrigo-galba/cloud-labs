# Cloud labs

Code, docs and all stuff related to cloud.  
Tools found here: AWS tools, Terraform, Python, Go, Kubernetes, Ansible and more.  

## Basic tools installing reference

### AWS CLI v2

[linux doc](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html)

```
sudo apt install unzip
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
```

### Serverless framework tool

[Getting started doc](https://www.serverless.com/framework/docs/getting-started)
Linux/MacOS  
```bash
curl -o- -L https://slss.io/install | bash
$ sls --version
Framework Core: 2.62.0 (standalone)
Plugin: 5.4.6
SDK: 4.3.0
Components: 3.17.1
```