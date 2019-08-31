"""Services"""
from sendgrid import SendGridAPIClient, Attachment
from sendgrid.helpers.mail import Mail
from . import config

class NotificationService:
    """Notification Service"""

    def __init__(self):
        pass

    def send_email(self, mail):
        """Send an email"""
        message = Mail(
            from_email=mail.sender,
            to_emails=mail.receipient,
            subject=mail.subject,
            plain_text_content=mail.message)

        try:
            client = SendGridAPIClient(config.SENDGRID_API_KEY)
            response = client.send(message)
            print(response.__dict__)
            return {
                'status': response.status_code,
                'msg': 'email sent'
            }
        except Exception as e:
            return {
                'status': 500,
                'msg': str(e)
            }
