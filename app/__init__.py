from flask import Flask
from flask_login import LoginManager
from app.main.controllers import main
from app.admin.controllers import admin
from config import Config

app = Flask(__name__,
            instance_relative_config=True,
            template_folder='templates')

app.config.from_object(Config)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

app.register_blueprint(main, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')

app.jinja_env.add_extension('jinja2.ext.loopcontrols')
