# -*- coding:utf-8 -*-

# from cart import cart_bule
from . import cart_bule # 会在当前目录下引入cart_bule，如果没有，就会进入__init__.py文件中查找
from flask import render_template


# 使用蓝图中的装饰器装饰cart_list
@cart_bule.route('/cart_list')
def cart_list():

    #
    return render_template('cart.html')