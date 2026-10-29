# Makefile of A-Maze-ing
#
# Everything runs with the "python" of a virtual environment (.venv).
# On macOS there is only "python3" outside a venv, so it is used once,
# just to create the venv. Inside the venv "python" always exists.

VENV	= .venv
PYTHON	= $(VENV)/bin/python
MAIN	= a_maze_ing.py
CONFIG	= config.txt

# create the virtual environment (only if it does not exist yet)
$(PYTHON):
	python3 -m venv $(VENV)

# install the tools needed for lint and for building the package
install: $(PYTHON)
	$(PYTHON) -m pip install -r requirements.txt

run: $(PYTHON)
	$(PYTHON) $(MAIN) $(CONFIG)

# same as run but inside pdb (Python debugger)
debug: $(PYTHON)
	$(PYTHON) -m pdb $(MAIN) $(CONFIG)

# remove caches and build folders (the .whl at the root is kept)
clean:
	find . -name "__pycache__" -type d -prune -not -path "./$(VENV)/*" \
		-exec rm -rf {} +
	rm -rf .mypy_cache .pytest_cache
	rm -rf build dist *.egg-info

# also remove the virtual environment
fclean: clean
	rm -rf $(VENV)

lint: install
	$(PYTHON) -m flake8 . --exclude $(VENV),build,dist
	$(PYTHON) -m mypy . --warn-return-any --warn-unused-ignores \
		--ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict: install
	$(PYTHON) -m flake8 . --exclude $(VENV),build,dist
	$(PYTHON) -m mypy . --strict

# build the mazegen package and copy the wheel to the root of the repo
build: install
	$(PYTHON) -m build
	cp dist/mazegen-*.whl .

.PHONY: install run debug clean fclean lint lint-strict build
