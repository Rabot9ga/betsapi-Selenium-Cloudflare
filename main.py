import time
import undetected_chromedriver as uc




try:
    driver = uc.Chrome()
    driver.maximize_window()
    driver.get("http://www.anycoindirect.eu/")
    time.sleep(100)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()


