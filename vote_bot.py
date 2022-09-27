from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


import time

for x in range (100):
    print(f'x is now {x}')
    driver = webdriver.Chrome("/usr/local/bin/chromedriver")
    driver.get('https://pantagraph.com/sports/high-school/football/vote-for-the-pantagraph-week-5-football-player-of-the-week/collection_930f2c64-3de6-11ed-86bb-5fbaa39f7510.html#anchor_item_7');
    time.sleep(2) # Let the user actually see something!
    chk = driver.find_elements('xpath', "//input[@type='radio']")

    x = 0
    for element in chk:
        if x == 2:
            element.click()
        x = x + 1


    time.sleep(2) # Let the user actually see something!

    chk = driver.find_elements('xpath', "//input[@type='submit']")
    # //*[@id="poll-c415b872-3dec-11ed-abd2-27648723ef1f-form"]/button[1]


    button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='poll-c415b872-3dec-11ed-abd2-27648723ef1f-form']/button[1]")))
    button.click()
    time.sleep(2) # Let the user actually see something!



    driver.quit()


