include Makefile.include

## Add your make instructions here

PROJECT=py

MODE = mod
# MODE = app
init: init-$(SHELL_IS) ## Initialize Project MODE=mod<|app>
	echo include Makefile.$(MODE).include > Makefile
	mv app $(PROJECT)

init-bash:

init-powershell:

