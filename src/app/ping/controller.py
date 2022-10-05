
import json
from flask.blueprints import Blueprint


ping = Blueprint('ping', __name__)

@ping.route('/ping', methods = ['POST'])
def test():
    return json.dumps({
        'status': 'up'
    })