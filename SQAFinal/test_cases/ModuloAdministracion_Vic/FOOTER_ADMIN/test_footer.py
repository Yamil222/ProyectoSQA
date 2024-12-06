
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class Testfooter:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://vicent42.com/sistemas/ProyectoRM2/')
        time.sleep(3)

    def teardown_method(self):
        self.driver.quit()
        print("Prueba de login completada")

    def test_login(self):
        # Llenar campos de usuario y contraseña
        self.driver.find_element(By.ID, "usuario").send_keys("admin")
        time.sleep(1)
        self.driver.find_element(By.ID, "clave").send_keys("admin")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block']").click()
        time.sleep(3)

        # Validar que se haya iniciado sesión correctamente
        actual = self.driver.find_element(By.XPATH, "//div[text()='2024 © PASTELERIA ']").text 
        esperado = "2024 © PASTELERIA ZAZA."
        print(f"- VALOR ACTUAL = {actual}, - VALOR ESPERADO = {esperado}")
        assert actual == esperado, f"Los valores no coinciden. ESPERADO: {esperado}, ACTUAL: {actual}"
        
        actual1 = self.driver.find_element(By.XPATH, "//a[text()='ZAZA']").text 
        esperado1 = "ZAZA"
        print(f"- VALOR ACTUAL = {actual1}, - VALOR ESPERADO = {esperado1}")
        assert actual1 == esperado1, f"Los valores no coinciden. ESPERADO: {esperado1}, ACTUAL: {actual1}"

       
    