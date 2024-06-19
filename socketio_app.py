from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, emit
from flask_cors import CORS
from Database.models import TestUpdateData
from Database.db import Session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins="*")
CORS(app)

@app.route('/')
def index():
    return render_template('realtime.html')

@app.route('/get_data')
def get_data():
    print("Getting data")
    session = Session()
    try:
        data = session.query(TestUpdateData).all()
        return jsonify([d.to_dict() for d in data])
    except Exception as e:
        return {"error": str(e)}, 400
    finally:
        session.close()

@app.route('/emit_update', methods=['POST'])
def emit_update():
    data = request.get_json()
    print("Broadcasting data update: ", data)
    socketio.emit('data_update_response', data)
    return '', 200

@socketio.on('connect')
def handle_connect():
    print("Client connected")
    emit('response', {'message': 'Connected to the server'})

@socketio.on('disconnect')
def handle_disconnect():
    print("Client disconnected")

if __name__ == "__main__":
    socketio.run(app, debug=True, port=5001)
