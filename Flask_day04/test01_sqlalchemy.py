# -*- coding:utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# 配置mysql数据库参数
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@192.168.72.60:3306/flask_test_07'
# 不追踪数据库操作，节约性能
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 创建连接到数据库的对象
db = SQLAlchemy(app)

# 1.当查询出role时，可以很方便的通过属性关联查询到role所对应的所有的user数据
    # role.users  (一查多)
# 2.当查询出user时，可以很方便的通过属性关联查询到user所对应的所有的role数据
    # user.role   (多查一)


class Role(db.Model):
    """角色模型类：一"""

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # 建立一查多和多查一的关联
    # users = db.relationship('User') : 是给Role模型类定义属性，属性内部关联的是User模型数据
    # users = db.relationship('User', backref='role') 是给relationship的第一个模型类参数，绑定一个属性，属性内部保存的是Role模型数据
    users = db.relationship('User', backref='role', lazy='dynamic')


    def __repr__(self):
        return '<Role: %s>' % self.name


class User(db.Model):
    """角色模型类：多"""

    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(64))
    password = db.Column(db.String(64))
    # 外键
    role_id = db.Column(db.Integer, db.ForeignKey(Role.id))

    def __repr__(self):
        return '<User: %s-%s-%s-%s>' % (self.name,self.email,self.password,self.role_id)


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':

    # 为了方便后续的测试时，数据库的数据都重新加载一份，我在此处需要先删除在创建，并没有实际的意义
    db.drop_all()
    # 使用非迁移的方式建表
    db.create_all()

    # 添加测试数据：角色 ： 一
    ro1 = Role(name='admin')
    db.session.add(ro1)
    db.session.commit()
    # 再次插入一条数据
    ro2 = Role(name='user')
    db.session.add(ro2)
    db.session.commit()

    # 添加用户数据：多
    us1 = User(name='wang', email='wang@163.com', password='123456', role_id=ro1.id)
    us2 = User(name='zhang', email='zhang@189.com', password='201512', role_id=ro2.id)
    us3 = User(name='chen', email='chen@126.com', password='987654', role_id=ro2.id)
    us4 = User(name='zhou', email='zhou@163.com', password='456789', role_id=ro1.id)
    us5 = User(name='tang', email='tang@itheima.com', password='158104', role_id=ro2.id)
    us6 = User(name='wu', email='wu@gmail.com', password='5623514', role_id=ro2.id)
    us7 = User(name='qian', email='qian@gmail.com', password='1543567', role_id=ro1.id)
    us8 = User(name='liu', email='liu@itheima.com', password='867322', role_id=ro1.id)
    us9 = User(name='li', email='li@163.com', password='4526342', role_id=ro2.id)
    us10 = User(name='sun', email='sun@163.com', password='235523', role_id=ro2.id)
    db.session.add_all([us1, us2, us3, us4, us5, us6, us7, us8, us9, us10])
    db.session.commit()


    app.run(debug=True)

    """
    查询所有用户数据
    查询有多少个用户
    查询第1个用户
    查询id为4的用户[3种方式]
    查询名字结尾字符为g的所有数据[开始/包含]
    查询名字不等于wang的所有数据[2种方式]
    查询名字和邮箱都以 li 开头的所有数据[2种方式]
    查询password是 `123456` 或者 `email` 以 `itheima.com` 结尾的所有数据
    查询id为 [1, 3, 5, 7, 9] 的用户列表
    查询name为liu的角色数据
    查询所有用户数据，并以邮箱排序
    每页3个，查询第2页的数据
    """