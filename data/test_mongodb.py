from pymongo import MongoClient
from src.config.config import MONGO_DB_URL

uri = MONGO_DB_URL

client = MongoClient(uri)

try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)