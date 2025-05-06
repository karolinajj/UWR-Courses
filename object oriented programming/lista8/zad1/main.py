from handlers import ArchivingHandler, InvalidMessageHandler, OtherHandler, OrderHandler, ComplaintHandler, ComplimentHandler, ClassifierHandler
from utils import Message, Request

if __name__ == "__main__":
    archiver = ArchivingHandler()
    invalid_handler = InvalidMessageHandler(archiver)
    other_handler = OtherHandler(invalid_handler)
    order_handler = OrderHandler(other_handler)
    complaint_handler = ComplaintHandler(order_handler)
    compliment_handler = ComplimentHandler(complaint_handler)
    classifier = ClassifierHandler(compliment_handler)

    messages = [
        Message("Complaint about service", "I am not satisfied."),
        Message("Compliment to staff", "Great job"),
        Message("Order 1", "I would like to cancel my order."),
        Message("Question", "How much is shipping?"),
        Message("Invalid Message", "")
    ]

    for msg in messages:
        print("\nTest:")
        req = Request(msg)
        classifier.handle(req)

    

