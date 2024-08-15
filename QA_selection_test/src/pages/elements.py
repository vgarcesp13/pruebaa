import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from faker import Faker
from src.pages.incorrectelement import Incorrect_Tables

class Web_tables():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.__elements = '.element-group:nth-child(1) .header-wrapper'
        self.__web_tables = '.show #item-3 > .text'
        self.__add = 'addNewRecordButton'
        self.__edit = '#edit-record-1 path'
        self.__delete = '#delete-record-3 > svg'
        
        #variables para web tables formulario
        self.__f_name = 'firstName'
        self.__l_name = 'lastName'
        self.__email = 'userEmail'
        self.__age = 'age'
        self.__salary = 'salary'
        self.__department = 'department'
        self.__submit = 'submit'
    
    def click_elements(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.__elements)))
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.__elements))).click()
        
    def click_web_tables(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.__web_tables)))
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.__web_tables))).click() 
        
    def add_web_tables(self):
        self.wait.until(EC.visibility_of_element_located((By.ID, self.__add)))
        self.wait.until(EC.element_to_be_clickable((By.ID, self.__add))).click()    
    
    def fill_web_tables(self):
        fake = Faker()
        random_f_name = fake.first_name()
        random_l_name = fake.last_name()
        random_email = fake.email()
        random_age = fake.random_int(min=18, max=100)
        random_salary = fake.random_int(min=5000, max=10000)
        random_department = "IT" 
        time.sleep(2)
        
        # Llenar datos
        self.wait.until(EC.visibility_of_element_located((By.ID, self.__f_name))).send_keys(random_f_name)
        self.wait.until(EC.visibility_of_element_located((By.ID, self.__l_name))).send_keys(random_l_name)
        self.wait.until(EC.visibility_of_element_located((By.ID, self.__email))).send_keys(random_email)
        self.wait.until(EC.visibility_of_element_located((By.ID, self.__age))).send_keys(random_age)
        self.wait.until(EC.visibility_of_element_located((By.ID, self.__salary))).send_keys(random_salary)
        self.wait.until(EC.visibility_of_element_located((By.ID, self.__department))).send_keys(random_department)
        
        # Enviar el formulario
        self.wait.until(EC.element_to_be_clickable((By.ID, self.__submit))).click()
        time.sleep(2)
        
    def edit_web_tables(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.__edit)))
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.__edit))).click()
        self.wait.until(EC.visibility_of_element_located((By.ID, self.__f_name))).clear()
        self.wait.until(EC.visibility_of_element_located((By.ID, self.__f_name))).send_keys('Editado')
        self.wait.until(EC.element_to_be_clickable((By.ID, self.__submit))).click()
        time.sleep(2)
    
    def delete_web_tables(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR,  self.__delete)))
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR,  self.__delete))).click()
        time.sleep(2)
    
    def options_web_tables(self):
        self.click_elements()
        self.click_web_tables()
        self.add_web_tables()
        self.fill_web_tables()
        self.edit_web_tables()
        self.delete_web_tables()
        time.sleep(2)
        return Incorrect_Tables(driver=self.driver)
        
        
        