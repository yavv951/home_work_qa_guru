
def func_print_name_args(function):
    string_name = function.__name__
    var_names = function.__code__.co_varnames
    if string_name and var_names:
        return print(f"name function - {string_name}, args function - {var_names}")
    elif string_name:
        return print(f"name function - {string_name} and not have args")
    else:
        return print(f"not have are func and args")

def open_browser():
    pass


def go_to_companyname_homepage(page_url):
    pass


def find_registration_button_on_login_page(page_url, button_text):
    pass

functions = (open_browser, go_to_companyname_homepage, find_registration_button_on_login_page)
for func in functions:
    func_print_name_args(func)

