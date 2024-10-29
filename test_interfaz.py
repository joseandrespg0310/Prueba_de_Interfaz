"""
Antes de ejecutar el test, ejecutar el siguiente comando para instalar la libreria necesaria

pip install selenium webdriver-manager
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestSIU:
    def setup_method(self):
        self.driver=webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://enlace.univalle.edu/san/webform/PAutenticar.aspx')
        time.sleep(1)
    def teardown_method(self):
        self.driver.quit()
        print("Prueba de interfaz finalizada")
    def test_verify_frgt_password_txt(self):
        actual=self.driver.find_element(By.XPATH,"//input[contains(@id, 'Recupera')]").get_attribute("valor")
        esperado="¿Haz olvidado tu USUARIO?"
        print(actual)
        time.sleep(1)
        assert actual==esperado, f"FALLO:actual:{actual},esperado:{esperado}"
        
    def test_verify_wrong_password_txt(self):
        actual=self.driver.find_element(By.XPATH,"//input[contains(@id, 'Recupera')]").get_attribute("valor")
        esperado="¿Haz olvidado tu USUARIO?"
        print(actual)
        time.sleep(1)
        assert actual==esperado, f"FALLO:actual:{actual},esperado:{esperado}"     
        
