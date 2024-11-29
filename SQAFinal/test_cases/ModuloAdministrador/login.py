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

def iniciar_sesion(driver, usuario, clave):
    """Realiza el inicio de sesión con las credenciales dadas."""
    driver.find_element(By.XPATH, "//input[@id='usuario']").send_keys(usuario)
    time.sleep(1)
    driver.find_element(By.XPATH, "//input[@id='clave']").send_keys(clave)
    time.sleep(3)
    driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-block']").click()
    time.sleep(3)

def navegar_a_modulo_usuarios(driver):
    """Navega al módulo de usuarios."""
    driver.find_element(By.XPATH, "//strong[text()=' USUARIOS ']").click()
    time.sleep(2)



def prueba_visual():
    """Ejecuta la prueba visual desde el inicio de sesión."""
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    try:
        driver.get('https://vicent42.com/sistemas/ProyectoRM2/')
        iniciar_sesion(driver, "admin", "admin")
        navegar_a_modulo_usuarios(driver)
      
        print("Prueba visual completada")
    finally:
        driver.quit()

# Ejecutar la prueba
prueba_visual()