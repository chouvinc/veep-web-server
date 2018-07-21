from flask import Blueprint, render_template


main = Blueprint('main', __name__, template_folder='templates')


@main.route('/')
def index():

    test = {
        "hello": "Hello",
        "world": "World"
    }

    return render_template("index.htm", test=test)

@main.route('/')
def projects():

	test = {
	"hello": "Hello",
	"world": "World"
	}
	return render_template("projects.htm",test2=test)