import xml.etree.ElementTree as ET
from base_class import DataAccessHandler

class XmlAccessHandler(DataAccessHandler):
    def __init__(self, file_path):
        self.file_path = file_path

    def connect(self):
        print(f"Opening file: {self.file_path}")

    def get_data(self):
        tree = ET.parse(self.file_path)
        return tree.getroot()

    def process_data(self, data):
        longest_node = max(data.iter(), key=lambda el: len(el.tag))
        print(f"Node with the longest name: {longest_node.tag}")

    def disconnect(self):
        print("Disconnecting from XML file.")

