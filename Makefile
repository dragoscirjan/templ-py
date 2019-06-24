PIP_FLAGS=--trusted-host pypi.org --trusted-host pypi.python.org
PIP_INSTALL=env/bin/pip install $(PIP_FLAGS)
PYTHON=env/bin/python

.PHONY: clean virtualenv test docker dist dist-upload

clean:
	find . -name '*.py[co]' -delete

virtualenv:
ifneq (,$(shell which python3))
	python3 -m venv env
	$(PIP_INSTALL) -r requirements.txt || ( \
		curl https://bootstrap.pypa.io/get-pip.py | $(PYTHON) && $(PIP_INSTALL) -r requirements.txt \
	)
else
	virtualenv --prompt '|> pytempl <| ' env
endif
	$(PIP_INSTALL) -r requirements-dev.txt || ( \
		curl https://bootstrap.pypa.io/get-pip.py | $(PYTHON) && $(PIP_INSTALL) -r requirements-dev.txt \
	)
	$(PYTHON) setup.py develop
	@echo
	@echo "VirtualENV Setup Complete. Now run: source env/bin/activate"
	@echo

test:
	$(PYTHON) -m pytest \
		-v \
		--cov=pytempl \
		--cov-report=term \
		--cov-report=html:coverage-report \
		tests/

docker: clean
	docker build -t pytempl:latest .

dist: clean
	rm -rf dist/*
	$(PYTHON) setup.py sdist
	$(PYTHON) setup.py bdist_wheel

dist-upload:
	twine upload dist/*
