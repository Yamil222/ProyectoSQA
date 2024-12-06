
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

    def test_login_exitoso(self):
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

    def test_login_fallido(self):
        # Llenar campos con credenciales incorrectas
        self.driver.find_element(By.ID, "usuario").send_keys("usuario_invalido")
        time.sleep(1)
        self.driver.find_element(By.ID, "clave").send_keys("clave_invalida")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block']").click()
        time.sleep(3)

        # Validar mensaje de error
        actual = self.driver.find_element(By.XPATH, "//div[contains(@class, 'alert-danger')]").text
        esperado = "Usuario o contraseña Incorrecta"
        print(f"- VALOR ACTUAL = {actual}, - VALOR ESPERADO = {esperado}")
        assert esperado in actual, f"El mensaje no coincide. ESPERADO: {esperado}, ACTUAL: {actual}"
        
    def test_cerrar_sesion(self):
        # Iniciar sesión primero
        self.driver.find_element(By.XPATH, "//input[@id='usuario']").send_keys("admin")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='clave']").send_keys("admin")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block']").click()
        time.sleep(3)
    
        # Cerrar sesión
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-danger']").click()  # Botón "Salir"
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[text()='Si']").click()  
        time.sleep(2)
        # Validar que el formulario de login sea visible nuevamente
        actual = self.driver.find_element(By.XPATH, "//strong[text()='Iniciar Sesión']").text
        esperado = "Iniciar Sesión"
        print(f"- VALOR ACTUAL = {actual}, - VALOR ESPERADO = {esperado}")
        assert actual == esperado, f"Los valores no coinciden. ESPERADO: {esperado}, ACTUAL: {actual}"
    
