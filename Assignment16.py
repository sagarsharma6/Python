##All 4 questions done in single question below

import pymongo
client=pymongo.MongoClient()
database=client['Students']
collection=database['students']
for i in range(10):
    name=input("Enter name: ")
    marks=int(input("Enter marks:"))
    if(marks<0 or marks>100):
        print("Invalid marks,skipping data of current student named",name)
        continue
    collection.insert_one({'Name':name,'Marks':marks})
data=collection.find({'Marks':{'$gt':80}})
for document in data:
    print(document)
