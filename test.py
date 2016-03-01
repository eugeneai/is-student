from components import Student
from interfaces import IStudent, IStorage
from mongo import *



def test1():
    assert IStudent.implementedBy(Student)
    ivanov=Student(name="Ivanov Ivan")
    assert IStudent.providedBy(ivanov)

    ivanov.add("programming", 5)
    ivanov.add("programming", 4)
    ivanov.add("programming", 3)
    assert ivanov.grades("programming")==[5,4,3]
    assert ivanov.average("programming")==4
    ivanov.add("programming", 5)
    assert abs(ivanov.average("programming")-(5*2+4+3)/4)<0.01
    #ivanov.average("funcan")
    return ivanov

def test_db1():
    assert IStorage.implementedBy(MongoDBStorage)
    assert IMongoDBStorage.implementedBy(MongoDBStorage)
    ivanov=test1()
    db=MongoDBStorage()
    #oldsize=db.size()
    id_ivanov=db.store(ivanov)
    #assert db.size()==oldsize+1
    i=db.get(id_ivanov, Student)
    print (ivanov)
    print (i)
    assert i.equals(ivanov)
    #db.remove(id_ivanov)
    #assert db.size()==oldsize


if __name__=="__main__":
    print ()
    test_db1()
    print ()
    print ("Ok")
    quit()
