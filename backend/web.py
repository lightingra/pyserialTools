from multiprocessing import Process

import flask
from flask_bootstrap import Bootstrap5
from gevent import pywsgi
from flask import render_template

app = flask.Flask(__name__)

app.config['SECRET_KEY'] = 'secret!'

bootstrap = Bootstrap5(app)

@app.route('/')

def index():
    return render_template('index.html')

def service(port):
    # app.run(debug=False, port=port)
    # 
    server = pywsgi.WSGIServer(('0.0.0.0', port), app)
    server.serve_forever()

app_process: Process

def start_service(port=5000):
    global app_process

    app_process = Process(target=service, args=(port,))
    app_process.daemon = True
    app_process.start()
    return app_process

def stop_service():
    global app_process
    
    if app_process:
        app_process.join()
