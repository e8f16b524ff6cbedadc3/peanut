.PHONY: default

default: run


run:
	python peanut/main.py

dep_install:
	python -m pip install -U pip -r requirements.txt
