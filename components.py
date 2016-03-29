from interfaces import IStudent, IStorage, IDctionaryStorage, ILoadEvent, IStoreEvent, IID
from zope.interface import implementer, adapter
from zope.component import getUtility, subscribers


import sqlite3


@implementer(IStudent)
class Student(object):
    """Implements a student.
    """
    #implements(IStudent)

    def __init__(self, name=None, stub=False):
        """Initialize the students

        Arguments:
        - `name`: Name of the student
        """
        if name != None:
            self.name = name
        if stub:
            self.name = "<NonExitent>"
        self._grades = {}

    def add(self, subject, grade):
        self._grades.setdefault(subject, []).append(grade)

    def replace_grades(self, subject, grades):
        self._grades[subject]=grades

    def grades(self, subject=None):
        if subject==None:
            return self._grades
        else:
            return self._grades[subject]

    def average(self, subject):
        try:
            grades=self._grades[subject]
        except KeyError as e:
            raise ValueError("wrong subject")

        s=sum(grades)
        return float(s)/len(grades)

    def equals(self, other):
        if self.name!=other.name:
            return False

        return set(self._grades)==set(other._grades)

    def __str__(self):
        return "Student(name={}, grades={})".format(
            self.name, self._grades)

#@implementer(ILoadEvent)
#@adapter(IID)
class StudentLoader(object):
    def __init__(self, obj):
        self.obj=obj
    def storage(self):
        return getUtility(IStorage, name="database")
    def load(self):
        return self.storage().get(self.obj.id, Student)
    def store(self):
        return self.storage().store(self.obj)

@implementer(IID)
class id_holder(object):
    def __init__(self, id):
        self.id=id

def load_object(id):
    oid=id_holder(id)
    obj=subscribers([oid], ILoadEvent)[0].load()
    return obj
