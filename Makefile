install:
	virtualenv --version || pip install virtualenv
	virtualenv -p /usr/bin/python3 .env

test: test-all

test-all:
	. .env/bin/activate && PYTHONENV=pwd python -m unittest

test-1:
	. .env/bin/activate && PYTHONENV=pwd python -m unittest -v test.task_1.FillSpiralMatrixTest

test-2:
	. .env/bin/activate && PYTHONENV=pwd python -m unittest -v test.task_2.HaveSameItemsTest

test-3:
	. .env/bin/activate && PYTHONENV=pwd python -m unittest -v test.task_3.EmitterTest

clear:
	find . -name "*.pyc" -type f -delete
	find . -name "__pycache__" -type d -delete
	rm -rf .env
