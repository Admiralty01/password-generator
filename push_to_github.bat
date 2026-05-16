@echo off
echo Capturing errors... Please wait.
cd /d "c:\Users\hp\Desktop\password_generator_v1.py" > git_log.txt 2>&1
git init >> git_log.txt 2>&1
git branch -M main >> git_log.txt 2>&1
git remote set-url origin https://github.com/Admiralty01/password-generator.git >> git_log.txt 2>&1
git remote -v >> git_log.txt 2>&1
git add . >> git_log.txt 2>&1
git commit -m "Upgrade to Hybrid Passphrase Suite v.2" >> git_log.txt 2>&1
git push -u origin main -f >> git_log.txt 2>&1
echo.
echo Finished capturing log!
pause
