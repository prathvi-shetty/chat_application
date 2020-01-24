from flask import Flask, render_template
from flask_socketio import SocketIO, emit
from flask_cors import CORS, cross_origin
app = Flask(__name__)
app.config['SECRET_KEY']='prathvishetty'
socketio = SocketIO(app,cors_allowed_origins="*")

@app.route('/')
@cross_origin()
def index():
    return render_template('./ChatApp.html')


@socketio.on('my event')
@cross_origin()
def handle_event( json ):
    print(str(json))
    socketio.emit('my response', json)

if __name__ == '__main__':
    socketio.run(app,host='0.0.0.0', debug= False)
