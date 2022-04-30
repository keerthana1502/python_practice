import pymongo
connection_url="mongodb://localhost:27017"
client = pymongo.MongoClient(connection_url)
db = client['users']
collection = db['employee']
#collection.insert_one({"name":"ocean"})
#collection.insert_many([{"name":"keerthana","number":5,"department":"CSE"},
                       #{"name":"kishore","number":6,"department":"IT"},
                       #{"name":"Ajay","number":7,"department":"ECE"},
                       #{"name":"shakthi","number":8,"department":"EEE"}])
query = {"name":"shakthi"}
#ret = collection.find_one(query)
#print(ret)
'''ret1=collection.find()
for i in ret1:
    print(i)
newData={"$set":{"name":"shanmu"}}
collection.update_one(query,newData)
ret1=collection.find()
for i in ret1:
    print(i)'''
collection.delete_one(query)
