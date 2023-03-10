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
        # make clear dict from string
        raw_body_string = event["body"]
        body_string = raw_body_string.replace("\n", "").replace(" ", "").replace('\\"', '\"').replace("'", "\"")
        user_item = json.loads(body_string)
        user_id = event["pathParameters"]["id"]

        table = get_table_with_creds()
        key = {'ID': user_id}
        raw_previous_user_data = table.get_item(Key=key)
        previous_user_data = convert_decimals_to_floats(raw_previous_user_data)

        updated_user_item = {
            'ID': user_id,
            'added': previous_user_data['Item']['added'],
            'updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'ITEM': user_item
        }

        table.put_item(Item=updated_user_item)

        print("--- Method PUT --- User with id=" + user_id + " was updated at " + datetime.now().strftime('%Y-%m-%d %H:%M:%S')
              + ". Current state of item: " + str(previous_user_data["Item"])
              + ". Previous state of item: " + str(updated_user_item))

        return {
            'statusCode': 201,
            'body': json.dumps(updated_user_item)
        }
    except Exception as err:
        print(err)
        return {
            'statusCode': 400,
            'body': json.dumps("Item was not found. Check passed id of item.")
        }

