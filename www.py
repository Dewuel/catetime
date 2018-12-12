from application import app



'''
统一拦截器
'''
from web.interceptors.AuthInterceptor import *


from web.controllers.index import route_index
from web.controllers.user.User import route_user
from web.controllers.account.index import route_account
from web.controllers.food.index import route_food
from web.controllers.member.index import route_member
from web.controllers.finance.index import route_finance
from web.controllers.stat.index import route_stat

'''
蓝图功能，配置所以url
'''
app.register_blueprint(route_index, url_prefix='/')
app.register_blueprint(route_user, url_prefix="/user")
app.register_blueprint(route_account, url_prefix='/account')
app.register_blueprint(route_food, url_prefix='/food')
app.register_blueprint(route_member, url_prefix='/member')
app.register_blueprint(route_finance, url_prefix='/finance')
app.register_blueprint(route_stat, url_prefix='/stat')

