# -*- coding:utf-8 -*-


from flask import Blueprint

# 创建蓝图对象：参数1是蓝图名称
order_blue = Blueprint('order', __name__)

# 使用蓝图里面的route注册一个路由，并绑定一个视图
@order_blue.route('/order_list')
def order_list():
    return 'order_list'