@echo off
echo ================================
echo Configurando Git para este PC...
echo ================================

REM === Configurar nome e email (altere aqui!)
git config --global user.name "samnabr"
git config --global user.email "snr.abreu@gmail.com"

echo Nome e e-mail configurados com sucesso!

REM === Comandos para commit e push ===
echo.
echo Adicionando arquivos...
git add .

echo Criando commit...
git commit -m "primeiro commit"

echo Criando branch main...
git branch -M main

echo Adicionando repositório remoto...
git remote add origin https://github.com/samnabr/leitura_lei.git

echo Enviando para o GitHub...
git push -u origin main

echo ================================
echo Finalizado! Verifique o GitHub :)
pause
