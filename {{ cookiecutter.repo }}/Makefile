DOCS_FILES = $(wildcard docs/*.rst docs/*.md docs/*.ipynb)
PY_FILES = $(wildcard tests/*.py src/*/*.py)
IPYNB_FILES = $(wildcard *.ipynb)
REPORTS = $(patsubst %.ipynb, %.html, $(IPYNB_FILES))
SCRIPTS = $(patsubst %.ipynb, %.py, $(IPYNB_FILES))

all: docs $(REPORTS) $(SCRIPTS)
docs: docs/_build/html/index.html
reports: $(REPORTS)
scripts: $(SCRIPTS)

docs/_build/html/index.html: $(DOCS_FILES) $(PY_FILES)
	sphinx-build -M html docs/ docs/_build

%.html: %.ipynb
	jupyter nbconvert $^

%.py: %.ipynb
	jupyter nbconvert --to python $^

.PHONY: all docs reports scripts
