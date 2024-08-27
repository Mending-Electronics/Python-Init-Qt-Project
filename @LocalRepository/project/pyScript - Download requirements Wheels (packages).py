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
system("title " + "Script - Download requirements Wheels (packages)")


dirProject = os.getcwd()
dirPkgs = os.path.join(dirProject, 'packages')


print(PrintStyle.bold(
    PrintStyle.color("\n [ VIRTUAL ENVIRONMENT : ", PrintStyle.YELLOW
                     ) + PrintStyle.color("You are currently in the activated Virtual Environment", PrintStyle.WHITE
                                          )) + PrintStyle.bold(PrintStyle.color(" ]", PrintStyle.YELLOW)))


# Ask the user if they want to freeze the current installed packages
user_input = input("\n Do you want to freeze the current installed packages in your virtual environment before downloading? (yes/no): \n")

# Check the user's response
if user_input.lower() == 'yes':
    # Run the 'pyScript - Freeze requirements packages (with version).py' script
    subprocess.call(['python', 'pyScript - Freeze requirements packages (with version).py'])
else:
    pass


print(PrintStyle.bold(PrintStyle.color("""
 Downloading all requirements Wheels...
""", PrintStyle.WHITE)))

subprocess.call([
    '.venv\\Scripts\\activate.bat',
    '&&',
    'cd', os.path.join(dirPkgs),
    '&&',
    'pip', 'download', '-r', 'requirements.txt',
    ])

print(PrintStyle.bold(PrintStyle.color("""
 The Wheels files of all your additional packages has been downloaded to the 'packages' folder
""", PrintStyle.GREEN)))

input("Press Enter to continue...")
