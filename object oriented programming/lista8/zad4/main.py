from base_class import DataAccessHandler
from database_handler import SumColumnStrategy, get_db_data
from xml_handler import LongestNodeNameStrategy, get_xml_data

if __name__ == "__main__":
    print("Database:")
    handler = DataAccessHandler(SumColumnStrategy())
    handler.execute(get_db_data)

    print("\nXML:")
    handler = DataAccessHandler(LongestNodeNameStrategy())
    handler.execute(get_xml_data)
