# You will need 3 bits of info, the webpage, the radio button value corresponding to the person and the button name to submit

#  On my linux box, I can leave the WebDriverWait commented out for the radio button but uncomment for the mac


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from datetime import datetime




from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options


import time

start_time = datetime.now()

good_count = 0
bad_count = 0

for x in range (3000):
    try:
        # print(f'x is now {x}')

        options = Options()
        options.page_load_strategy = 'eager'
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.set_page_load_timeout(30.0) 
        driver.get('https://pantagraph.com/sports/high-school/football/vote-for-the-pantagraph-week-7-football-player-of-the-week/collection_b0451718-6706-11ee-a902-23943352856c.html')
        # time.sleep(2) # Let the user actually see something!
        chk = driver.find_elements('xpath', "//input[@type='radio']")
        # print("check 1")

        radio_counter = 0
        for element in chk:
            if radio_counter == 3:
                id=element.id
                # print(element.is_enabled())
                # element = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, id)))
                # print("waited")
                element.click()
            radio_counter = radio_counter + 1

        # print("before button clickable")
        button = WebDriverWait(driver, 1).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='poll-24391bac-6710-11ee-947b-ff1dd6785565-form']/button[1]")))
        # button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH,"//*[@id='poll-c415b872-3dec-11ed-abd2-27648723ef1f-form']/button[1]")))

        
        button.click()
        good_count = good_count +1
        print(f"good count {good_count}")
        time.sleep(2) # Let the user actually see something!
    except Exception as error:
        bad_count = bad_count + 1
        print(f"bad {bad_count}")
        pass


    driver.quit()



end_time = datetime.now()

current_time = end_time.strftime("%H:%M:%S")
print(f"duration {end_time - start_time}")
print("Current Time =", current_time)

