#!/bin/bash
date
echo "Args: $@"
env
echo "This is my simple test job!."
echo "AWS jobId: $AWS_BATCH_JOB_ID"
echo "AWS jobQueue: $AWS_BATCH_JQ_NAME"
echo "AWS computeEnvironment: $AWS_BATCH_CE_NAME"
echo "Sleeping for $1 seconds"
sleep $1
date
echo "bye bye!!"