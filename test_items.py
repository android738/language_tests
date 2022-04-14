import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_browser_languages(browser):
    browser.get(link)
    wait = WebDriverWait(browser, 15)
    try:
        # Дожидаемся полной загрузки страницы, опираясь на элемент описания продукта
        wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#product_description"))) 
        time.sleep(30)
        # Проверяем наличие кнопки добавления в корзину (что количество элементов, найденных по данному селектору больше нуля)
        assert len(browser.find_elements(By.CSS_SELECTOR, ".btn-add-to-basket")) > 0, "\"Add to basket\" button does not exists"
    except Exception:
        raise ValueError("Не удалось загрузить страницу.")
