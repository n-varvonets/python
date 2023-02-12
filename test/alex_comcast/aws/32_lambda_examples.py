# documentation dor all methods of boto3 lib in aws services
# https://boto3.amazonaws.com/v1/documentation/api/latest/index.html
# As an example there you can see 2 lamda func

import boto3, json


def lambda_handler(event, context):
    """Lambda func to list S3 Buckets"""
    print(event, context)
    myS3 = boto3.client('s3')
    try:
        result = myS3.list_buckets()
        print(f"result {result}")
        output = ""
        for bucket in result["Buckets"]:
            output = output + bucket["name"] + "<br>"
        return{
            'statusCode': 200,
            'body': json.dumps("<h1><font color=green>S3 Buckets List:<font><br><br>" + output)
        }
    except:
        return{
            'statusCode': 400,
            'body': json.dumps("<h1><font color=red>my custom Error!</font><br><br>")
        }


# 2nd lamda func
import boto3, os, json, time


AWS_DEFAULT_REGION = "ca-central-1"
os.environ['AWS_DEFAULT_REGION'] = AWS_DEFAULT_REGION
bucket_name = 'lambda.created.me - ' + str(time.time())


def lambda_handler_(event, context):
    """Lambda func to  create S3 Buckets"""
    myS3 = boto3.client('s3')
    try:
        result = myS3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': AWS_DEFAULT_REGION
            }
        )
        return{
            'statusCode': 200,
            'body': json.dumps("<h1><font color=green>S3 Created Successfully:</font><br><br>" )
        }
    except:
        return{
            'statusCode': 400,
            'body': json.dumps("<h1><font color=red>my custom Error!</font><br><br>")
        }





