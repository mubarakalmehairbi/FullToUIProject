import os
from toui import Page, get_global_app, __version__
from toui._helpers import info

app = get_global_app()

sign_up_pg = Page("assets/sign-up.html", url="/sign-up")
sign_up_pg.set_navigation_bar("assets/navbar.html")
sign_up_pg.set_footer("assets/footer.html")

# Google Cloud app constants (if you want to add sign in with google feature)
GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID") # You can get this from the Google Cloud Console
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET") # You can get this from the Google Cloud Console
CUSTOM_HOST = os.environ.get("CUSTOM_HOST") # This is unnecessary most of the time. You can delete it. It is only
# needed if you are using a reverse proxy such as running the app on GitHub Codespaces.

def sign_up():
    """This function is called when the user submits the sign up form."""
    pg = app.get_user_page()
    email = pg.get_element("email").get_value()
    email_help = pg.get_element("email-help")
    if app.email_exists(email):
        set_help_text(email_help, "This email is already in use.", False)
        return
    if "@" not in email or "." not in email:
        set_help_text(email_help, "This email is invalid.", False)
        return
    set_help_text(email_help, "Email is valid.", True)
    password = pg.get_element("password").get_value()
    password_help = pg.get_element("password-help")
    if len(password) < 8:
        password_help.set_content("Password must be at least 8 characters long.")
        set_help_text(password_help, "Password must be at least 8 characters long.", False)
        return
    set_help_text(password_help, "Password is valid.", True)
    terms = pg.get_element("terms").has_attr("checked")
    print(f"Terms: {terms}")
    terms_help = pg.get_element("terms-help")
    if not terms:
        set_help_text(terms_help, "You must agree to the terms and conditions.", False)
        return
    set_help_text(terms_help, "", True)
    verification_section = pg.get_element("verification-section")
    cls = verification_section.get_attr("class", default="").replace("is-hidden", "")
    verification_section.set_attr("class", cls)
    app.user_vars["email"] = email
    app.user_vars["password"] = password
    app.user_vars["verification_code"] = "1234" # This should be generated randomly and sent to the user's email
    app.open_new_page("/sign-up#verification-section")

def set_help_text(element, text, success=True):
    element.set_content(text)
    cls = element.get_attr("class", default="").replace("has-text-danger", "").replace("has-text-success", "")
    if success:
        cls += " has-text-success"
    else:
        cls += " has-text-danger"
    element.set_attr("class", cls)

def verify():
    """This function is called when the user verifies their account."""
    pg = app.get_user_page()
    verification_code = pg.get_element("verification-code").get_value()
    if verification_code != app.user_vars["verification_code"]:
        set_help_text(pg.get_element("verify-help"), "The verification code is incorrect.", False)
        return
    set_help_text(pg.get_element("verify-help"), "The verification code is correct.", True)
    progress_bar = pg.get_element("progress-bar")
    cls = progress_bar.get_attr("class", default="").replace("is-hidden", "")
    success = app.signup_user(username=app.user_vars['email'], password=app.user_vars['password'], email=app.user_vars['email'])
    progress_bar.set_attr("class", cls)
    if success:
        sign_in_success = app.signin_user(username=app.user_vars['email'], password=app.user_vars['password'], email=app.user_vars['email'])
        if not sign_in_success:
            pg.get_element("sign-up-status").set_content("The account was created, but there was error occurred while signing you in.")
            pg.get_element("sign-up-status").set_attr("class", "notification is-danger")
            return
        app.open_new_page("/dashboard")
    else:
        pg.get_element("sign-up-status").set_content("An error occurred while signing you up.")
        pg.get_element("sign-up-status").set_attr("class", "notification is-danger")

def sign_in_with_google():
    """This function is called when the user clicks the sign in with google button."""
    info(f"ToUI version: {__version__}")
    pg = app.get_user_page()
    if GOOGLE_CLIENT_ID is None or GOOGLE_CLIENT_SECRET is None:
        print("You must set the GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET variables to use sign in using google feature.")
        return
    app.sign_in_using_google(client_id=GOOGLE_CLIENT_ID, client_secret=GOOGLE_CLIENT_SECRET, after_auth_url="/dashboard",
                             custom_host=CUSTOM_HOST) # You can delete the custom_host argument
    
sign_up_pg.get_element("sign-up").onclick(sign_up)
sign_up_pg.get_element("verify").onclick(verify)
sign_up_pg.get_element("google").onclick(sign_in_with_google)
