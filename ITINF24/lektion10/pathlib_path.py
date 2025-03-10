from pathlib import Path

p = print

cwd = Path.cwd()
p("cwd", cwd)
cwd_parent_dir = cwd.parent
p("cwd_parent_dir", cwd_parent_dir)

p("dirname", cwd.name)
p("basename", cwd.)
# p("exists(/etc/ssh/sshd_config)", os.path.exists("/etc/ssh/sshd_config"))
