from flask import Flask , render_template 
from flask_socketio import SocketIO , emit

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/chat')
def index():
    return render_template('index.html')

@socketio.on('envioMensagem')
def messagereceived(json):
    print(json)
    emit('receberMensagem', json,broadcast=True)

if __name__ == '__main__':
   socketio.run(app,'192.168.0.1',5000)