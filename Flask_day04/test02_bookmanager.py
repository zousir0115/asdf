# -*- coding:utf-8 -*-

from flask import Flask, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)

app.config['SECRET_KEY'] = '23ukfrolmrti'

# 配置mysql数据库参数
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:mysql@192.168.72.60:3306/flask_book_07'
# 不追踪数据库操作，节约性能
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# 创建连接到数据库的对象
db = SQLAlchemy(app)


class BookForm(FlaskForm):
    """书籍信息管理的表单类"""
    author = StringField(u'作者：', validators=[DataRequired()])
    book = StringField(u'书名：', validators=[DataRequired()])
    submit = SubmitField(u'添加')


# 准备模型类
class Author(db.Model):
    """作者模型类：一"""
    __tablename__ = 'authors'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # 定义关联查询的关系
    books = db.relationship('Book', backref='author', lazy='dynamic')


class Book(db.Model):
    """书籍模型类：一"""
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    # 外键
    author_id = db.Column(db.Integer, db.ForeignKey(Author.id))


@app.route('/', methods=['GET', 'POST'])
def index():
    # 创建WTF对象
    book_form = BookForm()

    if request.method == 'POST':
        # 处理添加逻辑
        if book_form.validate_on_submit():
            # 能够进入这里说明是做添加，并且输入框都有值
            # 接受参数：作者名和书名
            # author_name = request.form.get('author')
            # book_name = request.form.get('book')
            author_name = book_form.author.data
            book_name = book_form.book.data

            # 查询作者并判断是否存在
            author = Author.query.filter(Author.name==author_name).first()
            if author:

                # 查询书籍并判断是否存在
                book = Book.query.filter(Book.name==book_name, Book.author_id==author.id).first()
                if book:
                    # 提示书名已存在
                    flash(u'书名已存在')
                else: # 书名不存在
                    # 将书籍绑定到该作者
                    book = Book(name=book_name, author_id=author.id)
                    try:
                        db.session.add(book)
                        db.session.commit()
                    except Exception as e:
                        print e
                        # 回滚
                        db.session.rollback()
                        flash(u'添加书籍失败')

            else: # 作者不存在
                # 添加新的作者:当author没有add和commit到数据库时，没有id
                author = Author(name=author_name)
                # 添加新的书籍
                # 当author没有add和commit到数据库时，没有id
                # book = Book(name=book_name, author_id=author.id)
                book = Book(name=book_name)
                # 利用了backref的反向应用给书籍绑定外键
                book.author = author

                try:
                    # db.session.add_all([author,book])
                    # db.session.add(author)

                    # 只需要add关联了author的book即可
                    db.session.add(book)
                    db.session.commit()
                except Exception as e:
                    print e
                    db.session.rollback()
                    flash(u'添加作者和书籍失败')

    # 查询数据
    authors = Author.query.all()

    # 渲染模板
    return render_template('01_bookmanager.html', form=book_form, authors=authors)


if __name__ == '__main__':

    db.drop_all()
    db.create_all()

    # 生成数据
    au1 = Author(name='老王')
    au2 = Author(name='老尹')
    au3 = Author(name='老刘')
    # 把数据提交给用户会话
    db.session.add_all([au1, au2, au3])
    # 提交会话
    db.session.commit()
    bk1 = Book(name='老王回忆录', author_id=au1.id)
    bk2 = Book(name='我读书少，你别骗我', author_id=au1.id)
    bk3 = Book(name='如何才能让自己更骚', author_id=au2.id)
    bk4 = Book(name='怎样征服美丽少女', author_id=au3.id)
    bk5 = Book(name='如何征服英俊少男', author_id=au3.id)
    # 把数据提交给用户会话
    db.session.add_all([bk1, bk2, bk3, bk4, bk5])
    # 提交会话
    db.session.commit()

    app.run(debug=True)