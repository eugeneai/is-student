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

    def equals(other):
        """True if self is equal logically to other"""

class IStorage(Interface):
    def store(obj):
        """Store an object into a storage."""

    def get(key, class_):
        """Retrieve an object from s storage."""

    def remove(key):
        """Revove the object referenced by a key
        from the storage."""

    def size():
        """Returns the number of the objects in
        a database."""

class IDctionaryStorage(IStorage):
    """Stores object in a dictionary.
    A marker interface.
    """

class ISQLiteStorage(IStorage):
    """Stores objects through an ISQLStorabeObject
    component"""

class IMongoDBStorage(IStorage):
    """Stores objects into a mongodb"""

class IMongoDBStorable(Interface):
    """
    """

    def store_in(db):
        """Store self into a db"""

    def load(db, key, obj):
        """Convert data into a class_ instance"""
