SQLALCHEMY_DATABASE_URI = 'mysql://root:password@127.0.0.1:3306/food_db'
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = True
SQLALCHEMY_ECHO = True
SQLALCHEMY_ENCODING = "utf-8"
AUTH_COOKIE_NAME = 'cate_time'

# 过滤url
IGNORE_URLS = [
    "^/user/login"
]

IGNORE_CHECK_LOGIN_URLS = [
    "^/static",
    "^/favicon.ico"
]
