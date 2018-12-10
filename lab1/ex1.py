from pymongo import MongoClient

uri = "mongodb://admin:truongminhhieu0511@ds127604.mlab.com:27604/c4e24lab1"
client = MongoClient(uri)
db = client.get_database()
account_collection = db["accounts"]
for account in account_collection.find():
    print(account)
new_account = {
    "user name": "a1",
    "email": "truonghieu0511@gmail.com",
    "phone": "0395641198",
    "password":"123",
    "yob":21
}

  
print(new_account)
client.close()