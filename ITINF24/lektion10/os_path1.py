import os

p = print

cwd = os.getcwd()

p("cwd", cwd)
p("basename", os.path.basename(cwd))
