from flask import Flask
from app.main.controllers import main
from app.admin.controllers import admin

app = Flask(__name__,
            instance_relative_config=True,
            template_folder='templates')


app.register_blueprint(main, url_prefix='/')
app.register_blueprint(admin, url_prefix='/admin')

app.jinja_env.add_extension('jinja2.ext.loopcontrols')
