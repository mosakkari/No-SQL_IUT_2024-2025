from pymongo import MongoClient
import os

CLUSTER_UNAME = os.getenv("CLUSTER_UNAME")
CLUSTER_PASSWD = os.getenv("CLUSTER_PASSWD")

client = MongoClient(f"mongodb+srv://{CLUSTER_UNAME}:{CLUSTER_PASSWD}@cluster0.rdbul.mongodb.net/")
print(client.list_database_names())
