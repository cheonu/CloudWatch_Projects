import boto3

aws_mag_con=boto3.session.Session(profile_name="chedev")

ec2_con_re=aws_mag_con.resource(service_name="ec2",region_name='us-east-2')
ec2_con_cli=aws_mag_con.client(service_name="ec2",region_name="us-east-2")
'''
f1_ebs_vol={"Name":"status","Values":["available"]}
for each_volume in ec2_con_re.volumes.filter(Filters=[f1_ebs_vol]):
    if not each_volume.tags:
        print(each_volume.id, each_volume.state, each_volume.tags)
        print("Deleting all unused volumes.......")
        each_volume.delete()

print("Deleted all unused tags")
'''
for each_item in ec2_con_cli.describe_volumes()['Volumes']:
    if not "Tags" in each_item and each_item['State']=="available":
        print('Deleting ',each_item["VolumeId"])
        ec2_con_cli.delete_volume(VolumeId=each_item["VolumeId"])

print("Deleting all unused volumes")


