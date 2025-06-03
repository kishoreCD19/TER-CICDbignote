import boto3

# Initialize clients
sqs = boto3.client('sqs', region_name='us-east-1')
ec2 = boto3.client('ec2', region_name='us-east-1')

# SQS Queue Check
def check_sqs(queue_url):
    response = sqs.get_queue_attributes(
        QueueUrl=queue_url,
        AttributeNames=['ApproximateNumberOfMessages']
    )
    print(f"Messages in queue: {response['Attributes']['ApproximateNumberOfMessages']}")

# EC2 Instance Health Check
def check_ec2_health():
    statuses = ec2.describe_instance_status(IncludeAllInstances=True)
    for status in statuses['InstanceStatuses']:
        print(f"Instance: {status['InstanceId']} - Health: {status['InstanceStatus']['Status']}")

if __name__ == "__main__":
    check_sqs('https://sqs.us-east-1.amazonaws.com/123456789012/my-queue')  # Replace with your queue URL
    check_ec2_health()
