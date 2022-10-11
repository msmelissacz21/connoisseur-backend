from asyncio import constants
import json
from flask.blueprints import Blueprint
from app.repository.recipes import save, get_recipe_by_id, scan_all_recipes
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
    print(request.json)
    content = request.json
    recipe_id = content['id']
    user_id = content['userID']
    name = content['name']
    image = content['image']
    recipe_content = content['content']

    r = save(recipe_id, user_id, name, image, recipe_content)
    return json.dumps(r), 200, {'Access-Control-Allow-Origin': '*'}
