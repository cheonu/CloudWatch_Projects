#Create a CloudWatch Events rule using put_rule
import boto3
cloudwatch_events=boto3.client("events")

response = cloudwatch_events.put_rule(
    Name='cloud_consult_event',
    ScheduleExpression='rate(5 minutes)',
    State='ENABLED',
    RoleArn='arn:aws:iam::967250075457:role/chedev_cloudwatch',
)

print(response["RuleArn"])
