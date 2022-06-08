from .menu import CursesWindow
from .azure import get_azure_accounts, set_azure_account

def main():
    accounts = get_azure_accounts()
    menu_lst = [x.get("name") for x in accounts]

    window = CursesWindow()
    index = window.menu(menu_lst)

    if index is not None:
        set_azure_account(accounts[index].get("id"))
        print("Azure subscription set to:")
        print("name :", accounts[index].get("name"))
        print("id   :", accounts[index].get("id"))
        print()
    else:
        print("Nothing happend...")
