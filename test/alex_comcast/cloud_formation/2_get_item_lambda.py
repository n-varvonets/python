import boto3, json
from boto3.dynamodb.conditions import Key


def lambda_handler(event, context):
    # print('event --- ', event)
    try:
        # Define the AWS access key ID and secret access key for the IAM user
        aws_access_key_id = 'AKIASBKR2UWDIH5HHM4W'
        aws_secret_access_key = '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'

        # Create a session with the IAM user credentials
        session = boto3.Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )

        # Create a DynamoDB client using the session
        dynamodb = session.client('dynamodb')

        # Define the table name
        table_name = 'Users'

        # Add the item to the table
        user_id = event['queryStringParameters']['id']
        user_name = event['queryStringParameters']['name']

        response = dynamodb.get_item(
            TableName=table_name,
            Key={
                'id': {'S': str(user_id)},
                'name': {'S': str(user_name)}
            }
        )
        # print("response=", response)
        response_body = {
            "id": str(response["Item"]["id"]),
            "name": str(response["Item"]["name"]),
            "status_method": "Active"

        }
        return {
            'statusCode': 200,
            'body': json.dumps(response_body)
        }

    except Exception as err:
        print(err)
        return {
            'statusCode': 400,
            'body': json.dumps("<h1><font color=red>my custom Error!</font><br><br>")
        }