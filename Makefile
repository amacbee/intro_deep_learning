venv := .venv

curl:=$(shell which curl)

clean:
	rm -rf $(venv)
	@find . -maxdepth 2 -name "__pycache__" -o -name "*.egg*" -o -name ".tox" -exec rm -rf "{}" \;
	@find . -type f -name "*.pyc" -exec rm -f "{}" \;

init: clean venv/create
	cd ./data/ && $(curl) -C - -O http://www.iro.umontreal.ca/~lisa/deep/data/mnist/mnist.pkl.gz
	@echo '"source $(venv)/bin/activate"'

setup:
	pip install -U pip
	pip install -U -r $(CURDIR)/requirements.txt
	python ./pre_processing.py

run:
	ipython notebook

app:
	cd ./app_neural_network && python app.py

python/install:
	yum install -y python-devel gcc libffi-devel openssl-devel
	curl -kL https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python

virtualenv/install:
	pip install -U pip
	pip install -U virtualenv virtualenvwrapper
	export WORKON_HOME=$(HOME)/.virtualenvs
	export PROJECT_HOME=$(HOME)/dev/virtualenv
	@echo '"source `which virtualenvwrapper.sh`" or "pyenv rehash" ?'

venv/create:
	@if [ ! -d $(venv) ]; then \
		virtualenv --no-site-packages --distribute $(venv); \
	fi
