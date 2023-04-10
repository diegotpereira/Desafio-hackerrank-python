from compareTriplets import compareTriplets

class TestCompareTriplets:
    def test_example1(self):
        assert compareTriplets([1, 2, 3], [3, 2, 1]) == [1, 1]

    def test_example2(self):
        assert compareTriplets([17, 28, 30], [99, 16, 8]) == [2, 1]

    def test_example3(self):
        assert compareTriplets([4, 4, 4], [5, 5, 5]) == [0, 3]
