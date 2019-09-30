import boto3
import xlwt


def get_ec2_list():

    session = boto3.Session()
    ec2_re = boto3.resource(service_name="ec2")
    wb  =xlwt.Workbook()
    ws = wb.add_sheet("Test2 Sheet")
    r=1
    ws.write(0,0,'DNS')
    ws.write(0,1,'ID')
    ws.write(0,2,'STATE')
    ws.write(0,3,'IMAGE_ID')
    for i in ec2_re.instances.all():
        print(i.public_dns_name, i.id, i.state["Name"], i.image_id)

        ws.write(r,0,i.public_dns_name)
        ws.write(r,1,i.id)
        ws.write(r,2,i.state["Name"])
        ws.write(r,3,i.image_id)
        r=r+1
    wb.save("output.xls")

#instance_list=[]
get_ec2_list()
#print list(instance_list)
#for i in instance_list.get_ec2_list():
 #   print (i.cl[0])
#instance_details = list(instance_list)
#for i in instance_list:
 #   print (instance_list)
#print(instance_list)

# session = boto3.Session()
# ec2_re = session.resource(service_name="ec2")
#wb = xlwt.Workbook()
#ws = wb.add_sheet("Test1 Sheet")
#ws.write(0,0,'instance_list')


# for i in ec2_re.instances.all():
#   print(i.public_dns_name,i.id,i.state["Name"],i.image_id)

# ec2 = boto3.resource('ec2')

# print("Trying to find Running Instances")
# instances = ec2.instances.filter(
#   Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

# for instance in instances:
#   print(instance.id, instance.instance_type)

# print("Trying to find Stopped Instances")
# instances = ec2.instances.filter(
#   Filters=[{'Name': 'instance-state-name', 'Values': ['stopped']}])

# for instance in instances:
#    print(instance.id, instance.instance_type)

# print("Trying to find Terminated Instances")
# instances = ec2.instances.filter(
#   Filters=[{'Name': 'instance-state-name', 'Values': ['terminated']}])

# for instance in instances:
#    print(instance.id, instance.instance_type)
