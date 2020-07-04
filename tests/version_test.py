
from py_greet.version import get_static_version

###
# Model for using Pytest
###

# import pytest

# def test_hello():
#   assert get_static_version() == '0.0.1'


###
# Model for using UnitTest
###

import unittest

class VersionTestCase(unittest.TestCase):

  def test_get_static_version(self):
    self.assertEqual(get_static_version(), '0.0.1')
