import boto3
import datetime
aws_mag_con=boto3.session.Session(profile_name="chedev")
ec2_con_re=aws_mag_con.resource(service_name="ec2",region_name="us-east-2")
'''
for each_snap in ec2_con_re.snapshots.filter(OwnerIds=["967250075457"]):
    print(each_snap)
'''
'''
f_size={'Name': 'volume-size','Values': ['10',]}
for each_snap in ec2_con_re.snapshots.filter(OwnerIds=["967250075457"],Filters=[f_size]):
    print(each_snap)
'''
today=datetime.datetime.now()
start_time=str(datetime.datetime(today.year, today.month,today.day,4,15,44))
f_size={'Name': 'volume-size','Values': ['8',]}
for each_snap in ec2_con_re.snapshots.filter(OwnerIds=["967250075457"],Filters=[f_size]):
    print(each_snap.start_time.strftime("%Y %M %D %H:%M:%S"))
