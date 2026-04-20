# Global - den står utan indentering
calls = 1


def hello():
    # global gör så att vi kan skriva till variabeln
    global calls
    # Vi kan läsa den globala
    greet = "hello" * calls
    print(greet, calls)
    # Men inte skriva, då blir det fel
    calls = 100


def hello_failure():
    # Vi kan läsa den globala
    greet = "hello" * calls
    print(greet, calls)
    # Men inte skriva, då blir det fel
    # calls = 100


hello()
hello()
