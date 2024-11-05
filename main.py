import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException

running = True
runCount = 0
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

#link = input("Put in link to run:\n")
link = "www.https://google.com"

while running:
    if driver.current_url != link:
        if len(driver.window_handles) > 1:
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
        driver.get(link)
        runCount += 1
        time.sleep(1)
    if runCount == 10:
        running = False
