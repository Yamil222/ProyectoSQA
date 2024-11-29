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
    """Elimina al usuario indicado por su nombre o identificación."""
    # Buscar el botón de eliminar correspondiente al usuario
    # Aquí se asume que hay un botón "Eliminar" junto a cada usuario listado
    driver.find_element(By.XPATH, f"//tr[td[text()='{usuario}']]//button[text()='Eliminar']").click()
    time.sleep(1)

    # Confirmar la eliminación (si hay una ventana emergente de confirmación)
    driver.find_element(By.XPATH, "//a[text()='Si']").click()
    time.sleep(3)

def cerrar_sesion(driver):
    """Cierra la sesión del usuario."""
    driver.find_element(By.XPATH, "//button[text()='Salir']").click()
    time.sleep(3)
    driver.find_element(By.XPATH, "//a[text()='Si']").click()
    time.sleep(3)

def prueba_visual():
    """Ejecuta la prueba visual para eliminar un usuario."""
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.maximize_window()
    try:
        # Abrir la lista de usuarios
        abrir_lista_usuarios(driver)
        
        # Eliminar el usuario especificado (por ejemplo, "CR7")
        eliminar_usuario(driver, "CR7")
        
        # Cerrar sesión
        cerrar_sesion(driver)
        print("Prueba visual completada")
    finally:
        driver.quit()

# Ejecutar la prueba
prueba_visual()
