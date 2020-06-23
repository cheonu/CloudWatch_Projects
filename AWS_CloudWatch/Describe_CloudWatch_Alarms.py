import boto3
#create cloudwatch client
cloudwatch=boto3.client("cloudwatch")

#list the alarms of insufficient data through the pagination interface

paginator=cloudwatch.get_paginator("describe_alarms")
for response in paginator.paginate(StateValue='INSUFFICIENT_DATA'):
    print(response["MetricAlarms"])
