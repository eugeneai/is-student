from components import Student

def test1():
    ivanov=Student(name="Ivanov Ivan")
    ivanov.add("programming", 5)
    ivanov.add("programming", 4)
    ivanov.add("programming", 3)
    assert ivanov.avg("programming")==4

if __name__=="__main__":
    test1()
    quit()
