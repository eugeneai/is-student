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
