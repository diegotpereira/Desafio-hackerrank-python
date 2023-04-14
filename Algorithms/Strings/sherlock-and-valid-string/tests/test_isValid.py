from isValid import isValid
import pytest

class TestIsValid:
    
    def test_valid_input(self):
        
        assert isValid("aabbcd") == "NO"
        
        assert isValid("aabbccddeefghi") == "NO"
        
        # assert isValid("abcdefghhgfedecba") == "YES"
        
        assert isValid("aabbc") == "YES"
        
    # def test_invalid_input(self):
    #     with pytest.raises(TypeError):
    #         isValid(123)
    #     with pytest.raises(ValueError):
    #         isValid("")