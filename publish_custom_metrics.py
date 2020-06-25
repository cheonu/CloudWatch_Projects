import boto3

cloudwatch=boto3.client("cloudwatch")

response = cloudwatch.put_metric_data(
    Namespace='SITE/TRAFFIC',
    MetricData=[
        {
            'MetricName': 'PAGES_VISITED',
            'Dimensions': [
                {
                    'Name': 'UNIQUE_PAGES',
                    'Value': 'URLS'
                },
            ],
            'Unit': 'None',
            'Value': 1.0
        },
    ]
)

print(response)