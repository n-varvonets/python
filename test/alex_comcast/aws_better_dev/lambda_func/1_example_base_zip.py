import json
# <api-lambda_func-url-of-recourse-not-method>?transactionId=4&type=PURCHASE&amount=550
# https://in7hefeaqg.execute-api.ca-central-1.amazonaws.com/test_env/transstions?transactionId=4&type=PURCHAS&amount=550

print('Loading function --')


def lambda_handler(event, context):
        try:
            print('  ----  event is.. ', event)
            # 1. Parse out query string params
            transaction_id = event["queryStringParameters"]["transactionId"]
            transaction_type = event["queryStringParameters"]["type"]
            transaction_amount = event["queryStringParameters"]["amount"]

            print("transaction_id=" + transaction_id)
            print("transaction_type=" + transaction_type)
            print("transaction_amount=" + transaction_amount)

            # 2. Construct the body of the response object
            transaction_response = {
                "transaction_id": transaction_id,
                "transaction_type": transaction_type,
                "transaction_amount": transaction_amount
            }

            # 3. Construct http response
            # response_object = {
            #     "statusCode": 200,
            #     "headers": transaction_type,
            #     f"transaction_amount[]": transaction_amount
            # }
            response_object = {}
            response_object["statusCode"] = 200
            response_object["body"] = json.dumps(transaction_response)

            return response_object
        except Exception as err:
            print(err)
            return{
                'statusCode': 400,
                'body': json.dumps("<h1><font color=red>my custom Error!</font><br><br>")
            }


"""Feature difference"""
#  №|       feature                       |      REST      |      HTTP      |   description
# ----------------------------------------------------------------------------------------------------------------------------------
#  1| Usage Plans & API Keys              |      yes       |       no       | assign a key to specific user by his plan of our app
#  2| API Caching                         |      yes       |       no       | make our service calls faster by caching them
#  3| Testing / Mocking                   |      yes       |       no       |
#  4| Request Validation & transformation |      no        |       yes      |
#  5| ALB Integration                     |      no        |       yes      | App load balancing for services (EC2)
# -----------------------------------------------------------------------------------------------------------------------------------
"""WARN: Use HTTP *everytime*, except when the feature isn't supported"""

