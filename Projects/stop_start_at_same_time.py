import boto3
aws_mag_con=boto3.session.Session(profile_name="root")
ec2_con_re=aws_mag_con.resource(service_name="ec2",region_name="us-east-1")
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name="us-east-1")
'''
all_instances_ids=[]
for each_in in ec2_con_re.instances.all():
	all_instances_ids.append(each_in.id)
#print(dir(ec2_con_re.instances))
waiter=ec2_con_cli.get_waiter('instance_running')
print("Starting all instances ......")
ec2_con_re.instances.start()
waiter.wait(InstanceIds=all_instances_ids)
print("your all instaces are up and running")
'''
'''
np_sers_ids=[]
f1={"Name": "tag:Name", "Values":['Non_Prod']}
for each_in in ec2_con_re.instances.filter(Filters=[f1]):
	np_sers_ids.append(each_in.id)

print(np_sers_ids)
