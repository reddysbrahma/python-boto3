import boto3
session = boto3.Session()
ec2_re = session.resource(service_name="ec2")
for i in ec2_re.instances.all():
    print(i.public_dns_name,i.id,i.state["Name"],i.image_id)

ec2 = boto3.resource('ec2')

print("Trying to find Running Instances")
instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

for instance in instances:
    print(instance.id, instance.instance_type)

print("Trying to find Stopped Instances")
instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}])

for instance in instances:
    print(instance.id, instance.instance_type)

print("Trying to find Terminated Instances")
instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['terminated']}])

for instance in instances:
    print(instance.id, instance.instance_type)