import unittest
import test
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts')))
from string_reverse_for_loop import reverse
def test_reverse_of_string():
    assert reverse("hello") == "olleh"
    assert reverse("hello") != ""
test_reverse_of_string()
print("test passed")