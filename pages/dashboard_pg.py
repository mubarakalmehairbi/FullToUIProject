from toui import Page, get_global_app, IFrameElement

app = get_global_app()

dashboard_pg = Page("assets/dashboard.html", url="/dashboard")

dashboard_pg.set_navigation_bar("assets/navbar.html")
dashboard_pg.set_footer("assets/footer.html")

def do_something_when_dashboard_loads():
    """This function is called when the page is loaded."""
    # Check if the user is signed in
    if not app.is_signed_in():
        return app.redirect_response("/sign-in")
    else:
        pg = app.get_user_page()
        # Set the email field to the user's email
        pg.get_element("email").set_content(app.get_current_user_data("email"))
        # Set the display name (if it exists)
        name = app.get_current_user_data("display-name")
        if name is not None:
            pg.get_element("current-display-name-header").set_content(name)
            pg.get_element("current-display-name-settings").set_content(f"Your current display name: {name}")
        else:
            pg.get_element("current-display-name-settings").set_content("Your current display name: None")
        # Add a table under analytics section
        table = "<embed src=\"./dashboard_table.html\" width='100%' height='400px'>"
        pg.get_element("data-table").set_content(table)
        # Add figure under analytics section
        fig = "<embed src=\"./dashboard_plot.html\" width='100%' height='400px'>"
        pg.get_element("data-figure").set_content(fig)
        return pg.to_str()

dashboard_pg.on_url_request(do_something_when_dashboard_loads, display_return_value=True)

def open_section(section_id):
    pg = app.get_user_page()
    for section in pg.get_elements(class_name="dashboard-section"):
        cls = section.get_attr("class", default="")
        if section.get_attr("id") == section_id:
            cls = cls.replace("is-hidden", "")
        else:
            if "is-hidden" not in cls:
                cls += " is-hidden"
        section.set_attr("class", cls)

def sign_out():
    """Signs out the user"""
    app.signout_user()
    app.open_new_page("/sign-in")

def change_display_name():
    """Changes the displayed name of the user"""
    pg = app.get_user_page()
    new_name = pg.get_element("display-name").get_value()
    if new_name.strip() != "":
        app.set_current_user_data("display-name", new_name)
        pg.get_element("current-display-name-header").set_content(new_name)
        pg.get_element("current-display-name-settings").set_content(f"Your current display name: {new_name}")


dashboard_pg.add_function(open_section)
dashboard_pg.get_element("change-display-name").onclick(change_display_name)
dashboard_pg.get_element("sign-out").onclick(sign_out)



