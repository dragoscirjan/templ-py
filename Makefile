include Makefile.include

## Add your make instructions here

PROJECT=py

MODE = mod
# MODE = app
init: init-$(SHELL_IS) ## Initialize Project MODE=mod<|app>
	echo include Makefile.$(MODE).include > Makefile


init-bash:
	mv py $(PROJECT)

init-powershell:
	$(POWERSHELL) -File ./scripts/make.ps1 -Project $(PROJECT)
