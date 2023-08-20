from reed_data.quotes_by_author import quotes_by_author


def commander(com: list):
    print(f"{com=}")
    # while True:
    match com[0]:
        case "name":
            # print(f"{com[1]=}")
            # yield quotes_by_author(com[1])
            # yield print(f"{com[1]=}")
            quotes_by_author(com[1])
        case "tag":
            print(com[1])
            # yield com[1]
        case "exit":
            ...
            # break
        case _:
            ...
            # break
