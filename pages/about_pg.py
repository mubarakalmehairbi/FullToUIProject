from toui import Page

about_pg = Page("assets/about.html", url="/about")

# Set the navigation bar for the about page
about_pg.set_navigation_bar("assets/navbar.html")

# Set the footer for the about page
about_pg.set_footer("assets/footer.html")