from bson import ObjectId
from pymongo import MongoClient
from pymongo.errors import PyMongoError

from src.ui.theme.color import GRAY, YELLOW


class MongoDataSource:

    def __init__(self, mongo_uri: str, db_name: str) -> None:
        print(f"{YELLOW}{self.__class__.__name__} Init.{GRAY}")
        # self.uri = mongo_uri
        # self.db_name = db_name
        # self.client = None
        # self.db = None

        self.client = MongoClient(mongo_uri)
        self.db = self.client[db_name]

    def get_documents(self, collection_name: str, query: dict) -> list:
        """ Returns documents from a MongoDB collection. """ 
        try:
            return list(self.db[collection_name].find(query))
        except PyMongoError as e:
            print(f"Error al obtener documentos: {e}")


    def get_document(self, collection_name: str, query: dict) -> dict:
        """Retorna un único documento que cumple con la query o None si no existe."""
        try:
            return self.db[collection_name].find_one(query)
        except PyMongoError as e:
            print(f"Error al obtener el documento: {e}")
    
    def close(self) -> None:
        """ Closes the connection to the MongoDB client. """
        self.client.close()
    
if __name__ == "__main__":
    mongo = MongoDataSource(mongo_uri="mongodb://localhost:27017", db_name="alesar")
    doc = mongo.get_document("receipts", query={"_id": ObjectId("62fd785e10b5575cdb4e367c")})
    print(doc)
    print(type(doc))