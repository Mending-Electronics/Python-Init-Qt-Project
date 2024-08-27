@echo off

@title=Re-Install project venv from downloaded Wheels 

set dirProject="%cd%"
set dirPkgs="%dirProject%\pkgs"
set dirPip="%dirPkgs%\pip"

@title=Prompt of the .venv
@color 3F

@echo Autor: Alexandre JALLET 10.2023


call .venv\Scripts\activate.bat && @echo. && @echo Installing Python Installer Packages... && @echo. && cd "%dirPip%" && python setup.py install && @echo. && @echo Installing requirements Wheels... && @echo. && cd "%dirPkgs%" && pip install --no-index --find-links . -r requirements.txt && pause
