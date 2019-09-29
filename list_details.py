import boto3
from termcolor import colored

ec2 = boto3.resource('ec2')

for i in ec2.instances.all():

    print("Id: {0}\tState: {1}\tPub. DNS: {2}\tAMI ID: {3}\tInstance Type: {4}".format(
        colored(i.id, 'cyan'),
        colored(i.state['Name'], 'green'),
        colored(i.public_dns_name, 'blue'),
        colored(i.image_id, 'yellow'),
        colored(i.instance_type,'red')
    ))

