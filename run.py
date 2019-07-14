from app import app as application

# chamado manualmente com: $ flask run
if __name__ == "__main__":
    import os
    application.run(host='0.0.0.0', port=os.getenv('SERVER_PORT'))
