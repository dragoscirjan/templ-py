
from python_template.hello import hello

###
# Model for using Pytest
###

# import pytest

# def test_hello():
#   assert hello('World') == 'Hello World!'


###
# Model for using UnitTest
###

import unittest

class HelloTestCase(unittest.TestCase):

  def test_hello(self):
    self.assertEqual(hello('World'), 'Hello World!')
