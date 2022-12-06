import os
from flask import Flask, request
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
        return '<h1>Index</h1>'

    @app.route('/rgb', methods=['POST'])
    @cross_origin()
    def change_rgb():
        rgb_data = request.get_json()
        print(int(rgb_data['r']))
        return 'Success'

    print('Starting Flask!')
    return app
if __name__ == '__main__':
    create_app().run(host='0.0.0.0', port=5000, debug=True)

