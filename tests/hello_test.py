"""Testing py_greet.hello"""

# ##
# Model for using Pytest
# ##

# import pytest
# from py_greet.hello import hello

# def test_hello():
#   assert hello('World') == 'Hello World!'


###
# Model for using UnitTest
###

import unittest
from py_greet.hello import hello


class HelloTestCase(unittest.TestCase):
  """`hello` Test Case"""

  def test_hello(self):
    """Testing `hello` returns proper message"""
    self.assertEqual(hello('World'), 'Hello World!')
