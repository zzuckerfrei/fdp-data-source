from pymongo import MongoClient
from pprint import pprint
import datetime

# # 1. DB connection
# client = MongoClient(host='localhost', port=27017, username='root', password='root')
#
# # 2. DB 접근
# db = client['test']
#
# # 3. Collection 접근
# collection = db['testCollection']
# ## posts collection접근
# posts = db.posts
#
# # 4. Documents 생성
# post = {"name": "Mike",
#         "age": 40,
#         "hobby": ["mongodb", "python", "pymongo"],
#         "date": datetime.datetime.now()
#         }
# collection_id = collection.insert_one(post).inserted_id
# post_id = posts.insert_one(post).inserted_id
#
client = MongoClient(host='localhost', port=27017, username='root', password='root')

db = client['test-db']
collection = db['event']

data_event_1 = {
  "id" : "44a69b91-c642-40b1-a615-db11054b3adb",
  "index" : 3,
  "period" : 1,
  "timestamp" : "00:00:00.000",
  "minute" : 0,
  "second" : 0,
  "type" : {
    "id" : 18,
    "name" : "Half Start"
  },
  "possession" : 1,
  "possession_team" : {
    "id" : 217,
    "name" : "Barcelona"
  },
  "play_pattern" : {
    "id" : 1,
    "name" : "Regular Play"
  },
  "team" : {
    "id" : 217,
    "name" : "Barcelona"
  },
  "duration" : 0.0,
  "related_events" : [ "11493e75-0d53-4489-8ccf-a2d2752661ec" ]
}

result_id = collection.insert_one(data_event_1).inserted_id

if __name__ == '__main__':
    # print(client.list_database_names())
    # print(db)
    # print(collection)
    # print(posts)
    #
    # # Collection 리스트 조회
    # print(db.list_collection_names())
    # print(post_id)
    # print(collection_id)
    # pprint(posts.find_one())

    print("=====show collection=====")
    for dict in collection.find():
        pprint(dict)
