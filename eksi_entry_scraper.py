from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os
from openpyxl import Workbook
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def setup_driver():
    chrome_driver_path = r"C:\\Users\\Omer\\Desktop\\chromedriver.exe"
    chrome_binary_path = r"C:\\Users\\Omer\\Desktop\\chrome-win64\\chrome.exe"

    options = webdriver.ChromeOptions()
    options.binary_location = chrome_binary_path
    options.add_argument("--start-maximized")

    service = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=service, options=options)

    return driver

def extract_entries(driver, entry_count, sheet):
    WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "li[data-id]"))
    )
    entry_blocks = driver.find_elements(By.CSS_SELECTOR, "li[data-id]")

    print(f"\U0001F4C4 Sayfada {len(entry_blocks)} entry bulundu.")

    for entry_element in entry_blocks:
        try:
            content_el = entry_element.find_element(By.CLASS_NAME, "content")
            author_el = entry_element.find_element(By.CLASS_NAME, "entry-author")
            date_el = entry_element.find_element(By.CLASS_NAME, "entry-date")

            content = content_el.text.strip()
            user = author_el.text.strip()
            timestamp = date_el.get_attribute("title") or date_el.text.strip()

            entry_count += 1
            print(f"{entry_count}. Entry by {user} ({timestamp}):\n{content}\n" + "-" * 40)
            sheet.append([entry_count, user, timestamp, content])
        except Exception as e:
            print(f"⚠️ Entry atlanıyor: {e}")
            continue

    return entry_count

def click_next_page(driver):
    try:
        pagination = driver.find_element(By.CSS_SELECTOR, "div.pager")
        links = pagination.find_elements(By.TAG_NAME, "a")
        for link in links:
            if "sonraki sayfa" in link.get_attribute("title"):
                driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", link)
                time.sleep(1)
                driver.execute_script("arguments[0].click();", link)
                time.sleep(3)
                return True
        return False
    except (NoSuchElementException, ElementClickInterceptedException) as e:
        print(f"❌ Sonraki sayfa tıklanamadı: {e}")
        return False

# \U0001F501 Ana akış
wb = Workbook()
ws = wb.active
ws.append(["Sıra", "Yazar", "Tarih", "İçerik"])

driver = setup_driver()
slug = "umut-ozkirimli--411351"
start_page = 8
entry_count = 0

url = f"https://eksisozluk.com/{slug}?p={start_page}"
driver.get(url)

while True:
    entry_count = extract_entries(driver, entry_count, ws)
    if not click_next_page(driver):
        break

output_path = os.path.join(os.environ['USERPROFILE'], 'Desktop', 'entryler.xlsx')
try:
    wb.save(output_path)
    print(f"\n✅ Tüm işlem tamam. Toplam {entry_count} entry '{output_path}' dosyasına kaydedildi.")
except Exception as e:
    print(f"❌ Excel dosyası kaydedilemedi: {e}")

driver.quit()
