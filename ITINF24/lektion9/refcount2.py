import sys

lst = []


def lst_add_print(obj):
    lst.append(obj)
    print(lst)


obj = ["hello"]
en_till_var = obj
print(sys.getrefcount(obj))
# försvinner först: import refcount, refcount.obj = None, refcount.en_till_var = None
