import boto3

def lambda_handler(event, context):
    # Replace 'us-west-2' with your desired AWS region
    region = 'us-west-2'

    try:
        # Create a boto3 RDS client for the specified region
        rds_client = boto3.client('rds', region_name=region)

        # Replace 'your_db_instance_identifier' with your actual RDS DB instance identifier
        db_instance_identifier = 'your_db_instance_identifier'

        # Describe the RDS instance
        response = rds_client.describe_db_instances(DBInstanceIdentifier=db_instance_identifier)

        print(f"DB Response: {response}")

        # You can return the details as a response if needed
        return {
            "statusCode": 200,
            "body": {
                "DB response": response
            }
        }

    except Exception as e:
        # Handle any errors
        return {
            "statusCode": 500,
            "body": str(e)
        }

