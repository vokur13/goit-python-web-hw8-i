from utilities.commands import COMMANDS


def operate(operator):
    return COMMANDS[operator]


def command_handler(com):
    com_ = list()
    for item in com:
        com_.append(item.strip())
    args = com_[1:]
    for arg in args:
        if "," in arg:
            arg_ = arg.split(",")
            return operate(com_[0])(arg_)
        else:
            return operate(com_[0])(args[0])
