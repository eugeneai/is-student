from interfaces import IStudent, IStorage, IDctionaryStorage
from zope.interface import implementer, adapter
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

    def grades(self, subject):
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

"""
@implementer(IDctionaryStorage)
class DictionaryStorage(object):
    def __init__(self):
        self.storage={}

    def put(self, obj):
        key=len(self.storage)
        self.storage[key]=obj
        return key

    def get(self, key):
        return self.storage[key]

    def remove(self, key):
        del self.storage[key]

    def size(self):
        return len(self.storage)

@implementer(ISQLiteStorage)
@adapts(IStudent)
class SQLiteStudentStorer(object):
    def __init__(self, student):
        self.student=student
        self.connect()

    def put(self, obj):


    def get(self, key):

    def remove(self, key):

    def size(self):
        ...
"""
