import os
from selenium.webdriver.support.ui import WebDriverWait

class Uploadimg:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.up = "input[type='file']"
        self.img_up = "per.png"

    def get_img_path(self, imgfile):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, "..", "..", "..", "resources", "img", imgfile)
        ##Ruta absulta
        canonical_path = os.path.abspath(file_path)
        return canonical_path

    def upload_img(self):
        #encuentra archivo y sube
        upload_imagen = self.driver.find_element_by_css_selector(self.up)









