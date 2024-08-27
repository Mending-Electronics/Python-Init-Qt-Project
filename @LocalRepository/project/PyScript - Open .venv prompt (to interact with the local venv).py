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
system("title " + "Terminal of the .venv")




print(PrintStyle.bold(
    PrintStyle.color("\n [ VIRTUAL ENVIRONMENT : ", PrintStyle.YELLOW
                     ) + PrintStyle.color("You are currently in the activated Virtual Environment", PrintStyle.WHITE
                                          )) + PrintStyle.bold(PrintStyle.color(" ]", PrintStyle.YELLOW)))


print(PrintStyle.bold(PrintStyle.color("""
 If you need to check the python version used in your venv
 Use the commande bellow :
""", PrintStyle.WHITE)))

print(PrintStyle.bold(PrintStyle.color("    python --version", PrintStyle.CYAN)))



print(PrintStyle.bold(PrintStyle.color("""
 If you need to embeded other specifics packages in your venv
 Install it with the commande bellow :
""", PrintStyle.WHITE)))

print(PrintStyle.bold(PrintStyle.color("    pip install 'name of the package'", PrintStyle.CYAN)))



print(PrintStyle.bold(PrintStyle.color("""
 If you need to upgrading pip in your venv
 Use the commande bellow :
""", PrintStyle.WHITE)))

print(PrintStyle.bold(PrintStyle.color("    python.exe -m pip install --upgrade pip", PrintStyle.CYAN)))



print(PrintStyle.bold(PrintStyle.color("""
 If you need to check all packages was installed in your venv
 Use the commande bellow :
""", PrintStyle.WHITE)))

print(PrintStyle.bold(PrintStyle.color("    pip list", PrintStyle.CYAN)))

print(PrintStyle.bold(PrintStyle.color("""
 If you need information about an installed package in your venv
 Use the commande bellow : """, PrintStyle.WHITE)))

print(PrintStyle.color(" *only work if the package was installed in the venv", PrintStyle.YELLOW))

print(PrintStyle.bold(PrintStyle.color("\n    pip show 'name of the package'", PrintStyle.CYAN)))

print('\n')


subprocess.call([
    '.venv\\Scripts\\activate.bat',
    '&&',
    'cmd /k'
    ])
