from behave import given, when, then, step
import pytest 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@given(u'launch chrome browser')
def step_impl(context):
   context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


@when(u'open opencart login page')
def step_impl(context):
    context.driver.get("https://awesomeqa.com/ui/index.php?route=common/home")
    context.driver.maximize_window()

@when(u'search "{Product}"')
def step_impl(context,Product):
    
    search=context.driver.find_element(By.NAME,"search")
    search.send_keys(Product+ Keys.ENTER)

    
@then(u'verify we are on the search "{Product}"')
def step_impl(context,Product):
    WebDriverWait(context.driver,5).until(EC.title_is(f"Search - {Product}"))
    assert context.driver.title==f"Search - {Product}",f"Title is: {context.driver.title} but it should be: Search - {Product}"

@then(u'close browser')
def step_impl(context):
    context.driver.quit




    
@then(u'search Phone product')
def step_impl(context):
    
    search=context.driver.find_element(By.NAME,"search")
    search.send_keys('Phone'+ Keys.ENTER)


@then(u'add Phone to cart')
def step_impl(context):
    WebDriverWait(context.driver,5).until(EC.element_to_be_clickable((By.XPATH,'//button[contains(@onclick,"cart.add")]')))
    cart_button=context.driver.find_element(By.XPATH,'//button[contains(@onclick,"cart.add")]')
    cart_button.click()
    

@then(u'verify it indeed was added')
def step_impl(context):
    WebDriverWait(context.driver,5).until(EC.text_to_be_present_in_element((By.ID,"cart-total"),"123.20"))
    cart=context.driver.find_element(By.ID,"cart-total")
    assert cart.text=="1 item(s) - $123.20",f'product not added correctly:{cart.text}, it should be  1 item(s) - $123.20'

    