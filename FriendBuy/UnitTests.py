from InMemoryDatabase import InMemoryDatabase


class UnitTests:
    def __init__(self):
        self.runAllTests()

    def runAllTests(self):
        self.__testSetAndGet()
        self.__testUnset()
        self.__testNumEqualTo()
        self.__testBeginAndRollback()
        self.__testCommit()
        self.__testAll()
        print("All tests ran")

    def __testSetAndGet(self):
        database = InMemoryDatabase()
        res = 10
        name = "x"
        database.set(name, res)
        exp = database.get(name)
        if res != exp:
            print("Test Failure")

    def __testUnset(self):
        database = InMemoryDatabase()
        res = 10
        name = "x"
        database.set(name, res)
        exp = database.get(name)
        if res != exp:
            print("Test Failure")
        database.unset(name)
        if database.get(name) != "NULL":
            print("Test Failure")

    def __testNumEqualTo(self):
        database = InMemoryDatabase()
        ten = 10
        a = "a"
        b = "b"
        database.set(a, ten)
        database.set(b, ten)

        if database.numEqualTo(ten) != 2:
            print("Test Failure")

        if database.numEqualTo(20) != 0:
            print("Test Failure")

        database.set(b, 30)
        if database.numEqualTo(ten) != 1:
            print("Test Failure")

    def __testBeginAndRollback(self):
        database = InMemoryDatabase()
        database.begin()
        ten = 10
        a = "a"
        database.set(a, ten)
        if database.get(a) != ten:
            print("Test Failure")
        database.begin()
        twenty = 20
        database.set(a, twenty)
        if database.get(a) != twenty:
            print("Test Failure")
        database.rollback()
        if database.get(a) != ten:
            print("Test Failure")
        database.rollback()
        if database.get(a) != "NULL":
            print("Test Failure")

    def __testCommit(self):
        database = InMemoryDatabase()
        database.begin()
        ten = 10
        a = "a"
        database.set(a, ten)
        database.begin()
        twenty = 20
        database.set(a, twenty)
        database.commit()
        if database.get(a) != twenty:
            print("Test Failure")
        if database.rollback() != "NO TRANSACTION":
            print("Test Failure")

    def __testAll(self):
        database = InMemoryDatabase()
        ten = 10
        a = "a"
        database.set(a, ten)
        database.begin()
        if database.get(a) != ten:
            print("Test Failure")
        database.unset(a)
        if database.get(a) != "NULL":
            print("Test Failure")
        database.rollback()
        if database.numEqualTo(ten) != 1:
            print("Test Failure")










