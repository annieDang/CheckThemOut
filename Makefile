.PHONY: venv install test activate main

VENV_DIR := venv

# Create virtual environment
venv:
	python3 -m venv $(VENV_DIR)

# Activate virtual environment
activate:
	source venv/bin/activate 
	
# Install dependencies
install:
	pip install -r requirements.txt

# Run tests
test:
	pytest
	
main:
	pytest
