# -*- coding:utf-8 -*-
# 这里面书写用户模块代码


from manage import app


@app.route('/user_info')
def user_info():
    return 'user_info'