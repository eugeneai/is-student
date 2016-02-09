from components import Student
from interfaces import IStudent

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
    ivanov.average("funcan")

if __name__=="__main__":
    test1()
    print ()
    print ("Ok")
    quit()
