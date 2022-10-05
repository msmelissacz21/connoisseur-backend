from app.app import create_app
from apig_wsgi import make_lambda_handler

handle = make_lambda_handler(create_app())
    
def handler(event, context):
    event['httpMethod'] = event['requestContext']['http']['method']
    event['path'] = event['requestContext']['http']['path']
    return handle(event, context)