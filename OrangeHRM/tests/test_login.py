import pytest 
from utilities.test_data import Test_Data
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from pages.login_page import Login_Page 
import time 
from selenium import webdriver
from tests.base_test import Base_Test



class TestLogin(Base_Test):

    def test_Login_Username(self):
        assert self.driver.title=='Employee Management', f'The title was {self.driver.title} but it should be Employee Management'