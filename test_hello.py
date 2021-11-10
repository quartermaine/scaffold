from hello import add

def test_add():
    assert add(1, 2) == 3
    assert add(3, 2) == 5
    assert add(10, 13) == 23
    assert add(-3, 4) == 1

