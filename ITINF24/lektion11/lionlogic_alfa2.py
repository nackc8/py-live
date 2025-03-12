def process(filenames, show_filename, show_linenumbers):
    output_lines = []
    for filename in filenames:
        with open(filename) as fp:
            contentlines = fp.readlines()

        if show_filename:
            new_line = f'{filename}:\n\n"'
            output_lines.append(new_line)

        for lineno_line_tuple in enumerate(contentlines, 1):
            lineno = lineno_line_tuple[0]
            line = lineno_line_tuple[1]
            if show_linenumbers:
                new_line = f"{lineno} {line}"
                output_lines.append(new_line)
            else:
                output_lines.append(line)
    return output_lines
