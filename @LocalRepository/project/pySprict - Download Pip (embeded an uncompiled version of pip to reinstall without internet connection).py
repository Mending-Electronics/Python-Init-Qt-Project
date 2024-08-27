# Author         : Alexandre JALLET
# DATE           : 2023/12/28
# VERSION        : 0.1
# Licence        : OPEN


import importlib
import subprocess
import os
import shutil
import tarfile

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
system("title " + "Script -  Download Pip (embeded an uncompiled version of pip to reinstall without internet connection)")


# TEST : IF THE 'requests' PACKAGE WAS INSTALLED (needed for the VenvCreator Form)
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
print(PrintStyle.bold(
    PrintStyle.color("\n[ TEST : ", PrintStyle.YELLOW
                     ) + PrintStyle.color("IF THE 'requests' PACKAGE WAS INSTALLED", PrintStyle.WHITE
                                          )) + PrintStyle.bold(PrintStyle.color(" ]", PrintStyle.YELLOW)))

try:
    importlib.import_module('requests')
    print(PrintStyle.bold(PrintStyle.color( "\n'requests' package is already installed !\n", PrintStyle.GREEN)))
except ImportError:
    print(PrintStyle.color( "\nError : 'requests' is not installed.", PrintStyle.RED))
    print(PrintStyle.color( "Installing now...", PrintStyle.CYAN))
    package_name = "requests"
    subprocess.run(["pip", "install", package_name])



import requests



# Download the uncompiled version of PIP in .tar.gz from PYPI
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
print(PrintStyle.bold(
    PrintStyle.color("\n[ DOWNLOAD : ", PrintStyle.YELLOW
                     ) + PrintStyle.color("THE UNCOMPILED VERSION OF PIP IN .TAR.GZ FROM THE PYPI REPOSITORY PLATFORM ", PrintStyle.WHITE
                                          )) + PrintStyle.bold(PrintStyle.color(" ]", PrintStyle.YELLOW)))
print(PrintStyle.bold(PrintStyle.color("""
This script is only useful for reinstalling your virtual environment on another computer without an Internet connection.
You need to download and embeded the uncompiled version of pip.""" , PrintStyle.YELLOW)))




print("\nPlease choose an option:")
print(" 1. Enter your pip version URL ")
print(PrintStyle.color("  * Go to : https://pypi.org/project/pip/#history" , PrintStyle.YELLOW))
print(PrintStyle.color("  * Select the version of pip you need" , PrintStyle.YELLOW))
print(PrintStyle.color("  * In the download menu, juste right-click on the pip.tar.gz link and copy the link\n" , PrintStyle.YELLOW))
print(" 2. As default : Continue with the 23.3.2 pip version ")
print(" 3. Exit the script")

choice = input()

if choice == '1':
    url = input("Please enter the URL: ")

    while True:
        if url == '':
            print("You didn't entered the URL: ")
        else:
            print("You entered the URL: ", url)


elif choice == '2':
    # URL of the file to download
    url = 'https://files.pythonhosted.org/packages/b7/06/6b1ad0ae8f97d7a0d6f6ad640db10780578999e647a9593512ceb6f06469/pip-23.3.2.tar.gz'

elif choice == '3':
    print("Exiting the script.")


else:
    print("Invalid choice. Please choose either 1, 2 or 3.")


# Create a 'packages' directory in the current directory if it doesn't exist
packages_dir = os.path.join(os.getcwd(), 'packages')
os.makedirs(packages_dir, exist_ok=True)


print(PrintStyle.bold(PrintStyle.color( "\nDownload the *.tar.gz file into the 'packages' directory", PrintStyle.CYAN)))
# Download the file into the 'packages' directory
response = requests.get(url, stream=True)
file_name = os.path.join(packages_dir, url.split("/")[-1])
with open(file_name, 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
del response

print(PrintStyle.bold(PrintStyle.color( "\nExtract the .tar.gz file to the 'packages' directory", PrintStyle.CYAN)))
# Extract the .tar.gz file to the 'packages' directory
with tarfile.open(file_name, 'r:gz') as tar_ref:
    tar_ref.extractall(path=packages_dir)

# If a 'pip' directory already exists in the 'packages' directory, delete it
pip_dir = os.path.join(packages_dir, 'pip')
if os.path.exists(pip_dir):
    shutil.rmtree(pip_dir)

print(PrintStyle.bold(PrintStyle.color( "\nRename the extracted folder to 'pip' within the 'packages' directory", PrintStyle.CYAN)))
# Rename the folder that begins with 'pip' to 'pip' within the 'packages' directory
for name in os.listdir(packages_dir):
    if name.startswith('pip') and os.path.isdir(os.path.join(packages_dir, name)):
        os.rename(os.path.join(packages_dir, name), pip_dir)


print(PrintStyle.bold(PrintStyle.color( "\nPIP is already embeded !\n", PrintStyle.GREEN)))

input("Press Enter to continue...")
