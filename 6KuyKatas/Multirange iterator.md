Let's look at the following generator:
```
def gen():
    for i in range(2):
        for j in range(3):
            yield (i, j)
```
If we print all yielded values, we'll get
```
(0, 0)
(0, 1)
(0, 2)
(1, 0)
(1, 1)
(1, 2)
```
For a given parameter list N you must return an iterator, which goes through all possible tuples A, where Ai changes from 0 to Ni.
