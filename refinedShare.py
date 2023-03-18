# This is an automatic mero share, share filler bot.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from pathlib import Path
import time

dic = {}

print('Enter the number of Kitta to apply.')
number = input()
dic['number'] = number
file = open('data.txt')
for line in file:
    x = line.split('=\'')
    a = x[0]
    b = x[1]
    c = len(b)-2
    b = b[0:c]
    dic[a] = b

driver = webdriver.Firefox()
driver.get('https://meroshare.cdsc.com.np/#/login')
time.sleep(2)

branch = driver.find_element_by_id('selectBranch')
branch.click()
branchId = driver.find_element_by_class_name('select2-search__field')
branchId.click()
branchId.send_keys(dic['dpid'])
branchId.send_keys(Keys.ENTER)

user = driver.find_element_by_id('username')
user.send_keys(dic['username'])

passer = driver.find_element_by_id('password')
passer.send_keys(dic['password'])

time.sleep(2)
passer.submit()

time.sleep(3)
# portion to select the myASBA section
link = driver.find_element_by_link_text('My ASBA')
link.click()

time.sleep(1)
# to find if there's an IPO section with ordinary shares
try:
    clicker = driver.find_element_by_class_name('btn-issue')
    clicker.click()
    bank = driver.find_element_by_xpath('//*[@id="selectBank"]')
    bank.click()
    bank.send_keys(Keys.DOWN)
    bank.send_keys(Keys.ENTER)
    bank.click()
    bank.send_keys(Keys.DOWN)
    bank.send_keys(Keys.ENTER)
    num = driver.find_element_by_id('appliedKitta')
    num.send_keys(dic['number'])
    crn = driver.find_element_by_id('crnNumber')
    crn.send_keys(dic['crn'])
    dis = driver.find_element_by_id('disclaimer')
    dis.click()
    link = driver.find_element_by_xpath('/html/body/app-dashboard/div/main/div/app-issue/div/wizard/div/wizard-step[1]/form/div[2]/div/div[5]/div[2]/div/button[1]').click()
    trans = driver.find_element_by_id('transactionPIN')
    trans.send_keys(dic['pin'])
    final = driver.find_element_by_xpath('/html/body/app-dashboard/div/main/div/app-issue/div/wizard/div/wizard-step[2]/div[2]/div/form/div[2]/div/div/div/button[1]').click()
except:
    print('No Ordinary shares open at the moment.')
