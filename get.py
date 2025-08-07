import json
import boto3

def lambda_handler(event, context):

    dynamodb = boto3.resource('dynamodb', region_name='us-west-1')
    table = dynamodb.Table('StudetnsDataForm')
    response = table.scan()
    data = response['Items']

    while 'LastEvaluatedKey' in response:
        response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
        data.extend(response['Items'])

    return data