from flask_socketio import emit
from app import socketio

def broadcast_update(data):
    socketio.emit('update', data)
