# Author         : Alexandre JALLET
# DATE           : 2023/11/03
# VERSION        : 0.1
# Licence        : OPEN

import os
import sys
import shutil
import inquirer
import subprocess

from inquirer.themes import GreenPassion


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



# Execute the command and capture the output
output = subprocess.check_output(['py', '-0p'], universal_newlines=True)

# Split the output into lines
lines = output.strip().split('\n')

# Create a list of tuples containing the version and path of each Python installation
versions = [(line.split()[0], line.split()[1]) for line in lines]

# Extract the version numbers from the list of tuples
version_numbers = [version[0] for version in versions]


q = [
    inquirer.Text("name", message="What's your project name?", default=""),
    inquirer.List("docker", message="Do you want to create a Docker?", choices=["yes", "no"], default="no"),
    inquirer.List("git", message="Do you want to create a Git Repository?", choices=["yes", "no"], default="yes"),
    inquirer.List("pythonVersion",message="Choose the Python version for your virtual environment", choices=version_numbers)
]

answers = inquirer.prompt(q, theme=GreenPassion())

name = answers["name"]
docker = answers["docker"]
git = answers["git"]
pythonVersion = answers["pythonVersion"]

#Replace the spaces by a "_"
name = name.replace(" ", "_")

# Assume pythonVersion is a string that contains "-64" or "-32"
# For example, pythonVersion = "3.9.7-64"

# Replace "-64" by "" using the replace method
pythonVersion = pythonVersion.replace("-64", "")

# Alternatively, replace "-32" by "" using the replace method
pythonVersion = pythonVersion.replace("-32", "")



# Get the current dir into a variable
dirStart = os.getcwd()


# Create a Project folder
os.mkdir(name)

# Get the current dir of the project folder into a variable
dirProject = os.path.join(dirStart, name)

# Go to the project folder
os.chdir(dirProject)

# Create a folder for downloadable hors-line package
#if venv need to be redeploye on a hors-line device
os.mkdir("packages")

# Get the current dir of the Packages folder into a variable
pkgsDir = os.path.join(dirProject, "packages")
# Go to the Packages folder
os.chdir(pkgsDir)


# Create a folder for embeded an uncompiled version of Python Installer Package (PIP) 
#if venv need to be redeploye on a hors-line device
os.mkdir("pip")

# Go to the project folder
os.chdir(dirProject)





# Needed Directories

# Repository Directory
repoSources = os.path.join(dirStart, "@LocalRepository")
venvSources = os.path.join(dirStart, "@LocalRepository\.venv", )
projectSources = os.path.join(dirStart, "@LocalRepository\project", )

# Project Directory
venvDestination = os.path.join(dirProject, ".venv", )




# CREATION : VIRTUAL ENVIRONMENT
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
print(PrintStyle.bold(
    PrintStyle.color("\n\n[ CREATION : ", PrintStyle.YELLOW
                     ) + PrintStyle.color("VIRTUAL ENVIRONMENT", PrintStyle.WHITE
                                          )) + PrintStyle.bold(PrintStyle.color(" ]", PrintStyle.YELLOW)))

print(PrintStyle.bold(PrintStyle.color(f"Creating a new Python {pythonVersion} virtual environment...", PrintStyle.WHITE)))
print(PrintStyle.bold(PrintStyle.color(f"Wait few secondes", PrintStyle.CYAN)))

command = f"py {pythonVersion} -m venv .venv"
subprocess.run(command, shell=True)

print(PrintStyle.bold(PrintStyle.color(f"\nPython {pythonVersion} virtual environment was successfully created !" , PrintStyle.GREEN)))




# COPY : EMBEDED 'requirements.txt' FILE IN THE PROJECT
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
print(PrintStyle.bold(
    PrintStyle.color("\n\n[ COPY : ", PrintStyle.YELLOW
                     ) + PrintStyle.color("EMBEDED 'requirements.txt' FILE IN THE PROJECT", PrintStyle.WHITE
                                          )) + PrintStyle.bold(PrintStyle.color(" ]", PrintStyle.YELLOW)))

# Copy the file "requirements.txt" from dirStart to dirProject

try:
    print(PrintStyle.bold(PrintStyle.color(f"Copy the file 'requirements.txt' in the project folder ...", PrintStyle.WHITE)))
    shutil.copy(os.path.join(repoSources, "requirements.txt"), dirProject)
    print(PrintStyle.bold(PrintStyle.color("\nFile 'requirements.txt' copied !" , PrintStyle.GREEN)))
except:
    print(PrintStyle.color("Error : File 'requirements.txt' not found.", PrintStyle.RED))




# ACTIVATE AND PREPARE : VIRTUAL ENVIRONMENT
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
print(PrintStyle.bold(
    PrintStyle.color("\n\n[ ACTIVATION : ", PrintStyle.YELLOW
                     ) + PrintStyle.color("VIRTUAL ENVIRONMENT", PrintStyle.WHITE
                                          )) + PrintStyle.bold(PrintStyle.color(" ]", PrintStyle.YELLOW)))



# Activating the virtual environment
print(PrintStyle.bold(PrintStyle.color("Activating the virtual environment...", PrintStyle.WHITE)))
subprocess.call(['.venv\\Scripts\\activate.bat'], shell=True)
print(PrintStyle.bold(PrintStyle.color("\nThe virtual environment is currently activate !" , PrintStyle.GREEN)))



#INSTALL : INSTALLATION OF THE LATEST VERSION OF PYTHON INSTALLER PACKAGE (PIP)
#==============================================================================
print(PrintStyle.bold(
    PrintStyle.color("\n\n[ INSTALL : ", PrintStyle.YELLOW
                     ) + PrintStyle.color("INSTALLATION OF THE LATEST VERSION OF PYTHON INSTALLER PACKAGE (PIP)", PrintStyle.WHITE
                                          )) + PrintStyle.bold(PrintStyle.color(" ]", PrintStyle.YELLOW)))


# Upgrading pip
print(PrintStyle.bold(PrintStyle.color("Upgrading Python Installer Package (pip)...", PrintStyle.WHITE)))

try:
    subprocess.call(['.venv\\Scripts\\activate.bat', '&&', 'python.exe', '-m', 'pip', 'install', '--upgrade', 'pip'])
    print(PrintStyle.bold(PrintStyle.color("\nPython Installer Package (pip) successfully installed !" , PrintStyle.GREEN)))
except:
    print(PrintStyle.color("Error : pip can't be installed.", PrintStyle.RED))








#INSTALL : INSTALLATION OF ALL REQUIRED PACKAGES FROM 'requirements.txt'
#=======================================================================
print(PrintStyle.bold(
    PrintStyle.color("\n\n[ INSTALL : ", PrintStyle.YELLOW
                     ) + PrintStyle.color("INSTALLATION OF ALL REQUIRED PACKAGES FROM 'requirements.txt'", PrintStyle.WHITE
                                          )) + PrintStyle.bold(PrintStyle.color(" ]", PrintStyle.YELLOW)))


# Installing the packages in 'requirements.txt'
print(PrintStyle.bold(PrintStyle.color("Installing the packages from 'requirements.txt' list...", PrintStyle.WHITE)))

try:
    subprocess.call(['.venv\\Scripts\\activate.bat', '&&', 'pip', 'install', '-r', 'requirements.txt'])
    print(PrintStyle.bold(PrintStyle.color("\nAll listed packages was successfully installed !" , PrintStyle.GREEN)))
except:
    print(PrintStyle.color("Error : packages can't be installed.", PrintStyle.RED))






#INSTALL : INSTALLATION OF THE DJANGO 'App'
#==========================================
print(PrintStyle.bold(
    PrintStyle.color("\n\n[ INSTALL : ", PrintStyle.YELLOW
                     ) + PrintStyle.color("INSTALLATION OF THE DJANGO 'App'", PrintStyle.WHITE
                                          )) + PrintStyle.bold(PrintStyle.color(" ]", PrintStyle.YELLOW)))

# Creating Django 'App'
print(PrintStyle.bold(PrintStyle.color("Creating the Django 'App'...", PrintStyle.WHITE)))

try:
    os.chdir(venvDestination)  
    subprocess.call(['Scripts\\activate.bat', '&&', 'cd', '.\\', '&&', 'django-admin', 'startproject', 'App', '.'])
    print(PrintStyle.bold(PrintStyle.color("\nDjango 'App' successfully created !" , PrintStyle.GREEN)))
except:
    print(PrintStyle.color("Error : Django 'App' can not be created.", PrintStyle.RED))





#SETUP : CONFIGUARTION OF THE DJANGO 'App'
#=========================================
print(PrintStyle.bold(
    PrintStyle.color("\n\n[ SETUP : ", PrintStyle.YELLOW
                     ) + PrintStyle.color("CONFIGUARTION OF THE DJANGO 'App'", PrintStyle.WHITE
                                          )) + PrintStyle.bold(PrintStyle.color(" ]", PrintStyle.YELLOW)))

os.chdir(venvDestination+ '\\App')

# Editing the Django 'App' settings.py file
try:
    with open('settings.py', 'r') as file:
        filedata = file.read()

    # Patch "import os"
    print(PrintStyle.bold(PrintStyle.color("Editing the Django 'App' settings.py file...", PrintStyle.WHITE)))
    filedata = filedata.replace('from pathlib import Path', """
import os
from pathlib import Path
    """)
    
    print(PrintStyle.bold(PrintStyle.color("\n'import os' package added !" , PrintStyle.GREEN)))


    # Patch Templates DIR
    filedata = filedata.replace("'DIRS': [],", "'DIRS': [os.path.join(BASE_DIR, 'templates')],")

    print(PrintStyle.bold(PrintStyle.color("\n'Templates' directory declaration added !" , PrintStyle.GREEN)))

    # Patch Statics files DIR
    filedata = filedata.replace("STATIC_URL = 'static/'", """
STATIC_URL = 'static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
    """)

    print(PrintStyle.bold(PrintStyle.color("\n'Static' directory declaration added !" , PrintStyle.GREEN)))

    with open('settings.py', 'w') as file:
        file.write(filedata)
except:
    print(PrintStyle.color("Error : Can not access to the Django 'App' settings.py file.", PrintStyle.RED))








# Editing the Django 'App' urls.py file
try:
    with open('urls.py', 'r') as file:
        filedata = file.read()

    # Patch "import os"
    print(PrintStyle.bold(PrintStyle.color("\nEditing the Django 'App' urls.py file...", PrintStyle.WHITE)))
    filedata = filedata.replace('from django.urls import path', """
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home'),

]
    """)
    
    print(PrintStyle.bold(PrintStyle.color("\n'Templates\index.html' successfully assigned as a Home page !" , PrintStyle.GREEN)))


    with open('urls.py', 'w') as file:
        file.write(filedata)
except:
    print(PrintStyle.color("Error : Can not access to the Django 'App' urls.py file.", PrintStyle.RED))








# ADD : EMBEDED USEFULL SCRIPTS IN THE PROJECT
# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
print(PrintStyle.bold(
    PrintStyle.color("\n\n[ COPY : ", PrintStyle.YELLOW
                     ) + PrintStyle.color("EMBEDED USEFULL SCRIPTS IN THE PROJECT", PrintStyle.WHITE
                                          )) + PrintStyle.bold(PrintStyle.color(" ]", PrintStyle.YELLOW)))


# Copy all folders and files from "projectSources" to the "dirProject" directory
print(PrintStyle.bold(PrintStyle.color("Copy project elements :  ", PrintStyle.WHITE)))
print(PrintStyle.bold(PrintStyle.color("    * Source : '@LocalRepository\project'", PrintStyle.CYAN)))
print(PrintStyle.bold(PrintStyle.color(f"    * Destination : '{name}'", PrintStyle.CYAN)))

try:
    shutil.copytree(projectSources, dirProject, dirs_exist_ok=True)
    print(PrintStyle.bold(PrintStyle.color("\nFolder 'project' successfully copied !" , PrintStyle.GREEN)))
except:
    print(PrintStyle.color("Error : project folder can not be copied !", PrintStyle.RED))


# Copy all folders and files of "venvSources" to the "venvDestination" directory
print(PrintStyle.bold(PrintStyle.color("\nCopy .venv elements :", PrintStyle.WHITE)))
print(PrintStyle.bold(PrintStyle.color("    * Source : '@LocalRepository\.venv'", PrintStyle.CYAN)))
print(PrintStyle.bold(PrintStyle.color(f"    * Destination : '{name}\.venv'", PrintStyle.CYAN)))

try:
    shutil.copytree(venvSources, venvDestination, dirs_exist_ok=True)
    print(PrintStyle.bold(PrintStyle.color("\nFolder '.venv' successfully copied !" , PrintStyle.GREEN)))    
except:
    print(PrintStyle.color("Error : .venv folder can not be copied !", PrintStyle.RED))




#print('''
#************************************************************
#You are currently in the activated Virtual Environment
#************************************************************
#''')

#print('If you need to embed other specific packages in your venv, install them with the command below:')
#print('pip install \'name of the package\'')




os.startfile(venvDestination)


input("\n\nPress enter to exit")
exit()
	
	
	

