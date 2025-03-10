from pathlib import Path

p = print

cwd = Path.cwd()
p("cwd", cwd)
cwd_parent_dir = cwd.parent
p("cwd_parent_dir", cwd_parent_dir)

p("dirname", cwd.name)
p("basename", cwd.parent)
ssh_config = Path("/etc/ssh/sshd_config")
p("ssh_config.exists()", ssh_config.exists())

