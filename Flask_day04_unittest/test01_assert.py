# -*- coding:utf-8 -*-


def demo(num1, num2):

    # 断言：是断定某个条件一定满足，如果不满足，就报指定的异常
    # 提示：我们编写的单元测试，如果测试的结果跟预期不符。会使用断言来抛出异常
    assert isinstance(num1, int), u'num1必须是int'
    assert isinstance(num2, int), u'num2必须是int'
    assert num2 != 0, u'num2不能为0'

    print (num1 / num2)


demo(10, 0)

