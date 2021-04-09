#Import all the modules

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import pyperclip, time

#Create a new selenium instance

browser = webdriver.Firefox(firefox_profile=None, firefox_binary=None, timeout=30, capabilities=None, proxy=None, executable_path="geckodriver", options=None, service_log_path="geckodriver.log", firefox_options=None, service_args=None, desired_capabilities=None, log_path=None, keep_alive=True)

browser.get('https://mail.tm/en/')	#Go to mail.tm

browser.window_handles[0]	#Name the current tab as handle 0

time.sleep(3)	#Wait for 3 seconds before executing the next line of code

#Finding elements, clicking on them and entering the required info 

emailcopy = browser.find_element_by_css_selector('#address')
emailcopy.click()

email = pyperclip.paste()	#Store the contents of the clipboard in the email variable

browser.execute_script("window.open('about:blank', 'tab2');")	#Creating a new tab 'tab2'
browser.switch_to.window("tab2")	#Switching to the new tab

time.sleep(3)

browser.get('https://www.instagram.com/accounts/emailsignup/')

time.sleep(5)

emailfield = browser.find_element_by_css_selector('div.WZdjL:nth-child(4) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
emailfield.send_keys(email)
namefield = browser.find_element_by_css_selector('div.WZdjL:nth-child(5) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
namefield.send_keys('Account Name')
usernamefield = browser.find_element_by_css_selector('div.WZdjL:nth-child(6) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
usernamefield.send_keys('username')
passwordfield = browser.find_element_by_css_selector('div.WZdjL:nth-child(7) > div:nth-child(1) > label:nth-child(1) > input:nth-child(2)')
passwordfield.send_keys('password')
signup = browser.find_element_by_css_selector('div.bkEs3:nth-child(1) > button:nth-child(1)')
signup.click()

time.sleep(3)

year = Select(browser.find_element_by_css_selector('span.O15Fw:nth-child(3) > select:nth-child(2)'))
year.select_by_value('year')

nextpage = browser.find_element_by_css_selector('.L3NKy')
nextpage.click()

browser.switch_to.window(browser.window_handles[0])		#Switching to the first tab to copy the verification code

time.sleep(20)

openmail = browser.find_element_by_css_selector('.h-12 > span:nth-child(1)')
openmail.click()

time.sleep(3)

vericode = browser.find_element_by_css_selector('.text-2xl').text
newvericode = vericode[:6]

browser.switch_to.window("tab2")	#Switching to 'tab2' for entering the verification code

confirmation = browser.find_element_by_css_selector('.j_2Hd')
confirmation.send_keys(newvericode)

nextview = browser.find_element_by_css_selector('.L3NKy')
nextview.click()
