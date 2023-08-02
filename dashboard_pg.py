from toui import Page, get_global_app

app = get_global_app()

dashboard_pg = Page("assets/dashboard.html", url="/dashboard")

dashboard_pg.set_navigation_bar("assets/navbar.html")
dashboard_pg.set_footer("assets/footer.html")

def do_something_before_dashboard_loads():
    """This function is called before the page is loaded."""
    # Check if the user is signed in
    if not app.is_signed_in():
        return app.redirect_response("/sign-in")

dashboard_pg.on_url_request(do_something_before_dashboard_loads, display_return_value=True)

