import pytest
from staircase import staircase

class TestStaircase:

    def test_staircase(self):

        # assert staircase(6) == "     #\n"
        assert staircase(6) == "     #\n    ##\n   ###\n  ####\n #####\n######"

    
    def test_staircase_zero(self):
        assert staircase(0) == ""

    def test_staircase_negative(self):
        with pytest.raises(ValueError):
            staircase(-5)

    def test_staircase_float(self):
        with pytest.raises(TypeError):
            staircase(2.5)