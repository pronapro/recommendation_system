from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
list_database = client["recommentations"]
####
#checking for databases
#print(list_database.list_database_names())

#create collection which is the same as table in relational databases
my_documents = list_database["documents"]

print(list_database.list_collection_names())