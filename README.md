# FullToUIProject
A template for a full app created using ToUI. You can use this template and customize it to create your own app. ToUI is a Python framework for creating user interfaces from HTML code easily. Learn about ToUI [here](https://github.com/mubarakalmehairbi/ToUI).

# How to use this template
## Method 1: From GitHub repo
Click on "Use this template" button above.

## Method 2:
Install [ToUI](https://github.com/mubarakalmehairbi/ToUI) then run the command:
```
toui init --full
```

# What are the files in this template?
The project contains the following:
- `main.py`: the main script of the app. This is the first script that you should look at and the script that you should run when developing the app.
- `pages` folder: each script inside `pages` folder is the backend of a web page:
    - `home_pg.py`: the backend for the home page.
    - `about_pg.py`: the backend for the "about" page.
    - `contact_pg.py`: the backend for the "contact" page.
    - `calculator_pg.py`: the backend for a simple calculator page.
    - `sign_in.py`: the backend for the sign in page.
    - `sign_up.py`: the backend for the sign up page.
    - `dashboard_pg.py`: the backend for a simple dashboard page.
- `assets` folder: contains the HTML files for the web pages. The HTML files in this template are styled using Bulma CSS Framework: https://bulma.io/. You will find HTML class names that refer to Bulma CSS classes.
- `security.py`: adds some security to the app. This script must be revised before publishing the app.
- `requirements.txt`: lists the python packages required to run the app.
- `LICENSE`: the license of the app. You can change it to any license you want.
- `Procfile`: a file required to deploy the app to Heroku. You can remove it if you want to deploy the app elsewhere.
