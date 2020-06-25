
import json

import boto3

cloudwatch_events=boto3.client('events')

response = cloudwatch_events.put_events(
    Entries=[
        {
            'Source': 'CloudWatch_events_function',
            'Resources': [
                'arn:aws:logs:us-east-1:967250075457:log-group:/aws/lambda/CloudWatch_events_function:*',
            ],
            'DetailType': 'appRequestSubmitted',
            'Detail': json.dumps({'key1':'value1','key2':'value2'}),
        },
    ]
)

print(response["Entries"])
