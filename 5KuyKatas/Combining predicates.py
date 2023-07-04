def predicate(func):
    return Predicate(func)


class Predicate:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        return self.func(*args, **kwargs)

    def __and__(self, other):
        return Predicate(
            lambda *args, **kwargs: (
                    self.func(*args, **kwargs)
                    and other.func(*args, **kwargs)
            )
        )

    def __or__(self, other):
        return Predicate(
            lambda *args, **kwargs: (
                    self.func(*args, **kwargs)
                    or other.func(*args, **kwargs)
            )
        )

    def __invert__(self):
        return Predicate(
            lambda *args, **kwargs: not self.func(*args, **kwargs)
        )