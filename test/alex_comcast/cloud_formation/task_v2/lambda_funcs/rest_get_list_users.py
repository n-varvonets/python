import boto3
import json
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
    LIMIT_LIST_ITEMS = 100  # by my logic I set max 1000 items per 1 req - for prevalence overload

    try:
        table = get_table_with_creds()
        raw_response_with_decimal = table.scan(Limit=LIMIT_LIST_ITEMS)
        response = convert_decimals_to_floats(raw_response_with_decimal)
        response["Items"].extend([{"Count": response['Count']}])  # add len els of list

        return {
            'statusCode': 200,
            'body': json.dumps(response["Items"])
        }

    except Exception as err:
        print("Occur an err=", err)
        return {
            'statusCode': 400,
            'body': json.dumps("There some wrong data. Check in cloudwatch it.")
        }

