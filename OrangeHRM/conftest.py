import pytest 
from utilities.test_data import Test_Data
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.login_page import Login_Page 
import time 



@pytest.fixture()
def launchbrowser(request):

    

    service=Service(executable_path="chromedriver.exe")
    global driver
    driver= webdriver.Chrome(service=service)
    if 'function_test' in request.keywords:
        request.cls.driver = driver
        yield 
        time.sleep(1)
        driver.quit()



    else :
       driver.get(Test_Data.url)
       driver.maximize_window()
    
       global loginpage
       loginpage=Login_Page(driver)
       loginpage.Set_Username(Test_Data.username)
       loginpage.Set_Password(Test_Data.password)
       loginpage.Click_Login_Button()
    
       request.cls.driver = driver
       yield  
       time.sleep(1)
       driver.quit