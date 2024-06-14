from behave import given, when, then, step
import pytest 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
import time 
from selenium.webdriver.support.ui import WebDriverWait

@given(u'launch chrome browser')
def step_impl(context):
   service=Service(executable_path="chromedriver.exe")
   context.driver= webdriver.Chrome(service=service)


@when(u'open opencart login page')
def step_impl(context):
    context.driver.get("https://awesomeqa.com/ui/index.php?route=common/home")
    context.driver.maximize_window()

@when(u'search "{Product}"')
def step_impl(context,Product):
    
    search=context.driver.find_element(By.NAME,"search")
    search.send_keys(Product+ Keys.ENTER)

    #button=context.driver.find_element(By.CLASS_NAME,"btn btn-default btn-lg")
    #button.click()

@then(u'verify we are on the search "{Product}"')
def step_impl(context,Product):
    #WebDriverWait(context.driver,5).until(EC.title_is(f"Search - {Product}"))
    assert context.driver.title==f"Search - {Product}",f"Title is: {context.driver.title} but it should be: Search - {Product}"

@then(u'close browser')
def step_impl(context):
    context.driver.quit