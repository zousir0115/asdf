# -*- coding:utf-8 -*-

from flask import Flask, render_template
from flask_mail import Mail, Message
from threading import Thread


app = Flask(__name__)


# 配置邮件：服务器／端口／安全套接字层／邮箱名／授权码
app.config['MAIL_SERVER'] = "smtp.yeah.net"
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = "dailyfreshzxc@yeah.net"
app.config['MAIL_PASSWORD'] = "dailyfresh123"
app.config['MAIL_DEFAULT_SENDER'] = 'FlaskAdmin<dailyfreshzxc@yeah.net>'

# 发送邮件的对象，并跟app建立关联
mail = Mail(app)


def async_send_mail(message):
    """异步发送邮件"""
    # 应用上下文是线程局部变量：在这个线程中执行的current_app，跟视图中的current_app不是一个
    # 结论：如果要在子线程中使用应用上下文。需要在子线程中开启上下文、创建一个上下文环境
    with app.app_context():
        mail.send(message)


@app.route('/send_mail')
def send_mail():

    # 准备要发送的内容
    message = Message()
    message.subject = '我是邮件的标题'
    # 收件人列表
    message.recipients = ['zhangjiesharp@163.com']
    message.body = '我是邮件的正文内容 text'
    # 后面设置的邮件的正文内容会覆盖前面设置的
    message.html = '<h1>我也是邮件的正文内容 html</h1>'

    # 发送邮件:会阻塞响应
    # mail.send(message)

    # 创建子线程,异步的发送邮件
    thread = Thread(target=async_send_mail, args=(message, ))
    thread.start()

    return '发送中......'


@app.route('/')
def index():
    return render_template('02_mail.html')


if __name__ == '__main__':
    app.run(debug=True)