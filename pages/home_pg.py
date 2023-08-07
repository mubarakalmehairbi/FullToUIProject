import os
from toui import Page, get_global_app

# Get the app object
app = get_global_app()

# Create a page object for the home page
home_pg = Page("assets/home.html", url="/")

# Set the navigation bar for the home page
home_pg.set_navigation_bar("assets/navbar.html")

# Set the footer for the home page
home_pg.set_footer("assets/footer.html")

# Creating some functions that can be called from the HTML
def update_text():
    """Updates the text on the page to be the same as the input box."""
    pg = app.get_user_page()
    input_value = pg.get_element("input").get_value()
    pg.get_element("output").set_content(input_value)
    pg.get_element("extra-instructions").set_content("That was an example of a function being called from the HTML!")

# Add `update_text()` function to the page
home_pg.add_function(update_text)
# Now `update_text` can be called from the HTML! There is a button in home.html labeled "Update Text Using Python" that calls the function.

# Add another function to the page
def open_tab(tab_id):
    """Opens a tab with the given ID. The class names here refer to Bulma CSS classes. https://bulma.io/"""
    pg = app.get_user_page()
    # Get elements that have the class `tabcontent`.
    tabscontents = pg.get_elements(class_name="tabcontent")
     # Get all the tab buttons
    tabbuttons = pg.get_element("tabs-list").get_elements("li")
    # Hide all the tabs contents except the one with the given ID.
    for tabcontent, tabbutton in zip(tabscontents, tabbuttons):
        content_cls = tabcontent.get_attr("class")
        button_cls = tabbutton.get_attr("class")
        if button_cls is None:
            button_cls = ""
        if tabcontent.get_id() == tab_id:
            # Show the tab content and make the tab button active
            content_cls = content_cls.replace("is-hidden", "")
            tabcontent.set_attr("class", content_cls)
            if not "is-active" in button_cls:
                button_cls += " is-active"
            tabbutton.set_attr("class", button_cls)
        else:
            # Hide the tab content and make the tab button inactive
            if not "is-hidden" in content_cls:
                content_cls += " is-hidden"
            tabcontent.set_attr("class", content_cls)
            button_cls = button_cls.replace("is-active", "")
            tabbutton.set_attr("class", button_cls)

# Add `open_tab()` function to the page
home_pg.add_function(open_tab)

# Add a function to be called when file is uploaded
def upload_file():
    """This function is called when a file is uploaded. It saves the file in the server."""
    pg = app.get_user_page()
    files = pg.get_element("file").get_files()
    for file in files:
        if file.size > 1000000:
            pg.get_element("upload-status").set_content("File too large!")
            return
        with open(".uploaded_file", "w") as stream:
            file.save(stream)
        pg.get_element("upload-status").set_content("File uploaded!")

# Call `upload_file()` when a file is uploaded and a button is clicked.
home_pg.get_element("upload").onclick(upload_file)

def download_file():
    """This function is called when the user clicks on the download button. It downloads the home.html file."""
    pg = app.get_user_page()
    filepath = "assets/home.html"
    app.download(filepath)

# Call `download_file()` when the download button is clicked.
home_pg.get_element("download").onclick(download_file)

