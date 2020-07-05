"""Testing py_greet.version"""

###
# Model for using Pytest
###

# import pytest
# from py_greet.version import get_static_version

# def test_hello():
#   assert get_static_version() == '0.0.1'

###
# Model for using UnitTest
###

import unittest
from py_greet.version import get_static_version


class VersionTestCase(unittest.TestCase):
  """`get_static_version` Test Case"""

  def test_get_static_version(self):
    """Testing `get_static_version` returns proper value"""
    self.assertEqual(get_static_version(), '0.0.1')
