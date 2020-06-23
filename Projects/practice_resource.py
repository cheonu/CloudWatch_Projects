import boto3

aws_mag_con=boto3.session.Session(profile_name="root")

iam_con_re=aws_mag_con.resource(service_name="iam",region_name="us-east-2")
ec2_con_re=aws_mag_con.resource(service_name="ec2",region_name="us-east-2")
s3_con_re=aws_mag_con.resource(service_name="s3",region_name="us-east-2")

for each_item in ec2_con_re.instances.all():
	print(each_item.instance_id)
	



