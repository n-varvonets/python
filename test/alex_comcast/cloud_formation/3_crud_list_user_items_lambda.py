import boto3
import json
from datetime import datetime
import uuid
from decimal import Decimal

# mockdata
# from crud_data_events import event_get_user as event


TABLE_NAME = 'users'
LIMIT_LIST_ITEMS = 1000  # by my logic I set max 1000 items per 1 req - for prevalence overload

# Define the AWS access key ID and secret access key for the IAM user
aws_access_key_id = 'AKIASBKR2UWDIH5HHM4W'
aws_secret_access_key = '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'


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
            'body': json.dumps("Object Not Found, check user ID or correctness the url")
        }


def delete_user(table, user_id):
    key = {'ID': user_id}
    response = table.delete_item(Key=key)
    print('del----', response)
    return


def update_user_item(table, user_id, new_item):
    key = {'ID': user_id}
    response = table.get_item(Key=key)

    print("response=", response)

    updated_user_item = {
        'ID': user_id,
        'added': response['Item']['added'],
        'updated': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        'ITEM': new_item
    }

    print("updated_user_item=", updated_user_item)

    try:
        table.put_item(Item=updated_user_item)

        print("updated_user_item=", updated_user_item)

        response = {
            "status_code": 200,
            "Item": updated_user_item
        }
        return response

    except Exception as e:
        print('--- Method POST --- Error=', e, updated_user_item)
        return {"status_code": 404}


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
        current_time_executing_func = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

        # our crud logic
        if event['httpMethod'] == "POST":

            # make clear dict from string
            raw_body_string = event["body"]
            body_string = raw_body_string.replace("\n", "").replace(" ", "").replace('\\"', '\"').replace("'", "\"")

            user_item = json.loads(body_string)
            response = create_new_user(table, user_item)

            print("--- Method POST --- New user '" + response['name_user'] + "' with id=" + response[
                "entity_id"] + " was created at " + current_time_executing_func)

            return {
                'statusCode': 201,
                'body': json.dumps(response)
            }

        elif event['httpMethod'] == "GET" and event['path'] != '/users':

            user_id = event['pathParameters']['id']
            response = get_user_by_id(table, user_id)
            return {
                'statusCode': 200,
                'body': json.dumps(response)
            }

        elif event['httpMethod'] == "PUT":

            # make clear dict from string
            raw_body_string = event["body"]
            body_string = raw_body_string.replace("\n", "").replace(" ", "").replace('\\"', '\"').replace("'", "\"")
            user_item = json.loads(body_string)
            user_id = event["pathParameters"]["id"]

            response = update_user_item(table, user_id=user_id, new_item=user_item['NEW_ITEM'])
            if response['status_code'] == 200:
                print(
                    "--- Method PUT --- User with id=" + user_id + " was updated at " + current_time_executing_func + ". Current state of item: " + str(
                        response["Item"]))

                return {
                    'statusCode': 201,
                    'body': json.dumps(response)
                }
            else:
                return {
                    'statusCode': response['status_code'],
                    'body': json.dumps("Item was not found. Check passed id of item.")
                }

        elif event['httpMethod'] == "DELETE":
            delete_user_id = event["pathParameters"]["id"]
            key = {'ID': delete_user_id}
            deleted_user = table.get_item(Key=key)

            delete_user(table, delete_user_id)

            print(
                "--- Method DELETE --- User with id=" + delete_user_id + " was deleted at " + current_time_executing_func + ". Data deleted item: " + str(
                    deleted_user))

            return {'statusCode': 204}

        elif event['httpMethod'] == "GET" and event['path'] == '/users':
            raw_response_with_decimal = table.scan(Limit=LIMIT_LIST_ITEMS)
            response = convert_decimals_to_floats(raw_response_with_decimal)

            return {
                'statusCode': 200,
                'body': json.dumps(response)
            }

    except Exception as err:
        print(err)
        return {
            'statusCode': 400,
            'body': json.dumps("<h1><font color=red>my custom Error!</font><br><br>")
        }

