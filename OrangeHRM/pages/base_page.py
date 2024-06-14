import pytest 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Base_Page:

	def __init__(self,driver):
		self.driver=driver
		
		

	#Selenium Actuators common to all pages 

	def find(self,*locator):
		return self.driver.find_element(*locator)

	def finds(self,*locator):
		return self.driver.find_elements(*locator)

	def click(self,element):
		return element.click()

	def write_text(self,element,message):
		
		return element.send_keys(message)

	def get_text(self,element):
		return element.text()

	def wait(self,time:int,element,option:int,*text):
		if option==0:
			WebDriverWait(self.driver,time).until(EC.presence_of_element_located(element))
		if option==1:
			WebDriverWait(self.driver,time).until(EC.element_to_be_clickable(element))
		if option==2:
			WebDriverWait(self.driver,time).until(EC.text_to_be_present_in_element(element,*text))
		if option==3:
			WebDriverWait(self.driver,time).until(EC.title_is(*text))