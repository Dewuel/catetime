from flask import Blueprint
from common.libs.Helper import ops_render

route_account = Blueprint('account_page', __name__)


@route_account.route('/index')
def account():
    return ops_render('account/index.html')
