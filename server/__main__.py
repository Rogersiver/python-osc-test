import os
from flask import Flask, request
from flask_cors import CORS, cross_origin
from pythonosc.udp_client import SimpleUDPClient
import logging
from waitress import serve
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        # Would realistically come from data store
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

    ip = "192.168.1.183"
    port = 7771
    client = SimpleUDPClient(ip, port)  # Create client

    @app.route('/rgb', methods=['POST'])
    @cross_origin()
    def change_rgb():
        rgb_data = request.get_json()
        client.send_message("/r", int(rgb_data['rgb']['r']))
        client.send_message("/g", int(rgb_data['rgb']['g']))
        client.send_message('/b', int(rgb_data['rgb']['b']))
        client.send_message('/a', 1)
        logging.info(rgb_data)
        return 'Changed Color!'

    print('Starting Flask!')
    return app


if __name__ == '__main__':
    app = create_app()
    serve(app, host='0.0.0.0', port=5000)
