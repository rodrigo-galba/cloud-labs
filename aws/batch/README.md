# AWS Batch script

## IAM

### Create IAM policy

```
aws iam create-policy --policy-name cronjob_policy --policy-document file://policy.json
```

### Create IAM role

```
aws iam create-role --role-name cronjob-role --assume-role-policy-document file://trust-policy.json
export policy_arn=$(aws iam list-policies --query 'Policies[?PolicyName==`cronjob_policy`].Arn' --output text)
aws iam attach-role-policy --policy-arn $policy_arn --role-name cronjob-role
```

### Create ECR repository

```
aws ecr create-repository --repository-name cronjob-ecr
export ecr_arn=$(aws ecr describe-repositories --query 'repositories[?repositoryName==`cronjob-ecr`].repositoryArn' --output text)
echo $ecr_arn
export ecr_uri=$(aws ecr describe-repositories --query 'repositories[?repositoryName==`cronjob-ecr`].repositoryUri' --output text)
aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin $ecr_uri
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
export cronjob_role_arn=\"arn:aws:iam::419277227138:role/cronjob-role\"
export ecr_uri=\"$ecr_uri\"
aws batch register-job-definition --job-definition-name cronjob-template --type container --container-properties '{ "image": '$ecr_uri', "command": [ "5"], "executionRoleArn": '$cronjob_role_arn',  "resourceRequirements": [{ "type": "VCPU", "value": "1"}, { "type": "MEMORY", "value": "2048" }], "networkConfiguration": { "assignPublicIp": "ENABLED" }  }' --platform-capabilities "FARGATE"
```

### Submit job

```
aws batch submit-job --job-name simple-cron --job-queue cronjob-queue --job-definition cronjob-template
```


##### references

- https://docs.aws.amazon.com/batch/latest/userguide/Batch_GetStarted.html
- IAM policy generator https://awspolicygen.s3.amazonaws.com/policygen.html
- https://docs.aws.amazon.com/batch/latest/userguide/batch-cwe-target.html
- https://docs.aws.amazon.com/cli/latest/reference/batch/register-job-definition.html
- https://aws.amazon.com/pt/blogs/compute/creating-a-simple-fetch-and-run-aws-batch-job/
- https://docs.aws.amazon.com/batch/latest/userguide/execution-IAM-role.html
