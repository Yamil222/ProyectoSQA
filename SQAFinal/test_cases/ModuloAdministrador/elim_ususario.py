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

def abrir_lista_usuarios(driver):
    """Abre la lista de usuarios donde se encuentran los botones de eliminación."""
    driver.find_element(By.XPATH, "//button[@text()='Lista de Usuarios']").click()
    time.sleep(2)

def eliminar_usuario(driver, usuario):
  
    
    driver.find_element(By.XPATH, f"//tr[td[text()='{usuario}']]//button[text()='Eliminar']").click()
    time.sleep(1)

  
    driver.find_element(By.XPATH, "//a[text()='Si']").click()
    time.sleep(3)

def cerrar_sesion(driver):
    """Cierra la sesión del usuario."""
    driver.find_element(By.XPATH, "//button[text()='Salir']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//a[text()='Si']").click()
    time.sleep(3)

def prueba_visual():
   
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    try:
       
        abrir_lista_usuarios(driver)
       
        eliminar_usuario(driver, "CR7")
        
       
        cerrar_sesion(driver)
        print("Prueba visual completada")
    finally:
        driver.quit()

# Ejecutar la prueba
prueba_visual()
