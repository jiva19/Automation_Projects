import pytest 
from utilities.test_data import Test_Data
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.login_page import Login_Page 
import time 

@pytest.mark.usefixtures('launchbrowser')
class Base_Test():
    pass 
