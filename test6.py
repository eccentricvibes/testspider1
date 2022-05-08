# import pymongo
# # client = pymongo.MongoClient(host='localhost', port=27017)
# client = pymongo.MongoClient('mongodb://localhost:27017/')
# # db = client.alex_db
# db = client['alex_db']
# # collection = db.students
# collection = db['students']
#
# student1 = {
#     "id": "20220331",
#     "name": "aiyc",
#     "age": 18,
#     "gender": "male",
# }
#
# student2 = {
#     "id": "20220334",
#     "name": "alex",
#     "age": 16,
#     "gender": "male",
# }
#
# result = collection.insert_many([student1, student2])
# print(result)
from faker import Faker
import pymongo
import random
client = pymongo.MongoClient(host="localhost", port=27017)
db = client.test
# db = client["test"]
collection = db.students_Alex
faker = Faker()
# collection = db["students_Alex"]
student = {
    "id": "27017",
    "name": "Jendan",
    "age": 20,
    "gender": "male"
}
for i in range(10):
    d1 = {
        "name": faker.name(),
        "age": random.randint(10, 30),
        "address": faker.address(),
        "city": faker.city(),
    }

    d2 = {
        "name": faker.name(),
        "age": random.randint(10, 30),
        "address": faker.address(),
        "city": faker.city(),
    }

    collection.insert_many([d1, d2])

# result = collection.find_one({"name": "Sierra Fry"})
# print(result)
import datetime
from bson.objectid import ObjectId
generated_time = datetime.datetime(2022, 3, 4)
id = ObjectId.from_datetime(generated_time)
result = collection.find_one({"_id": id})
print(result)
# result = collection.insert_one(student)
# print(result)
