def validate_hello(greetings):
    g = ['hello', 'ciao', 'salut', 'hallo', 'hola', 'ahoj', 'czesc']
    for s in g:
        if s in greetings.lower():
            return True
    return False