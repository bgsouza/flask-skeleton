from flask_restful import Resource, marshal
from app import db
from app.util.http import request

class Hello(Resource):

    def get(self):
        return {"message": "Oláaa Enfermeira!"}, 200        

    def post(self):
        pass

    def put(self):
        pass

    def update(self):
        pass