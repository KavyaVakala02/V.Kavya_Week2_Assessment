class Notification:
    def send(self, message):
        raise NotImplementedError("Subclass didnot implement this method")
class EmailNotification(Notification):
    def send(self, message):  #method to return mail is sending
        return f"Sending Email: {message}"
class SMSNotification(Notification):  #class for sms notification
    def send(self, message):
        return f"Sending SMS: {message}"
# Create instances of EmailNotification and SMSNotification
email_notification = EmailNotification()
sms_notification = SMSNotification()
print(email_notification.send("Email msg"))  # Email notification
print(sms_notification.send("SMS msg!"))      # SMS notification
