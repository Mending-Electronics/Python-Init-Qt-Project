@echo off

@title=Freeze requirements packages (with version)

set dirStart=%cd%

set "year=%DATE:~6,4%"
set "month=%DATE:~3,2%"
set "day=%DATE:~0,2%"
set "formattedDate=%year%_%month%_%day%"
echo %formattedDate%



@title=Prompt of the .venv
@color 3F

@echo Autor: Alexandre JALLET 10.2023


call .venv\Scripts\activate.bat && @echo. && @echo Packages intalled - Freeze the 'requirements.txt' : && @echo. && pip freeze && pip freeze > "%cd%/%formattedDate%_freeze_requirements.txt" && pause
pause
