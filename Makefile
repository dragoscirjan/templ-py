PY_VER:=
PIP_FLAGS=--trusted-host pypi.org --trusted-host pypi.python.org

GLOBAL_PYTHON=python$(PY_VER)
GLOBAPL_PIP=pip$(PY_VER)
GLOBAL_PIP_INSTALL=$(GLOBAPL_PIP) install $(PIP_FLAGS)

ifeq (Windows_NT,$(OS))
	LOCAL_PYTHON=env/Scripts/python
	LOCAL_PIP=env/Scripts/pip
else
	LOCAL_PYTHON=env/bin/python
	LOCAL_PIP=env/bin/pip
endif

LOCAL_PIP_INSTALL=$(LOCAL_PIP) install $(PIP_FLAGS)

VIRTUALENV_ARGS?=--python python$(PY_VER)

.PHONY: clean virtualenv test docker dist dist-upload

clean:
	find . -name '*.py[co]' -delete
	find . -type d -iname "*__pycache__*" -delete

virtualenv:
	$(GLOBAL_PIP_INSTALL) virtualenv
	virtualenv $(VIRTUALENV_ARGS) --prompt '|> pytempl <| ' env
	$(LOCAL_PIP) install -r requirements-dev.txt
	$(LOCAL_PYTHON) setup.py develop
	@echo
	@echo "VirtualENV Setup Complete. Now run: source env/bin/activate"
	@echo

test:
	python -m pytest \
		-v \
		--cov=pytempl \
		--cov-report=term \
		--cov-report=html:coverage-report \
		tests/

docker: clean
	docker build -t pytempl:latest .

dist: clean
	rm -rf dist/*
	$(GLOBAL_PYTHON) setup.py sdist
	$(GLOBAL_PYTHON) setup.py bdist_wheel

dist-upload:
	twine upload dist/*
