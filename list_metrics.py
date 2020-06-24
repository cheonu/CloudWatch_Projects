import boto3

cloudwatch=boto3.client("cloudwatch")
'''
response = cloudwatch.list_metrics(
    Namespace='Web_Server_CPU_Utilization',
    MetricName='CPUUtilization',)
print(response)
'''

#using pagination method

response=cloudwatch.get_paginator("list_metrics")
for i in response.paginate(Namespace='AWS/Logs',
    MetricName='IncomingLogEvents',
    Dimensions=[{'Name':'LogGroupName'}]):

    print(i["Metrics"])
