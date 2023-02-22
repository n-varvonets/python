import boto3
import json
import decimal


TABLE_NAME = 'new_users'

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
    try:

        # Create a session with the IAM user credentials and connect to our table in dynamoDB
        session = boto3.Session(
            aws_access_key_id=aws_access_key_id,
            aws_secret_access_key=aws_secret_access_key
        )
        dynamodb = session.resource('dynamodb')  # resource лучше чем client(т.к. не нужно указьівать тип значения)
        table = dynamodb.Table(TABLE_NAME)

        user_id = event['queryStringParameters']
        raw_user = table.get_item(Key=user_id)
        item_without_decimals = remove_decimal(raw_user["Item"])

        sns = session.resource('sns')
        # Выбираем тему SNS по ее имени
        topic = sns.Topic('arn:aws:sns:ca-central-1:140294923654:ITEM-new-users')

        # Опубликовываем сообщение в SNS топик
        topic.publish(Message=json.dumps(item_without_decimals))
        return {
            'statusCode': 200,
            'body': json.dumps("Topic was successfully published")
        }

    except Exception as err:
        print(err)
        return {
            'statusCode': 404,
            'body': json.dumps("Item Not Found in DB")
        }


# ВАЖНО: не забудь настроить права для user-a IAM на топик в policy
# {
#     "Version": "2012-10-17",
#     "Statement": [
#         {
#             "Effect": "Allow",
#             "Action": [
#                 "sns:Publish"
#             ],
#             "Resource": "arn:aws:sns:us-east-1:123456789012:MyTopic"
#         }
#     ]
# }