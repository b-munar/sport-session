from flask import Flask
from flask_restful import Api
from src.controllers.ping_controller import Ping
from src.controllers.sport_session_controller import SportSessionController
from src.controllers.sessions_avg_controller import SessionAVGController

def create_app():
    app = Flask(__name__)
    api = Api(app)
    api.add_resource(Ping, '/sport-session/ping')
    api.add_resource(SportSessionController, '/sport-session')
    api.add_resource(SessionAVGController, '/sport-session/avg')
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True, port=80, host='0.0.0.0')
else:
    gunicorn_app = create_app()