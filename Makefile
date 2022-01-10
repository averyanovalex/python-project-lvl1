install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run -u alexey -p 1

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 brain_games

brain-games:
	poetry run brain-games

brain-even:
	poetry run brain-even

brain-calc:
	poetry run brain-calc
