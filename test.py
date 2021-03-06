from components import Student, load_object
from interfaces import IStudent, IStorage, IMongoDBStorage
#from mongo import *
from zope.configuration.xmlconfig import xmlconfig
from zope.component import getUtility

xmlconfig(open("remote.zcml"))

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
    db=getUtility(IStorage, name="database")
    id_ivanov=db.store(ivanov)
    i=db.get(id_ivanov, Student)
    print (ivanov)
    print (i)
    assert i.equals(ivanov)

def get_student(id):
    return load_object(id)

def test_remote():
    import rpyc
    conn=rpyc.classic.connect('localhost')
    test=conn.modules.test
    stud=test.get_student('56f11bf572bb0a1e27160741')
    print (stud)
    print (type(stud))

if __name__=="__main__":
    print ()
    #test_db1()
    test_remote()
    print ()
    print ("Ok")
    quit()
