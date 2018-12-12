from flask import Blueprint
from common.libs.Helper import ops_render

route_food = Blueprint('food_page', __name__)


@route_food.route('/index')
def index():
    return ops_render('food/index.html')


@route_food.route('/set')
def food_set():
    return ops_render('food/set.html')


@route_food.route('/cat')
def food_cate():
    return ops_render('food/cat.html')


@route_food.route('/cat-set')
def food_setting():
    return ops_render('food/cat_set.html')


@route_food.route('/info')
def food_info():
    return ops_render('food/info.html')
