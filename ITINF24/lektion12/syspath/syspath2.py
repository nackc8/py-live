import sys

# Vi förlitar oss på miljövariabeln PYTHONPATH istället.
# sys.path.append("/tmp/minmodd")
#
# Funkar till exempel med:
# PYTHONPATH=/tmp/minmodd python3 lektion12/syspath2.py
import modden

# extern fil enligt:
# echo 'print("HELLO FROM MINMODD")' > /tmp/minmodd/modden.py


print(sys.path)
