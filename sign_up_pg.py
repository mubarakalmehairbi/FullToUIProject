from toui import Page, get_global_app

app = get_global_app()

sign_up_pg = Page("assets/sign-up.html", url="/sign-up")

sign_up_pg.set_navigation_bar("assets/navbar.html")
sign_up_pg.set_footer("assets/footer.html")

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
    terms = pg.get_element("terms").get_value()
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
        pg.get_element("content").set_content("Invalid verification code.")
        pg.get_element("content").set_attr("class", "notification is-danger")
        return
    progress_bar = pg.get_element("progress-bar")
    cls = progress_bar.get_attr("class", default="").replace("is-hidden", "")
    success = app.signup_user(username=app.user_vars['email'], password=app.user_vars['password'], email=app.user_vars['email'])
    progress_bar.set_attr("class", cls)
    if success:
        app.open_new_page("/dashboard")
    else:
        pg.get_element("sign-up-status").set_content("An error occurred while signing you up.")
        pg.get_element("sign-up-status").set_attr("class", "notification is-danger")
    
sign_up_pg.get_element("sign-up").onclick(sign_up)
sign_up_pg.get_element("verify").onclick(verify)
