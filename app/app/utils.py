from pymongo import MongoClient

connect_url = 'mongodb+srv://mayank:mymongodb@cluster0.2ytui.mongodb.net/results?retryWrites=true&w=majority'


def get_db_handle(db_name):
    client = MongoClient(connect_url)
    db = client[db_name]
    return db


def get_collection_handle(db_handle, collection_name):
    return db_handle[collection_name]
