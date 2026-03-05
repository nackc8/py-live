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
    for arg in sys.argv[1:]:
        if arg == "-c" or arg == "-C" or arg == "--complement":
            if option_complement:
                raise InvalidInputError("Only specify complement once!")
            option_complement = True
            print(arg)
except InvalidInputError as e:
    print("Call error: ", str(e), file=sys.stderr)
    sys.exit(1)
