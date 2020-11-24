#Python script to launch anyother program
import os
import subprocess

program=input("Enter path of your program: ")

try:
	subprocess.Popen(program)
except:
	print("Error opening program!")
