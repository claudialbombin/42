# Makefile of A-Maze-ing

PYTHON	= python3
PIP		= $(PYTHON) -m pip
MAIN	= a_maze_ing.py
CONFIG	= config.txt

# install the tools needed for lint and for building the package
install:
	$(PIP) install -r requirements.txt

run:
	$(PYTHON) $(MAIN) $(CONFIG)

# same as run but inside pdb (Python debugger)
debug:
	$(PYTHON) -m pdb $(MAIN) $(CONFIG)

# remove caches and build folders (the .whl at the root is kept)
clean:
	find . -name "__pycache__" -type d -prune -exec rm -rf {} +
	rm -rf .mypy_cache .pytest_cache
	rm -rf build dist *.egg-info

lint:
	flake8 .
	mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports \
		--disallow-untyped-defs --check-untyped-defs

lint-strict:
	flake8 .
	mypy . --strict

# build the mazegen package and copy the wheel to the root of the repo
build:
	$(PYTHON) -m build
	cp dist/mazegen-*.whl .

.PHONY: install run debug clean lint lint-strict build
