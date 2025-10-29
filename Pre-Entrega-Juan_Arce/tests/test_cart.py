from selenium.webdriver.common.by import By
from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def test_cart(login_in_driver):
    driver = login_in_driver
        
    wait = WebDriverWait(driver,10)
    
    try:
        	
        driver.find_element(By.CSS_SELECTOR, ".inventory_item button").click()
	
        titulo_producto = driver.find_element(By.CSS_SELECTOR, ".inventory_item_name").text
	
        contador_carrito = driver.find_element(By.CLASS_NAME,"shopping_cart_badge").text
	
        assert contador_carrito == "1", "No se ha agregado el producto al carrito"
	
        driver.find_element(By.CSS_SELECTOR, ".shopping_cart_link").click()
	
        wait.until(EC.url_contains("/cart.html"))
        
        titulo_producto_carrito = driver.find_element(By.CSS_SELECTOR,".cart_item .inventory_item_name").text
	
        assert titulo_producto == titulo_producto_carrito, "El producto no coincide"
	
    except Exception as e:
        print(f"Error al agregar producto al carrito: {e}")
        raise
  
    