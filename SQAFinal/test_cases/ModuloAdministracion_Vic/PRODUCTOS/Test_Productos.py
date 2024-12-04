from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestProducto:
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
        # Navegar a la sección de Productos
        self.driver.find_element(By.XPATH, "//strong[text()=' PRODUCTOS ']").click()
        time.sleep(2)
        # Abrir el modulo para registrar un nuevo Producto
        self.driver.find_element(By.XPATH, "//button[@data-target='#nuevo_producto']").click()
        time.sleep(2)
        # Llenar el formulario de registro de Producto
        self.driver.find_element(By.XPATH, "//input[@id='codigo']").send_keys("68554")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@id='nombre_insertar']").send_keys("Pastel de 3 leches")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@id='cantidad']").send_keys("5")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@id='Precio']").send_keys("50.00")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@id='descripcion_insertar']").send_keys("Torta elaborada de 3 tipos de leche")
        time.sleep(0.5)
        # Registrar el Producto
        self.driver.find_element(By.XPATH, "(//button[@class='btn btn-primary'])[7]").click()
        time.sleep(4)
        actual = self.driver.find_element(By.XPATH, "//tbody//tr//td[text()='68554']").text
        esperado = "68554"
        print("-VALOR ACTUAL=", actual,"-VALOR ESPERADO=",esperado)
        assert esperado == actual, f"LOS VALORES NO COINCIDEN ESPERADO:'{esperado}' ACTUAL:'{actual}'"

    def test_modificar_Producto(self):
        self.driver.find_element(By.XPATH, "//input[@id='usuario']").send_keys("admin")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='clave']").send_keys("admin")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block']").click()
        time.sleep(3)     
        self.driver.find_element(By.XPATH, "//strong[text()=' PRODUCTOS ']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[@data-target='##editar_producto_6']").click()
        time.sleep(2)


        self.driver.find_element(By.XPATH, "//input[@id='codigo']").clear()
        ###
        self.driver.find_element(By.XPATH, "//input[@id='codigo']").send_keys("110011")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@id='nombre_editar_6']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='nombre_editar_6']").send_keys("Torta de Limon")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@id='cantidad']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='cantidad']").send_keys("25")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@id='precio']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='precio']").send_keys("10.00")
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@id='descripcion_editar_6']").clear()
        self.driver.find_element(By.XPATH, "//input[@id='descripcion_editar_6']").send_keys("Deliciosa torta de limon con crema vegetal") 
        time.sleep(0.5)
        self.driver.find_element(By.XPATH, "//input[@id='nombre_editar_6']//parent::div//parent::div//following-sibling::div//button[@class='btn primarybtn-']").click()
        time.sleep(3)
        actual = self.driver.find_element(By.XPATH, "//tbody//tr//td[text()='110011']").text
        esperado = "110011"
        print("-VALOR ACTUAL=", actual,"-VALOR ESPERADO=",esperado)
        assert esperado == actual, f"LOS VALORES NO COINCIDEN ESPERADO:'{esperado}' ACTUAL:'{actual}'"

    def test_eliminar_Producto(self):

        self.driver.find_element(By.XPATH, "//input[@id='usuario']").send_keys("admin")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='clave']").send_keys("admin")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block']").click()
        time.sleep(3) 
        self.driver.find_element(By.XPATH, "//strong[text()=' PRODUCTOS ']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//td[text()='111116']//following::td//button[@class='btn btn-danger']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//button[text()='Si!']").click()
        time.sleep(3)

        try:
         actual = self.driver.find_element(By.XPATH, "//tbody//tr//td[text()='111116']").text
        except:
         actual = None
        esperado = None
        print("-VALOR ACTUAL=", actual, "-VALOR ESPERADO=", esperado)
        assert esperado == actual, f"LOS VALORES NO COINCIDEN ESPERADO:'{esperado}' ACTUAL:'{actual}'"

    def test_buscar_Producto(self):
        self.driver.find_element(By.XPATH, "//input[@id='usuario']").send_keys("admin")
        time.sleep(1)
        self.driver.find_element(By.XPATH, "//input[@id='clave']").send_keys("admin")
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//strong[text()=' PRODUCTOS ']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@type='search']").send_keys("11111")
        time.sleep(2)
    
        actual = self.driver.find_element(By.XPATH, "//tbody//tr//td[text()='11111']").text
        esperado = "11111"
        print("-VALOR ACTUAL=", actual, "-VALOR ESPERADO=", esperado)
        assert esperado == actual, f"LOS VALORES NO COINCIDEN ESPERADO:'{esperado}' ACTUAL:'{actual}'"

    
        # Salir del sistema
        self.driver.find_element(By.XPATH, "//button[text()='Salir']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//a[text()='Si']").click()
        time.sleep(3)