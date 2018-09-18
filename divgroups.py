import boto3
import datetime
def lambda_handler(event, context):
    ec2=boto3.resource('ec2')
    d = datetime.date.today()
    x=d.strftime('%m')
    x='AMI_%s' % x
    
    
    def count_instances(ec2):
        total_instances = 0
        instances = ec2.instances.filter(          Filters=[
                {
                    'Name': 'instance-state-name',
                    'Values': [
                        'running',
                    ]
                }
            ])
        for _ in instances:
            total_instances += 1
        return total_instances
    num_instances = count_instances(ec2)
    ec2client = boto3.client('ec2')
    response = ec2client.describe_images(
        Filters=[
            {
                'Name': 'name',
                'Values': [
                    '{0}'.format(x),    
                ]
                
            }
        ]
        
    )
    
    x=response["Images"]
    if (len(x) != 0):
       
        y=(x[0]["ImageId"])
    

        response = ec2client.describe_instances(
            Filters=[
                {
                    'Name': 'image-id',
                    'Values': [
                        '{}'.format(y),
                    ]
                }
            ]
        )
        instancelist = []
        for reservation in (response["Reservations"]):
            for instance in reservation["Instances"]:
                instancelist.append(instance["InstanceId"])
        x=len(instancelist)
        x=x-1
        y=x/3
        temp1=y*2
        temp2=y*3
        rem=x%3
        list1= []
        list2= []
        list3= []
        rem_list=[]
        print "3 groups created with %s number of instances" % (y)
        print (rem)
        i=0
        while i <= x:
            while i <= y:
                list1.append(instancelist[i])
                i += 1
            while (i > y and i <= temp1):
                list2.append(instancelist[i])
                i += 1
            while (i > temp1 and i <= temp2):
                list3.append(instancelist[i])
                i += 1
            while (i > temp2 and i <= x):
                rem_list.append(instancelist[i])
                i += 1
        
    
    
        print (list1)
        print (list2)
        print (list3)
    
        if (len(list1) != 0):
            response = ec2client.create_tags(Resources=list1,Tags=[{
                'Key': 'PacthingGroup',
                'Value': 'GroupA'
            },]
            )
            print (response)
    
        if (len(list2) != 0):
            response = ec2client.create_tags(Resources=list2,Tags=[{
                'Key': 'PacthingGroup',
                'Value': 'GroupB'
            },]
            )
    
        if (len(list3) != 0):
            response = ec2client.create_tags(Resources=list3,Tags=[{
                'Key': 'PacthingGroup',
                'Value': 'GroupC'
            },]
            )
    
    
    
     
        print "Observed %s instances running " % (num_instances)
    
