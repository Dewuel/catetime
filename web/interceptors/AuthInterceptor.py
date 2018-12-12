# -*- coding: utf-8 -*-
from application import app
from flask import request, redirect, g
from common.models.user import User
from common.libs.user.UserSevice import UserService
from common.libs.UrlManager import UrlManager
import re


@app.before_request
def before_request():
    path = request.path

    ignore_urls = app.config['IGNORE_URLS']
    ignore_check_login_urls = app.config['IGNORE_CHECK_LOGIN_URLS']

    pattern = re.compile('%s' % "|".join(ignore_check_login_urls))
    if pattern.match(path):
        return

    pattern = re.compile('%s' % '|'.join(ignore_urls))
    if pattern.match(path):
        return

    user_info = check_login()

    g.current_user = None
    if user_info:
        g.current_user = user_info

    app.logger.info(user_info)
    if not user_info:
        return redirect(UrlManager.buildUrl("/user/login"))

    return


'''判断用户是否登录'''


def check_login():
    cookie = request.cookies
    auth_cookie = cookie[app.config['AUTH_COOKIE_NAME']] if app.config['AUTH_COOKIE_NAME'] in cookie else None
    app.logger.info(auth_cookie)
    if auth_cookie is None:
        return False

    auth_info = auth_cookie.split("#")
    if len(auth_info) != 2:
        return False
    try:
        user_info = User.query.filter_by(uid=auth_info[1]).first()
        app.logger.info(user_info)
    except Exception:
        return False

    if user_info is None:
        return False

    if auth_info[0] != UserService.geneAuthCode(user_info):
        return False

    return user_info
