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

# En fabrik som ger tillbaka kompletta och
# användbara funktioner
def fun_fac():
    lst = []

    def inner_fun(obj):
        lst.append(obj)
        print(lst)

    return inner_fun


add_print1 = fun_fac()
add_print2 = fun_fac()

add_print1("Hej")
add_print2("Hello")
add_print2("Super")
add_print2("Mario")
add_print2("World")
add_print1("Benny!")
```

### Referenser

Blir referenser enligt:
```mermaid
flowchart LR
var_add_print1 --> 1_fun_inner_fun
1_fun_inner_fun --> 1_lst
var_add_print2 --> 2_fun_inner_fun
2_fun_inner_fun --> 2_lst

```
`lst` är nyskapad, likaså `fun_inner_fun`. Båda skapades av vår fabrik.

### Skapadet och anropen

```mermaid
sequenceDiagram
    Note over modulen: add_print1 =
    modulen->>fun_fac: (inga arg)
    Note over fun_fac: Skapar ny lista `lst` och en ny function `inner_fun`
    fun_fac-->>modulen: funktionspekaren till 1_fun_inner_fun

    Note over modulen: add_print2 =
    modulen->>fun_fac: (inga arg)
    Note over fun_fac: Skapar ny lista `lst` och en ny function `inner_fun`
    fun_fac-->>modulen: funktionspekaren till 2_fun_inner_fun
    Note over modulen: anropen följer
    add_print1_Hej -> 1_fun_inner_fun: d

```
    add_print2_Hello
    add_print2_Super
    add_print2_Mario
    add_print2_World
    add_print1_Benny

