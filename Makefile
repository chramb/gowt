PYTHON ?= $(shell command -v python)
MAKEFILE =$(abspath $(MAKEFILE_LIST))

.PHONY: help clean

# Usage:
#
#	make [rule]
#
# Rules:

help:
#	help 	- print this help message
	@grep '#' $(MAKEFILE) | grep -v '##'  | sed -e 's:# ::' -e 's:#::'

clean:
#	clean	- remove generated files
	@rm -rf \
		./.coverage \
		./.mypy_cache \
		./.pytest_cache \
		./{src,tests}/**/__pycache__ \
		./dist \
		./htmlcov \
