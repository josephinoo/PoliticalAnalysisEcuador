
PYTHON = python3

.PHONY = help setup test run clean


FILES = input output


.DEFAULT_GOAL = help
help:
	@echo "---------------HELP-----------------"
	@echo "To setup the project type make setup"
	@echo "To test the project type make test"
	@echo "To run the project type make run"
	@echo "----------"
run:
	${PYTHON} main.py

