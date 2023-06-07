def lazy(n):
    def lazy_decorator(func):
        def wrapper(*args, **kwargs):
            if n > 0:
                if lazy_decorator.count == n:
                    result = func(*args, **kwargs)
                else:
                    result = None
                lazy_decorator.count -= 1

            elif n < 0:
                if lazy_decorator.count + 1 == 0:
                    result = None
                else:
                    result = func(*args, **kwargs)
                lazy_decorator.count += 1

            if lazy_decorator.count == 0:
                lazy_decorator.count = n

            return result

        lazy_decorator.count = n
        return wrapper
    return lazy_decorator

