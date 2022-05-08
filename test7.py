# import pymongo
from faker import Faker
# client = pymongo.MongoClient(host="localhost", port=27017)
# # client = pymongo.MongoClient("mongodb://localhost:27017")
# db = client.test
# db = client["test"]
# # collections = db.students
# collection = db["students"]
#
# student = {
#     "id": "2701111",
#     "name": "Jordan",
#     "age": 20,
#     "gender": "male",
# }
#
# student1 = {
#     "id": "2701111",
#     "name": "Jordan",
#     "age": 20,
#     "gender": "male",
# }
#
# student2 = {
#     "id": "2701111",
#     "name": "Jordan",
#     "age": 20,
#     "gender": "male",
# }
#
# result = collection.insert_one(student)
# result = collection.insert_many([student1, student2])
# print(result)
import pymongo

student1 = student1 = {"id": "2701111",
"name": "Jordan",
"age": 20,
"gender": "male",
}

def db(db_name="default_db", table_name="default_table", insert_data="None"):
    print("Setting up database and relaying a connection...")
    client = pymongo.MongoClient(host="localhost", port=27017)
    print("Connection successful.")
    # db = client.test
    # collection = db[db_name]
    print("Creating database...")
    db = client[db_name]
    print(f"Database: {db_name} successfully created!")

    print("Setting up database table...")
    collection = db[table_name]
    print(f"{table_name} successfully created!")
    print(f"Inserting data into database...{insert_data}")
    if isinstance(insert_data, list):
        result = collection.insert_many(insert_data)
    elif isinstance(insert_data, dict):
        result = collection.insert_one(insert_data)
    print(result)

def generate_data():
    faker = Faker()
    data_lst = []
    for i in range(100):
        dict_data = {
            "id": i,
            "name": faker.name(),
            "email": faker.email(),
            "address": faker.address(),
        }
        data_lst.append(dict_data)
    return data_lst



if __name__ == "__main__":
    data = {
        "name": "aiyc",
        "age": 14,
        "grade": 12,
    }
    db(insert_data=data)
    # db(insert_data=generate_data())
    print(generate_data())