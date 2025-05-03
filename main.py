import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://nextspaceflight.com/launches/past/?page=1&search=')
driver.maximize_window()
time.sleep(1)

def scrap():
    details_click = driver.find_elements(By.CLASS_NAME, 'mdc-button__label')
    details_lst = [i for i in details_click if i.text == 'DETAILS']
    return details_lst

def get_details(lst):
    place = lst[0]
    place.click()
    date = driver.find_element(By.ID, 'localized').text
    outcome = driver.find_element(By.CSS_SELECTOR, 'section h6 span').text
    company = driver.find_element(By.XPATH, '/html/body/div/div/main/div/section[2]/div/div[1]/div/div[1]').text
    status = driver.find_element(By.XPATH, '/html/body/div/div/main/div/section[2]/div/div[1]/div/div[2]').text
    new_status = status[8:]
    price = driver.find_element(By.XPATH, '/html/body/div/div/main/div/section[2]/div/div[1]/div/div[3]').text
    new_price = price[7:]
    if ' Thrust' == new_price[:7]:
        new_price = 'Unknown'    
    headings = driver.find_elements(By.TAG_NAME, 'h3')
    location = None
    for heading in headings:
        if heading.text.strip() == "Location":
            section = driver.execute_script("return arguments[0].nextElementSibling;", heading)
            try:
                location = section.find_element(By.CSS_SELECTOR, 'h4.mdl-card__title-text').text
                break
            except:
                continue
    mission_details = driver.find_element(By.CSS_SELECTOR, 'section div div p').text
    lst.pop(0)
    final_lst = [new_status, company, date, location, outcome, mission_details, new_price]
    print(final_lst)
    driver.back()
    return final_lst

def go_next():
    try:
        next = driver.find_element(By.XPATH, '/html/body/div/div/main/div/div[2]/div[2]/span/div/a[1]/span')
        next.click()
        time.sleep(1)
        return True
    except:
        return False    

class Rockets:
    def __init__(self, status, company, date, location, outcome, details, price, order):
        self.status = status
        self.company = company
        self.date = date
        self.location = location
        self.outcome = outcome
        self.details = details
        self.price = price
        self.order = order

# use lst from details to make rocket
count = 0
def main():
    lst = scrap()
    while lst:
        count += 1
        time.sleep(1)
        deets = get_details()
        def make_rockets(lst):
            Rockets(lst[0], lst[1], lst[2], lst[3], lst[4], lst[5], lst[6], count)   
        make_rockets(deets)
    if go_next():
        go_next
        main()
    print('The end')


    

