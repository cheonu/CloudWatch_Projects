import boto3

aws_mag_con_chedev=boto3.session.Session(profile_name="chedev")
sts_con_cli=aws_mag_con_chedev.client(service_name="sts",region_name="us-east-1")
response=sts_con_cli.get_caller_identity()
print(response['UserId'])
