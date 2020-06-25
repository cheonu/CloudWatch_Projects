import boto3

cloudwatch=boto3.client("cloudwatch")

#using simple list_metrics method

response = cloudwatch.list_metrics(
    Namespace='AWS/Logs',
    MetricName='IncomingLogEvents',)
print(response["Metrics"])


#using pagination method
'''
response=cloudwatch.get_paginator("list_metrics")
for i in response.paginate(Namespace='AWS/Logs',
    MetricName='IncomingLogEvents',
    Dimensions=[{'Name':'LogGroupName'}]):

    print(i["Metrics"])
'''
