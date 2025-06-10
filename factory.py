class Notification:
    def notify(self) -> str:
        raise NotImplementedError("Subclass must implement this method")


class EmailNotification(Notification):
    def notify(self):
        return "Sending email..."


class SMSNotification(Notification):
    def notify(self):
        return "Sending sms..."


class NotificationFactory:
    def create_notification(self, type: str) -> Notification:
        if type == "email":
            return EmailNotification()
        elif type == "sms":
            return SMSNotification()
        raise ValueError("Invalid notification type")


notification_factory = NotificationFactory()
email_notification = notification_factory.create_notification("email")
sms_notification = notification_factory.create_notification("sms")

assert email_notification.notify() == "Sending email..."
assert sms_notification.notify() == "Sending sms..."

try:
    notification_factory.create_notification("")
except ValueError:
    assert True
