# -*- coding:utf-8 -*-


from flask import Blueprint

# 如果在这里导入views，会出现cart_bule不存在时，被导入了
# from cart import views

# 创建蓝图对象
cart_bule = Blueprint('cart', __name__)


# 方便manage.py在导入cart_bule时。能够让views里面的蓝图注册路由可以被执行到
from cart import views

