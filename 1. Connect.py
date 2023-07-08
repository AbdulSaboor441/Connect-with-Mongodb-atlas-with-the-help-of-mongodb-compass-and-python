import pymongo

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb+srv://Abdul_Saboor:AWW-475@cluster0.3t7vtj2.mongodb.net/"
    )

    show_all_databases = client.list_database_names()
    print(show_all_databases)

    db = client["codewithharry"]
    show_all_collections = db.list_collection_names()
    print(show_all_collections)

    collection = db["codewithharry"]

    # insert_one_document = collection.insert_one({"_id":1,"name":"A"})

    insert_one_more_document = collection.insert_one({"_id":2,"name":"B"})
