import os
from toui import Page, get_global_app

app = get_global_app()

sign_in_pg = Page("assets/sign-in.html", url="/sign-in")

sign_in_pg.set_navigation_bar("assets/navbar.html")
sign_in_pg.set_footer("assets/footer.html")

# Google Cloud app constants (if you want to add sign in with google feature)
GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID") # You can get this from the Google Cloud Console
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET") # You can get this from the Google Cloud Console
CUSTOM_HOST = os.environ.get("CUSTOM_HOST") # This is unnecessary most of the time. You can delete it. It is only
# needed if you are using a reverse proxy such as running the app on GitHub Codespaces.

def sign_in():
    """This function is called when the user clicks the sign in button."""
    pg = app.get_user_page()
    email = pg.get_element("email").get_value()
    password = pg.get_element("password").get_value()
    progress = pg.get_element("progress")
    cls = progress.get_attr("class", default="").replace("is-hidden", "")
    progress.set_attr("class", cls)
    success = app.signin_user(username=email, password=password, email=email)
    cls += " is-hidden"
    progress.set_attr("class", cls)
    if success:
        app.open_new_page("/dashboard")
    else:
        status = pg.get_element("sign-in-status")
        cls = status.get_attr("class", default="").replace("is-hidden", "")
        status.set_attr("class", cls)
        status.set_content("An error occurred while signing you in. Try using a different username or password.")

def sign_in_with_google():
    """This function is called when the user clicks the sign in with google button."""
    pg = app.get_user_page()
    if GOOGLE_CLIENT_ID is None or GOOGLE_CLIENT_SECRET is None:
        print("You must set the GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET variables to use sign in using google feature.")
        return
    app.sign_in_using_google(client_id=GOOGLE_CLIENT_ID, client_secret=GOOGLE_CLIENT_SECRET, after_auth_url="/dashboard",
                             custom_host=CUSTOM_HOST) # You can delete the custom_host argument
    
sign_in_pg.get_element("sign-in").onclick(sign_in)
sign_in_pg.get_element("google").onclick(sign_in_with_google)
