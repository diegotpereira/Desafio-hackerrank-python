from timeConversion import timeConversion

class TestTimeConversion:
    
    def test_timeConversion_1(self):
        
        assert timeConversion("07:05:45PM") == "19:05:45"
        
    def test_timeConversion_2(self):
        
        assert timeConversion("12:00:00PM") == "12:00:00"
        
    def test_timeConversion_3(self):
        assert timeConversion("12:00:00AM") == "00:00:00"