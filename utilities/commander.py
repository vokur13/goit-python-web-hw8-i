def commander(commands):
    while True:
        com = input("Enter command: ").split(":")
        if com[0] in commands and com[0] not in ["exit"]:
            yield com
        elif com[0] in commands and com[0] in ["exit"]:
            yield com
            break
        else:
            break


if __name__ == "__main__":
    pass
