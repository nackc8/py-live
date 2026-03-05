import sys

# Lets mimic the tr command:
#        NAME
#          tr - translate or delete characters
#
#        ...
#
#        SYNOPSIS
#        tr [OPTION]... STRING1 [STRING2]
#        -c, -C, --complement
#               use the complement of ARRAY1
#        -d, --delete
#               delete characters in ARRAY1, do not translate


class InvalidInputError(ValueError):
    pass


try:
    option_complement = False
    option_delete = False
    all_args = sys.argv[1:]
    if (all_args) == 0:
        raise InvalidInputError("No arguments given")

    for index, arg in enumerate(all_args):
        print("arg: ", arg)
        if arg == "-c" or arg == "-C" or arg == "--complement":
            if option_complement:
                raise InvalidInputError("Only specify complement once!")
            option_complement = True
        elif arg == "-d" or arg == "--delete":
            if option_delete:
                raise InvalidInputError("Only specify delete once!")
            option_delete = True
        else:
            break

    # All non option arguments
    if arg == "--":
        pos_args = all_args[index + 1 :]
    else:
        pos_args = all_args[index:]

    if option_delete and len(all_args) != 1:
        raise InvalidInputError("extra operand")
    if not option_delete and len(all_args) != 2:
        raise InvalidInputError("missings operand")

    array1 = all_args[0]
    array2 = all_args[1] if not option_delete else None
except InvalidInputError as e:
    print("Call error: ", str(e), file=sys.stderr)
    sys.exit(1)


print("complement option:", option_complement)
print("delete option:", option_delete)
print("array1:", array1)
print("array2:", array2)
