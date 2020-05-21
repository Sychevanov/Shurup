from app import db,user_datastore
from models import User, Role
#p2 = Post(title = 'First2 posts! 3-test ', body = 'First2 post body')  создание поста и добавление в базу данных
#db.session.add(p2)
#db.session.commit()
#print(p2.slug)  чтобы вывести
#posts = Posts.query.all() выводит все посты
#p2 = Post.query.filter(Post.title.contains('first')).all() филтр по поиску
                      #(Post.title=='First posts').first()название целого тайтла тогда найдет весь тайтл и выведет обект

#tag = Tag(name = 'Python') 
#db.session.add_all([p1,p2]) это чтобы передлать сразу всен
#db.session.commit()
#t = Tag.query.first() создание зависимсоти мжду тегом и постом
#post1 = Post.query.filter(Post.id==1)
#post1 = post1.first()
#post1.tags.append(t)
#db.session.add(post1)
#db.session.commit()
#>>> from app import db
#>>> from app import user_datastore
#>>> user_datastore.create_user(email='roman.sychevanov@gmail.com',password = 'admin')
#<User (transient 57978736)>
#>>> db.session.commit()
#>>> from models import User         САОЗДАНИЕ НОВОГО ЮЗЕРА
#>>> user = User.query.first()
#>>> user
#<User 1>
#>>> user.id
#1
#>>> user.email
#'monte.tashion2@yandex.ru'
user = User.query.first()
print(user.email)
#user_datastore.create_role(name='admin', discription='administrator')
role = Role.query.first()
db.session.commit()
user_datastore.add_role_to_user(user, role)
db.session.commit()