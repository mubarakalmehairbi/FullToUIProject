from toui import Page, get_global_app

app = get_global_app()

calculator_pg = Page("assets/calculator.html", url="/calculator")

calculator_pg.set_navigation_bar("assets/navbar.html")
calculator_pg.set_footer("assets/footer.html")

def add():
    """Adds the two numbers in the input boxes and displays the result."""
    pg = app.get_user_page()
    num1 = float(pg.get_element("num1").get_value())
    num2 = float(pg.get_element("num2").get_value())
    result = num1 + num2
    pg.get_element("result").set_content(f"Result: {result}")
    pg.get_element("extra-instructions").set_content("The two numbers were sent to Python. Python added the two numbers then sent them back to HTML!")

# Call the function when an element is clicked
calculator_pg.get_element("calculate").onclick(add)