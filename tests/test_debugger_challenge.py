from lib.debugger_challenge import *

def test_letter_counter():
    counter = LetterCounter("Digital Punk")
    result = counter.calculate_most_common()
    assert result == [2, 'i']