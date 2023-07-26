import boto3

def lambda_handler(event, context):
    # Initialize the ECS client
    ecs_client = boto3.client('ecs', region_name='your_region')

    try:
        # List all ECS clusters
        response = ecs_client.list_clusters()

        # Extract cluster ARNs from the response
        cluster_arns = response.get('clusterArns', [])

        return cluster_arns

    except Exception as e:
        return str(e)