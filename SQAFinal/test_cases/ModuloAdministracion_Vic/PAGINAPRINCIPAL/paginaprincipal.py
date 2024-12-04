from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestFooter:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://vicent42.com/sistemas/ProyectoRM2/Views/index.php')
        time.sleep(3)

    def teardown_method(self):
        self.driver.quit()
        print("Prueba del footer completada")

    def test_productos(self):
      self.driver.find_element(By.XPATH, "(//button[text()='Detalles'])[1]").click()
      time.sleep(4)
      self.driver.find_element(By.XPATH, "(//button[text()='Cerrar'])[1]").click()
      time.sleep(2)
     

      actual = self.driver.find_element(By.XPATH, "(//h4[text()='Torta Chocolate'])[2]").text
      esperado = "Torta Chocolate"
      print("-VALOR ACTUAL=", actual, "-VALOR ESPERADO=", esperado)
      assert esperado == actual, f"LOS VALORES NO COINCIDEN ESPERADO:'{esperado}' ACTUAL:'{actual}'"
    
    
    def test_incio_login(self):
      
      self.driver.find_element(By.XPATH, "//a[text()='INICIO']").click()
      time.sleep(4)
      self.driver.find_element(By.XPATH, "//a[text()='POSTRES']").click()
      time.sleep(2)
      self.driver.find_element(By.XPATH, "//a[text()='TORTAS']").click()
      time.sleep(2)
      self.driver.find_element(By.XPATH, "//a[text()='CONTACTO']").click()
      time.sleep(2)
      self.driver.find_element(By.XPATH, "//a[text()='INICIO DE SESION']").click()
      time.sleep(4)
      
      actual = self.driver.find_element(By.XPATH, "//strong[text()='Iniciar Sesión']").text
      esperado = "Iniciar Sesión"
      print("-VALOR ACTUAL=", actual, "-VALOR ESPERADO=", esperado)
      assert esperado == actual, f"LOS VALORES NO COINCIDEN ESPERADO:'{esperado}' ACTUAL:'{actual}'"
    
    def test_footer(self):
      self.driver.find_element(By.XPATH, "//a[text()='CONTACTO']").click()
      time.sleep(3)
   
      
      actual = self.driver.find_element(By.XPATH, "//label[text()='WhatsApp']").text
      esperado = "WhatsApp"
      print("-VALOR ACTUAL=", actual, "-VALOR ESPERADO=", esperado)
      assert esperado == actual, f"LOS VALORES NO COINCIDEN ESPERADO:'{esperado}' ACTUAL:'{actual}'"
    