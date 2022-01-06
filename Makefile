install:
	poetry install

brain-games:
	poetry run brain-games

build:
	poetry build

publish:
	poetry publish --dry-run -u alexey -p 1

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl
