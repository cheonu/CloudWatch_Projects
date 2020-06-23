#!/usr/bin/env
import boto3
from pprint import pprint

session=boto3.session.Session(profile_name="chedev")
ec2_client=session.client(service_name="ec2",region_name="us-east-2")
list_of_volids=[]
f_prod_backup={"Name":"tag:Prod","values":["backup","Backup"]}
#for each_vol in ec2_client.describe_volumes()["Volumes"]:
#    list_of_volids.append(each_vol["VolumeId"])

paginator = ec2_client.get_paginator('describe_volumes')
for each_page in paginator.paginate(Filters=[f_prod_backup]):
    pprint(each_page)

print("The list of volids are: ",list_of_volids)
