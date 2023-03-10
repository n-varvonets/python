import boto3
import json
from datetime import datetime
import uuid


def get_table_with_creds():

    # Define the AWS access key ID and secret access key for the IAM user
    aws_access_key_id = 'AKIASBKR2UWDIH5HHM4W'
    aws_secret_access_key = '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'

    TABLE_NAME = 'users'

    # Create a session with the IAM user credentials and connect to our table in dynamoDB
    session = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )
    dynamodb = session.resource('dynamodb')  # resource лучше чем client(т.к. не нужно указьівать тип значения)
    table = dynamodb.Table(TABLE_NAME)

    return table


def lambda_handler(event, context):
    try:
        # make clear dict from string
        raw_body_string = event["body"]
        body_string = raw_body_string.replace("\n", "").replace(" ", "").replace('\\"', '\"').replace("'", "\"")
        user_item = json.loads(body_string)

        new_item = {
            'ID': str(uuid.uuid4()),
            'added': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'ITEM': user_item
        }

        table = get_table_with_creds()
        table.put_item(Item=new_item)

        # for cloudwatch log-group
        print("--- Method POST --- New user was created at " + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + " with data" + str(new_item))

        return {
            'statusCode': 201,
            'body': json.dumps(new_item)
        }

    except Exception as err:
        print("Occur an err=", err)
        return {
            'statusCode': 400,
            'body': json.dumps("There some wrong data. Check in cloudwatch it.")
        }

