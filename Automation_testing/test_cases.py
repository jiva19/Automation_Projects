import pytest 
import function
import openpyxl as xls
from test_data import Test_Data
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import time 


@pytest.fixture(autouse="True")
def LaunchBrowser():
 global driver
 service=Service(executable_path="chromedriver.exe")
 driver= webdriver.Chrome(service=service)
 driver.get(Test_Data.url)
 driver.maximize_window()

 function.Click_Image(driver)
 function.Switch_Page(driver)
 function.Switch_to_bottom_frame(driver)

 yield 
 time.sleep(1)
 driver.quit
 
 
def test_first():
    function.Switch_to_Base_page(driver)
    function.Go_Home(driver)
    
    assert driver.title=='Learn Software Testing & Test Automation',f'Driver is:{driver.title} but it should be: Learn Software Testing & Test Automation'

def test_second():
    function.Move_Slide(driver,25)
    value_slide=function.Value_Slide(driver)
    
    assert int(value_slide)==93, f'Value is: {value_slide} but shold be 83'

def test_third():
    function.Switch_to_Base_page(driver)
    function.Go_Login(driver)

    user=driver.find_element(By.ID, "email")
    pasword=driver.find_element(By.ID, "login-password")
    buton=driver.find_element(By.ID, "login")
    
    
    Fails=True
    wb = xls.load_workbook(filename=Test_Data.document)
    ws = wb.worksheets[0]
    for row in range(2,5):
     for col in range(1,ws.max_column+1):
        if col==1:
           function.Clear_Bar(user)
           enter1=function.Read_Excel(row,col,ws)
           if enter1==None:
               enter1=""
           user.send_keys(enter1)
        elif col==2:
          function.Clear_Bar(pasword)
          enter2=function.Read_Excel(row,col,ws)
          if enter2==None:
               enter2=""
          pasword.send_keys(enter2)
        elif col==3:
            buton.click()
            error_list=function.Create_Excel_List(row,col,ws)
            errors=function.Create_Pge_List(driver,Test_Data.error_dict)
        elif col==4:
            Expected=errors==error_list
            if Expected:
               function.Write_Excel(row,col,'Fails found',Test_Data.document,ws,wb)
            if not Expected:
               function.Write_Excel(row,col,'Fails not found',Test_Data.document,ws,wb)
               Fails=False
    assert Fails,f'Check excel file, one case did not give expected errors'    
    