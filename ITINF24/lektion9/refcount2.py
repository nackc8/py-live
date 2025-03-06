import sys

def 

obj = ["hello"]
en_till_var = obj
print(sys.getrefcount(obj))
# försvinner först: import refcount, refcount.obj = None, refcount.en_till_var = None
