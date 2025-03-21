# unionfind-link
With this UnionFind library you will get a basic library for checking: 
- Is this element in same set like another element?
- joining elements together in one set

Currently there is no rank implemented, so the tree structure is simple.
Only a reverse tree structure is supported.
Meaning, for printing the elements in the set, it goes through all elements to test the set.

Nor the less it is a good start for answering the mentioned question and joining sets.

Have Fun!
Basti


```python
    # - test linking
    uf = UnionFind()
    uf.union(1, 2)
    uf.union(3, 4)
    uf.union(5, 6)
    uf.union(1, 3)
    uf.union(6, 4)

    assert uf.connected(1, 6)

    # = test with None
    root = uf.find(7)
    try:
        uf.union(7, 8)
    except:
        uf.add(7)

    assert not uf.connected(7,8)
    uf.union(7,8)
    assert uf.connected(7,8)

    # = test without None
    uf.findOrCreate(9)
    uf.union(9,10)
    assert uf.connected(9,10)

```

## Example Application

A realy good application for unionfind structures is clustering with closest-pairs.
See: https://github.com/BastiYourDeveloper/clustering-closest-pairs 

*Enjoy the UnionFind structure with methods like findOrCreate() and find().*
Method find() can be used to test if element is already in UnionFind structure, and returns None if not.
