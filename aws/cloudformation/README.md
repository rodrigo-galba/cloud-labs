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
$ aws cloudformation update-stack --stack-name simpleBucket --template-body file://simple_bucket.yml --region us-east-1
```