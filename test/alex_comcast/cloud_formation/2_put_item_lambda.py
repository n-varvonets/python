import boto3
import json
from datetime import datetime
import uuid

GET_RAW_PATH = ""
POST_RAW_PATH = "/test/create-update_new-user"


def create_new_user(table, user_item):

    # gathering params
    user_id = str(uuid.uuid4())

    new_item = {
        'ID': user_id,
        'added': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'ITEM': user_item
    }

    response = table.put_item(
        Item=new_item
    )
    # make proper response
    response = {
        "entity_id": user_id,
        "name_user": user_item['name'],
        "status_in_db": "was successfully created"
    }

    return response


def lambda_handler(event, context):
    print('event=', event)

    try:
        # Define the AWS access key ID and secret access key for the IAM user
        aws_access_key_id = 'AKIASBKR2UWDIH5HHM4W'
        aws_secret_access_key = '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'

        # Create a session with the IAM user credentials and connect to our table in dynamoDB
        session = boto3.Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )
        dynamodb = session.resource('dynamodb')  # resource лучше чем client(т.к. не нужно указьівать тип значения)
        table_name = 'new_users'
        table = dynamodb.Table(table_name)

        # make clear dict from string
        raw_body_string = event["body"]
        body_string = raw_body_string.replace("\n", "").replace(" ", "").replace('\\"', '\"').replace("'", "\"")
        user_item = json.loads(body_string)

        response = ""
        if event['rawPath'] == POST_RAW_PATH:
            response = create_new_user(table, user_item)

        return {
            'statusCode': 200,
            'body': json.dumps(response)
        }
    except Exception as err:
        print(err)
        return {
            'statusCode': 400,
            'body': json.dumps("<h1><font color=red>my custom Error!</font><br><br>")
        }
