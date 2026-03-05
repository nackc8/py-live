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

    print("loop is breaked! pos_args = ", pos_args)
except InvalidInputError as e:
    print("Call error: ", str(e), file=sys.stderr)
    sys.exit(1)
