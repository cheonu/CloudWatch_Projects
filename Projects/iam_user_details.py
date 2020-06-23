import boto3
import datetime
session=boto3.session.Session(profile_name="chedev")
iam_con_re=session.resource(service_name="iam")
iam_con_cli=session.client(service_name="iam")
'''
iam_user_ob=iam_con_re.User("chedev")

print(iam_user_ob.user_id,iam_user_ob.user_name,iam_user_ob.create_date.strftime("%Y-%M-%D"))
'''

grp_ob=iam_con_cli.list_groups()
print(grp_ob)



