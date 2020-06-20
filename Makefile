include Makefile.include

## Add your make instructions here

PROJECT=python_template

MODE = mod
# MODE = app
init: init-$(SHELL_IS) ## Initialize Project MODE=mod<|app>
	echo include Makefile.$(MODE).include > Makefile


init-bash:
ifneq ($(PROJECT),python_template)
	mv python_template $(PROJECT)
endif
	grep python_template . -Rin | awk -F ':' '{ print $git $1 }' | while read f; do sed -e 's/python_template/$(PROJECT)/g' -i $$f; done

init-powershell:
	$(POWERSHELL) -File ./.scripts/make.ps1 -Action init -Project $(PROJECT)
