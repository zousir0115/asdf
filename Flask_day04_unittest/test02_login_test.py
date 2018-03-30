# -*- coding:utf-8 -*-

import unittest

from flask import json

from test02_login import app


class LoginTestCase(unittest.TestCase):
    """登录测试用例"""

    def setUp(self):
        """测试开始执行前调用
        1.会做初始化的操作
        2.连接到数据库
        3.开启测试模式
        """
        pass

    def test_login_empty_username_password(self):
        """测试缺少用户名和密码
        预期 ： errcode必须是 -2
        """

        # 模拟发送网络请求,获取测试客户端
        client = app.test_client()
        # 测试客户端发送请求
        response = client.post('/login', data={'username': 'itheima'})
        # 得到响应结果：response_data == 即使响应回来的json字符串
        response_data = response.data
        # 将response_data转成字典
        response_dict = json.loads(response_data)
        # 获取状态码
        errcode = response_dict.get('errcode')
        real_errcode = -2

        # 使用断言，判断状态码跟预期是否相符
        assert errcode == real_errcode, 'errcode should be %s, but current ercode is %s' % (real_errcode,errcode)


    def tearDown(self):
        """测试结束后执行的
        1.做数据销毁的动作
        2.断开数据库sesion的动作
        """
        pass