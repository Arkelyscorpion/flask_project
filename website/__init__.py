from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '00000121asddfja91jalLKLKJ()134i'
    return app
    