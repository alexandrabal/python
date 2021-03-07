
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup

if __name__=="__main__":
    driver = webdriver.Chrome()

    # creem un driver de firefox
    # chrome si firefox e o clasa
    driver.get('https://htmlcolorcodes.com')
    # te asiguri ca functioneaza pe toate

    agree_button = driver.find_element_by_xpath(".//button[text()=\"AGREE\"]")
    sleep(3)
    # block python timp de 2 secunde
    # # sasu de 10 secunde
    # # in situatia asta te folosesti de selenium ca sa il opresti

    agree_button = webdriverwait(driver,10).until(agree_button.element_to_be_clickable(By.XPATH,".//button[text()=\"AGREE\""))
    agree_button.click()

    agree_button.click()
    print(agree_button)
    # selenium poate sa importe chestii dinamice
    #

    sleep(3)

    soup = BeautifulSoup (dirver.page_source, features = "html.parser")

