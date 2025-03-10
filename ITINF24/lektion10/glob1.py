import glob
import pathlib

# .------- filnamn
# glob.glob()
#      ^----- funktionsnamn

cwd = pathlib.Path().cwd()

result1 = glob.glob("*.txt")

print("cwd", cwd)
print("result1", result1)

# för att rekursivt få med py-filer, som i underkat/intemig.py
result2 = glob.glob("**/*.py")
print("result2", result2)
