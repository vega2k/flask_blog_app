from app import db
from models import User, Post


user = User(username='user', email='user@blog.com', password='password')
db.session.add(user)
db.session.commit()

post1 = Post(title='첫 번째 포스트', content='첫 번째 포스트 내용', author=user)
post2 = Post(title='두 번째 포스트', content='두 번째 포스트 내용', author=user)

db.session.add(post1)
db.session.add(post2)
db.session.commit()