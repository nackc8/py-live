import os

p = print

cwd = os.getcwd()

p("cwd", cwd)
p("dirname", os.path.dirname(cwd))
p("basename", os.path.basename(cwd))
p("/etc/ssh/sshd_config", os.path.exists()
