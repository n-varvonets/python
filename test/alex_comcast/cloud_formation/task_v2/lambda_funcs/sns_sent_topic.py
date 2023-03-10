import boto3
import json
import decimal


TABLE_NAME = 'users'
TOPIC_REGION = 'ca-central-1'
AWS_ACC_ID = '140294923654'
SNS_TOPIC = 'SNS-users-topic'

# Define the AWS access key ID and secret access key for the IAM user
aws_access_key_id = 'AKIASBKR2UWDIH5HHM4W'
aws_secret_access_key = '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'


def remove_decimal(obj):
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    elif isinstance(obj, dict):
        return {k: remove_decimal(v) for k, v in obj.items()}
    elif isinstance(obj, (list, tuple)):
        return [remove_decimal(x) for x in obj]
    else:
        return obj


def lambda_handler(event, context):
    response = {}
    try:

        # Create a session with the IAM user credentials and connect to our table in dynamoDB
        session = boto3.Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )
        dynamodb = session.resource('dynamodb')  # resource лучше чем client(т.к. не нужно указьівать тип значения)
        table = dynamodb.Table(TABLE_NAME)

        user_id = event['pathParameters']['id']
        key = {"ID": user_id}
        raw_user = table.get_item(Key=key)
        item_without_decimals = remove_decimal(raw_user["Item"])
        response['item_data'] = item_without_decimals

        sns = session.resource('sns')
        # Выбираем тему SNS по ее имени, где :140294923654: -  (AWS account ID), а имя топика даешь при создании стека в cloudfrom
        topic = sns.Topic('arn:aws:sns:' + TOPIC_REGION + ':' + AWS_ACC_ID + ':' + SNS_TOPIC)

        # Опубликовываем сообщение в SNS топик
        topic.publish(Message=json.dumps(item_without_decimals))

        response['status'] = "successfully published"

        return {
            'statusCode': 200,
            'body': json.dumps(response)
        }

    except Exception as err:
        print(err)
        return {
            'statusCode': 404,
            'body': json.dumps("Item Not Found in DB")
        }
