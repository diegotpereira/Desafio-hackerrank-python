from simpleArraySum import simpleArraySum

class TestSimpleArraySum:
    def test_simpleArraySum(self):
        assert simpleArraySum([1, 2, 3, 4, 10, 11]) == 31
        assert simpleArraySum([5, 10, 15, 20]) == 50
        assert simpleArraySum([0, 0, 0, 0, 0]) == 0