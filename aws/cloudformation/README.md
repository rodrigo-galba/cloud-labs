# AWS Cloud formation samples

### Simple bucket

To create the `simpleBucket` stack:  
```sh
$ aws cloudformation create-stack --stack-name simpleBucket --template-body file://simple_bucket.yml --region us-east-1
{
    "StackId": "arn:aws:cloudformation:us-east-1:517787923146:stack/simpleBucket/492802d0-2e90-11ec-9d5f-0a000044ce87"
}
```

To get its status:  
```sh
$ aws cloudformation describe-stacks --stack-name simpleBucket | jq '.Stacks[0].StackStatus'
"CREATE_COMPLETE"
```

To destroy the stack:  
```bash
aws cloudformation delete-stack --stack-name simpleBucket
$ aws cloudformation describe-stacks --stack-name simpleBucket | jq '.Stacks[0].StackStatus'

An error occurred (ValidationError) when calling the DescribeStacks operation: Stack with id simpleBucket does not exist
```

To update a stack:  
```bash
aws cloudformation update-stack --stack-name simpleBucket --template-body file://simple_bucket.yml --region us-east-1
```

## IAM Role integration

```shell
aws cloudformation create-stack \
                     --stack-name iamrole \
                     --capabilities CAPABILITY_IAM \
                     --template-body file://MyIamRole.yaml
IAM_ROLE_ARN=$(aws cloudformation describe-stacks \
                                    --stack-name iamrole \
--query "Stacks[0].Outputs[?OutputKey=='IamRole'].OutputValue" \
--output text)
aws sts assume-role --role-arn $IAM_ROLE_ARN \
                      --role-session-name tmp
# Here goes the output of the command. I will store the access credentials in the env vars
#$ export AWS_ACCESS_KEY_ID=… 
#$ export AWS_SECRET_ACCESS_KEY=…
#$ export AWS_SESSION_TOKEN=…
aws cloudformation create-stack \
                     --stack-name mybucket \
                     --template-body file://MyBucket.yaml
```

## IAM Service role

1. Create a service role:
```shell
aws cloudformation create-stack \
                     --stack-name cfniamrole \
                     --capabilities CAPABILITY_IAM \
                     --template-body file://CfnIamRole.yaml
```

2. Get created role ARN:
```shell
IAM_ROLE_ARN=$(aws cloudformation describe-stacks \
                                    --stack-name cfniamrole \
--query "Stacks[0].Outputs[?OutputKey=='IamRole'].OutputValue" \
--output text)
```

3. Run stack creation using the Role ARN:
```shell
aws cloudformation create-stack \
     --stack-name mybucket \
     --template-body file://simple_bucket.yml \
     --role-arn $IAM_ROLE_ARN
```

## Drift detection

1. Create a stack:

```shell
aws cloudformation create-stack \
                     --stack-name cfniamrole \
                     --capabilities CAPABILITY_IAM \
                     --template-body file://CfnIamRole.yaml
```

2. Go to the console and run drift detection on that stack manually
3. Add an extra policy to the role and rerun drift detection:
```shell
$ ROLENAME=$(aws cloudformation describe-stack-resources --stack-name cfniamrole --query "StackResources[0].PhysicalResourceId" --output text)
$ aws iam attach-role-policy --role-name $ROLENAME --policy-arn "arn:aws:iam::aws:policy/AdministratorAccess"
```

4. Go to drift changes and see the difference.

## 3 tier stack

To create core-stack for the first time:
```shell
aws cloudformation create-stack --stack-name core-stack --template-body file://stack/core.yaml \
  --parameters file://stack/test-env.json
```

To update core-stack:
```shell
aws cloudformation update-stack --stack-name core-stack --template-body file://stack/core.yaml
 --parameters file://stack/test-env.json
```

## General questions

1. Which API method is invoked when we create a CloudFormation stack? 
2. What is a CloudFormation service role? 
3. Which IAM policies are used if we do not specify the CloudFormation service role? 
4. How is the information about stack resources stored in CloudFormation? 
5. What happens if we delete the resource created by CloudFormation and try to create the same stack? 
6. What happens if we delete the resource created by CloudFormation and try to update the same stack? 
7. Why can't CloudFormation recreate the deleted resource?

## Further reading

- CloudFormation service roles: [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-servicerole.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-servicerole.html)
- Drift detection in CloudFormation: [https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-stack-drift.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-iam-servicerole.html)



