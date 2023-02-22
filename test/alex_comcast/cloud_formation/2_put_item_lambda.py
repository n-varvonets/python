import boto3
import json
from datetime import datetime
import uuid


def update_user(user_item):
    # print('user_item=', user_item, type(user_item)) #

    # Define the AWS access key ID and secret access key for the IAM user
    aws_access_key_id = 'AKIASBKR2UWDIH5HHM4W'
    aws_secret_access_key = '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'

    # Create a session with the IAM user credentials
    session = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )
    dynamodb = session.resource('dynamodb')  # resource лучге тем,
    # что не надо указьівать каждтій раз тип данньіх с значению как {'S': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

    table_name = 'new_users'
    table = dynamodb.Table(table_name)

    # gathering params
    # todo реализовать логику, если метод put, то не трограем дату добавления
    if True:  # если create user -  удием в усвловие
        added_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    user_id = str(uuid.uuid4())

    new_item = {
        'ID': user_id,
        'added': added_date,
        'updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'ITEM': user_item
    }

    response = table.put_item(
        Item=new_item
    )

    return response


def lambda_handler(event, context):

    # get params
    raw_body_string = event["body"]
    body_string = raw_body_string.replace("\n", "").replace(" ", "").replace('\\"', '\"').replace("'", "\"")
    user_item = json.loads(body_string)

    response = update_user(user_item)

    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
