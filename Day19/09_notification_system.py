class Notification:

    def send(self):
        print("Sending Notification")

class Email(Notification):

    def send(self):
        print("Email Sent")

class SMS(Notification):

    def send(self):
        print("SMS Sent")

Email().send()
SMS().send()
