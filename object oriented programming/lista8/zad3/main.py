from download_database import DatabaseAccessHandler
from download_xml import XmlAccessHandler
import os

if __name__ == "__main__":
    print("Database: ")
    db_path = os.path.join(os.getcwd(), "sales.db")
    db_handler = DatabaseAccessHandler(db_path)
    db_handler.execute()

    print("\nXML: ")

    xml_file_path = os.path.join(os.getcwd(), "data.xml")
    xml_handler = XmlAccessHandler(xml_file_path)
    xml_handler.execute()
