@echo off
echo ================================
echo Iniciando atualização do projeto via Git
echo ================================

REM === Configurações globais (só precisa uma vez, mas está aqui por segurançaa)
git config --global user.name "samnabr"
git config --global user.email "snr.abreu@gmail.com"

REM === Verificar se há alterações
git status --porcelain > temp_git_status.txt
for /f %%i in ('type temp_git_status.txt ^| find /c /v ""') do set COUNT=%%i
del temp_git_status.txt

if %COUNT%==0 (
    echo Nenhuma alteração encontrada. Nada para enviar ao GitHub.
    goto FIM
)

echo.
echo Adicionando arquivos modificados...
git add .

echo.
set /p mensagem="Digite a mensagem do commit: "
git commit -m "%mensagem%"

echo.
echo Enviando para o GitHub...
git push origin main

:FIM
echo ================================
echo Finalizado! Verifique o GitHub :)
pause
