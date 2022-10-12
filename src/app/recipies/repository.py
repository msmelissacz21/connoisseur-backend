import os
import boto3
from dynamodb_json import json_util as json

# interacts with database, saves, gets, deletes recipes in database

client = boto3.client('dynamodb')
table_name = 'recipes'

def get_recipe_by_id(id: int):
    response = client.get_item(TableName=table_name, Key={'recipe_id':{'N': id}})
    return json.loads(response['Item'])

def scan_all_recipes():
    response = client.scan(TableName=table_name)
    return json.loads(response['Items'])

def save(id, userID, name, image, content):
    recipe = {}
    recipe['recipe_id'] = id  # this is the partition key in DynamoDB for the recipe table
    recipe['userID'] = userID
    recipe['name'] = name
    recipe['image'] = image
    recipe['content'] = content
    record = json.dumps(recipe, as_dict=True)
    client.put_item(TableName=table_name, Item=record)
    return {'status': 'saved'}