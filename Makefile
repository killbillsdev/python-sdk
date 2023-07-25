publish:build
	@echo "Publishing version specified in pyproj.toml ! ..."
	python3 -m twine upload dist/*
	@echo "Done"

install: 
	@echo "Installing..."
	python3 -m pip install .
	@echo "Done"

build:
	@echo "Building..."
	python3 -m build
	@echo "Done"

test:
	@echo "Testing..."
	cd ./src/killbills_sdk && python3 -m pytest -p no:warnings -vsv
	@echo "Done"		

.PHONY: build install publish
