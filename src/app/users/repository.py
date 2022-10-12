import boto3
from dynamodb_json import json_util as json


# interacts with database, saves, gets, deletes users in database

client = boto3.client('dynamodb')
table_name = 'users'

def get_user_by_id(id: int):
    response = client.get_item(TableName=table_name, Key={'user_id':{'S': id}})
  
    if 'Item' in response:
        return json.loads(response['Item'])
    else:
        return None

def save(user):
    record = json.dumps(user, as_dict=True)
    client.put_item(TableName=table_name, Item=record)
    return {'status': 'saved'}



