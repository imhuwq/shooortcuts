#!/bin/bash

# Clean previous builds
rm -rf build/ dist/ *.egg-info/

# Build package
python -m build

# Upload to PyPI
twine upload dist/*

# Clean up
rm -rf build/ dist/ *.egg-info/ 