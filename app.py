from flask import Flask, render_template
from flask_socketio import SocketIO

App = Flask(__name__)
socketio = SocketIO(App)

@App.route('/')
def index():
  return render_template('index.html')

@socketio.on('Change')
def change(data):
    print("any")
    socketio.emit("ChangeText", data)

if __name__ == '__main__':
  socketio.run(App)
