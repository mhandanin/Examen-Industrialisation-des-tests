import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os


class TestExercice2:
    """Tests pour l'extraction d'informations de livres"""
    
    def setup_method(self):
        """Initialiser le driver avant chaque test"""
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    def teardown_method(self):
        """Fermer le driver après chaque test"""
        self.driver.quit()
    
    def test_books_page_loads(self):
        """Test que la page se charge correctement"""
        self.driver.get("http://books.toscrape.com/")
        
        assert "All products" in self.driver.page_source
    
    def test_books_list_found(self):
        """Test que la liste de livres est trouvée"""
        self.driver.get("http://books.toscrape.com/")
        time.sleep(2)
        
        articles = self.driver.find_elements(By.CSS_SELECTOR, ".product_pod")
        assert len(articles) > 0, "Aucun livre trouvé"
    
    def test_books_extraction_first_20(self):
        """Test l'extraction de 20 livres"""
        self.driver.get("http://books.toscrape.com/")
        time.sleep(2)
        
        articles = self.driver.find_elements(By.CSS_SELECTOR, ".product_pod")
        assert len(articles) == 20, f"Attendu 20 livres, trouvé {len(articles)}"
    
    def test_books_contain_required_info(self):
        """Test que chaque livre contient les informations requises"""
        self.driver.get("http://books.toscrape.com/")
        time.sleep(2)
        
        articles = self.driver.find_elements(By.CSS_SELECTOR, ".product_pod")
        
        for article in articles:
            titre = article.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
            assert titre is not None and titre != ""
            
            prix = article.find_element(By.CSS_SELECTOR, ".price_color").text
            assert prix is not None and prix != ""
            
            disponibilite = article.find_element(By.CSS_SELECTOR, ".instock").text
            assert "stock" in disponibilite.lower()
            
            url_relative = article.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("href")
            assert url_relative is not None and url_relative != ""
            
            note = article.find_element(By.CSS_SELECTOR, ".star-rating").get_attribute("class")
            assert "One" in note or "Two" in note or "Three" in note or "Four" in note or "Five" in note
    
    def test_first_book_details(self):
        """Test les détails du premier livre"""
        self.driver.get("http://books.toscrape.com/")
        time.sleep(2)
        
        first_article = self.driver.find_element(By.CSS_SELECTOR, ".product_pod")
        
        titre = first_article.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
        assert titre == "A Light in the Attic"
        
        prix = first_article.find_element(By.CSS_SELECTOR, ".price_color").text
        assert "" in prix or "$" in prix
        
        disponibilite = first_article.find_element(By.CSS_SELECTOR, ".instock").text
        assert "In stock" in disponibilite
