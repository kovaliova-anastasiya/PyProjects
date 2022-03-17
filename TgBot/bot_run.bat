@echo off

call %~dp0telegram_bot\venv\Scripts\activate

cd %~dp0telegram_bot

set TOKEN=5201727084:AAGVp7kZfmfTwrY9ETNFzNnvYIJYjKU_QSw

python bot_telegram.py

pause