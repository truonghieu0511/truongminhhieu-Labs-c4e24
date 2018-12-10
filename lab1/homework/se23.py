from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(uri)
db = client.get_database()
post_collection = db["post"]
new_document ={
    "title": "xuân này con không về ",
    "author" :"Tr Hiếu",
    "content" :"năm trước con về làm cái máy giặt ko biết nay về lần nữa nhà ta sẽ mất cái gì đây . Nên năm nay con ko về nữa :(" 
}
post_collection.insert_one(new_document)
client.close()