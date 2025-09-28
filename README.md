# SWEN-352-PYTHON-MOCK

# To initalize and activate venv
1. py -m venv .venv
2. source .venv/bin/activate

# Make sure to install requirements
pip install -r requirements.txt

# To run unit tests in python
1. python -m unittest discover
2. py -m unittest discover

# To measure code coverage
1. coverage run --source=library/ -m unittest discover

2. coverage html OR coverage report
