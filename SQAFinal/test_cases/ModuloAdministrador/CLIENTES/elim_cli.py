"""
Antes de ejecutar el test, ejecutar los siguientes comandos para instalar las librerias necesarias

pip install selenium webdriver-manager

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestEliminarCliente:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://vicent42.com/sistemas/ProyectoRM2/')
        time.sleep(5)

    def teardown_method(self):
        self.driver.quit()
        time.sleep(5)
        print("Prueba visual completada")

    def test_eliminar_cliente(self):
        # Iniciar sesión
        self.driver.find_element(By.XPATH, "//input[@id='usuario']").send_keys("admin")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='clave']").send_keys("admin")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block']").click()
        time.sleep(3)


        self.driver.find_element(By.XPATH, "//strong[text()=' CLIENTES ']").click()
        time.sleep(2)


        self.driver.find_element(By.XPATH, "(//button[@class='btn btn-danger'])[8]").click()
        time.sleep(2)

  
        self.driver.find_element(By.XPATH, "//button[text()='Si!']").click()
        time.sleep(3)

        try:
            self.driver.find_element(By.XPATH, "//td[text()='30']")
            print("El cliente no se eliminó correctamente.")
        except:
            print("El cliente fue eliminado correctamente.")

 
        self.driver.find_element(By.XPATH, "//button[text()='Salir']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[text()='Si']").click()
        time.sleep(3)
