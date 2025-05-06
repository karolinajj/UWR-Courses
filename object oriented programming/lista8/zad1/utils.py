class Message:
    def __init__(self, title, content):
        self.title = title
        self.content = content

class Request:
    def __init__(self, message):
        self.message = message
        self.type = None         # compliment, complaint, orders, other
        self.invalid = False