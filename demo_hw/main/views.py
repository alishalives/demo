# Импорт класса Blueprint и render_template
from flask import Blueprint, render_template

# Создание нового Blueprint
main_blueprint = Blueprint('main_blueprint', __name__, template_folder='./templates')


# Создание вьюшки
@main_blueprint.route('/')
def main_page():
    return render_template('index.html')


