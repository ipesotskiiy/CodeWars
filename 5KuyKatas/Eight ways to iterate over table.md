__Problem__

Since table has four corners, there are eight ways to iterate over its' elements ((by rows then by columns | by columns then by rows) * (top left to bottom right | top right to bottom left | bottom left to top right | bottom right to top left)).

Implement forward iterator that can be constucted with two directions as parameters that returns table items in specified order. (c++: implement begin(dir0,dir1) and end() functions, python: implement walk(dir0,dir1) function)

For example iterator with directions up left must return (one by one):
```
9, 6, 3, 8, 5, 2, 7, 4, 1
```
for table
```
{{1,2,3},
 {4,5,6},
 {7,8,9}}
```
For simplicity lets assume that table have at least one row and at least one column and we dont need to test for that.

**C++**

Iterator must support assignment.

__Python__

Iterator must be lazy (assuming Table.data have __getitem__(key) and __len__() implemented on both dimensions).
