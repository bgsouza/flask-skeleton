from app import db
# Lib para gerenciar hashs de password e verifição de password
from werkzeug.security import generate_password_hash, check_password_hash

class Contact(db.Model):
    __tablename__ = "contacts"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    name = db.Column(db.String(35), nullable=False)
    cellphone = db.Column(db.String(15), nullable=False, unique=True)

    def __init__(self, name, cellphone):
        self.name = name
        self.cellphone = cellphone
    
    def __repr__(self):
        return f"<Contacts: {self.name}"