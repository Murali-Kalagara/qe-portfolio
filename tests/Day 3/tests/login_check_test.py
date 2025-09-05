import unittest
import test
import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'scripts')))
from login_check import userid_password_check
 
def test_userid_password_check():
    assert userid_password_check('Test', 'Test123') == True
    assert userid_password_check('Test', 'wrongpass') == False
    assert userid_password_check('unknown', 'Test123') == False

print("All passed")