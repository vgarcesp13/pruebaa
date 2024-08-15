import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from faker import Faker

from src.pages.widgets import Select_Menu


class New_users():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.__bookstore = '.element-group:nth-child(6) .header-text'
        self.__login_click = '.show #item-0'
        self.__register = 'newUser'
        self.__send = 'register'

        # Datos del Formulario de nuevo registro
        self.__f_name = 'firstname'
        self.__l_name = 'lastname'
        self.__u_name = 'userName'
        self.__passw = 'password'

    def click_book(self):
        elemento = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.__bookstore)))
        self.driver.execute_script("arguments[0].scrollIntoView();", elemento)
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.__bookstore))).click()

    def click_login(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.__login_click)))
        login_click = self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.__login_click)))
        login_click.click()

    def click_new_user(self):
        elemento = self.wait.until(EC.visibility_of_element_located((By.ID, self.__register)))
        self.driver.execute_script("arguments[0].scrollIntoView();", elemento)
        self.wait.until(EC.element_to_be_clickable((By.ID, self.__register))).click()

    def fill_new_user(self):
        fake = Faker()
        random_f_name = fake.first_name()
        random_l_name = fake.last_name()
        random_u_name = fake.user_name()
        random_passw = fake.password()

        # Llenar datos
        self.wait.until(EC.visibility_of_element_located((By.ID, self.__f_name))).send_keys(random_f_name)
        self.wait.until(EC.visibility_of_element_located((By.ID, self.__l_name))).send_keys(random_l_name)
        self.wait.until(EC.visibility_of_element_located((By.ID, self.__u_name))).send_keys(random_u_name)
        self.wait.until(EC.visibility_of_element_located((By.ID, self.__passw))).send_keys(random_passw)
        
        time.sleep(5) # Pausa para resolver el captcha manualmente
    
        # Enviar el formulario
        self.wait.until(EC.element_to_be_clickable((By.ID, self.__send))).click()
        time.sleep(1)

        self.driver.back()


    def options_login(self):
        self.click_book()
        self.click_login()
        self.click_new_user()
        self.fill_new_user()
        time.sleep(2)
        return Select_Menu(driver=self.driver)
