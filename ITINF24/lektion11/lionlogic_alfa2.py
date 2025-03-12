def process(filename):
    return [filename, "hej", "jopp"]


for filename in filenames:
    with open(filename) as fp:
        contentlines = fp.readlines()

    # lite nytt: är samma som att skriva
    # if show_filename == True
    if show_filename:
        print(filename, ":", sep="", end="\n\n")

    # alt sätt: (med unboxing av tupeln)
    # for lineno, line in enumerate(contentlines, 1):

    for lineno_line_tuple in enumerate(contentlines, 1):
        lineno = lineno_line_tuple[0]
        line = lineno_line_tuple[1]
        if show_linenumbers:
            print(lineno, line, end="")
        else:
            print(line, end="")
