from pymongo import MongoClient
from settings import config


client = MongoClient(config.dsn)  # type:ignore[var-annotated]
db = client[config.DB_NAME]
collection = db[config.DB_COLLECTION]


templates_forms = [
    {
        "form_name": "name 1",
        "date": "date",
        "phone": "phone",
        "email": "email",
        "text": "text",
    },
    {
        "form_name": "name 2",
        "date": "date",
        "email": "email",
        "text": "text",
    },
    {
        "form_name": "name 3",
        "date": "date",
        "phone": "phone",
        "text": "text",
    },
    {
        "form_name": "name 4",
        "date": "date",
        "phone": "phone",
        "email": "email",
    },
    {
        "form_name": "name 5",
        "date": "date",
        "phone": "phone",
    },
]

if __name__ == "__main__":
    collection.insert_many(templates_forms)
