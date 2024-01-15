import json
import boto3
import time

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('billcalcdatabase')

t = time.localtime()
current_time = time.strftime("%H:%M:%S", t)

def lambda_handler(event, context):
    # TODO implement
    numberOfItems = int(event['number'])
    PriceOfEach = int(event['price'])
    result = numberOfItems*PriceOfEach
    
    response = table.put_item(
        Item = {
            'ID': str(result),
            'Time': current_time
        })
    
    return {
        'statusCode': 200,
        'body': json.dumps('Your bill is Rs. ' + str(result))
    }
