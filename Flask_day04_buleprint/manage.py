# -*- coding:utf-8 -*-

from flask import Flask
# from user import user_info  # 会出现循环引用
from order import order_blue

# from cart.views import cart_bule
from cart import cart_bule

app = Flask(__name__)

# 将订单模块的蓝图注册到app:告诉app我们的order_blue里面有哪些路由和视图的关系
app.register_blueprint(order_blue)
app.register_blueprint(cart_bule)


@app.route('/')
def index():
    return 'index'


# 以下代码被拷贝到user.py
# @app.route('/user_info')
# def user_info():
#     return 'user_info'


# 以下代码被拷贝到order.py
# @app.route('/order_list')
# def order_list():
#     return 'order_list'


if __name__ == '__main__':

    print app.url_map

    app.run(debug=True)