# Author         : Alexandre JALLET
# DATE           : 2023/12/28
# VERSION        : 0.1
# Licence        : OPEN

import os
import sys
import shutil
import subprocess

#Creation of print style class
class PrintStyle:
    RESET = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    REVERSE = '\033[7m'

    BLACK = '\033[30m'
    GREEN = '\033[32m'
    RED = '\033[31m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    PURPLE = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'

    @staticmethod
    def color(text, color):
        return f'{color}{text}{PrintStyle.RESET}'
    
    @staticmethod
    def bold(text):
        return f'{PrintStyle.BOLD}{text}{PrintStyle.RESET}'

    @staticmethod
    def underline(text):
        return f'{PrintStyle.UNDERLINE}{text}{PrintStyle.RESET}'

    @staticmethod
    def reverse(text):
        return f'{PrintStyle.REVERSE}{text}{PrintStyle.RESET}'

os.system('color')


from os import system
system("title " + "Script - Re-Install project from downloaded Wheels (to recreate the venv on an other computer)")


dirProject = os.getcwd()
dirPkgs = os.path.join(dirProject, 'packages')
dirPip = os.path.join(dirPkgs, 'pip')


print(PrintStyle.bold(
    PrintStyle.color("\n [ VIRTUAL ENVIRONMENT : ", PrintStyle.YELLOW
                     ) + PrintStyle.color("You are currently in the activated Virtual Environment", PrintStyle.WHITE
                                          )) + PrintStyle.bold(PrintStyle.color(" ]", PrintStyle.YELLOW)))

print(PrintStyle.bold(PrintStyle.color("""
Check if Python Installer Packages was already installed...
""", PrintStyle.WHITE)))

try:
    # Get and print the Python installer Package (pip) version installed on the device
    pipVersion = subprocess.check_output(["pip", "--version"]).decode("utf-8")
    print(PrintStyle.bold(PrintStyle.color( "\nThe current version of PIP :", PrintStyle.CYAN)))
    print(pipVersion)
    print(PrintStyle.bold(PrintStyle.color( "Python installer Package (pip) was already Installed !", PrintStyle.GREEN)))

except:
    print(PrintStyle.color( "Error : Python installer Package (pip) is not installed on this device.", PrintStyle.RED))

    print(PrintStyle.bold(PrintStyle.color("""
    Installing Python Installer Packages...
    """, PrintStyle.WHITE)))

    try:
        print((PrintStyle.color("Try online installation...", PrintStyle.CYAN)))
        subprocess.call([
            '.venv\\Scripts\\activate.bat',
            '&&',
            'python.exe', '-m', 'pip', 'install', '--upgrade', 'pip'
            ])
            
    except:
        print((PrintStyle.color("Try offline installation if the uncompiled version of pip was embeded in the project in the 'packages' folder...", PrintStyle.CYAN)))

        file_path = "packages\\pip\\setup.py"

        if os.path.isfile(file_path):
            print(f"The file '{file_path}' exists.")

            subprocess.call([
                '.venv\\Scripts\\activate.bat',
                '&&',
                'cd', os.path.join(dirPip),
                '&&',
                'python', 'setup.py', 'install',
                ])
        else:
            print(f"The file '{file_path}' does not exist.")
        

  
print(PrintStyle.bold(PrintStyle.color("""
Installing requirements Wheels from 'packages' folder...
""", PrintStyle.WHITE)))

subprocess.call([
    '.venv\\Scripts\\activate.bat',
    '&&',
    'cd', os.path.join(dirPkgs),
    '&&',
    'pip', 'install', '--no-index', '--find-links', '.', '-r', 'requirements.txt'
    ])

print(PrintStyle.bold(PrintStyle.color("\nPackages installation done !", PrintStyle.GREEN)))

input("\nPress Enter to continue...")
