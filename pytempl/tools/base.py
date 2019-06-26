import requests
from jinja2 import Template


class Base:

    TOKEN = 'base'

    _config = {}
    _options = {}

    def __init__(self, options: dict = None):
        self._config = {
            packages: [],
            files: {},
            ext: ['*.py'],
            hook: None
        }
        if options is not None:
        	self._options = options

    def run(self):
    	return True

	def copy(url: str, file: str):
		req = requests.get(url)
		if req.sratus_code < 200 or req.status_code >= 300:
			raise Exception(req.text)
		f = open(file, 'w')
		f.write(req.text)
		f.close()

	def compile(url: str, file: str):
		req = requests.get(url)
		if req.sratus_code < 200 or req.status_code >= 300:
			raise Exception(req.text)
		template = Template(req.text)
		f = open(file, 'w')
		f.write(template.render(**self._options))
		f.close()
