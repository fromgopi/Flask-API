from flask import Blueprint, current_app,render_template

main_blueprint = Blueprint('main', __name__, template_folder='templates')

@main_blueprint.route('/')
def main():
    current_app.logger.info("Rendering Main page....")
    return render_template('index.html')

