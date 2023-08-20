from commander import commander

if __name__ == "__main__":
    res = input("Enter command: ").split(":")
    com_ = list()
    for item in res:
        com_.append(item.strip())
    # print(com_)
    commander(com_)
