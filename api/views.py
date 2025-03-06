from flask import Blueprint, render_template

views_blueprint = Blueprint('views_str', __name__)

@views_blueprint.route('/', methods=['GET'])
def home():
    return render_template('markdown.html')
