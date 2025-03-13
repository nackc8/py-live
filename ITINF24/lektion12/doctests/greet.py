def greet(name = None)
    if name is None:
        return "Hello stranger!"
    else:
        return f"Hello {name}!"
