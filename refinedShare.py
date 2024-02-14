# This is an automatic mero share, share filler bot.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pathlib import Path
import time

info = {}

print('Enter the number of Kitta to apply.')
number = input()
info['number'] = number
file = open('data.txt')
for line in file:
    x = line.split('=\'')
    a = x[0]
    b = x[1]
    c = len(b)-2
    b = b[0:c]
    info[a] = b

driver = webdriver.Firefox()
driver.get('https://meroshare.cdsc.com.np/#/login')
time.sleep(2)

branch = driver.find_element(By.ID, 'selectBranch')
branch.click()
branchId = driver.find_element(By.CLASS_NAME, 'select2-search__field')
branchId.click()
branchId.send_keys(info['dpid'])
branchId.send_keys(Keys.ENTER)

user = driver.find_element(By.ID, 'username')
user.send_keys(info['username'])

passer = driver.find_element(By.ID, 'password')
passer.send_keys(info['password'])

time.sleep(2)
passer.submit()

time.sleep(3)
# portion to select the myASBA section
link = driver.find_element(By.LINK_TEXT, 'My ASBA')
link.click()

time.sleep(1)

# improved version or should I say, 'the corrected' version

# to find if there's an IPO section with ordinary shares
# first we'll try and create iterations for the selection of divs such that only the correct ones are selected by the users.
reportSelector = driver.find_element(By.LINK_TEXT, 'Apply for Issue')
reportSelector.click()
time.sleep(3)
main_divs = driver.find_elements(By.CSS_SELECTOR, '.company-list')

target_text = 'Ordinary Shares'

for main_div in main_divs:
    span_elements = main_div.find_elements(By.CSS_SELECTOR, ".isin")
    for i, span_element in enumerate(span_elements):
        current_text = span_element.text

        # Compare the text content
        if current_text == target_text:
            print(f"Span element {i + 1} text matches the target text: {target_text}")
            # fill the share and exit
            try:
                clicker = driver.find_element(By.CLASS_NAME, 'btn-issue')
                clicker.click()
                bank = driver.find_element(By.XPATH, '//*[@id="selectBank"]')
                bank.click()
                bank.send_keys(Keys.DOWN)
                bank.send_keys(Keys.ENTER)
                bank.click()
                bank.send_keys(Keys.DOWN)
                bank.send_keys(Keys.ENTER)
                num = driver.find_element(By.ID, 'appliedKitta')
                num.send_keys(info['number'])
                crn = driver.find_element(By.ID, 'crnNumber')
                crn.send_keys(info['crn'])
                dis = driver.find_element(By.ID, 'disclaimer')
                dis.click()
                link = driver.find_element(By.XPATH, '/html/body/app-dashboard/div/main/div/app-issue/div/wizard/div/wizard-step[1]/form/div[2]/div/div[5]/div[2]/div/button[1]').click()
                trans = driver.find_element(By.ID, 'transactionPIN')
                trans.send_keys(info['pin'])
                final = driver.find_element(By.XPATH, '/html/body/app-dashboard/div/main/div/app-issue/div/wizard/div/wizard-step[2]/div[2]/div/form/div[2]/div/div/div/button[1]').click()
                exit()
            except:
                print('No Ordinary shares open at the moment.')
        else:
            print(f"Span element {i + 1} text does not match the target text: {target_text}")
driver.quit()
