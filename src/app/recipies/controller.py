from asyncio import constants
import json
from flask.blueprints import Blueprint
from .repository import save, get_recipe_by_id, scan_all_recipes
from app.users.repository import get_user_by_id
from app.users.repository import save as save_user
from flask import request


# all recipe endpoint exist here

recipes = Blueprint('recipes', __name__)

@recipes.route('/recipes', methods = ['GET'])
def get_recipe():
    recipe_id = request.args.get('recipe_id')
    return get_recipe_by_id(recipe_id)

@recipes.route('/all-recipes', methods = ['GET'])
def get_all_recipes():
    return scan_all_recipes(), 200, {'Access-Control-Allow-Origin': '*'}

@recipes.route('/recipes', methods = ['POST'])
def test():
    content = json.loads(request.data)
    recipe_id = content['id']
    user_id = content['userID']
    name = content['name']
    image = content['image']
    recipe_content = content['content']

    r = save(recipe_id, user_id, name, image, recipe_content)

    user = get_user_by_id(user_id)
    user['recipe_ids'].append(recipe_id)
    save_user(user)
    
    return json.dumps(r), 200, {'Access-Control-Allow-Origin': '*'}
