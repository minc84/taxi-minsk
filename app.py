import os
from flask import Flask
from config import Configuration #Загружаем из файла config  конфигурации
#from flask_login import LoginManager # загружаем поддержку афторизации

app = Flask(__name__) #Регистрация приложение
app.config.from_object(Configuration) # подключаем конфиг
#login_manager = LoginManager(app) # 


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"



if __name__ == '__main__':
		app.run(host=os.getenv('IP', '127.0.0.1'),
			port=int(os.getenv('PORT', 4100)))
