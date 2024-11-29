"""
Antes de ejecutar el test, ejecutar el siguiente comando para instalar la libreria necesaria

pip install selenium webdriver-manager
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time 

# Configuración automática del WebDriver
driver = webdriver.Chrome()

# Maximizar la ventana del navegador
driver.maximize_window()

# Abrir url en el navegador
driver.get('https://vicent42.com/sistemas/ProyectoRM2/')



def abrir_formulario_editar_usuario(driver):
    """Abre el formulario para registrar un nuevo usuario."""
    driver.find_element(By.XPATH, "//button[@text()='Editar']").click()
    time.sleep(2)

def rellenar_formulario_usuario(driver, nombre, usuario, correo, clave, rol, estado, sucursal):
    """Rellena el formulario con los datos del nuevo usuario."""
    driver.find_element(By.XPATH, "//input[@id='nombre_insertar']").send_keys(nombre)
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//input[@id='usuario_insertar']").send_keys(usuario)
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//input[@id='correo_insertar']").send_keys(correo)
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//input[@id='clave']").send_keys(clave)
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//input[@id='confirmar']").send_keys(clave)
    time.sleep(0.5)
    driver.find_element(By.XPATH, "//select[@id='rol']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, f"//option[@value='{rol}']").click()
    time.sleep(2)
    driver.find_element(By.XPATH, "(//select[@id='estado']//option)[1]").click()
    time.sleep(2)
    driver.find_element(By.XPATH, f"((//select[@id='id_sucursal'])[7]//option)[{sucursal}]").click()
    time.sleep(2)

def registrar_usuario(driver):
    """Registra al nuevo usuario."""
    driver.find_element(By.XPATH, "//button[text()='Registrar']").click()
    time.sleep(4)

def cerrar_sesion(driver):
    """Cierra la sesión del usuario."""
    driver.find_element(By.XPATH, "//button[text()='Salir']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//a[text()='Si']").click()
    time.sleep(3)
    
    
    
    def prueba_visual():
     """Ejecuta la prueba visual desde el inicio de sesión."""
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    try:
     
        def abrir_formulario_editar_usuario(driver)
        rellenar_formulario_usuario(driver, "Cristiano", "CR7", "CR7@gmail.com", "cristiano", "Administrador", "Activo", 5)
        registrar_usuario(driver)
        cerrar_sesion(driver)
        print("Prueba visual completada")
    finally:
        driver.quit()

# Ejecutar la prueba
    prueba_visual()
    