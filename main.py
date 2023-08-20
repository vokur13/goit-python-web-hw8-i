from utilities.commander import commander
from utilities.command_handler import command_handler
from utilities.commands import COMMANDS


def main():
    for com in commander(COMMANDS):
        print(command_handler(com))


if __name__ == "__main__":
    main()
