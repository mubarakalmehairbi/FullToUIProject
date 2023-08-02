from toui import Page, get_global_app

app = get_global_app()

sign_in_pg = Page("assets/sign-in.html", url="/sign-in")

sign_in_pg.set_navigation_bar("assets/navbar.html")
sign_in_pg.set_footer("assets/footer.html")
