"""Test messages"""
import asyncio
from src.chalicelib.services import NotificationService
from src.chalicelib.models import Email

def test_email_output():
    """test email"""
    mail = Email(
        receipient='email',
        sender='h',
        message='',
        subject='test'
    )
    service = NotificationService()

    result = service.send_email(mail)
    assert isinstance(result, dict)

