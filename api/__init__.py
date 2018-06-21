from flask import Flask, abort, g, render_template, request, current_app
from api.main.controller import main_blueprint
from api.utils import get_instance_folder_path, get_app_base_path
from api.trees.TreeController import tree_mold

app = Flask(__name__, instance_path=get_instance_folder_path(),
            instance_relative_config=True)


@app.errorhandler(404)
def page_not_found(error):
    current_app.logger.error('Page not found: %s', (request.path, error))
    return render_template('404.html'), 404


@app.errorhandler(500)
def internal_server_error(error):
    current_app.logger.error('Server Error: %s', error)
    return render_template('500.html'), 500


app.register_blueprint(main_blueprint, url_prefix='/')
app.register_blueprint(tree_mold, url_prefix='/oak')