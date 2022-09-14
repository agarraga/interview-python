MODULE := interapp

run:
	@python -m $(MODULE)

test:
	@pytest

lint:
	@flake8
	@bandit

clean:
	rm -rf .pytest_cache

deps:
	@pip install -r requirements.txt
