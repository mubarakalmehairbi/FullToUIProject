"""
Welcome to ToUI full project template. This template is a good starting point for building your own app with
much less effort.

The HTML files in this template are styled using Bulma CSS Framework: https://bulma.io/. You
will find HTML class names that refer to Bulma CSS classes.

This script is the main script of your app. It creates the app object, connects to a database, and adds the
pages to the app. It also adds some security measures to the app.
"""
import os
from toui import Website, DesktopApp, set_global_app

SECRET_KEY = os.urandom(50) # Change this to a string that is hard to guess and store it somewhere safe.
DATABASE_URI = f"sqlite:///{os.getcwd()}/.my_dummy_database2.db" # Change this to the URI of your database.

# Create the app. You can create a desktop app by replacing `Website` with `DesktopApp`
app = Website(__name__, assets_folder="assets", secret_key=SECRET_KEY)
app.add_user_database_using_sql(DATABASE_URI, other_columns=["user_metadata"]) # Adds a user-specific database to the app.
#"user_metadata" is just a json string for storing extra info about the user, you can remove it if you don't need it.

# Allows the app to be shared across Python scripts
set_global_app(app)

# Import the home page in order to run the home_pg.py script and to add the page to the app. Do the same for
# the other pages.
from home_pg import home_pg
from about_pg import about_pg
from contact_pg import contact_pg
from sign_in_pg import sign_in_pg
from sign_up_pg import sign_up_pg
from dashboard_pg import dashboard_pg
from calculator_pg import calculator_pg

app.add_pages(home_pg, contact_pg, about_pg, sign_in_pg, sign_up_pg, dashboard_pg, calculator_pg)

# Add some security measures. You need to check `security.py` before deploying the app.
from security import ws_validation, data_validation
app.set_ws_validation(ws_validation)
app.set_data_validation(data_validation)

# Get the Flask app instance. This will be helpful when deploying the app.
flask_app = app.flask_app

if __name__ == "__main__":
    app.run(debug=True)

