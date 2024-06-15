import connexion
from flask_socketio import SocketIO

# Create the Connexion application instance
app = connexion.App(__name__, specification_dir='./')
app.add_api('swagger.yml')

# Get the underlying Flask app instance
flask_app = app.app

# Initialize SocketIO
socketio = SocketIO(flask_app)

if __name__ == '__main__':
    socketio.run(flask_app, debug=True)
