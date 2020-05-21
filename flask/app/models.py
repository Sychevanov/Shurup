from app import db
from datetime import datetime
import re
from flask_security import UserMixin, RoleMixin




def slugify(s):
    pattern = r'[^\w+]'
    return re.sub(pattern, '-', s)

post_tag = db.Table('post_tags', #создание еще онйо таблицы в бд для того чтобы связывать пост с тегами
                    db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                    db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
    )    


class Post(db.Model):
    id  = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    slug = db.Column(db.String(140), unique=True)
    body = db.Column(db.Text)
    created = db.Column(db.DateTime, default=datetime.now())

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()

    tags = db.relationship('Tag', secondary=post_tag, backref=db.backref('posts',lazy='dynamic'))

    def generate_slug(self):
        if self.title:
            self.slug = slugify(self.title)
    
    def __repr__(self):
        return '<Post id : {}, title: {}>'.format (self.id,self.title)

class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    slug = db.Column(db.String(140), unique=True)

    def __init__(self,*args, **kwargs):
        super(Tag, self).__init__(*args, **kwargs)
        self.slug = slugify(self.name)

    def __repr__(self):
        return '{}'.format (self.name) 

### flask security###

roles_users = db.Table('roles_users',
            db.Column('user_id',db.Integer(), db.ForeignKey('user.id')),
            db.Column('role_id',db.Integer(), db.ForeignKey('role.id'))
        )

class User(db.Model,UserMixin):
    id = db.Column(db.Integer(),primary_key=True)
    email = db.Column(db.String(100),unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    roles = db.relationship('Role',secondary='roles_users', backref=db.backref('users',lazy='dynamic'))

#фласк бииткриб иил как то так, для хеширования пароля

class Role(db.Model,RoleMixin):
    id = db.Column(db.Integer(),primary_key=True)
    name = db.Column(db.String(100),unique=True)
    discription = db.Column(db.String(255)) # вот здесь опечатка дескрипитион пишиется, через e