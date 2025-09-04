import unittest
import test
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts')))
from largest_of_unlimited_numbers import biggest_number

def test_biggest_number():
    assert biggest_number([44,55,66]) == 66.0
    assert biggest_number([2,1]) != 1.0
test_biggest_number()
print("test passed")