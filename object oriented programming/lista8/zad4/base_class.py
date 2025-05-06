from abc import ABC, abstractmethod

class DataProcessingStrategy(ABC):
    @abstractmethod
    def process(self, data):
        pass

class DataAccessHandler:
    def __init__(self, strategy: DataProcessingStrategy):
        self.strategy = strategy

    def execute(self, data_source_func):
        self.connect()
        data = data_source_func()
        self.strategy.process(data)
        self.disconnect()

    def connect(self):
        print("Connecting")

    def disconnect(self):
        print("Disconnecting")
