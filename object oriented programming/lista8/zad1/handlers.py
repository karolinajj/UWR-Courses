from abc import ABC, abstractmethod

# Abstract handler
class Handler(ABC):
    def __init__(self, next_handler=None):
        self.next_handler = next_handler

    @abstractmethod
    def handle(self, request):
        pass

class ClassifierHandler(Handler):
    def handle(self, request):
        msg = request.message
        if not msg.title or not msg.content:
            request.invalid = True
            print("Invalid message: empty title or content.")
        else:
            title = msg.title.lower()
            if "compliment" in title:
                request.type = "compliment"
            elif "complaint" in title:
                request.type = "complaint"
            elif "order" in title:
                request.type = "order"
            else:
                request.type = "other"

        if self.next_handler:   #passing request to the next handler (if exists)
            self.next_handler.handle(request)

class ComplimentHandler(Handler):
    def handle(self, request):
        if request.type == "compliment":
            print("Processing compliment message...")
        if self.next_handler:
            self.next_handler.handle(request)

class ComplaintHandler(Handler):
    def handle(self, request):
        if request.type == "complaint":
            print("Processing complaint message...")
        if self.next_handler:
            self.next_handler.handle(request)

class OrderHandler(Handler):
    def handle(self, request):
        if request.type == "order":
            print("Processing order message...")
        if self.next_handler:
            self.next_handler.handle(request)

class OtherHandler(Handler):
    def handle(self, request):
        if request.type == "other":
            print("Processing other type of message...")
        if self.next_handler:
            self.next_handler.handle(request)

class InvalidMessageHandler(Handler):
    def handle(self, request):
        if request.invalid:
            print("Processing invalid message...")
        if self.next_handler:
            self.next_handler.handle(request)


class ArchivingHandler(Handler):
    def handle(self, request):
        print("Archiving message...")

        with open("archived_messages.txt", "a", encoding="utf-8") as file:
            file.write(f"{request.message.title}\n")
            file.write(f"{request.message.content}\n")
            file.write("\n")
        request.result = "Archived message."
        return request.result

