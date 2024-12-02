"""
Antes de ejecutar el test, ejecutar los siguientes comandos para instalar las librerias necesarias

pip install selenium webdriver-manager

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestCliente:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://vicent42.com/sistemas/ProyectoRM2/')
        time.sleep(5)

    def teardown_method(self):
        self.driver.quit()
        time.sleep(5)
        print("Prueba visual completada")

    def test_registrar_cliente(self):
        # Iniciar sesión
        self.driver.find_element(By.XPATH, "//input[@id='usuario']").send_keys("admin")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='clave']").send_keys("admin")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block']").click()
        time.sleep(3)

        # Navegar a la sección de clientes
        self.driver.find_element(By.XPATH, "//strong[text()=' CLIENTES ']").click()
        time.sleep(2)

        # Abrir el modal para registrar un nuevo cliente
        self.driver.find_element(By.XPATH, "//button[@data-target='#nuevo_cliente']").click()
        time.sleep(2)

        # Llenar el formulario de registro de cliente
 
        self.driver.find_element(By.XPATH, "//input[@id='ruc_insertar']").send_keys("1287345678")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@id='nombre_insertar']").send_keys("Carlos Perez")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@id='direccion_insertar']").send_keys("calle colorado")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@id='telefono']").send_keys("23453899")
        time.sleep(0.5)
    

        # Registrar el cliente
        self.driver.find_element(By.XPATH, "(//button[@class='btn btn-primary'])[7]").click()
        time.sleep(4)

        # Salir del sistema
        self.driver.find_element(By.XPATH, "//button[text()='Salir']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[text()='Si']").click()
        time.sleep(3)