import boto3

cloudwatch=boto3.client("cloudwatch")

cloudwatch.put_metric_alarm(
    AlarmName='cloud_consult',
    AlarmDescription='Alarm when CPU utilization exceeds 70%',
    ActionsEnabled=False,
    MetricName='CPUUtilization',
    Namespace='AWS/EC2',
    Statistic='Average',
    EvaluationPeriods=1,
    Threshold=70.0,
    ComparisonOperator='GreaterThanThreshold',
    Dimensions=[
        {
          'Name': 'InstanceId',
          'Value': 'INSTANCE_ID'
        },
    ],
    Unit='Seconds'
)
