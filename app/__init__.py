from flask_restful import Api
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_redis import FlaskRedis
from app.config.flask_settings import Config
from dotenv import load_dotenv
import os
from os.path import join, dirname

# Create .env file path.
dotenv_path = join(dirname(__file__), '.env')
# Load environments
load_dotenv(dotenv_path)

# Variáveis declaradas aqui para sererm usadas no main.py pelo $ flask shell
# Incialização do Banco de Dados
db = SQLAlchemy()
# Redis init
#redis_store = FlaskRedis()

# def create_app(config_name):
app = Flask(__name__)
app.config.from_object(Config)
api = Api(app, prefix="/api/v1")
db.init_app(app)
#redis_store.init_app(app)

# Registro de  Rotas vs Controllers
from app.controllers.contacts import Contacts
api.add_resource(Contacts, "/contacts")

from app.controllers.hello import Hello
api.add_resource(Hello, "/hello")

from app.controllers.healthcheck import Healthcheck
api.add_resource(Healthcheck, "/healthcheck")

# return app
