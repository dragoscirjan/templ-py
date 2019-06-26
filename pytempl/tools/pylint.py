from pytempl.tools import Base


class Pylint(Base):
    """
    :see: https://www.pylint.org/
    """

    TOKEN = 'pylint'

    def __init__(self):
    	super().__init__()
        self._config.update({
            'files': {
            	'pylintrc': 'https://raw.githubusercontent.com/PyCQA/pylint/master/pylintrc'
            },
            'hook': 'pylint',
            'order': 1000
            'packages': ['pylint']
        })
