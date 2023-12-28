# DJANGO PRACTICE
This is a project used to learn, practice and apply missing skills about django.

## Required
- To run the project, you need to install python version 3.11 or higher and install the environments to use python.
- Install virtual environment

## How to use
### For Linux or MacOS operating systems, replace py with python
1. First, clone this repository on your computer
> git clone https://github.com/hothanhtuan1209/django.git

2. Next, move into the directory containing this file:
> cd django
> cd practice
> cd django_practice

3. Checkout to branch develop
> git checkout develop

4. You should create virtual environment and install pyenv
- Create virtual environment named 'venv'
> python -m venv venv

- Run virtual environment for Windows
> .\venv\Scripts\activate

- Run virtual environment for MacOS
> source venv/bin/

- Deactivate a virtual environment
> deactivate

- To install all packages and extensions in project
> pip install -r requirements.txt 

5. Create database
> py manage.py makemigrations
> py manage.py migrate

6. Create superuser
> py manage.py createsuperuser

7. Running server
>py manage.py runserver

8. In web browser, access
> localhost:8000

## Contribute
 - If you want to contribute to this project, please create a pull request and clearly describe the changes you propose
