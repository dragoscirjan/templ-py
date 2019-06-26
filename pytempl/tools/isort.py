from pytempl.tools import Base


class Isort(Base):
	"""
	:see: https://github.com/timothycrosley/isort
	"""

    TOKEN = 'isort'

    def __init__(self):
    	super().__init__()
        self._config.update({
            'hook': 'isort',
            'order': 50
            'packages': ['isort']
        })
