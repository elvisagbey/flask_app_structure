from . import main
from flask import render_template


@main.route('/', methods=['GET', 'POST'])
def index():
    name = 'Elvis'
    return render_template('index.html', name=name)
