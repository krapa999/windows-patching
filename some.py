import json
import boto3

def lambda_handler(event, context):
    # TODO implement
    #client=boto3.client('ssm')
    #response=client.describe_instance_information()
    
    #ec2r = boto3.resource('ec2', region_name='us-east-1')
    
    #ssm_instance=[]
    #for r in response['InstanceInformationList']:
        # ssm_instance.append('{0}'.format(r['InstanceId']))
    
    #print ssm_instance
    
    ##ec2re=boto3.resource('ec2')
    #instance=ec2re.Instance('{0}'.format(ssm_instance[0]))
    #role_arn=instance.iam_instance_profile
    
    #print role_arn
    
    
    def subtract_lists(a, b):
        """ Subtracts two lists. Throws ValueError if b contains items not in a """
        # Terminate if b is empty, otherwise remove b[0] from a and recurse
        return a if len(b) == 0 else [a[:i] + subtract_lists(a[i+1:], b[1:]) 
                                  for i in [a.index(b[0])]][0]
    
    total=[]
    all_running_instances = [i for i in ec2r.instances.filter(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])]
    for instance in all_running_instances:
        total.append('{0}'.format(instance.id))
        
    print total
    
    print ssm_instance
    
    #instancelist=list(set(total)-set(ssm_instance))
    
    print instancelist
    
    #instancelist= subtract_lists(total, ssm_instance)
    
    #print instancelist
    client = boto3.client('ec2')

    response=client.describe_iam_instance_profile_associations(
        Filters=[
            {
                'Name': 'state',
                'Values': [
                    'associated',
                ]
            },
            {
                'Name': 'instance-id',
                'Values': total
            }
            
            ]
        )
    print response
    
    iam_instance=[]
    for r in response['IamInstanceProfileAssociations']:
        iam_instance.append('{0}'.format(r['InstanceId']))
        
    print iam_instance
    
    
    instancelist1= list(set(total)-set(iam_instance))   
    
    print instancelist1
    
    #print (role_arn['Arn'])
    #print x
    y=len(instancelist1)
    if (x != 0):
        for i in instancelist1:
            try:
                client.associate_iam_instance_profile(
                    IamInstanceProfile={
                        'Arn': '{0}'.format(role_arn['Arn']),
                        'Name': 'CW'
                        },
                        InstanceId='{0}'.format(i)
                )
            except Exception as e:
                print e
            
    
    
    
    
