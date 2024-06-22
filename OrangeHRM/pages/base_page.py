import pytest 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui as gui
import time
import pyperclip
from pathlib import Path 


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


	#Function to automate the creation of a text file
    def Create_Text_File(self,name,text):

       x,y=gui.size()
       gui.hotkey('win','d')
       gui.moveTo((x*3)/4,y/2)
       gui.click()
       gui.hotkey('fn','f5')
       gui.rightClick()
       gui.hotkey('w','t')
       text_name=name
       gui.write(text_name)
       [(gui.press("enter"),time.sleep(2)) for i in range (2)]
       gui.write(text)
       gui.hotkey('ctrl','w')
       gui.press("enter") 
       gui.hotkey('win','d')
       gui.keyDown('shift')
       gui.click(button='right')
       gui.keyUp('shift')
       gui.moveRel(-176,186,1)
       gui.click()
       document=pyperclip.paste()
       head, sep, tail = document.partition("\\")
       paper2=tail[::-1]
       head,sep,tail=paper2.partition("\\")
       tail=tail[::-1]
       head=head[::-1]
       target = Path("C:/",tail,head[:-1])
       
       
       return str(target)