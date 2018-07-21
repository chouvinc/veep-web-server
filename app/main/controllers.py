from flask import Blueprint, render_template, url_for


main = Blueprint('main', __name__, template_folder='templates')


@main.route('/index')
@main.route('/')
def index():

    links = [
        {"title": "VEEP", "url": url_for('.index')},
        {"title": "Projects", "url": url_for('.projects')}
        # {"title": "Contact Us", "url": url_for('.contact_us')}
    ]

    footer_items = [
        {"title": "Social Media",
            "items": [
                # TODO figure out what social media we have
                {"title": "Facebook", "url": "/"},
                {"title": "Placeholder", "url": "/"}
            ]
        },
        {"title": "Apply",
            "items": [
                # TODO figure out which exec positions ppl can apply to
                {"title": "Project Manager", "url": "/"},
                {"title": "Digital Team", "url": "/"},
                {"title": "Marketing", "url": "/"},
                {"title": "Operations", "url": "/"},
                {"title": "Business Development", "url": "/"},
                {"title": "Project Member", "url": "/"}
            ]
        }
    ]

    # TODO fix all the links in footer_items to actually point to a page
    return render_template("index.htm", links=links, footer_items=footer_items)


@main.route('/projects')
def projects():


	return "Derp"
