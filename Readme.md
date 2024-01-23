# Backend Copyrightforever

Project name: **_CopyRightForever_**

**clone project using HTTPS or SSH**

**_HTTPS:_**
`git clone https://github.com/abdullahzulfiqar653/Backend-Copyrightforever.git`

**_SSH:_**
`git@github.com:abdullahzulfiqar653/Backend-Copyrightforever.git`

**make and activate environment for project using command given**

**1: making environment and installing dependencies**
**_Install python 3.11 on local machine https://www.python.org/_**

**i: installing poetry:**

**_windows:_** pip install poetry
**_macOS/Linux:_** pip3 install poetry

**ii: installing package:_**
open terminal in Backend-Copyrightforever and run

**2: Install all Packages _macOS/Linux/Windows:_**

```
poetry install
```

**3: Setup .env to load environment variables**

```
add .env file in main source directory at the same level with manage.py and .env.example
and setup all variables using the help of .env.example
```

**5: Run the Application and API in windows terminal or in vscode termnal**
Make sure to activate the virtual environment and you are in backend-paradise directory
_​use command to run django-server:_ python manage.py runserver
​_use command to run dramatiq:_ python manage.py rundramatiq
