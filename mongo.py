from pymongo import *
import datetime
from interfaces import *
from zope.interface import implementer
#from zope.component import adapter
from bson.objectid import ObjectId

@implementer(IMongoDBStorage)
class MongoDBStorage(object):
    def __init__(self, database="default", **kwargs):
        self.conn=MongoClient(**kwargs)
        self.db=self.conn[database]
        # self.db.students.delete_many({})

    def store(self, obj):
        o=IMongoDBStorable(obj)
        return o.store_in(self.db)

    def get(self, key, class_):
        obj=class_(stub=True)
        o=IMongoDBStorable(obj)
        o.load(self.db, key, obj)
        return obj

#@implementer(IMongoDBStorable)
#@adapter(IStudent)
class AdapterOfIStudentToIMongo(object):
    def __init__(self, student):
        self.student=student

    def store_in(self, db):
        stud={
            "name": self.student.name,
            "grades": self.student._grades
            }
        if hasattr(self.student, "obj_id"):
            db.students.delete_many({"_id":ObjectId(self.student.obj_id)})
        obj_id=str(db.students.insert_one(stud).inserted_id)
        self.student.obj_id=obj_id
        return obj_id

    def load(self, db, key, stub):
        stud=db.students.find_one({"_id":ObjectId(key)})
        stub.name=stud["name"]
        stub._grades=stud["grades"]

db=MongoDBStorage()

def test_mongo():
    """Test mongo
    """

    client = MongoClient()
    db = client['test-database']
    collection = db['test-collection']

    post = {"author": "Mike",
            "text": "My first blog post!",
            "tags": ["mongodb", "python", "pymongo"],
            "date": datetime.datetime.utcnow()}

    posts = db.posts
    post_id = posts.insert_one(post).inserted_id
    print ("Post ID:", post_id)

    #print (db.collection_names(include_system_collections=True))

    print (posts.find_one())

    print (posts.find_one({"author": "Mike"}))

    print (posts.find_one({"author": "Eliot"}))

    print (str(post_id))

assert IStorage.implementedBy(MongoDBStorage)
assert IMongoDBStorage.implementedBy(MongoDBStorage)


if __name__=="__main__":
    test_mongo()
    print ("Ok")
    quit()
