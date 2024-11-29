from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestFormulario:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://vicent42.com/sistemas/ProyectoRM2/") 
        time.sleep(2)
    def test_iniciar_sesion(self):  
        self.driver.find_element(By.ID, "usuario").send_keys("admin")  
        self.driver.find_element(By.ID, "clave").send_keys("admin")  
        self.driver.find_element(By.XPATH, "//button[text()='Iniciar']").click()
        time.sleep(3)
    def test_ingreso_nuevo_cliente(self):
        self.driver.get("https://vicent42.com/sistemas/ProyectoRM2/Clientes/Nuevo")  
        time.sleep(2)  
        self.driver.find_element(By.XPATH, "//input[@placeholder='Ruc/Dni']").send_keys("12345678901")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Nombre']").send_keys("Juan")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Dirección']").send_keys("Calle Colon 123")
        self.driver.find_element(By.XPATH, "//input[@placeholder='Teléfono']").send_keys("789456123")     
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Guardar')]").click()
        time.sleep(3)
    def teardown_method(self):
        self.driver.quit()
        print("Prueba finalizada")
if __name__ == "__main__":
    test = TestFormulario()
    test.setup_method()
    try:
        test.test_iniciar_sesion()
        test.test_ingreso_nuevo_cliente()
    finally:
        test.teardown_method()
