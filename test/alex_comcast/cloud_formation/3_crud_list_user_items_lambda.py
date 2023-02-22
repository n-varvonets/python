import boto3
import json
from datetime import datetime
import uuid

GET_RAW_PATH = "/test/get_user"
LIST_RAW_PATH = "/test/list_users"
DELETE_RAW_PATH = "/test/delete_user"
POST_RAW_PATH = "/test/create-new-user"
PUT_RAW_PATH = "/test/update-new-user"

TABLE_NAME = 'new_users'
LIMIT_LIST_ITEMS = 1000  # by my logic I set max 1000 items per 1 req - for prevalence overload

# Define the AWS access key ID and secret access key for the IAM user
aws_access_key_id = 'AKIASBKR2UWDIH5HHM4W'
aws_secret_access_key = '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'


def get_user_by_id(table, user_id):
    key = {'ID': user_id}
    try:
        response = table.get_item(Key=key)
        response = {
            "name": str(response["Item"]["ITEM"]["name"]),
            "age": str(response["Item"]["ITEM"]["age"]),
            "status_method": "Active"

        }
        return response

    except:
        return {
            'statusCode': 404,
            'body': json.dumps("Not found. Check user ID")
        }


def delete_user(table, user_id):
    key = {'ID': user_id}
    table.delete_item(Key=key)
    return


def update_user_item(table, user_id, new_item):
    key = {'ID': user_id}
    response = table.get_item(Key=key)

    updated_user_item = {
        'ID': user_id,
        'added': response['Item']['added'],
        'updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'ITEM': new_item
    }

    table.put_item(Item=updated_user_item)
    response = {
        "requests_status": 'User was successfully updated',
        "ITEM": updated_user_item
    }

    return response


def create_new_user(table, user_item):
    # gathering params
    new_user_id = str(uuid.uuid4())

    new_item = {
        'ID': new_user_id,
        'added': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'ITEM': user_item
    }

    table.put_item(
        Item=new_item
    )
    # make proper response
    response = {
        "entity_id": new_user_id,
        "name_user": user_item['name'],
        "status_in_db": "was successfully created"
    }

    return response


def lambda_handler(event, context):
    try:
        # Create a session with the IAM user credentials and connect to our table in dynamoDB
        session = boto3.Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )
        dynamodb = session.resource('dynamodb')  # resource лучше чем client(т.к. не нужно указьівать тип значения)
        table = dynamodb.Table(TABLE_NAME)

        # our crud logic
        if event['rawPath'] == POST_RAW_PATH:

            # make clear dict from string
            raw_body_string = event["body"]
            body_string = raw_body_string.replace("\n", "").replace(" ", "").replace('\\"', '\"').replace("'", "\"")

            user_item = json.loads(body_string)
            response = create_new_user(table, user_item)
            return {
                'statusCode': 201,
                'body': json.dumps(response)
            }
        elif event['rawPath'] == GET_RAW_PATH:

            user_id = event['queryStringParameters']['ID']
            response = get_user_by_id(table, user_id)

            return {
                'statusCode': 200,
                'body': json.dumps(response)
            }
        elif event['rawPath'] == PUT_RAW_PATH:

            # make clear dict from string
            raw_body_string = event["body"]
            body_string = raw_body_string.replace("\n", "").replace(" ", "").replace('\\"', '\"').replace("'", "\"")
            user_item = json.loads(body_string)

            response = update_user_item(table, user_id=user_item['user_id'], new_item=user_item['NEW_ITEM'])

            return {
                'statusCode': 201,
                'body': response
            }
        elif event['rawPath'] == DELETE_RAW_PATH:
            delete_user_id = event['queryStringParameters']['ID']
            delete_user(table, delete_user_id)
            return {'statusCode': 204}

        elif event['rawPath'] == LIST_RAW_PATH:
            response = table.scan(Limit=LIMIT_LIST_ITEMS)
            print('list_users=', response, type(response))
            return response


    except Exception as err:
        print(err)
        return {
            'statusCode': 404,
            'body': json.dumps("<h1><font color=red>my custom Error!</font><br><br>")
        }
