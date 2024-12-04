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
        print("")
        print("Prueba  completada")

    def test_registrar_cliente(self):

        self.driver.find_element(By.XPATH, "//input[@id='usuario']").send_keys("admin")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='clave']").send_keys("admin")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block']").click()
        time.sleep(3)

      
        self.driver.find_element(By.XPATH, "//strong[text()=' CLIENTES ']").click()
        time.sleep(2)

  
        self.driver.find_element(By.XPATH, "//button[@data-target='#nuevo_cliente']").click()
        time.sleep(2)

      
        print("Llenar el formulario de registro")
        ###
        self.driver.find_element(By.XPATH, "//input[@id='ruc_insertar']").send_keys("1233456")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@id='nombre_insertar']").send_keys("pruebas")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@id='direccion_insertar']").send_keys("calle colorado")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@id='telefono']").send_keys("23453899")
        time.sleep(0.5)
    

        # Registrar el cliente
        print("registro")
        self.driver.find_element(By.XPATH, "//button[text()='Registrar']").click()
        time.sleep(4)
        ###
        actual = self.driver.find_element(By.XPATH, "//tbody//tr//td[text()='1233456']").text
        ###
        esperado = "1233456"
        print("-VALOR ACTUAL=", actual,"-VALOR ESPERADO=",esperado)
        assert esperado == actual, f"LOS VALORES NO COINCIDEN ESPERADO:'{esperado}' ACTUAL:'{actual}'"

    #id 5
    def test_modificar_cliente(self):
     
        self.driver.find_element(By.XPATH, "//input[@id='usuario']").send_keys("admin")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='clave']").send_keys("admin")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block']").click()
        time.sleep(3)

     
        self.driver.find_element(By.XPATH, "//strong[text()=' CLIENTES ']").click()
        time.sleep(2)


        self.driver.find_element(By.XPATH, "//button[@data-target='#editar_cliente_5']").click()
        time.sleep(2)


        self.driver.find_element(By.XPATH, "//input[@id='ruc_edit_5']").clear()
        ###
        self.driver.find_element(By.XPATH, "//input[@id='ruc_edit_5']").send_keys("8877665")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@id='nombre_edit_5']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='nombre_edit_5']").send_keys("Carlos Gomez")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@id='direccion_edit_5']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='direccion_edit_5']").send_keys("Calle Principal 123")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@id='telefono_edit_5']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='telefono_edit_5']").send_keys("98765432")
        time.sleep(0.5)


        self.driver.find_element(By.XPATH, "//input[@id='ruc_edit_5']//parent::div//parent::div//following-sibling::div//button[@class='btn btn-primary']").click()
        time.sleep(4)

        ###
        actual = self.driver.find_element(By.XPATH, "//tbody//tr//td[text()='8877665']").text
        ###
        esperado = "8877665"
        print("-VALOR ACTUAL=", actual,"-VALOR ESPERADO=",esperado)
        assert esperado == actual, f"LOS VALORES NO COINCIDEN ESPERADO:'{esperado}' ACTUAL:'{actual}'"


    def test_eliminar_cliente(self):
     
        self.driver.find_element(By.XPATH, "//input[@id='usuario']").send_keys("admin")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='clave']").send_keys("admin")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block']").click()
        time.sleep(3)


        self.driver.find_element(By.XPATH, "//strong[text()=' CLIENTES ']").click()
        time.sleep(2)


        self.driver.find_element(By.XPATH, "//td[text()='1233456']//following::td//button[@class='btn btn-danger']").click()
        time.sleep(2)

  
        self.driver.find_element(By.XPATH, "//button[text()='Si!']").click()
        time.sleep(3)

        try:
         actual = self.driver.find_element(By.XPATH, "//tbody//tr//td[text()='1233456']").text
        except:
         actual = None  # Si el elemento no existe, el valor será None
        
        esperado = None  # Esperamos que no exista
        print("-VALOR ACTUAL=", actual, "-VALOR ESPERADO=", esperado)
        assert esperado == actual, f"LOS VALORES NO COINCIDEN ESPERADO:'{esperado}' ACTUAL:'{actual}'"


    def test_buscar_cliente(self):

        self.driver.find_element(By.XPATH, "//input[@id='usuario']").send_keys("admin")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='clave']").send_keys("admin")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block']").click()
        time.sleep(3)
    
 
        self.driver.find_element(By.XPATH, "//strong[text()=' CLIENTES ']").click()
        time.sleep(2)
    
    
        self.driver.find_element(By.XPATH, "//input[@type='search']").send_keys("8877665")
        time.sleep(2)
    
     
        actual = self.driver.find_element(By.XPATH, "//tbody//tr//td[text()='8877665']").text
        esperado = "8877665"
        print("-VALOR ACTUAL=", actual, "-VALOR ESPERADO=", esperado)
        assert esperado == actual, f"LOS VALORES NO COINCIDEN ESPERADO:'{esperado}' ACTUAL:'{actual}'"
    
        # Salir del sistema
        #self.driver.find_element(By.XPATH, "//button[text()='Salir']").click()
        #time.sleep(3)
        #self.driver.find_element(By.XPATH, "//a[text()='Si']").click()
        #time.sleep(3)
    
        
        
        