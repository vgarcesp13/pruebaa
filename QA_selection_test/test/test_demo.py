import time
from src.pages.forms import Forms_page
from src.pages.new_user import New_users
from src.pages.widgets import Select_Menu
from src.pages.elements import Web_tables
from src.pages.incorrectelement import Incorrect_Tables

class TestDemo:
    def test_mark_forms(self, init_driver):
        startpage = Forms_page(init_driver)
        homepage = startpage.start_home_page()

        # instancia New_users
        new_users_page = New_users(driver=init_driver)
        new_users_page.options_login()

        # instancia Widgets
        select_menu = Select_Menu(driver=init_driver)
        select_menu.options_select_menu()
        
        #instanciar Web_tables
        web_tables = Web_tables(driver=init_driver)
        web_tables.options_web_tables()
        
        #instanciar Incorrect_Tables
        incorrect_tables = Incorrect_Tables(driver=init_driver)
        incorrect_tables.options_web_tables_with_incorrect_data()

        time.sleep(2)
