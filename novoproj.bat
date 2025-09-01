@echo off

rem Cria um novo projeto Textual no diretório
rem especificado em linha de comando inicializando
rem ele com um ambiente virtual Pythone  framwork Textual
rem usando venv.
rem 
rem sintaxe:
rem novoproj <direório do projeto>

set NOME_PROJ=%1
python novoproj.py %NOME_PROJ%
cd %NOME_PROJ%
.venv\Scripts\activate
pip install textual