# DynamoDB stream - это функциональность DynamoDB, которая позволяет отслеживать изменения в таблицах DynamoDB.
# При каждом изменении данных в таблице, DynamoDB stream записывает новую версию записи в поток событий.
#
# Различные типы записей в потоке событий включают в себя:
#
#     Key attributes only: эта опция включает только первичные ключи записей, которые были изменены.
#     New image: этот тип записи включает все атрибуты новой версии записи после ее обновления.
#     Old image: этот тип записи включает все атрибуты предыдущей версии записи, которая была обновлена.
#     New and old images: этот тип записи включает как новую, так и старую версию записи.


# Amazon Kinesis Firehose - это сервис AWS, который позволяет быстро и легко загружать данные из разных источников
# в различные хранилища данных, в том числе в Amazon S3 и Amazon Elasticsearch. Для этого необходимо создать
# поток Firehose, который будет направлять логи в выбранное хранилище. При создании потока можно указать формат данных,
# например JSON, и настроить процесс трансформации данных.
#
# Для того чтобы использовать Kinesis Firehose для логирования в Lambda, необходимо настроить процесс записи логов
# в поток Firehose в функции Lambda. Это можно сделать с помощью библиотеки AWS SDK для Lambda. После того как логи
# будут направлены в поток Firehose, они будут автоматически сохранены в выбранное хранилище данных и будут
# доступны для анализа и мониторинга.


# не забудь добавить еще Pilicy:  AWSLambdaDynamoDBExecutionRole
# {
#     "Version": "2012-10-17",
#     "Statement": [
#         {
#             "Effect": "Allow",
#             "Action": [
#                 "dynamodb:DescribeStream",
#                 "dynamodb:GetRecords",
#                 "dynamodb:GetShardIterator",
#                 "dynamodb:ListStreams",
#                 "logs:CreateLogGroup",
#                 "logs:CreateLogStream",
#                 "logs:PutLogEvents"
#             ],
#             "Resource": "*"
#         }
#     ]
# }

import json
import boto3


def handle_create_user(record):
    print("------1.a.CREATE method start with eventID=" + record['eventID'] + "---------")
    # a. get newImage content
    new_image = record['dynamodb']['NewImage']
    # b. parse the values
    time_created = new_image["added"]["S"]
    user_id = new_image["ID"]["S"]
    user_item = new_image["ITEM"]["M"]
    user_name = user_item["name"]["S"]
    # c. print out
    print("------1.b.User '" + user_name + "with id=" + user_id + " was successfully created at " + time_created
          + "Here our user item:" + str(user_item))


def handle_update_user(record):
    print("------2.a.UPDATE method started with eventID=" + record['eventID'] + "---------")
    # a. get newImage content
    new_image = record['dynamodb']['NewImage']
    old_image = record['dynamodb']['OldImage']
    time_created = old_image["added"]["S"]

    # c. print out
    print("------2.b. User was successfully updated at " + time_created + "! Here data: "
          " - USER BEFORE: " + str(old_image) +
          " - USER AFTER: " + str(new_image)
          )


def handle_remove_user(record):
    print("------3.a. DELETE method started with eventID=" + record['eventID'] + "---------")
    # a. get newImage content
    old_image = record['dynamodb']['OldImage']
    time_created = old_image["added"]["S"]

    # c. print out
    print("------3.b. User was successfully updated " + time_created + "! Here the deleted data user data:" + str(old_image))


def lambda_handler(event, context):

    try:
        # 1.Iterate over each record
        for record in event['Records']:
            # 2.Handle event type
            if record['eventName'] == 'INSERT':
                handle_create_user(record)
            elif record['eventName'] == 'MODIFY':
                handle_update_user(record)
            elif record['eventName'] == 'REMOVE':
                handle_remove_user(record)
    except Exception as e:
        print(e)
        print('-------wrong---------')
        return "Oops!"
