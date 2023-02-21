import boto3, json
from boto3.dynamodb.conditions import Key


def lambda_handler(event, context):
    # print('event=', event)
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

        # get raw body
        raw_body_string = event["body"]

        # Remove newline characters and spaces from the string
        clear_string = raw_body_string.replace("\n", "").replace(" ", "")

        # Use json.loads to parse the string and create a dictionary
        new_user = json.loads(clear_string)

        # Define the item to be added to the table
        items = {
            'id': {'S': new_user['id']},
            'name': {'S': new_user['name']}
        }
        print('---items---', items)

        # Add the item to the table
        response = dynamodb.put_item(
            TableName=table_name,
            Item=items
        )
        # print('------', response, type(response))
        response_object = {}
        response_object["statusCode"] = 200
        response_object["body"] = json.dumps({f"{new_user['name']}": "was successfully created"})

        return response_object
    except Exception as err:
        print(err)
        return {
            'statusCode': 400,
            'body': json.dumps("<h1><font color=red>my custom Error!</font><br><br>")
        }