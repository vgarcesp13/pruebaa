import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from faker import Faker
from selenium.webdriver.common.keys import Keys

from .new_user import New_users
from .upload import Uploadimg

class Forms_page:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.__form = '.card:nth-child(2) .card-body'
        self.__practice_form = '.show #item-0'
        self.__name = 'firstName'
        self.__lastname = 'lastName'
        self.__email = 'userEmail'
        self.__contact = 'userNumber'
        self.__date = 'dateOfBirthInput'
        self.__subject = 'subjectsInput'
        self.__address = 'currentAddress'
        self.__send = 'submit'

    def click_forms(self):
        elemento = self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.__form)))
        self.driver.execute_script("arguments[0].scrollIntoView();", elemento)
        self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.__form))).click()

    def click_practice(self):
       self.wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, self.__practice_form)))
       self.wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.__practice_form))).click()



    def fill_form(self):
        fake = Faker()
        # Generar datos aleatorios
        random_f_name = fake.first_name()
        random_l_name = fake.last_name()
        random_email = fake.email()
        random_gender = fake.random_element(elements=('Male', 'Female', 'Other'))
        random_mobile = fake.msisdn()[:10]
        random_date = fake.date_of_birth(minimum_age=18, maximum_age=65).strftime('%d %B %Y')
        random_subjects = "Maths"
        random_hobbies = fake.random_element(elements=('Sports', 'Reading', 'Music'))
        random_current_address = fake.address()
        random_state = fake.random_element(elements=('NCR', 'Uttar Pradesh', 'Haryana', 'Rajasthan'))
        random_city = fake.random_element(elements=('Agra', 'Lucknow', 'Merrut'))

        # Llenar el formulario
        self.wait.until(EC.visibility_of_element_located((By.ID, self.__name))).send_keys(random_f_name)
        #time.sleep(1)

        self.wait.until(EC.visibility_of_element_located((By.ID, self.__lastname ))).send_keys(random_l_name)
         #time.sleep(1)

        self.wait.until(EC.visibility_of_element_located((By.ID, self.__email))).send_keys(random_email)
         #time.sleep(1)

        gender_xpath = f"//label[text()='{random_gender}']"
        self.wait.until(EC.visibility_of_element_located((By.XPATH, gender_xpath))).click()
         #time.sleep(1)

        self.wait.until(EC.visibility_of_element_located((By.ID, self.__contact ))).send_keys(random_mobile)
         #time.sleep(1)

        # Seleccionar fecha de nacimiento
        self.wait.until(EC.element_to_be_clickable((By.ID, self.__date))).click()
         #time.sleep(1)

        anio_xpath = "//option[text()='2000']"
        self.wait.until(EC.element_to_be_clickable((By.XPATH, anio_xpath))).click()
         #time.sleep(1)

        mes_xpath = "//option[text()='July']"
        self.wait.until(EC.element_to_be_clickable((By.XPATH, mes_xpath))).click()
         #time.sleep(1)

        dia_xpath = "//div[text()='15']"
        self.wait.until(EC.element_to_be_clickable((By.XPATH, dia_xpath))).click()
         #time.sleep(1)

        # Ingresar la materia
        subjects_input = self.wait.until(EC.visibility_of_element_located((By.ID, self.__subject )))
        subjects_input.send_keys(random_subjects)
        subjects_input.send_keys(Keys.RETURN)
         #time.sleep(1)

        # Seleccionar un hobby
        hobbies_xpath = f"//label[text()='{random_hobbies}']"
        self.wait.until(EC.element_to_be_clickable((By.XPATH, hobbies_xpath))).click()
         #time.sleep(1)

        # Subir la imagen
        uploader = Uploadimg(self.driver)  # Crear una instancia de Uploadimg
        img_path = uploader.get_img_path('per.png')
        self.driver.find_element(By.CSS_SELECTOR, uploader.up).send_keys(img_path)  # Subir la imagen
         #time.sleep(1)

        # Ingresar la dirección
        self.wait.until(EC.visibility_of_element_located((By.ID, self.__address))).send_keys(random_current_address)
         #time.sleep(1)


        """   # Seleccionar el estado
        self.wait.until(EC.element_to_be_clickable((By.ID, 'react-select-3-input'))).send_keys(random_state)
        time.sleep(3)  # Esperar 1 segundo

        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{random_state}']"))).click()
        time.sleep(2)

        # Seleccionar la ciudad
        self.wait.until(EC.element_to_be_clickable((By.ID, 'react-select-4-input'))).send_keys(random_city)
        time.sleep(1)
        
        self.wait.until(EC.element_to_be_clickable((By.XPATH, f"//div[text()='{random_city}']"))).click()
        time.sleep(1) """
       

        # Enviar el formulario
        self.wait.until(EC.element_to_be_clickable((By.ID, self.__send))).click()
        time.sleep(1)

        self.driver.back()

    def start_home_page(self):
        self.click_forms()
        self.click_practice()
        self.fill_form()
        time.sleep(2)
        return New_users(driver=self.driver)