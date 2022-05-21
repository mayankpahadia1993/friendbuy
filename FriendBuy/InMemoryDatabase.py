from collections import defaultdict


class InMemoryDatabase:
    def __init__(self):
        self.database = {}
        self.valueAnalytics = defaultdict(int)
        self.transactionBlocks = []
        self.transactionBlocks.append((self.database, self.valueAnalytics))

    def set(self, name, value):
        if name in self.database:
            prevValue = self.database[name]
            self.__reduceValue(prevValue)
        self.database[name] = value
        self.valueAnalytics[value] += 1

    def get(self, name):
        if name in self.database:
            print(self.database[name])
        else:
            print("NULL")

    def unset(self, name):
        if name in self.database:
            value = self.database[name]
            self.__reduceValue(value)
            self.database.pop(name)

    def numEqualTo(self, value):
        print(self.valueAnalytics[value])

    def begin(self):
        if self.__checkTransactionBlocks():
            prev = (self.transactionBlocks[-1][0].copy(), self.transactionBlocks[-1][1].copy())
            self.transactionBlocks.append(prev)
            self.__setCurrDatabase()

    def rollback(self):
        if len(self.transactionBlocks) <= 1:
            print("NO TRANSACTION")
        elif self.__checkTransactionBlocks():
            self.transactionBlocks.pop()
            self.__setCurrDatabase()

    def commit(self):
        if self.__checkTransactionBlocks():
            self.__setCurrDatabase()
            self.__clearAndAppend(self.database)

    def __setCurrDatabase(self):
        if self.__checkTransactionBlocks():
            (self.database, self.valueAnalytics) = self.transactionBlocks[-1]

    def __checkTransactionBlocks(self):
        if len(self.transactionBlocks) == 0:
            raise RuntimeError("TransactionBlocks can not be empty")
        return True

    def __clearAndAppend(self, data):
        self.transactionBlocks.clear()
        self.transactionBlocks.append(data)

    def __reduceValue(self, value):
        if self.valueAnalytics[value] > 0:
            self.valueAnalytics[value] -= 1
