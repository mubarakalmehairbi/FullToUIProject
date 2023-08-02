from toui import Page, get_global_app

# Get the app object
app = get_global_app()

# Create a page object for the contact page
contact_pg = Page("assets/contact.html", url="/contact")

# Set the navigation bar for the contact page
contact_pg.set_navigation_bar("assets/navbar.html")

# Set the footer for the contact page
contact_pg.set_footer("assets/footer.html")

def submit_message():
    """This function is called when the user submits a message."""
    pg = app.get_user_page()
    name = pg.get_element("name").get_value()
    email = pg.get_element("email").get_value()
    message = pg.get_element("message").get_value()
    print(f"Message received:\n\tName: {name}\n\tEmail: {email}\n\tMessage: {message}")
    # Show a success message
    pg.get_element("content").set_content("Message sent successfully!")
    pg.get_element("content").set_attr("class", "notification is-success")

contact_pg.get_element("submit").onclick(submit_message)