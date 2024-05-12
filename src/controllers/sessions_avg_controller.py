from flask_restful import Resource
from flask import Response
from sqlalchemy.sql import func
import json

from src.database.session import Session
from src.models.sport_session_model import SportSessionModel
from src.schemas.sport_session_schema import SportSessionDeserializeSchema, SportSessionSerializeSchema
from src.utils.authorization import authorization

class SessionAVGController(Resource):
    method_decorators = [authorization]
    def get(self, **kwargs):
        session = Session()
        query = session.query(func.avg(SportSessionModel.RPM).label('average_rpm'),
                              func.avg(SportSessionModel.VO).label('average_vo'),
                              func.avg(SportSessionModel.FTP).label('average_ftp'),
                              func.avg(SportSessionModel.KCAL).label('average_kcal')).filter(SportSessionModel.user==kwargs["user"]["id"]).all()
        results = [tuple(row) for row in query] 
        users = {'average_results':[{'RPM': results[0][0], 'VO':results[0][1], 'FTP':results[0][2], 'KCAL': results[0][3] }]}
        response = Response(
        response=json.dumps(users),
        status=200,
        mimetype='application/json'
        )
        session.close()
        return response

