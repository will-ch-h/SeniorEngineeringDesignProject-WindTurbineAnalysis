<<<<<<< HEAD
from flask import Flask, render_template
from flask_socketio import SocketIO
import subprocess
import serial
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
def stream_volt_data():
    try:
        ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        while True:
                if ser.in_waiting > 0:
                    line = ser.readline().decode('utf-8').strip()
                    if line:
                        socketio.emit('volt_update', {'data': line})         
    except Exception as e:
        print(f"Serial Error: {e}")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close() 

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    global thread_started
    if not thread_started:
        rpm_thread = threading.Thread(target=stream_rpm_data)
        rpm_thread.daemon = True
        rpm_thread.start()
        
        volt_thread = threading.Thread(target=stream_volt_data)
        volt_thread.daemon = True
        volt_thread.start()
        
        thread_started = True

if __name__ == '__main__':
=======
from flask import Flask, render_template
from flask_socketio import SocketIO
import subprocess
import serial
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
def stream_volt_data():
    try:
        ser = serial.Serial('/dev/ttyACM0', 9600, timeout=1)
        while True:
                if ser.in_waiting > 0:
                    line = ser.readline().decode('utf-8').strip()
                    if line:
                        socketio.emit('volt_update', {'data': line})         
    except Exception as e:
        print(f"Serial Error: {e}")
    finally:
        if 'ser' in locals() and ser.is_open:
            ser.close() 

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    global thread_started
    if not thread_started:
        rpm_thread = threading.Thread(target=stream_rpm_data)
        rpm_thread.daemon = True
        rpm_thread.start()
        
        volt_thread = threading.Thread(target=stream_volt_data)
        volt_thread.daemon = True
        volt_thread.start()
        
        thread_started = True

if __name__ == '__main__':
>>>>>>> a34e1904a327a0eb39cdf39878fdc7306cdeb28a
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)