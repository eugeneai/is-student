from zope.interface import Interface, Attribute

class IStudent(Interface):
    """Defines interface for student component.
    """

    name=Attribute("Name of the student")

    def add(subject, grade):
        """Adds a grade to student's grades"""

    def average(subject):
        """Returns the average student's grade
        for a subject"""

    def grades(subject):
        """Return list of grades for a subkect"""
