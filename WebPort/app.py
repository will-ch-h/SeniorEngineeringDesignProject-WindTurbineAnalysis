from flask import Flask, render_template
from flask_socketio import SocketIO
import subprocess
import threading
import sys
import os

app = Flask(__name__)
socketio = SocketIO(app)

process = None
thread_started = False

def stream_rpm_data():
    global process
    process = subprocess.Popen([sys.executable, '-u', 'tachometer.py'],
                               stdout=subprocess.PIPE,
                               stderr=subprocess.STDOUT,
                               universal_newlines=True)
    for line in iter(process.stdout.readline, ''):
        socketio.emit('rpm_update', {'data': line.strip()})
    
    process.stdout.close()
    process.wait()

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    global thread_started
    if not thread_started:
        thread = threading.Thread(target=stream_rpm_data)
        thread.daemon = True
        thread.start()
        thread_started = True

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)