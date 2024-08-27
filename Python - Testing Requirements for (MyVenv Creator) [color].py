# Author         : Alexandre JALLET
# DATE           : 2023/11/03
# VERSION        : 0.1
# Licence        : OPEN

import os
import sys
import importlib
import subprocess
import urllib.request


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

dirStart = os.getcwd()

# Test if it's Windows
try:
    if sys.platform == "win32":
        print(PrintStyle.reverse(f"\nThis script is currently powered by Python {sys.version} on Windows {os.name}." ))
    else:
        raise Exception

except:
    print(PrintStyle.color("Error : This script was designed for Windows", PrintStyle.RED))
    exit()




# Test : Docker Installation
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
print(PrintStyle.bold(
    PrintStyle.color("\n\n[ TEST : ", PrintStyle.YELLOW
                     ) + PrintStyle.color("IF DOCKER WAS INSTALLED", PrintStyle.WHITE
                                          )) + PrintStyle.bold(PrintStyle.color(" ]", PrintStyle.YELLOW)))

# Check if was installed
try:
    # Get and Print Docker version installed on the device	
    dockerVersion = subprocess.check_output(["docker", "--version"]).decode("utf-8")
    print(PrintStyle.bold(PrintStyle.color( "The current version of Docker :", PrintStyle.CYAN)))
    print(dockerVersion)
    print(PrintStyle.bold(PrintStyle.color( "Docker was already Installed !" , PrintStyle.GREEN)))

except:
    print(PrintStyle.color( "Error : Docker is not installed on this device." , PrintStyle.RED))
    print(PrintStyle.color( "Info  : Docker is only necessary if you want to containerize your development.", PrintStyle.WHITE))
    print(PrintStyle.color( "Install Docker application and restart this script. (optional)" , PrintStyle.YELLOW))



# Test : Git installation and GIT setup
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
print(PrintStyle.bold(
    PrintStyle.color("\n\n[ TEST : ", PrintStyle.YELLOW
                     ) + PrintStyle.color("IF GIT WAS INSTALLED", PrintStyle.WHITE
                                          )) + PrintStyle.bold(PrintStyle.color(" ]", PrintStyle.YELLOW)))


# Check if was installed
try:
    # Get and Print Git version installed on the device
    gitVersion = subprocess.check_output(["git", "--version"]).decode("utf-8")
    print(PrintStyle.bold(PrintStyle.color( "The current version of Git :", PrintStyle.CYAN)))
    print(gitVersion)
    print(PrintStyle.bold(PrintStyle.color( "Git was already installed !" , PrintStyle.GREEN)))
    
    print(PrintStyle.bold(PrintStyle.color( "\nGIT setup user info :", PrintStyle.CYAN)))

    # Check if GIT was Setup
    try:
        # Get and print GIT setup User info
        name = subprocess.check_output(['git', 'config', 'user.name']).decode().strip()
        email = subprocess.check_output(['git', 'config', 'user.email']).decode().strip()
        print(f"User name: {name}")
        print(f"Email: {email}")
        
        print(PrintStyle.bold(PrintStyle.color( "\nGit was already setup !" , PrintStyle.GREEN)))
    except subprocess.CalledProcessError:
        print(PrintStyle.color("Git is not set up with a name and email." , PrintStyle.RED))

        # Start GIT Setup
        if not check_git_config():
            subprocess.call(['git', 'config', '--global', 'user.name', 'Your Name'])
            subprocess.call(['git', 'config', '--global', 'user.email', 'your_email@example.com'])

except:
    print(PrintStyle.color( "Error : Git is not installed on this device." , PrintStyle.RED))
    print(PrintStyle.color( "Install Git application and restart this script." , PrintStyle.RED))





# List all python version installed on the device and their PATH
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
print(PrintStyle.bold(
    PrintStyle.color("\n\n[ TEST : ", PrintStyle.YELLOW
                     ) + PrintStyle.color("LIST PYTHON VERSION INSTALLED ON THE DEVICE", PrintStyle.WHITE
                                          )) + PrintStyle.bold(PrintStyle.color(" ]", PrintStyle.YELLOW)))

try:
    # Print the active python --versions
    pyVersion = subprocess.check_output(["python", "--version"]).decode("utf-8")
    print(PrintStyle.bold(PrintStyle.color( "The current version of Python already actived :", PrintStyle.CYAN)))
    print(pyVersion)

    print(PrintStyle.bold(PrintStyle.color( "Other versions of python already installed :", PrintStyle.CYAN)))
    
    # Execute the command and capture the output
    output = subprocess.check_output(['py', '-0p'], universal_newlines=True)

    # Split the output into lines
    lines = output.strip().split('\n')

    # Create a list of tuples containing the version and path of each Python installation
    versions = [(line.split()[0], line.split()[1]) for line in lines]

    # Print the list of versions as a table
    print('| Version | Path \n|---------|--------------------------------------')
    for version in versions:
            print(f'| {version[0]} | {version[1]}')

    print(PrintStyle.bold(PrintStyle.color( "\nPython was already Installed !", PrintStyle.GREEN)))

except:
    print(PrintStyle.color( "Error : Python is not installed on this device.", PrintStyle.RED))
    print(PrintStyle.color( "Install Python and restart this script.", PrintStyle.RED))






# Test : Python installer Package (pip) installation
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
print(PrintStyle.bold(
    PrintStyle.color("\n\n[ TEST : ", PrintStyle.YELLOW
                     ) + PrintStyle.color("IF PYTHON INSTALLER PACKAGE (PIP) WAS INSTALLED", PrintStyle.WHITE
                                          )) + PrintStyle.bold(PrintStyle.color(" ]", PrintStyle.YELLOW)))


# Trying to install the upgrade of Python Installer Package (PIP)
print(PrintStyle.bold(PrintStyle.color( "Trying to install the latest update of PIP :", PrintStyle.CYAN)))
try:
    subprocess.run(['python', '-m', 'pip', 'install', '--upgrade', 'pip', '--user'])
    
except:
    print(PrintStyle.color( "Error : PIP was not setup on this device." , PrintStyle.RED))
    print(PrintStyle.color( "Try to install it manualy" , PrintStyle.RED))

try:
    # Get and print the Python installer Package (pip) version installed on the device
    pipVersion = subprocess.check_output(["pip", "--version"]).decode("utf-8")
    print(PrintStyle.bold(PrintStyle.color( "\nThe current version of PIP :", PrintStyle.CYAN)))
    print(pipVersion)
    print(PrintStyle.bold(PrintStyle.color( "Python installer Package (pip) was already Installed !", PrintStyle.GREEN)))

except:
    print(PrintStyle.color( "Error : Python installer Package (pip) is not installed on this device.", PrintStyle.RED))
    print(PrintStyle.color( "Install Python installer Package (pip) and restart this script.", PrintStyle.RED))
	

 






# Test : PYPI setup
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
print(PrintStyle.bold(
    PrintStyle.color("\n\n[ TEST : ", PrintStyle.YELLOW
                     ) + PrintStyle.color("IF PYPI REPOSITORY IS AVAILABLE", PrintStyle.WHITE
                                          )) + PrintStyle.bold(PrintStyle.color(" ]", PrintStyle.YELLOW)))


# Testing internet connexion to access on PYPI platform
try:
    urllib.request.urlopen('https://pypi.org/', timeout=20)
    print(PrintStyle.bold(PrintStyle.color( "The Network connexion to the PYPI platform is currently  vailable !\n", PrintStyle.GREEN)))
except urllib.request.URLError:
    print(PrintStyle.color( "Error : PYPI network connexion unvailable !" , PrintStyle.RED))
    print(PrintStyle.color( "* Check your network connextion." , PrintStyle.YELLOW))
    print(PrintStyle.color( "* Check the state of your VPN.\n" , PrintStyle.YELLOW))
    print(PrintStyle.color( "* Check the state of your FireWall.\n" , PrintStyle.YELLOW))





# Test : Access and read the 'requirements.txt' file
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
print(PrintStyle.bold(
    PrintStyle.color("\n\n[ TEST : ", PrintStyle.YELLOW
                     ) + PrintStyle.color("IF 'requirements.txt' CAN BE FOUND AND READABLE", PrintStyle.WHITE
                                          )) + PrintStyle.bold(PrintStyle.color(" ]", PrintStyle.YELLOW)))

try:
    # Try to open 'requirements.txt' to check access
    repoSources = os.path.join(os.getcwd(), "@LocalRepository")
    os.chdir(repoSources) 
    file = open("requirements.txt", "r")
    print(PrintStyle.bold(PrintStyle.color( "'requirements.txt' was found !\n", PrintStyle.GREEN)))

    # Read and print the content of 'requirements.txt
    print(PrintStyle.bold(PrintStyle.color( "List of python packages required for your project :", PrintStyle.CYAN)))
    print(file.read())
    file.close()
    print(PrintStyle.bold(PrintStyle.color( "\n'requirements.txt' can be read !", PrintStyle.GREEN)))

except:
    print(PrintStyle.color( "Error : File 'requirements.txt' was not found in the root of the @LocalRepository directory.", PrintStyle.RED))
    print(PrintStyle.color( "Place the 'requirements.txt' file in the @LocalRepository directory.", PrintStyle.RED))




# TEST : IF THE 'inquirer' PACKAGE WAS INSTALLED (needed for the VenvCreator Form)
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
print(PrintStyle.bold(
    PrintStyle.color("\n\n[ TEST : ", PrintStyle.YELLOW
                     ) + PrintStyle.color("IF THE 'inquirer' PACKAGE WAS INSTALLED", PrintStyle.WHITE
                                          )) + PrintStyle.bold(PrintStyle.color(" ]", PrintStyle.YELLOW)))


try:
    importlib.import_module('inquirer')
    print(PrintStyle.bold(PrintStyle.color( "\n'inquirer' package is already installed !\n", PrintStyle.GREEN)))
except ImportError:
    print(PrintStyle.color( "\nError : 'inquirer' is not installed.", PrintStyle.RED))
    print(PrintStyle.color( "Error : Installing now...", PrintStyle.CYAN))
    print('inquirer is not installed. Installing now...')
    package_name = "inquirer"
    subprocess.run(["pip3", "install", package_name, "--user"])




input("\n\nPress enter to exit")
exit()
	
	
	
