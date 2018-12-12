from flask import Blueprint
from common.libs.Helper import ops_render

route_pad = Blueprint('pad_page', __name__)


@route_pad.route('/pad')
def pad():
    return ops_render("index/index.html")
