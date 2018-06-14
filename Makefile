install:
	virtualenv --version || pip install virtualenv
	virtualenv -p /usr/bin/python2.7 .env
	. .env/bin/activate && pip install -r requirements.txt

test: test-1 test-2 test-3

test-1:
	. .env/bin/activate && PYTHONENV=pwd python -m unittest test.task_1.FillSpiralMatrixTest

test-2:
	. .env/bin/activate && PYTHONENV=pwd python -m unittest test.task_2.HaveSameItemsTest

test-3:
	. .env/bin/activate && PYTHONENV=pwd python -m unittest test.task_3.EmitterTest

clear:
	find . -name "*.pyc" -type f -delete
	rm -rf .env
