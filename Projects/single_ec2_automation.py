import boto3
import time

aws_con=boto3.session.Session(profile_name="chedev")
ec2_con_re=aws_con.resource(service_name="ec2",region_name="us-east-2")
ec2_con_cli=aws_con.client(service_name="ec2",region_name="us-east-2")

'''
my_instance_object=ec2_con_re.Instance("i-01dd9dae87e37ff69")
print("starting given instance.....")
my_instance_object.start()
my_instance_object.wait_until_running()
print("Now your instance is up and running")
'''

'''
while True:
    my_instance_object=ec2_con_re.Instance("i-01dd9dae87e37ff69")
    print("ec2 instance is:  ",my_instance_object.state['Name'])
    if my_instance_object.state['Name']=="running":
        break
    print("Waiting to get running status")
    time.sleep(5)
    print("Now your instance is up and running")
'''

'''
print("Starting ec2 instance")
ec2_con_cli.start_instances(InstanceIds=["i-01dd9dae87e37ff69"])
waiter=ec2_con_cli.get_waiter('instance_running')
waiter.wait(InstanceIds=['i-01dd9dae87e37ff69'])
print("Now your ec2 instance is running")
'''

my_instance_object=ec2_con_re.Instance("i-01dd9dae87e37ff69")
print("starting given instance.....")
my_instance_object.start()
waiter=ec2_con_cli.get_waiter('instance_running')
waiter.wait(InstanceIds=['i-01dd9dae87e37ff69'])
print("Now your ec2 instance is running")