import boto3
aws_mag_con=boto3.session.Session(profile_name="chedev")
ec2_con_re=aws_mag_con.resource(service_name="ec2", region_name="us-east-2")
ec2_con_cli=aws_mag_con.client(service_name="ec2", region_name="us-east-2")

'''
#listing instance IDs from ec2 instances
for each_in in ec2_con_re.instances.all():
    print(each_in.id)
#listing instance IDs from ec2 instances using append
all_instance_ids=[]
for each_in in ec2_con_re.instances.all():
    all_instance_ids.append(each_in.id)
waiter=ec2_con_cli.get_waiter("instance_running")
print("starting all instances")
ec2_con_re.instances.start()
waiter.wait(InstanceIds=all_instance_ids)
print("Instances are up and running")
'''

np_servs_ids=[]
f1={"Name": "tag:name", "Values": ["Prod_Server"]}
for each_in in ec2_con_re.instances.filter(Filters=[f1]):
    np_servs_ids.append(each_in.id)
print(np_servs_ids)
