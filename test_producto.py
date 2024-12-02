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
    def test_registrar_Producto(self):
        # Iniciar sesión
        self.driver.find_element(By.XPATH, "//input[@id='usuario']").send_keys("admin")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='clave']").send_keys("admin")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block']").click()
        time.sleep(3)
        # Navegar a la sección de Productos
        self.driver.find_element(By.XPATH, "//strong[text()=' PRODUCTOS ']").click()
        time.sleep(2)
        # Abrir el modulo para registrar un nuevo Producto
        self.driver.find_element(By.XPATH, "//button[@data-target='#nuevo_producto']").click()
        time.sleep(2)
        # Llenar el formulario de registro de Producto
        self.driver.find_element(By.XPATH, "//input[@id='codigo']").send_keys("68554")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@id='nombre_producto']").send_keys("Pastel de 3 leches")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@id='cantidad']").send_keys("5")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@id='Precio']").send_keys("50.00")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@id='Descripcion']").send_keys("Torta elaborada de 3 tipos de leche")
        time.sleep(0.5)
        # Registrar el Producto
        self.driver.find_element(By.XPATH, "(//button[@class='btn btn-primary'])[7]").click()
        time.sleep(4)
        # Salir del sistema
        self.driver.find_element(By.XPATH, "//button[text()='Salir']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[text()='Si']").click()
        time.sleep(3)
