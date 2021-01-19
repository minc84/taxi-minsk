from flask_sqlalchemy import SQLAlchemy
from app import app 

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db' # добавляем в конфигурацию путь к БД
db = SQLAlchemy(app) 