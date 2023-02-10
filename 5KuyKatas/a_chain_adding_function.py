class add(int):
    def __call__(self, num: int) -> int:
        return add(self + num)