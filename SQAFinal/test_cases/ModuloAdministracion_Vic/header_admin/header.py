
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestLogin:
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
        actual = self.driver.find_element(By.XPATH, "//strong[text()='cr77']").text  # Nombre del usuario
        esperado = "cr77"
        print(f"- VALOR ACTUAL = {actual}, - VALOR ESPERADO = {esperado}")
        assert actual == esperado, f"Los valores no coinciden. ESPERADO: {esperado}, ACTUAL: {actual}"

        actual2 = self.driver.find_element(By.XPATH, "//strong[text()='Casa matrize']").text  # Nombre del usuario
        esperado2 = "Casa matrize"
        print(f"- VALOR ACTUAL = {actual2}, - VALOR ESPERADO = {esperado2}")
        assert actual2 == esperado2, f"Los valores no coinciden. ESPERADO: {esperado2}, ACTUAL: {actual2}"


        actual3= self.driver.find_element(By.XPATH, "//strong[text()='ZAZA, 04-Dec-2024']").text  # Nombre del usuario
        esperado3 = "ZAZA, 04-Dec-2024"
        print(f"- VALOR ACTUAL = {actual3}, - VALOR ESPERADO = {esperado3}")
        assert actual3 == esperado3, f"Los valores no coinciden. ESPERADO: {esperado3}, ACTUAL: {actual3}"