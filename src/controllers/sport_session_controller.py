from flask_restful import Resource
from flask import request

from src.database.session import Session
from src.models.sport_session_model import SportSessionModel
from src.schemas.sport_session_schema import SportSessionDeserializeSchema, SportSessionSerializeSchema
from src.utils.authorization import authorization

class SportSessionController(Resource):
    method_decorators = [authorization]
    def post(self, **kwargs):
        if(request.data):
            request_json = request.get_json()
        else:
            return "", 400
        
        sport_session_create_schema = SportSessionDeserializeSchema()
        
        errors = sport_session_create_schema.validate(request_json)
        if errors:
            print(errors)
            return "", 400
        
        sport_session_create_dump = sport_session_create_schema.dump(request_json)
        sport_session_create_dump["user"] = kwargs["user"]["id"]
        
        # token = kwargs["token"]
        # If you need to use another microservice,
        # use this token with the request library,
        # remember to paste the Bearer before the token
        
        session = Session()
        new_sport_session = SportSessionModel(**sport_session_create_dump)
        session.add(new_sport_session)
        session.commit()

        sport_session_created_schema = SportSessionSerializeSchema()
        sport_session_created_dump = sport_session_created_schema.dump(new_sport_session)
        return sport_session_created_dump, 201
    
    def get(self, **kwargs):
        sport_session_schema = SportSessionSerializeSchema()

        session = Session()
        query = session.query(SportSessionModel).filter(SportSessionModel.user==kwargs["user"]["id"])
        session.close()
        
        sport_sessions = [sport_session_schema.dump(sport_session) for sport_session in query]
        return {"sessions":sport_sessions}, 200

