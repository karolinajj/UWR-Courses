from abc import ABC, abstractmethod

class DataAccessHandler(ABC):
    def execute(self):
        self.connect()
        data = self.get_data()
        self.process_data(data)
        self.disconnect()

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def get_data(self):
        pass

    @abstractmethod
    def process_data(self, data):
        pass

    @abstractmethod
    def disconnect(self):
        pass
