import boto3
session = boto3.Session()
ec2_re = session.resource(service_name="ec2")
for i in ec2_re.instances.all():
    print(i.public_dns_name,i.id,i.state["Name"],i.image_id)