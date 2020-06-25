#Add a target to a rule using put_targets

import boto3
cloudwatch_events=boto3.client("events")

response = cloudwatch_events.put_targets(
    Rule='cloud_consult_event',
    Targets=[
        {
            'Id': 'CloudWatch_events_function',
            'Arn': 'arn:aws:logs:us-east-1:967250075457:log-group:/aws/lambda/CloudWatch_events_function:*',
        },
    ]
)

print(response)