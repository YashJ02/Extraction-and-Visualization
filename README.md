# Extraction-and-Visualization
This Project is about Scraping Tables From Wikipedia and Visualizing Data In Different Graphs and Charts.

## Instruction guide for running the project.
This is an open software project that can be installed and activated in any operating system and any particular machine having python installed.

### Setting up the Project
Before starting the Project create a virtual environment to store all the dependencies
- Open the terminal/cmd and navigate to the project folder.

- Install the VirtualEnv
```
pip3 install virtualenv
```
```
virtualenv venv
```
- Activate The virtual Environment
```
venv/Scripts/activate
```
- Now a ```(venv)``` is seen in the cmd path!

- Install the requirments.txt using
```
pip3 install -r requirements.txt
```
-Once all the above libraries are installed, your project is ready to be executed.

### Usage

- Go to the python terminal, and run the command
```
Python3 manage.py runserver.
```
- :+1: Congrats! The app should now be running

### Execution:

- Step 1 : After this a web page will be loaded for execution of the framework.
- Step 2 : Now the user will enter the keyword which he wants to study on wikipedia *(the keyword is case-sensitive)*, in the search box provided. The data will be scraped.
- Step 3 : Now the CSV file is Downloaded in the local storage. Given an option to load the stored CSV for analysis.
- Step 4 : Finally, user can select any plot among the options given, which will be suitable for the visualization process of his/her dataset.


