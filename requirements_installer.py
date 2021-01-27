import os

# Styling
bl = "echo. & "
equ = "="

# Creating the command line
cmd = 'color A0 & ' + bl*3 + 'echo "' + equ*15 + ' Installing requirements ' + equ*15 + '" & ' + bl*2 + 'echo. & '
cmd = cmd + 'pip install -U -r requirements.txt & ' + bl * 4
cmd = cmd + 'echo "' + equ*15 + ' Done ! ' + equ*15 + '" & ' + bl*3 + 'echo.'
cmd = 'cmd /k "' + cmd + '"'

# Executing the command line
os.system(cmd)