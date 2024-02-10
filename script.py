import time

from selenium.webdriver import ActionChains

import pageobject
from webelements import *
from driver import driver

def open_page(element):
    webel = WebDriverWait(driver, 10).until(EC.presence_of_element_located(element))
    driver.execute_script("arguments[0].click();", webel)
    # webel.click()
    time.sleep(1)
def open_tab(element):
    webel = WebDriverWait(driver, 10).until(EC.presence_of_element_located(element))
    action_chains = ActionChains(driver)
    action_chains.move_to_element(webel).perform()
    time.sleep(1)
driver.set_window_size(1920, 1080)

for i in range(3):
    open_page(pageobject.Uslugi)
    open_tab(pageobject.Afisha)
    open_page(pageobject.Afisha_Bezopasnoct)
    open_tab(pageobject.Resursi)
    open_page(pageobject.Resursi_Spisok)
    open_tab(pageobject.Afisha)
    open_page(pageobject.Afisha_Anonsi)
    open_tab(pageobject.O_nas)
    open_page(pageobject.Istoria_bibliotek)
    open_tab(pageobject.O_nas)
    open_page(pageobject.Publichni_otchet)
    open_tab(pageobject.O_nas)
    open_page(pageobject.Oficialny_documenti)
    open_tab(pageobject.O_nas)
    open_page(pageobject.SMI_o_bibliotekax)
    open_tab(pageobject.O_nas)
    open_page(pageobject.TV)
    open_tab(pageobject.Afisha)
    open_page(pageobject.Kultura_na_dom)
    open_tab(pageobject.Afisha)
    open_page(pageobject.Pushkinskaya_karta)
    open_tab(pageobject.Afisha)
    open_page(pageobject.Finansovaya_gramotnost)
    open_tab(pageobject.Afisha)
    open_page(pageobject.Bud_v_kurse)
    open_page(pageobject.Glavnaya)
    print(i)
    i = i+1

driver.quit()

