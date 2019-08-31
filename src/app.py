from chalice import Chalice
from chalicelib.models import Email

app = Chalice(app_name='messenger')

@app.route('/')
def index():
    return {'hello': 'world'}

@app.route('/emails', methods=['POST'])
def create_email():
    email_as_json = app.current_request.json_body
    email = Email(email_as_json)
    return email.send()
    # return {'email': email.__dict__}



