import glob
import pathlib

# .------- filnamn
# glob.glob()
#      ^----- funktionsnamn

cwd = pathlib.Path().cwd()

result = glob.glob("*.txt")

print("cwd", cwd)
print("result", result)
