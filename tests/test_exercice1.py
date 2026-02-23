import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class TestExercice1:
    """Tests pour le login sur the-internet.herokuapp.com"""
    
    def setup_method(self):
        """Initialiser le driver avant chaque test"""
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    def teardown_method(self):
        """Fermer le driver après chaque test"""
        self.driver.quit()
    
    def test_login_success(self):
        """Test du login réussi avec les bonnes credentials"""
        self.driver.get("https://the-internet.herokuapp.com/login")
        
        username = self.driver.find_element(By.ID, "username")
        username.send_keys("tomsmith")
        
        password = self.driver.find_element(By.ID, "password")
        password.send_keys("SuperSecretPassword!")
        
        btn = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        btn.click()
        
        time.sleep(2)
        success_message = self.driver.find_element(By.ID, "flash")
        assert "You logged into a secure area!" in success_message.text
    
    def test_login_invalid_username(self):
        """Test du login avec mauvais username"""
        self.driver.get("https://the-internet.herokuapp.com/login")
        
        username = self.driver.find_element(By.ID, "username")
        username.send_keys("invalid_user")
        
        password = self.driver.find_element(By.ID, "password")
        password.send_keys("SuperSecretPassword!")
        
        btn = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        btn.click()
        
        time.sleep(2)
        error_message = self.driver.find_element(By.ID, "flash")
        assert "Your username is invalid!" in error_message.text
    
    def test_login_invalid_password(self):
        """Test du login avec mauvais password"""
        self.driver.get("https://the-internet.herokuapp.com/login")
        
        username = self.driver.find_element(By.ID, "username")
        username.send_keys("tomsmith")
        
        password = self.driver.find_element(By.ID, "password")
        password.send_keys("WrongPassword")
        
        btn = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        btn.click()
        
        time.sleep(2)
        error_message = self.driver.find_element(By.ID, "flash")
        assert "Your password is invalid!" in error_message.text
