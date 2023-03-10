import boto3
import json
from datetime import datetime
import uuid
from decimal import Decimal


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


def convert_decimals_to_floats(obj):
    """
    Recursively convert Decimal values to floats in a dictionary.
    """
    if isinstance(obj, dict):
        return {k: convert_decimals_to_floats(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [convert_decimals_to_floats(elem) for elem in obj]
    elif isinstance(obj, Decimal):
        return float(obj)
    else:
        return obj


def lambda_handler(event, context):
    try:
        table = get_table_with_creds()

        # get old item data for log group
        delete_user_id = event["pathParameters"]["id"]
        key = {'ID': delete_user_id}
        deleted_user = table.get_item(Key=key)

        # delete user
        user_id = event['pathParameters']['id']
        key = {'ID': user_id}
        table.delete_item(Key=key)

        print("--- Method DELETE --- User with id=" + delete_user_id + " was deleted at " + datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ". Data deleted item: " + str(deleted_user))

        return {'statusCode': 204}

    except Exception as err:
        print(err)
        return {
            'statusCode': 400,
            'body': json.dumps("Object Not Found, check user ID and DB. Check in cloudwatch it.")
        }

