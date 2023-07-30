from toui import Website, DesktopApp, set_global_app

SECRET_KEY = "some secret string" # Change this to a harder to guess value.

# Create the app. You can create a desktop app by replacing `Website` with `DesktopApp`
app = Website(__name__, assets_folder="assets", secret_key=SECRET_KEY)

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

app.add_pages(home_pg, contact_pg, about_pg)

# Add some security measures. You need to check `security.py` before deploying the app.
from security import ws_validation, data_validation
app.set_ws_validation(ws_validation)
app.set_data_validation(data_validation)

# Get the Flask app instance. This will be helpful when deploying the app.
flask_app = app.flask_app

if __name__ == "__main__":
    app.run(debug=True)

