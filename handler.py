from __future__ import print_function
import urllib3
import boto3
url = "https://api.mockytonk.com/proxy/ab2198a3-cafd-49d5-8ace-baac64e72222"
sqs = boto3.resource('sqs')
queue = sqs.get_queue_by_name(QueueName='challengex-dev-ChallengeXQueue-IGSnalejevsF')

def request_handler(event, context):
    response = queue.send_message(MessageBody=event["body"])
    print(response)
    return {
        "statusCode": 200,
        "headers": {
            "my_header": "my_value"
        },
        "body": "success",
    };

def sqs_queue_handler(event, context):
    for record in event['Records']:
        payload = record["body"]
        http = urllib3.PoolManager()
        resp = http.request(
            "POST",
            url,
            body=payload
        )
        print(resp.data)
    return {
        "statusCode": 200,
        "headers": {
            "my_header": "my_value"
        },
        "body": "success",
    };

