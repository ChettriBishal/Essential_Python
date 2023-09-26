'''
class EmailNotification:
    def send_email(self, message):
        print(f"Sending email: {message}")

class SMSNotification:
    def send_sms(self, message):
        print(f"Sending SMS: {message}")

class NotificationService:
    def __init__(self, notifier):
        self.notifier = notifier

    def send_notification(self, message):
        self.notifier.send_notification(message)

here the high level code directly depends upon low level code
'''
#this can be updated as follows 

from abc import ABC, abstractmethod

class Notifier(ABC):
    @abstractmethod
    def send_notification(self, message):
        pass

class EmailNotification(Notifier):
    def send_notification(self, message):
        print(f"Sending email: {message}")

class SMSNotification(Notifier):
    def send_notification(self, message):
        print(f"Sending SMS: {message}")

class NotificationService:
    def __init__(self, notifier):
        self.notifier = notifier

    def send_notification(self, message):
        self.notifier.send_notification(message)

