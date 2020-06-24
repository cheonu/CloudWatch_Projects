import boto3

#create cloudwatch client

cloudwatch=boto3.client("cloudwatch")
response = cloudwatch.delete_alarms(
    AlarmNames=[
        'chedev',
    ]
)