from chalice import Chalice
import os

from chalicelib.controllers.email import EmailController

app = Chalice(app_name='messenger')

@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/emails', methods=['POST'])
def create_email():
    return EmailController(app, os.environ).send_email_sns()



