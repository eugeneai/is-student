from zope.interface import Interface, Attribute

class IStudent(Interface):
    """Defines interface for student component.
    """

    def add(subject, grade):
        """Adds a grade to student's grades"""

    def average(subject):
        """Returns the average student's grade
        for a subject"""
