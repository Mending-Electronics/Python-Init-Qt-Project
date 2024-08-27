@echo off

@title=Script - Download requirements Wheels (packages)

set dirProject="%cd%"
set dirPkgs="%dirProject%\pkgs"


@title=Prompt of the .venv
@color 3F

@echo Autor: Alexandre JALLET 10.2023


call .venv\Scripts\activate.bat && @echo. && @echo Packages intalled - Freeze the 'requirements.txt' : && @echo. && pip freeze && pip freeze > "%dirProject%/requirements.txt" && cd "%dirPkgs%" && pip freeze > "%dirPkgs%/requirements.txt" && @echo. && @echo Downloading all requirements Wheels... && @echo. && pip download -r requirements.txt && pause

