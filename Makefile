.PHONY: test test-all test-1 test-2 test-3 clear

test: test-all

test-all:
	python3 -m unittest

test-1:
	python3 -m unittest -v test.task_1.FillSpiralMatrixTest

test-2:
	python3 -m unittest -v test.task_2.HaveSameItemsTest

test-3:
	python3 -m unittest -v test.task_3.EmitterTest

clear:
	find . -name "*.pyc" -type f -delete
	find . -name "__pycache__" -type d -delete
