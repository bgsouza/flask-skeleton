from flask_restful import Resource, marshal
from app import db
from app.util.http import request

class Healthcheck(Resource):

    def get(self):
        return {"status": {"app": True}}, 200        

    def post(self):
        pass

    def put(self):
        pass

    def update(self):
        pass