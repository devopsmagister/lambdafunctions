import boto3

def lambda_handler(event, context):
    try:
        # Create an RDS client
        rds = boto3.client('rds')

        # Call the RDS API to describe instances
        response = rds.describe_db_instances()
        instance_status = []

        for instance in response['DBInstances']:
            instance_status.append("DB Name: {0}     DB Status: {1}     DB AZ: {2}".format(instance['DBInstanceIdentifier'], instance['DBInstanceStatus'], instance['AvailabilityZone']))

        return {
            'statusCode': 200,
            'RDS Details': instance_status
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': f"Error: {str(e)}"
        }
