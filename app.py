from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Die neue Predigten-App ist erfolgreich eingerichtet!'
