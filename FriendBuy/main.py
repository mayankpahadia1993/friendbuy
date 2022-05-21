from InMemoryDatabase import InMemoryDatabase


def performCommand(command, database):
    inputs = command.split(" ")
    if len(inputs) <= 0:
        raise RuntimeError("Wrong input given")
    if inputs[0] == "END":
        return False
    elif inputs[0] == "BEGIN":
        database.begin()
        return True
    elif inputs[0] == "ROLLBACK":
        database.rollback()
        return True
    elif inputs[0] == "COMMIT":
        database.commit()
        return True
    elif inputs[0] == "SET":
        if len(inputs) != 3:
            raise RuntimeError(f"SET - Wrong input given - {command}")
        database.set(inputs[1], inputs[2])
        return True
    elif inputs[0] == "GET":
        if len(inputs) != 2:
            raise RuntimeError(f"GET - Wrong input given - {command}")
        database.get(inputs[1])
        return True
    elif inputs[0] == "UNSET":
        if len(inputs) != 2:
            raise RuntimeError(f"UNSET - Wrong input given - {command}")
        database.unset(inputs[1])
        return True
    elif inputs[0] == "NUMEQUALTO":
        if len(inputs) != 2:
            raise RuntimeError(f"NUMEQUALTO - Wrong input given {command}")
        database.numEqualTo(inputs[1])
        return True
    else:
        raise RuntimeError(f"Wrong {command} given")


if __name__ == '__main__':
    inMemoryDatabase = InMemoryDatabase()
    while True:
        inputCommand = input().upper()
        if not performCommand(inputCommand, inMemoryDatabase):
            break
