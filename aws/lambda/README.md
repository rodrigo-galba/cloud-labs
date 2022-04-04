# AWS Lambda

## RDS access

1. Create a role to access VPC
2. Create RDS instance

```shell
aws rds create-db-instance --db-name ExampleDB --engine MySQL \
--db-instance-identifier MySQLForLambdaTest --backup-retention-period 3 \
--db-instance-class db.t2.micro --allocated-storage 5 --no-publicly-accessible \
--master-username myappuser --master-user-password myapppassword \
--profile guru
```

- https://docs.aws.amazon.com/pt_br/lambda/latest/dg/services-rds-tutorial.html
- https://aws.amazon.com/pt/premiumsupport/knowledge-center/lambda-sam-template-permissions/
