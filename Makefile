venv := $(CURDIR)/.venv
ENV  := env PATH=$(venv)/bin:$$PATH

WGET := $(shell which wget)
CURL := $(shell which curl)
ifdef WGET
	DL:=$(WGET) -c
else ifdef CURL
	DL:=$(CURL) -C - -O
endif

clean: venv/delete
	@find . -maxdepth 2 -name "__pycache__" -o -name "*.egg*" -o -name ".tox" -exec rm -rf "{}" \;
	@find . -type f -name "*.pyc" -exec rm -f "{}" \;

install: clean download venv/create
	$(ENV) pip install -U pip
	$(ENV) pip install -U -r $(CURDIR)/requirements.txt
	$(ENV) python ./pre_processing.py

download:
ifdef DL
	cd ./data/ && $(DL) http://www.iro.umontreal.ca/~lisa/deep/data/mnist/mnist.pkl.gz
else
	@echo "You need wget or curl installed to download"
	@exit 1
endif

run:
	$(ENV) ipython notebook

app:
	cd ./app_neural_network && $(ENV) python app.py

python/install:
	yum install -y python-devel gcc libffi-devel openssl-devel
	curl -kL https://raw.github.com/pypa/pip/master/contrib/get-pip.py | python

virtualenv/install:
	pip install -U pip virtualenv

venv/create:
	@if [ ! -d $(venv) ]; then \
		virtualenv --no-site-packages --distribute $(venv); \
	fi

venv/delete:
	rm -rf $(venv)
