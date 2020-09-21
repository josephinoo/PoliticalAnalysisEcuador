
GREEN := $(shell tput -Txterm setaf 2)
YELLOW := $(shell tput -Txterm setaf 3)
RESET := $(shell tput -Txterm sgr0)
PYTHON = python3


run:
	@echo "${YELLOW}--------------------------RUNNING----------------------------${RESET}"
	${PYTHON} main.py

packages:
	@echo "${YELLOW}-------------------------INSTALLING------------------------------${RESET}"
	pip3 install -r requirements.txt
	@echo "${GREEN}[+]installed packages${RESET}"
	@echo "${YELLOW}-----------------------------------------------------------------${RESET}"