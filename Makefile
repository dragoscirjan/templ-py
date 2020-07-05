include Makefile.include

## Add your make instructions here

PROJECT=py_greet
MODE = mod
# MODE = app
init: init-$(SHELL_IS) ## Initialize Project MODE=mod<|app>
	echo include Makefile.$(MODE).include > Makefile


init-bash:
ifneq ($(PROJECT),py_greet)
	mv py_greet $(PROJECT)
endif
	make init-$(OSFLAG)

init-LINUX:
	grep py_greet . -Rin | awk -F ':' '{ print git $$1 }' | while read f; do sed -e 's/py_greet/$(PROJECT)/g' -i $$f; done

init-OSX:
	grep py_greet . -Rin | awk -F ':' '{ print git $$1 }' | while read f; do sed -i -e 's/py_greet/$(PROJECT)/g' $$f; done

init-powershell:
	$(POWERSHELL) -File ./.scripts/make.ps1 -Action init -Project $(PROJECT)
