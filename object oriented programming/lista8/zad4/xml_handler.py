import xml.etree.ElementTree as ET
from base_class import DataProcessingStrategy

class LongestNodeNameStrategy(DataProcessingStrategy):
    def process(self, data):
        longest = max(data.iter(), key=lambda el: len(el.tag))
        print(f"Longest name node: {longest.tag}")


def get_xml_data():
    xml_content = """
    <root>
        <short>val</short>
        <node1><longestname>val</longestname></node1>
        <node>val</node>
    </root>
    """
    return ET.fromstring(xml_content)
