# PROJECT LOG

<br>
<br>

> Dates and Details of the work done for the project '**CipherVeil**'.

<br>

## 📅 29 JAN 2024
I submitted three project ideas to the guide for approval, and the guide approved the project idea titled ‘Steganography using custom ciper in Python Django’.

<br><br>


## 📅 9 FEB 2024

- submitted a Absract of the Project to Project Guide

    1. Research Area
    2. Objectives
    3. Requirements
    4. Modules with small Descriptions.
    5. Problem statement.

- uploaded the abstract file to the Documentation folder in project git repository.

<br> <br>

## 📅 13 FEB 2024

- Following packages and software were installed :

    1. Python
    2. PIP
    3. Postgresql
    4. Virtualenvwrapper-win
    5. Django
    6. python-decouple
    7. psycopg-binary 

- created a GitHub repository '**cipherveil**' to build,commit my project and to store other related files.
- updated the git ignore
- created a django project named '**cipherveil**'
- created a database named '**cipherveil**' in postgres using pgAdmin
- created .env file in root directory to store Postgresql credentials
- created a superuser for the project named as 'anas'
- created an app named 'frontlineapp' in the project
- changes were migrated & tables were automatically build by Django

<br>

**Changes made in settings.py file :**

- changed time zone to 'Asia/Kolkata'
- Imported config module from decouple to use the database credentials from the .env file
- added 'frontlineapp' to installed app section

<br><br>

## 📅 15 FEB 2024

- created a urls.py file for frontlineapp
- created a 'templates/frontlineapp' directory to store templates in frontilineapp

<br>

**urls.py file :**
- changes made
    1.  added url pattern for frontlineapp

<br>

**templates :**
- newly added
    1. base.html
    2. index.html

<br>


**views.py in frontlineapp :**
- newly added
    1.  index view

<br>

**urls.py in frontlineapp :**
- newly added URL patterns
    1.  index


<br><br>

## 📅 19 FEB 2024


**templates :**
- newly added
    1. home.html
    2. signin.html

<br>

**urls.py in frontlineapp :**
- newly added URL patterns
    1.  home
    2.  signin
    3.  signout



**views.py in frontlineapp :**
- newly added
    1.  signout view
    2.  signin view
    3.  home view

<br><br>

## 📅 21 FEB 2024

- created a 2 new apps named 'contactapp' and 'steganoapp'

<br>

**Changes made in settings.py file :**
    
- added 'contactapp' to installed app section
- added 'steganoapp' to installed app section

<br><br>

## 📅 3 MAR 2024

- created a urls.py in steganoapp
- created a directory '/templates/steganoapp' for steganoapp

<br>

**Changes made in settings.py file :**
- Added the code for MEDIA ROOT

<br>



**urls.py file :**
- changes made
    1.  added url pattern for steganoapp

<br>

**Changes made in urls.py file :**
- newly added URL patterns
    1.  encrypt
    2.  decrypt
    3.  downloading image


**Changes made in views.py file :**
- newly added function request
    1.  encrypt
    2.  decrypt
    3.  downloading image

**templates in steganoapp :**
- newly added
    1. encrypt.html
    2. decrypt.html