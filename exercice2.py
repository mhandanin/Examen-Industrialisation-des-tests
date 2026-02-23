from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import csv
from datetime import datetime

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))


print("=== Extraction d'informations sans login ===\n")
    
driver.get("http://books.toscrape.com/")
    
time.sleep(2)
    
livres = []
    
articles = driver.find_elements(By.CSS_SELECTOR, ".product_pod")
    
print(f"Nombre de livres trouvés: {len(articles)}\n")
    
for article in articles:

    titre = article.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("title")
        
    prix = article.find_element(By.CSS_SELECTOR, ".price_color").text
            
    disponibilite = article.find_element(By.CSS_SELECTOR, ".instock").text
            
    url_relative = article.find_element(By.CSS_SELECTOR, "h3 a").get_attribute("href")
    url = f"http://books.toscrape.com/{url_relative}"
            
    note_element = article.find_element(By.CSS_SELECTOR, ".star-rating")
    note = note_element.get_attribute("class").split()[-1]
            
    livre = {
        "titre": titre,
        "prix": prix,
        "disponibilite": disponibilite.strip(),
        "note": note,
        "url": url,
        "date_extraction": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
            
    livres.append(livre)
            
    print(f"Titre: {titre}")
    print(f"Prix: {prix}")
    print(f"Disponibilité: {disponibilite.strip()}")
    print(f"Note: {note}")
    print(f"URL: {url}")
    print("-" * 50)
            

    
if livres:
        with open('livres_extraits.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=livres[0].keys())
            writer.writeheader()
            writer.writerows(livres)
        print(f"\n {len(livres)} livres sauvegardés dans 'livres_extraits.csv'")
    

