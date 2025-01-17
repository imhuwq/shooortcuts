@echo off

:: Clean previous builds
rmdir /s /q build dist *.egg-info 2>nul

:: Build package
python -m build

:: Upload to PyPI
twine upload dist/*

:: Clean up
rmdir /s /q build dist *.egg-info 2>nul 