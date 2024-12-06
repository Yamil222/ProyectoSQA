"""
Antes de ejecutar el test, ejecutar los siguientes comandos para instalar las librerías necesarias:

pip install selenium webdriver-manager
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestVentas:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://vicent42.com/sistemas/ProyectoRM2/')
        time.sleep(2)

    def teardown_method(self):
        self.driver.quit()
        print("Prueba de ventas completada")

    def test_crear_venta(self):
        # Iniciar sesión
        self.driver.find_element(By.ID, "usuario").send_keys("admin")
        self.driver.find_element(By.ID, "clave").send_keys("admin")
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block']").click()
        time.sleep(2) 
        self.driver.find_element(By.XPATH, "//strong[text()=' VENTAS ']").click()
        time.sleep(2)
    # Navegar a la sección de "Nueva Venta"
        self.driver.find_element(By.XPATH, "//a[contains(text(),'NUEVA VENTA')]").click()
        time.sleep(2)
        
        # Seleccionar un producto
        self.driver.find_element(By.XPATH, "//input[@onkeyup='filtrarProductos(this.value)']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[contains(@id, 'btnSeleccionar_111116')]").click()  # Cambiar ID según el producto deseado
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[text()='×']").click()
        time.sleep(2)
        
        # Agregar cliente
        self.driver.find_element(By.XPATH, "//input[@id='nombre_cliente']").send_keys("Angel Sifuentes")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//button[text()='Asignar']").click()
        time.sleep(2) 
        # Procesar venta
        self.driver.find_element(By.XPATH, "//button[@id='procesarVenta']").click()
        time.sleep(2) 
        self.driver.find_element(By.XPATH, "//strong[text()=' VENTAS ']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[contains(text(),' VENTAS')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//select//option[text()='100']").click()
        time.sleep(3)
        print("Validando que la venta se haya registrado correctamente") 
        actual_nombre = self.driver.find_element(By.XPATH, "//td[text()='Angel Sifuentes']").text
        esperado_nombre = "Angel Sifuentes"
        
        actual_precio = self.driver.find_element(By.XPATH, "//td[text()='Angel Sifuentes']//following-sibling::td[text()='12.00']").text
        esperado_precio = "12.00"
        
     
        print(f"- NOMBRE ACTUAL = {actual_nombre}, - NOMBRE ESPERADO = {esperado_nombre}")
        print(f"- PRECIO ACTUAL = {actual_precio}, - PRECIO ESPERADO = {esperado_precio}")
        
       
        assert actual_nombre == esperado_nombre, f"El nombre no coincide. ESPERADO: {esperado_nombre}, ACTUAL: {actual_nombre}"
        assert actual_precio == esperado_precio, f"El precio no coincide. ESPERADO: {esperado_precio}, ACTUAL: {actual_precio}"
        
    def test_filtrar_venta_por_fecha(self):
     # Iniciar sesión
     self.driver.find_element(By.ID, "usuario").send_keys("admin")
     self.driver.find_element(By.ID, "clave").send_keys("admin")
     self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block']").click()
     time.sleep(2)

     # Navegar a la sección de Ventas
     self.driver.find_element(By.XPATH, "//strong[text()=' VENTAS ']").click()
     time.sleep(2)
     self.driver.find_element(By.XPATH, "//a[contains(text(),' VENTAS')]").click()
     time.sleep(2)

     # Filtrar por fecha

     self.driver.find_element(By.XPATH, "//input[@type='search']").send_keys("12.00")
     time.sleep(3)


     actual = self.driver.find_element(By.XPATH, "//td[text()='Angel Sifuentes']//following-sibling::td[text()='12.00']").text
     esperado = "12.00"
     print(f"- VALOR ACTUAL  = {actual}, - VALOR ESPERADO = {esperado}")
     assert actual == esperado, f"Los valores no coinciden.  ESPERADA: {esperado}, ACTUAL: {actual}"


