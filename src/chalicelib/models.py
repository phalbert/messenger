"""Models"""
import base64
from abc import ABC, abstractmethod
from .services import NotificationService

class MessageInterface(ABC):
    """Message Interface"""

    def __init__(self, **kwargs):
        self.receipient = kwargs.get('receipient')
        self.sender = kwargs.get('sender')
        self.message = kwargs.get('message')
        self.service = NotificationService()

    @abstractmethod
    def send(self):
        """abstract method"""
        pass

class Email(MessageInterface):
    """Email"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.subject = kwargs.get('subject')

    def init(self, json):
        self.receipient = json.get('receipient')
        self.sender = json.get('sender')
        self.message = json.get('message')
        self.subject = json.get('subject')
        self.service = NotificationService()

    def send(self):
        """send a message"""
        return self.service.send_email(self)