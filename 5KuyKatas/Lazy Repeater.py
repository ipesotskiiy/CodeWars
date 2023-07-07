def make_looper(string):
    global x
    x = list(string)
    return func

def func():
    y = x.pop(0)
    x.append(y)
    return y