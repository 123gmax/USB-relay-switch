Use the files in this folder to create standalone binary only

The template file is converted to .py file using 
   pyuic5 -x ./<Qt UI file>.ui -o <pythonfile name>.py
   
The generated file is imported by run_ubuntu.py

Executable is generated using pyinstaller
   pyinstaller run_ubuntu.py --onefile


