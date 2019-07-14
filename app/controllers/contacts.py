from flask_restful import Resource, marshal
from app import db
from app.models import Contact
from app.util.http import request
from app.schemas import contact_field

class Contacts(Resource):
    def get(self):
        contatos = Contact.query.all()
        # object, serializer, custom_key_json
        return marshal(contatos, contact_field, "xpto"), 200

    def post(self):
        payload = request.only(["name","cellphone"])

        name = payload["name"]
        cellphone = payload["cellphone"]

        contact = Contact(name, cellphone)

        db.session.add(contact)
        db.session.commit()

        return marshal(contact, contact_field, "contatos"), 200
    
    def put(self):
        payload = request.only(["id", "name", "cellphone"])
        
        _id = payload["id"]
        name = payload["name"]
        cellphone = payload["cellphone"]

        contact = Contact.query.get(_id)

        if not contact:
            return {"message": "Contato que vocẽ está tentando deletar ele não existe!"}, 200

        contact.name = name
        contact.cellphone = cellphone

        db.session.add(contact)
        db.session.commit()

        return marshal(contact, contact_field, "contact"), 200

    def delete(self):
        payload = request.only(["id"])
        _id = payload["id"]

        contact = Contact.query.get(_id)

        if not contact:
            return {"message": "Contato que vocẽ está tentando deletar ele não existe!"}, 200

        
        db.session.delete(contact)
        db.session.commit()

        return marshal(contact, contact_field, "contact"), 200