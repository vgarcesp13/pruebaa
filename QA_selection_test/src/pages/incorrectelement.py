import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class Incorrect_Tables():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.__add_new = 'addNewRecordButton'
        
        #variables para web tables formulario
        self.__f_name = 'firstName'
        self.__l_name = 'lastName'
        self.__email = 'userEmail'
        self.__age = 'age'
        self.__salary = 'salary'
        self.__department = 'department'
        self.__submit = 'submit'
    
    def add_tables(self):
        add_new_button = self.wait.until(EC.visibility_of_element_located((By.ID, self.__add_new)))
        self.wait.until(EC.element_to_be_clickable((By.ID, self.__add_new))).click()
        time.sleep(1) 
    
    def fill_web_tables_incorrect_data(self):
        # Usar valores inválidos
        invalid_f_name = ""  
        invalid_l_name = "" 
        invalid_email = "invalid-email" 
        invalid_age = "-1"  
        invalid_salary = "abcde"
        invalid_department = ""
        
        time.sleep(2)
        self.wait.until(EC.visibility_of_element_located((By.ID, self.__f_name))).send_keys(invalid_f_name)
        self.wait.until(EC.visibility_of_element_located((By.ID, self.__l_name))).send_keys(invalid_l_name)
        self.wait.until(EC.visibility_of_element_located((By.ID, self.__email))).send_keys(invalid_email)
        self.wait.until(EC.visibility_of_element_located((By.ID, self.__age))).send_keys(invalid_age)
        self.wait.until(EC.visibility_of_element_located((By.ID, self.__salary))).send_keys(invalid_salary)
        self.wait.until(EC.visibility_of_element_located((By.ID, self.__department))).send_keys(invalid_department)
        
        # Enviar el formulario
        time.sleep(5)
        self.wait.until(EC.element_to_be_clickable((By.ID, self.__submit))).click()
        
 
    def options_web_tables_with_incorrect_data(self):
        self.add_tables()
        time.sleep(2) 
        self.fill_web_tables_incorrect_data()
