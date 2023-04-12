from gradingStudents import gradingStudents

def test_gradingStudents():
    
    assert gradingStudents([73, 67, 38, 33]) == [75, 67, 40, 33]
    
    assert gradingStudents([22, 28, 25]) == [22, 28, 25]