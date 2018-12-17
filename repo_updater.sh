#!/bin/bash
#update daily every 2 hours
#Author: Solomon Amos

cd ~/projects/LearnPython_Class
git init
git add .
git commit -m "update Today's log:)"
git remote add origin https://github.com/udohsolomon/LearnPython_Class.git
git push -u origin master
git config credential.helper store