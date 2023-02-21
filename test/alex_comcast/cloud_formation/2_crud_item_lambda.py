import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Users')

GET_RAW_PATH = "/get_user"
CREATE_RAW_PATH = "/create_user"
UPDATE_RAW_PATH = "/update_user"
DELETE_RAW_PATH = "/delete_user"


def lambda_handler(event, context):
    aws_access_key_id = 'AKIASBKR2UWDIH5HHM4W'
    aws_secret_access_key = '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'

    # Create a session with the IAM user credentials
    session = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    # Create a DynamoDB client using the session
    dynamodb = boto3.resource('dynamodb', region_name="ca-central-1")
    table_name = 'Users'
    table = dynamodb.Table(table_name)

    print('event ------- ', event)
    print('context ------- ', context)
    print('table ------- ', table)

    try:

        if event['rawPath'] == GET_RAW_PATH:
            item_id = event['queryStringParameters']['id']

            response = table.get_item(
                Key={
                    'id': str(item_id),
                    'name': 'John'
                }
            )
            print("response['Item']----------", response['Item'])

            body = json.dumps(response)
            return {
                'statusCode': 200,
                'body': body
            }
        elif event['rawPath'] == CREATE_RAW_PATH:
            # Define the item to be added to the table
            item = {
                'id': {'S': '125'},
                'name': {'S': 'John'}
            }

            # Add the item to the table
            response = dynamodb.put_item(
                TableName=table_name,
                Item=item
            )
            print('------', response, type(response))
            response_object = {}
            response_object["statusCode"] = 200
            response_object["body"] = json.dumps(response)
            return response_object

    except Exception as err:
        print('err=', err)
        return {
            'statusCode': 400,
            'body': json.dumps("<h1><font color=red>my custom Error!</font><br><br>")
        }


{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "dynamodb:GetItem",
            "Resource": "arn:aws:dynamodb:ca-central-1:140294923654:nbu3ap7ref/*/*"
        }
    ]
}


# {
#     "Version": "2012-10-17",
#     "Statement": [
#         {
#             "Effect": "Allow",
#             "Action": "dynamodb:GetItem",
#             "Resource": "arn:aws:dynamodb:ca-central-1:<ACCOUNT_ID>:table/Persons*"
#         }
#     ]
# }
#
# stage = https://nbu3ap7ref.execute-api.ca-central-1.amazonaws.com/test/users
# //stage/method/resource
# "Resource": "arn:aws:dynamodb:ca-central-1:<ACCOUNT_ID>:table/Persons*"
