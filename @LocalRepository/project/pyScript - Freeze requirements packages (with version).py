# Author         : Alexandre JALLET
# DATE           : 2023/12/28
# VERSION        : 0.1
# Licence        : OPEN

import os
import sys
import shutil
import subprocess


from datetime import datetime

# Get the current date and time
now = datetime.now()

# Format the date and time
date = now.strftime("%Y_%m_%d_%H_%M_%S_")


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
system("title " + "Script - Freeze requirements packages (with version)")


dirProject = os.getcwd()
dirPkgs = os.path.join(dirProject, 'packages')


print(PrintStyle.bold(
    PrintStyle.color("\n [ VIRTUAL ENVIRONMENT : ", PrintStyle.YELLOW
                     ) + PrintStyle.color("You are currently in the activated Virtual Environment", PrintStyle.WHITE
                                          )) + PrintStyle.bold(PrintStyle.color(" ]", PrintStyle.YELLOW)))


print(PrintStyle.bold(PrintStyle.color("""
 Freeze the all aditional packages installed in your virtual environmemt :
""", PrintStyle.WHITE)))


subprocess.call([
    '.venv\\Scripts\\activate.bat',
    '&&',
    'pip', 'freeze',
    '&&',
    'pip', 'freeze', '>', os.path.join(dirPkgs, f'{date}requirements.txt'),
    '&&',
    'pip', 'freeze', '>', os.path.join(dirPkgs, 'requirements.txt')
    ])

print(PrintStyle.bold(PrintStyle.color("""
 The frozen file 'requirements.txt' has been added or updated to the 'packages' folder
""", PrintStyle.GREEN)))

input("Press Enter to continue...")
