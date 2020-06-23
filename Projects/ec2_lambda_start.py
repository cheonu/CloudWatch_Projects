import boto3

def lambda_handler(event, context):
    ec2_con_re=boto3.resource(service_name="ec2",region_name="us-east-2")
    test_env_filter={"Name" :"tags:env", "Values":["test"]}
    for each_in in ec2_con_re.instances.filter(Filters=[]):
        print(each_in.id)