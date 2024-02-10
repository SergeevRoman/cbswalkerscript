from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from driver import driver
import pageobject


webuslugi = WebDriverWait(driver, 10).until(EC.presence_of_element_located(pageobject.Uslugi))
webafisha = WebDriverWait(driver, 10).until(EC.presence_of_element_located(pageobject.Afisha))
webanonsi = WebDriverWait(driver, 10).until(EC.presence_of_element_located(pageobject.Afisha_Anonsi))

