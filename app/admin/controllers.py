from flask import Blueprint, request
from flask_login import current_user


admin = Blueprint('admin', __name__, template_folder='templates')

@admin.route('/admin')
@admin.route('/')
def index():
    if current_user.is_authenticated:
        return render_template("submit.htm")
    else:
        return render_template("login.htm")


@admin.route('/submit', methods=['POST'])
@admin.route('/submit/<table>')
def submit(table):
    form_data = request.form
