from cement import TestApp

from .pytempl import PyTempl

class PyTemplTest(TestApp,PyTempl):
    """A sub-class of PyTempl that is better suited for testing."""

    class Meta:
        label = 'pytempl'
