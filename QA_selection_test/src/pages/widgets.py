import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from src.pages.elements import Web_tables

class Select_Menu():
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.__widgets = '.element-group:nth-child(4) .header-text'
        self.__select = '.show #item-8 > .text'
        
        #Variables para el select menu
        self.__from_label = '//*[@id="withOptGroup"]'
        self.__option1 = 'react-select-5-option-2'

        self.__from_label2 = '//*[@id="selectOne"]/div/div[1]/div[1]'
        self.__option2 = 'react-select-6-option-0-3'
        
        self.__from_label3 = '//*[@id="oldSelectMenu"]'
        self.__option3 = '//*[@id="oldSelectMenu"]/option[9]'
        
        self.__from_label4 = "//div[@id='selectMenuContainer']/div[7]/div/div/div/div"
        self.__option4 = 'react-select-4-option-1'
        self.__option5 = 'react-select-4-option-3'
        
        self.__from_label5 = '//*[@id="cars"]'
        self.__option6 = '//*[@id="cars"]/option[1]'
        self.__option7 = '//*[@id="cars"]/option[3]'
    
    
    def click_widgets(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.__widgets)))
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.__widgets))).click()

    def click_select_menu(self):
        self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.__select)))
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.__select))).click()

    def select_value_from_label(self):
        #label esperar que este visible
        label = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.__from_label)))
        time.sleep(3)  
        label.click()
        
        option = self.wait.until(EC.visibility_of_element_located((By.ID, self.__option1)))
        option.click()

    def select_one_from(self):
        label = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.__from_label2)))
        time.sleep(3)  
        label.click()
        
        option = self.wait.until(EC.visibility_of_element_located((By.ID, self.__option2)))
        option.click()
        
    def select_old_style(self):
        label = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.__from_label3)))
        time.sleep(3)  
        label.click()
        
        option = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.__option3)))
        option.click()
          
    def select_multiselect(self):
        label = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.__from_label4)))
        time.sleep(3)  
        label.click()
        
        option = self.wait.until(EC.visibility_of_element_located((By.ID, self.__option4)))
        option.click()
        
        option = self.wait.until(EC.visibility_of_element_located((By.ID, self.__option5)))
        option.click()
        
    def select_standard(self):
        label = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.__from_label5)))
        time.sleep(3)  
        label.click()
        
        option = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.__option6)))
        option.click()
        
        time.sleep(1)  
        option = self.wait.until(EC.visibility_of_element_located((By.XPATH, self.__option7)))
        option.click()
        
    def options_select_menu(self):
        self.click_widgets()
        self.click_select_menu()
        self.select_value_from_label()
        self.select_one_from()
        self.select_old_style()
        #self.select_multiselect()
        self.select_standard()
        
        time.sleep(1)  
        return Web_tables(driver=self.driver)
