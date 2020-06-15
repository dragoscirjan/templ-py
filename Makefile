include Makefile.include

## Add your make instructions here

PROJECT=python_template

MODE = mod
# MODE = app
init: init-$(SHELL_IS) ## Initialize Project MODE=mod<|app>
	echo include Makefile.$(MODE).include > Makefile


init-bash:
	mv python_template $(PROJECT)
	sed -e 's/python_template/$(PROJECT)/g' -i Makefile.mod.include
	sed -e 's/python_template/$(PROJECT)/g' -i setup.py

init-powershell:
	$(POWERSHELL) -File ./.scripts/make.ps1 -Action init -Project $(PROJECT)
