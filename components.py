from interfaces import IStudent
from zope.interface import implementer


@implementer(IStudent)
class Student(object):
    """Implements a student.
    """
    #implements(IStudent)

    def __init__(self, name):
        """Initialize the students

        Arguments:
        - `name`: Name of the student
        """
        self.name = name

    def add(self, subject, grade):
        pass

    def average(self, subject):
        return 4
