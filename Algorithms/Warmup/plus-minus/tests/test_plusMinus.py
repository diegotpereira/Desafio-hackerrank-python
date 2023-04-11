from plusMinus import plusMinus

def test_plusMinus():
    assert plusMinus([-4, 3, -9, 0, 4, 1]) == "0.5\n0.333333\n0.166667"
    assert plusMinus([1, 2, 3, -1, -2, -3, 0, 0]) == "0.375\n0.375\n0.25"
    assert plusMinus([0, 0, 0]) == "0.0\n0.0\n1.0"

