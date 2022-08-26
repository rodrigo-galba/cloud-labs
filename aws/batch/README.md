# AWS Batch script

## Cloudformation Setup

### IAM

Create a role to give permission to create the stack:
```
aws cloudformation create-stack --stack-name cronjob-role --template-body file://templates/cronjob-stack-role.yaml --capabilities CAPABILITY_IAM
IAM_ROLE_ARN=$(aws cloudformation describe-stacks \
                                    --stack-name cronjob-role \
--query "Stacks[0].Outputs[?OutputKey=='IamRole'].OutputValue" \
--output text)
```

### VPC

Get default VPC using the command line

```
VPC_ID=$(aws ec2 describe-vpcs --filters Name=isDefault,Values=true --query "Vpcs[].VpcId" --region us-east-1 --output text)
```

Get subnets:
```
SUBNETS=$(aws ec2 describe-subnets --filters Name=vpc-id,Values=$VPC_ID --query "Subnets[].SubnetId" --output text)
SUBNET_PARAMS=$(echo $SUBNETS | sed 's/ /\\,/g')
$ echo $SUBNET_PARAMS
subnet-0536a594ba230b038\,subnet-0c81ae33fb10d598e\,subnet-01ad3b28e165c140e\,subnet-0950363a9f371885b\,subnet-0f844786492602113\,subnet-0e41e9a74343cb810
```

Get security groups:
```
SEC_GROUPS=$(aws ec2 describe-security-groups --filters Name=vpc-id,Values=$VPC_ID --query "SecurityGroups[].GroupId" --output text)
SEC_GROUPS_PARAMS=$(echo $SEC_GROUPS | sed 's/ /\\,/g')
$ echo $SEC_GROUPS_PARAMS
sg-096ad472e0aa6c8ac
```
## Batch

Create computing environment

```
STACK_NAME=cronjob-stack
aws cloudformation create-stack --stack-name $STACK_NAME --parameters ParameterKey=StackName,ParameterValue=$STACK_NAME ParameterKey=SubnetIds,ParameterValue=$SUBNET_PARAMS ParameterKey=SecGroupIds,ParameterValue=$SEC_GROUPS_PARAMS --template-body file://templates/cronjob-stack.yaml --role-arn $IAM_ROLE_ARN --capabilities CAPABILITY_IAM

aws cloudformation update-stack --stack-name $STACK_NAME --parameters ParameterKey=StackName,ParameterValue=$STACK_NAME ParameterKey=SubnetIds,ParameterValue=$SUBNET_PARAMS ParameterKey=SecGroupIds,ParameterValue=$SEC_GROUPS_PARAMS --template-body file://templates/cronjob-stack.yaml --role-arn $IAM_ROLE_ARN --capabilities CAPABILITY_IAM
```

## IAM

### Create IAM policy

```
aws iam create-policy --policy-name cronjob_policy --policy-document file://policy.json
```

### Create IAM role

```
aws iam create-role --role-name cronjob-role --assume-role-policy-document file://trust-policy.json
export policy_arn=$(aws iam list-policies --query 'Policies[?PolicyName==`cronjob_policy`].Arn' --output text)
export ecr_policy_arn=$(aws iam list-policies --query 'Policies[?PolicyName==`AmazonEC2ContainerRegistryPowerUser`].Arn' --output text)
aws iam attach-role-policy --policy-arn $policy_arn --role-name cronjob-role
aws iam attach-role-policy --policy-arn $ecr_policy_arn --role-name cronjob-role
```

### Create ECR repository

```
export AWS_REGION=us-east-1
export ecr_uri=$(aws ecr create-repository --repository-name cronjob-ecr | jq -r '.repository.repositoryUri')
export ecr_uri=$(aws ecr describe-repositories --query 'repositories[?repositoryName==`cronjob-ecr`].repositoryUri' --output text)
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $ecr_uri
export REGISTRY_ID=$(aws ecr describe-registry | jq -r '.registryId')
export DOCKER_REGISTRY_URI="${REGISTRY_ID}"
docker build -t cronjob-ecr .
docker tag cronjob-ecr:latest $ecr_uri:latest
docker push $ecr_uri:latest
```

### Create Batch compute environment

> Manual step.

```
<!-- aws batch create-compute-environment --cli-input-json file://batch-compute-environment.json -->
```

### Create a Job queue

```
aws batch create-job-queue --cli-input-json file://batch-job-queue.json
```

### Create a job definition

```
export cronjob_role_arn=\"$(aws iam list-roles --query 'Roles[?RoleName==`cronjob-role`].Arn' --output text)\"
export ecr_uri=\"$ecr_uri\"
aws batch register-job-definition --job-definition-name cronjob-template --type container --container-properties '{ "image": '$ecr_uri', "command": [ "5"], "executionRoleArn": '$cronjob_role_arn',  "resourceRequirements": [{ "type": "VCPU", "value": "1"}, { "type": "MEMORY", "value": "2048" }], "networkConfiguration": { "assignPublicIp": "ENABLED" }  }' --platform-capabilities "FARGATE"
```

### Submit job

```
aws batch submit-job --job-name simple-cron --job-queue cronjob-queue --job-definition cronjob-template
```

### Create a event rule

```
aws events put-rule --name scheduled-cronjob-task --schedule-expression "rate(1 minute)" 
aws events put-targets --rule scheduled-cronjob-task --targets "Id"="1","Arn"="arn:aws:batch:us-east-1:882118399350:job-queue/cronjob-queue","BatchParameters"="{"JobDefinition"="cronjob-template", "JobName"="scheduled-job-2"}","RoleArn"="arn:aws:iam::882118399350:role/service-role/Amazon_EventBridge_Invoke_Batch_Job_Queue_1733122509"
```

#### Disable rule

```
aws events disable-rule --name
```

##### references

- https://docs.aws.amazon.com/batch/latest/userguide/Batch_GetStarted.html
- IAM policy generator https://awspolicygen.s3.amazonaws.com/policygen.html
- https://docs.aws.amazon.com/batch/latest/userguide/batch-cwe-target.html
- https://docs.aws.amazon.com/cli/latest/reference/batch/register-job-definition.html
- https://aws.amazon.com/pt/blogs/compute/creating-a-simple-fetch-and-run-aws-batch-job/
- https://docs.aws.amazon.com/batch/latest/userguide/execution-IAM-role.html
