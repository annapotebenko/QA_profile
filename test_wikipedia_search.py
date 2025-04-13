from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

def test_wikipedia_search():
    # Запускаємо браузер
    driver = webdriver.Chrome()
    
    try:
        # Відкриваємо Wikipedia
        driver.get("https://www.wikipedia.org/")
        
        # Пошук поля для пошуку
        search_input = driver.find_element(By.NAME, "search")
        search_input.send_keys("QA Engineer")
        search_input.send_keys(Keys.RETURN)
        
        # Очікуємо, щоб сторінка завантажилась
        time.sleep(2)

        # Перевірка на те, чи заголовок сторінки містить потрібний текст нужный текст
        assert "QA engineer" in driver.title or "Software testing" in driver.page_source
        print("Тест пройдено успішно: Сторінка є!")
    
    except AssertionError:
        print("Тест не пройдено: Сторінка відсутня.")
    
    finally:
        driver.quit()
