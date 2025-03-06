from flask import Flask
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'randomstring'

    from .views import views_blueprint

    app.register_blueprint(views_blueprint, url_prefix='/')

    return app
