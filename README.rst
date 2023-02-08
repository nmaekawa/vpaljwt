vpaljwt
========

generate vpaljwt


overview
========


quickstart
==========

Create a virtual environment and install from source.::

    # clone this repo
    $> git clone https://github.com/nmaekawa/vpaljwt.git
    $>

    # create and activate a virtualenv
    $> virtualenv -p python3 venv
    $> source venv/bin/activate
    $(venv)>

    # install package
    $(venv)> cd vpaljwt
    $(venv) venv> pip install .
    $(venv) venv>

    # check help
    $(venv) venv> vpaljwt --help
    Usage: vpaljwt [OPTIONS]

    Options:
    --creds TEXT  json file with kondo api creds  [required]
    --help        Show this message and exit.


unit tests
==========


---eop

