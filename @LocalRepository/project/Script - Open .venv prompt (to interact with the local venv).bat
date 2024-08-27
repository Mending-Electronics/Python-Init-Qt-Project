@echo off

@title=Prompt of the .venv

@color 3F

@echo Autor: Alexandre JALLET 10.2023


call .venv\Scripts\activate.bat && @echo off && @echo. && @echo   ************************************************************ && @echo      You are currently in the activated Virtual Environment && @echo   ************************************************************ && @echo. && @echo  If you need to embeded other specifics packages in your venv && @echo  Install it with the commande bellow : && @echo  pip install 'name of the package' && @echo. && @echo  If you need to upgrading pip in your venv && @echo  Use the commande bellow : && @echo  python.exe -m pip install --upgrade pip && @echo. && cmd /k