@echo off
:: Ustaw ścieżkę do Conda, jeśli nie jest w PATH (w anaconda prompt polecenie - conda env list)
set CONDA_PATH=C:\Users\tomas\AppData\Local\Programs\anaconda3
call %CONDA_PATH%\condabin\conda.bat activate env_conda_3_12_7

:: Przejdź do katalogu ze skryptem
cd C:\Users\tomas\Analiza-danych-w-Python-09_12_24\Skrypt

:: Uruchom skrypt
python skrypt.py

:: (Opcjonalnie) Dezaktywuj środowisko
call conda deactivate
pause
