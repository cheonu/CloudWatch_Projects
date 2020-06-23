import boto3
aws_mag_con=boto3.session.Session(profile_name="root")
s3_con_cli=aws_mag_con.client(service_name="s3",region_name="us-east-1")
response=s3_con_cli.list_buckets()
for each_bucket in response['Buckets']:
	print(each_bucket['Name'])

