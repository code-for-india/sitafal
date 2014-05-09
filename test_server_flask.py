__author__ = 'ganesh'


from geventwebsocket.handler import WebSocketHandler
from gevent.pywsgi import WSGIServer
from flask import *
from flask import Flask, render_template
import socket
import time
from threading import Thread
from flask.ext.socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app)


