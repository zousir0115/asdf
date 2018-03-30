# -*- coding:utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager

# Migrate : 保证在迁移时，数据库和app能够建立关联
# MigrateCommand ： 保存的是迁移数据库的脚本，所以我们不需要自定义脚本实现数据库迁移
from flask_migrate import Migrate, MigrateCommand


app = Flask(__name__)

# 配置mysql数据库参数
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@192.168.72.60:3306/flask_migrate_07'
# 不追踪数据库操作，节约性能
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 创建连接到数据库的对象
db = SQLAlchemy(app)

# 创建脚本管理器对象
manager = Manager(app)
# 迁移时，让数据库和app建立关联
Migrate(app, db)
# 需要将迁移的脚本添加到脚本管理器中
# 参数1 ： 是迁移数据库时使用的脚本的别名。参数2就是迁移命令
manager.add_command('db', MigrateCommand)


class Role(db.Model):
    """角色模型类：一"""

    __tablename__ = 'roles'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    info = db.Column(db.String(64), unique=True)
    # 建立一查多和多查一的关联
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
    address = db.Column(db.String(64))
    # 外键
    role_id = db.Column(db.Integer, db.ForeignKey(Role.id))

    def __repr__(self):
        return '<User: %s-%s-%s-%s>' % (self.name,self.email,self.password,self.role_id)


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    # 使用脚本管理器启动程序
    manager.run()