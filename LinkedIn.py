#import required modules
from selenium.webdriver.opera.options import Options
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

from selenium import webdriver
import time
import os


class LinkedIn(object):

	#close already opened Edge browser Instances
	def closeAllEdgeInstances():
		try:
			os.system("taskkill /im msedgedriver.exe")
			os.system("taskkill /im msedge.exe")

		except:
			pass

			#launch LinkedIn
	def launchLinkedIn():
		global browser

		browser = webdriver.Edge(r"msedgedriver.exe")
		browser.maximize_window()
		browser.get('https://www.linkedin.in')

		#Login to LinkedIn
	def login():
		elmnt = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//*[contains(text(),"Sign in")]')))
		elmnt.click()
		time.sleep(3)
		elmnt = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@ aria-label="Email or Phone"]')))
		elmnt.click()
		elmnt.send_keys("cliona.melle@easyonlinemail.net")
		elmnt.send_keys(Keys.TAB)
		elmnt = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@ aria-label="Password"]')))
		elmnt.send_keys("ClionaMelle123")
		elmnt.send_keys(Keys.RETURN)

		#search 'autods' in LinkedIn
	def searchItem():
	
		try:
			time.sleep(10)
			elmnt = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@ aria-label="Search"]')))
			elmnt.click()
			elmnt.send_keys("autods")
			elmnt.send_keys(Keys.RETURN)
			time.sleep(5)

		except TimeoutException:
			print("Trying to find the given element but unfortunately no element is found")
		return True

		#click the 'Following' button on the page of AutoDS and Unfollow it.
	def clickFollowing():

		try:
			time.sleep(10)
			elmnt = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@href="https://www.linkedin.com/company/autods/"]')))
			elmnt.click()
			time.sleep(10)
			elmnt = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '//*[@aria-label="Following"]')))
			elmnt.click()
			time.sleep(5)
			elmnt = WebDriverWait(browser, 20).until(EC.presence_of_element_located((By.XPATH, '(//*[@class="artdeco-button__text"])[3]')))
			elmnt.click()
			time.sleep(5)

		except TimeoutException:
			print("Trying to find the given element but unfortunately no element is found")


			#main function
	if __name__ == '__main__':
		result = closeAllEdgeInstances()
		result = launchLinkedIn()
		result = login()
		result = searchItem()
		result = clickFollowing()
		result = closeAllEdgeInstances()
