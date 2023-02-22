import boto3
import json
from datetime import datetime
import uuid

GET_RAW_PATH = "/test/get_user"
POST_RAW_PATH = "/test/create-new-user"
PUT_RAW_PATH = "/test/update-new-user"
table_name = 'new_users'
# Define the AWS access key ID and secret access key for the IAM user
aws_access_key_id = 'AKIASBKR2UWDIH5HHM4W'
aws_secret_access_key = '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'

def get_user_by_id(table, user_id):
    print("222user_id=", user_id, type(user_id))
    response = table.get_item(
        Key=user_id
    )
    print('ssss', response)
    response = {
        "id": str(response["Item"]["ID"]),
        "name": str(response["Item"]["name"]),
        "age": str(response["Item"]["age"]),
        "status_method": "Active"

    }
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }


def create_new_user(table, user_item):
    # gathering params
    new_user_id = str(uuid.uuid4())

    new_item = {
        'ID': new_user_id,
        'added': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'ITEM': user_item
    }

    response = table.put_item(
        Item=new_item
    )
    # make proper response
    response = {
        "entity_id": new_user_id,
        "name_user": user_item['name'],
        "status_in_db": "was successfully created"
    }

    return {
        'statusCode': 201,
        'body': json.dumps(response)
    }


def lambda_handler(event, context):
    print('event=', event)

    try:
        # Create a session with the IAM user credentials and connect to our table in dynamoDB
        session = boto3.Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )
        dynamodb = session.resource('dynamodb')  # resource лучше чем client(т.к. не нужно указьівать тип значения)
        table = dynamodb.Table(table_name)

        # our crud logic
        response = ""

        if event['rawPath'] == POST_RAW_PATH:

            # make clear dict from string
            raw_body_string = event["body"]
            body_string = raw_body_string.replace("\n", "").replace(" ", "").replace('\\"', '\"').replace("'", "\"")

            user_item = json.loads(body_string)
            response = create_new_user(table, user_item)

        elif event['rawPath'] == GET_RAW_PATH:

            user_id = event['queryStringParameters']['ID']

            response = get_user_by_id(table, user_id)

        return response

    except Exception as err:
        print(err)
        return {
            'statusCode': 400,
            'body': json.dumps("<h1><font color=red>my custom Error!</font><br><br>")
        }
