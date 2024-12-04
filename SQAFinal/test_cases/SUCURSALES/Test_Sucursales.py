from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestSucursales:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('https://vicent42.com/sistemas/ProyectoRM2/')
        time.sleep(5)
    def teardown_method(self):
        self.driver.quit()
        time.sleep(5)
        print("Prueba visual completada")
    def test_registrar_Sucursal(self):
        # Iniciar sesión
        self.driver.find_element(By.XPATH, "//input[@id='usuario']").send_keys("admin")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='clave']").send_keys("admin")
        time.sleep(3)
        # Navegar a la sección de Sucursales
        self.driver.find_element(By.XPATH, "//strong[text()=' SUCURSALES']").click()
        time.sleep(2)
        # Abrir el modulo para registrar una nueva Sucursal
        self.driver.find_element(By.XPATH, "//button[@data-target='#nueva_sucursal']").click()
        time.sleep(2)
        # Llenar el formulario de registro de sucursales
        self.driver.find_element(By.XPATH, "//small[@id='charCountNombreInsertar']").send_keys("Hola Hola")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//small[@id='charCountUbicacionInsertar']").send_keys("Ceja calle 1")
        time.sleep(0.5)
        # Registrar la Sucursal
        self.driver.find_element(By.XPATH, "(//button[@class='btn btn-primary'])").click()
        time.sleep(4)

    def test_modificar_Sucursal(self):
        self.driver.find_element(By.XPATH, "//input[@id='usuario']").send_keys("admin")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='clave']").send_keys("admin")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block']").click()
        time.sleep(3)     
        self.driver.find_element(By.XPATH, "//strong[text()=' SUCURSALES']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@data-target='#editar_sucursal_1']").click()
        time.sleep(2)

        self.driver.find_element(By.XPATH, "//small[@id='charCountNombreEditar_1']").clear()
        self.driver.find_element(By.XPATH, "//small[@id='charCountNombreEditar_1']").send_keys("Buenos aires")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//small[@id='charCountUbicacionEditar_1']").clear()
        self.driver.find_element(By.XPATH, "//small[@id='charCountUbicacionEditar_1']").send_keys("Calacoto")
        time.sleep(0.5)

        #Guardar

        actual = self.driver.find_element(By.XPATH, "//tbody//tr//td[text()='Buenos airess']").text
        esperado = "Buenos aires"
        print("-VALOR ACTUAL=", actual,"-VALOR ESPERADO=",esperado)
        assert esperado == actual, f"LOS VALORES NO COINCIDEN ESPERADO:'{esperado}' ACTUAL:'{actual}'"

    def test_eliminar_Producto(self):

        self.driver.find_element(By.XPATH, "//input[@id='usuario']").send_keys("admin")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='clave']").send_keys("admin")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block']").click()
        time.sleep(3) 
        self.driver.find_element(By.XPATH, "//strong[text()=' SUCURSALES']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//td[text()='1']//following::td//button[@class='btn btn-danger']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[text()='Si!']").click()
        time.sleep(3)

        try:
         actual = self.driver.find_element(By.XPATH, "//tbody//tr//td[text()='1']").text
        except:
         actual = None
        esperado = None
        print("-VALOR ACTUAL=", actual, "-VALOR ESPERADO=", esperado)
        assert esperado == actual, f"LOS VALORES NO COINCIDEN ESPERADO:'{esperado}' ACTUAL:'{actual}'"

    def test_buscar_Sucursal(self):
        self.driver.find_element(By.XPATH, "//input[@id='usuario']").send_keys("admin")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='clave']").send_keys("admin")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//strong[text()=' SUCURSALES']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@type='search']").send_keys("2")
        time.sleep(2)
        actual = self.driver.find_element(By.XPATH, "//tbody//tr//td[text()='2']").text
        esperado = "2"
        print("-VALOR ACTUAL=", actual, "-VALOR ESPERADO=", esperado)
        assert esperado == actual, f"LOS VALORES NO COINCIDEN ESPERADO:'{esperado}' ACTUAL:'{actual}'"

        # Salir del sistema
        self.driver.find_element(By.XPATH, "//button[text()='Salir']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[text()='Si']").click()
        time.sleep(3)