from components import Student
from interfaces import IStudent, IStorage, IMongoDBStorage
#from mongo import *
from zope.configuration.xmlconfig import xmlconfig
from zope.component import getUtility

xmlconfig(open("configure.zcml"))

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
    ivanov=test1()
    db=getUtility(IMongoDBStorage, name="database")
    id_ivanov=db.store(ivanov)
    i=db.get(id_ivanov, Student)
    print (ivanov)
    print (i)
    assert i.equals(ivanov)

if __name__=="__main__":
    print ()
    test_db1()
    print ()
    print ("Ok")
    quit()
