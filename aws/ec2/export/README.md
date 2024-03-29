# EC2 instance export

- Create a bucket to send instance blob
- Give proper access to the EC2 service AWS account
- Change export.json file to refer the created bucket
- Get EC2 instance ID


## Import instance

```
aws ec2 import-image --description "Fastapi server" --disk-containers "file://./import.json"
```

## Instance export task

```
export ec2=i-0896777ee95bcce22
aws ec2 create-instance-export-task --instance-id $ec2 --target-environment vmware --export-to-s3-task file://./export.json
```

```
aws ec2 describe-export-tasks --export-task-ids export-$ec2
```

references
- https://docs.aws.amazon.com/vm-import/latest/userguide/vmexport.html
