# Refcount och scope

# "Enkel" refcount

```python
import sys

obj = ["hello"]  # refcount = 1
```

```mermaid
flowchart LR
    obj --> list_hello
```

```
en_till_var = obj  # refcount = 2
```
```mermaid
flowchart LR
    obj --> list_hello
    en_till_var --> list_hello
```

```
print(sys.getrefcount(obj))  # refcount = 3, inne i sys.getrefcount()
```

```mermaid
flowchart LR
    obj --> list_hello
    en_till_var --> list_hello
    sys.getrefcount -->list_hello
```

## Funktionsfabrik

```python
def fun_fac():
    lst = []

    def inner_fun(obj):
        lst.append(obj)
        print(lst)

    return inner_fun

add_print1 = fun_fac()
add_print2 = fun_fac()
```
Blir referenser enligt:
```mermaid
flowchart LR
var_add_print1 --> x
```
