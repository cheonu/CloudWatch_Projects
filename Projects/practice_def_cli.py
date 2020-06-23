import boto3
aws_mag_con=boto3.session.Session(profile_name=“root”)
iam_con_cli=aws_mag_con.client(service_name=“iam”,region_name=“us-east_1)
#ec2_con_cli=aws_mag_con.client(service_name=“ec2”,region_name=“us-east_1)
#s3_con_cli=aws_mag_con.client(service_name=“s3”,region_name=“us-east_1)

response=iam_con_cli.list_users()
print(response)





