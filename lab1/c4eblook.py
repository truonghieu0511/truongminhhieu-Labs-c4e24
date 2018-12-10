from pymongo import MongoClient



# 1 connect to database sever
uri = "mongodb://admin:truongminhhieu0511@ds127604.mlab.com:27604/c4e24lab1"
client = MongoClient(uri)


# 2 select database
db = client.get_database()

# 3 select collection
post_collection = db["posts"]
for post in post_collection.find():
    print(post)

# # 4 create document
# new_document = {
#     "title" : "hôm nay việt nam thắng ",
#     "post" : "mình vẫn ở nhà code ... điên à ! tao đi bão ",
# }

# # # 5 add document into collection
# post_collection.insert_one(new_document)
# 6 close connection
client.close()