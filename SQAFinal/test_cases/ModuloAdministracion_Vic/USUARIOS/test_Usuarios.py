"""
Antes de ejecutar el test, ejecutar los siguientes comandos para instalar las librerias necesarias

pip install selenium webdriver-manager

"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestUsuario:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://vicent42.com/sistemas/ProyectoRM2/')
        time.sleep(5)

    def teardown_method(self):
        self.driver.quit()
        time.sleep(5)
        print("")
        print("Prueba completada")

    def test_registrar_usuario(self):
        # Iniciar sesión
        self.driver.find_element(By.XPATH, "//input[@id='usuario']").send_keys("admin")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='clave']").send_keys("admin")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block']").click()
        time.sleep(3)

        # Navegar a la sección de usuarios
        self.driver.find_element(By.XPATH, "//strong[text()=' USUARIOS ']").click()
        time.sleep(2)

        # Abrir el modal para registrar un nuevo usuario
        self.driver.find_element(By.XPATH, "//button[@data-target='#nuevo_usuario']").click()
        time.sleep(2)

        # Llenar el formulario de registro de usuario
        print("Llenar el formulario de registro")
        self.driver.find_element(By.XPATH, "//input[@id='nombre_insertar']").send_keys("Juan Perez")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@id='usuario_insertar']").send_keys("jperez")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@id='correo_insertar']").send_keys("jperez@example.com")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@id='clave']").send_keys("123")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@id='confirmar']").send_keys("123")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//select[@id='rol']//option[text()='Administrador']").click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//select[@id='estado']//option[text()='Activado']").click()
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//form[@action='https://vicent42.com/sistemas/ProyectoRM2/Usuarios/insertar']//select//option[contains(text(), 'Casa matrize')]").click()
        time.sleep(0.5)
        # Registrar el usuario
        print("Registro")
        self.driver.find_element(By.XPATH, "//button[text()='Registrar']").click()
        time.sleep(4)

        # Validar que el usuario fue registrado
        actual = self.driver.find_element(By.XPATH, "//tbody//tr//td[text()='jperez']").text
        esperado = "jperez"
        print("-VALOR ACTUAL=", actual, "-VALOR ESPERADO=", esperado)
        assert esperado == actual, f"LOS VALORES NO COINCIDEN ESPERADO:'{esperado}' ACTUAL:'{actual}'"
   
    def test_modificar_usuario(self):
      # Iniciar sesión
      self.driver.find_element(By.XPATH, "//input[@id='usuario']").send_keys("admin")
      time.sleep(1)
      self.driver.find_element(By.XPATH, "//input[@id='clave']").send_keys("admin")
      time.sleep(3)
      self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block']").click()
      time.sleep(3)
   
      # Navegar a la sección de usuarios
      self.driver.find_element(By.XPATH, "//strong[text()=' USUARIOS ']").click()
      time.sleep(2)
   
      # Abrir el modal para modificar un usuario existente
      self.driver.find_element(By.XPATH, "//button[@data-target='#editar_usuario_5']").click()
      time.sleep(2)
   
      # Llenar el formulario para modificar el usuario
      print("Modificar el formulario de usuario")
      self.driver.find_element(By.XPATH, "//input[@id='nombre_edit_5']").clear()
      self.driver.find_element(By.XPATH, "//input[@id='nombre_edit_5']").send_keys("Pedro Lopez")
      time.sleep(0.5)
      self.driver.find_element(By.XPATH, "//input[@id='usuario_edit_5']").clear()
      self.driver.find_element(By.XPATH, "//input[@id='usuario_edit_5']").send_keys("plopez")
      time.sleep(0.5)
      self.driver.find_element(By.XPATH, "//input[@id='correo_edit_5']").clear()
      self.driver.find_element(By.XPATH, "//input[@id='correo_edit_5']").send_keys("plopez@example.com")
      time.sleep(0.5)
      self.driver.find_element(By.XPATH, "//input[@id='usuario_edit_5']//parent::div//following-sibling::div//select//option[contains(@value, 'Administrador')]").click()
      time.sleep(0.5)
      self.driver.find_element(By.XPATH, "//input[@id='usuario_edit_5']//parent::div//following-sibling::div//select//option[contains(text(), 'Activado')]").click()
      time.sleep(0.5)
      self.driver.find_element(By.XPATH, "//input[@id='usuario_edit_5']//parent::div//following-sibling::div//select//option[contains(text(), 'Casa matrize')]").click()
      time.sleep(0.5)
      # Guardar los cambios
      print("Guardar cambios")
      self.driver.find_element(By.XPATH, "//input[@id='usuario_edit_5']//parent::div//following::div//button[contains(text(), 'Guardar Cambios')]").click()
      time.sleep(4)
   
      # Validar que el usuario fue modificado
      actual = self.driver.find_element(By.XPATH, "//tbody//tr//td[text()='plopez']").text
      esperado = "plopez"
      print("-VALOR ACTUAL=", actual, "-VALOR ESPERADO=", esperado)
      assert esperado == actual, f"LOS VALORES NO COINCIDEN ESPERADO:'{esperado}' ACTUAL:'{actual}'"
    
    
    def test_buscar_usuario(self):
    # Iniciar sesión
     self.driver.find_element(By.XPATH, "//input[@id='usuario']").send_keys("admin")
     time.sleep(1)
     self.driver.find_element(By.XPATH, "//input[@id='clave']").send_keys("admin")
     time.sleep(3)
     self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block']").click()
     time.sleep(3)
 
     # Navegar a la sección de usuarios
     self.driver.find_element(By.XPATH, "//strong[text()=' USUARIOS ']").click()
     time.sleep(2)
 
     # Buscar un usuario
     self.driver.find_element(By.XPATH, "//input[@type='search']").send_keys("plopez")
     time.sleep(2)
 
     # Validar que el usuario aparece en la tabla
     actual = self.driver.find_element(By.XPATH, "//tbody//tr//td[text()='plopez']").text
     esperado = "plopez"
     print("-VALOR ACTUAL=", actual, "-VALOR ESPERADO=", esperado)
     assert esperado == actual, f"LOS VALORES NO COINCIDEN ESPERADO:'{esperado}' ACTUAL:'{actual}'"
 
    
    def test_eliminar_usuario(self):
     # Iniciar sesión
     self.driver.find_element(By.XPATH, "//input[@id='usuario']").send_keys("admin")
     time.sleep(1)
     self.driver.find_element(By.XPATH, "//input[@id='clave']").send_keys("admin")
     time.sleep(3)
     self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block']").click()
     time.sleep(3)
  
     # Navegar a la sección de usuarios
     self.driver.find_element(By.XPATH, "//strong[text()=' USUARIOS ']").click()
     time.sleep(2)
  
     # Eliminar el usuario con usuario 'plopez'
     self.driver.find_element(By.XPATH, "//td[text()='jperez']//following::td//button[@class='btn btn-danger']").click()
     time.sleep(2)
  
     # Confirmar la eliminación
     self.driver.find_element(By.XPATH, "//button[text()='Si!']").click()
     time.sleep(3)
  
    
     actual = self.driver.find_element(By.XPATH, "//td[text()='jperez']//following-sibling::td//div[text()='DESACTIVADO']").text
     esperado = "DESACTIVADO"
     print("-VALOR ACTUAL=", actual, "-VALOR ESPERADO=", esperado)
     assert esperado == actual, f"LOS VALORES NO COINCIDEN ESPERADO:'{esperado}' ACTUAL:'{actual}'"
  