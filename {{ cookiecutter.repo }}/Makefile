DOCS_FILES = $(wildcard docs/*.rst docs/*.md docs/*.ipynb)
TESTS = $(wildcard tests/*.py)
SRC_FILES = $(wildcard src/*/*.py)
IPYNB_FILES = $(wildcard *.ipynb)
REPORTS = $(patsubst %.ipynb, %.html, $(IPYNB_FILES))
SCRIPTS = $(patsubst %.ipynb, %.py, $(IPYNB_FILES))

all: $(REPORTS) $(SCRIPTS) docs
reports: $(REPORTS)
scripts: $(SCRIPTS)
docs: docs/_build/html/index.html

docs/_build/html/index.html: $(DOCS_FILES) $(TESTS) $(SRC_FILES)
	sphinx-build -M html docs/ docs/_build

%.html: %.ipynb
	jupyter nbconvert $^

%.py: %.ipynb
	jupyter nbconvert --to python $^

