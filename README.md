# Verloop-GoodReads

## Pre-Requisites
* Install Git (https://git-scm.com/download/win).
* After Installing git. Run the below command to initialize 
git on the directory you want to have your project.
```
C:\some_directory> git init
C:\some_directory> git config --global user.name Username of your git account
C:\some_directory> git config --global user.email Email of your git account
```
* Clone into the project.
```
C:\some_directory>git clone https://github.com/AkshayArni003/verloop-goodreads.git
C:\some_directory>cd verloop-goodreads
```
* First step after cloning is to install all the dependencies for the project to run
successfully.
* Install python if not there (https://www.python.org/downloads/windows/).
* Dependencies are requests and xmltodict. Follow below commands to install them.
```
C:\some_directory\verloop-goodreads> pip install requests
```
* After requests is installed successfully. Run below command
```
C:\some_directory\verloop-goodreads> pip install xmltodict
``` 
* We are set to run the python Script now. In the command prompt run
the below command.
```
C:\some_directory\verloop-goodreads>python request.py <GoodReads URL with string quotes>
example:
C:\some_directory\verloop-goodreads>python request.py https://www.goodreads.com/book/show/12067
```
* To run the Unit test. follow the below command.
```
C:\some_directory\verloop-goodreads>python -m unittest tests.py -v
```