class Email:
    def __init__(self, status):
        self.sent = status
    def sentFunction(self):
        if self.sent != 'sent':
            print('Send the message again')
        else: 
            print('Message was already sent')

instituto = Email('nsent')
print(instituto.sentFunction())
