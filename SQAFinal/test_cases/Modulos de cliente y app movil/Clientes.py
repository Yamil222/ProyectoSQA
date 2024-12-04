from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestCliente:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://vicent42.com/sistemas/ProyectoRM2/Views/") 
        time.sleep(2)
    def test_iniciar_sesion(self):  
        self.driver.get("https://vicent42.com/sistemas/ProyectoRM2/") 
        time.sleep(2)
        self.driver.find_element(By.ID, "usuario").send_keys("admin")  
        time.sleep(2)
        self.driver.find_element(By.ID, "clave").send_keys("admin")  
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[text()='Iniciar']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//a[@href='https://vicent42.com/sistemas/ProyectoRM2/Clientes/Listar']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@data-target='#nuevo_cliente']").click()
        time.sleep(2) 
        self.driver.find_element(By.XPATH, "//input[@id='ruc_insertar']").send_keys("12787")
        time.sleep(2) 
        self.driver.find_element(By.XPATH, "//input[@placeholder='Nombre']").send_keys("Robertoooo to to to")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Dirección']").send_keys("Calle Colon")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@placeholder='Teléfono']").send_keys("78945619")     
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary' and @type='submit']").click()
        time.sleep(2)
    #def test_verify_name(self):
        #esperado = "Robertoooo to to to"
        #actual = self.driver.find_element(By.XPATH, "//td[contains(text(), 'Robertoooo to to to')]").text
        #assert esperado == actual, f"FAIL: Esperado: {esperado}, Actual: {actual}"
        #print(f"Verificación de Nombre exitosa. Nombre: {actual}")

    #def test_verify_address(self):
        #esperado = "Calle Colon"
        #actual = self.driver.find_element(By.XPATH, "//td[contains(text(), 'Calle Colon')]").text
        #assert esperado == actual, f"FAIL: Esperado: {esperado}, Actual: {actual}"
        #print(f"Verificación de Dirección exitosa. Dirección: {actual}")
    #def teardown_method(self):
        self.driver.quit()
        print("Prueba finalizada")
if __name__ == "__main__":
    test = TestCliente()
    test.setup_method()
    try:
        test.test_iniciar_sesion()
        #test.test_verify_name()  
        #test.test_verify_address()  
    finally:
        test.teardown_method()