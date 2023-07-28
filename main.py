from toui import Website, set_global_app
import os

app = Website(__name__, assets_folder="assets", secret_key="make sure that this value is a secret")
set_global_app(app)

from home import home_pg
from contact import contact_pg
from about import about_pg

app.add_pages(home_pg, contact_pg, about_pg)

flask_app = app.flask_app

if __name__ == "__main__":
    app.run(debug=True)