import os
import pprint
pp = pprint.PrettyPrinter(width=41, compact=True)
from flask import Flask, render_template, request
from flask_cors import CORS, cross_origin

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
            SECRET_KEY='dev',
            DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
            )
    if test_config is None:
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    cors = CORS(app)
    app.config['CORS_HEADERS'] = 'Content-Type'

    @app.route('/hello')
    def hello():
        return 'Hello, World! Its Me'

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/rgb', methods=['POST'])
    @cross_origin()
    def change_rgb():
        rgb_data = request.get_json()
        pp.pprint(rgb_data)
        return 'Success'
    
    print('Starting Flask!')
    return app
