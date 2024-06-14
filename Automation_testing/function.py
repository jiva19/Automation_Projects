import openpyxl as xls
import pytest 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


def Click_Image(driver):
    WebDriverWait(driver,20).until(EC.element_to_be_clickable((By.XPATH,'//img[@class="screenshot-thumb__img" and contains(@src,"13_1")]')))
    acces=driver.find_element(By.XPATH,'//img[@class="screenshot-thumb__img" and contains(@src,"13_1")]')
    driver.execute_script("arguments[0].click();", acces)

def Switch_Page(driver):
    original=driver.current_window_handle
    WebDriverWait(driver,5).until(EC.number_of_windows_to_be(2))
    for i in driver.window_handles:
        if i != original:
            driver.switch_to.window(i)
            break

def Switch_to_bottom_frame(driver):
    WebDriverWait(driver,9).until(EC.presence_of_element_located((By.ID,"heatmap-iframe")))
    driver.switch_to.frame("heatmap-iframe")

def Switch_to_Base_page(driver):
    clickmap=driver.find_element(By.XPATH,'//div[contains(@data-qa,"liqo")]')
    clickmap.click()
    driver.switch_to.parent_frame()

def Go_Login(driver):
    WebDriverWait(driver,9).until(EC.element_to_be_clickable((By.XPATH,'//a[contains(@href,"/login")]')))
    login=driver.find_element(By.XPATH,'//a[contains(@href,"/login")]')
    driver.execute_script("arguments[0].click();",login)

def Go_Home(driver):
    home=driver.find_element(By.XPATH,'//a[contains(@class,"k clickmap_select_a") and substring(@href, string-length(@href) - string-length("/") +1) = "/"]')
    home.click()

def Move_Slide(driver,x:int):
    WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH,'//div[contains(@data-qa,"wesiyo")]')))
    slide=driver.find_element(By.XPATH,'//div[contains(@data-qa,"wesiyo")]')
    action=ActionChains(driver)
    action.drag_and_drop_by_offset(slide,x,0).perform()

def Value_Slide(driver):
    slide_input=driver.find_element(By.XPATH,'//input[contains(@class,"text-input slider-input slider")]')
    return slide_input.get_attribute("value")

def Clear_Bar(element):
    element.send_keys(Keys.CONTROL+'a')
    element.send_keys(Keys.BACKSPACE)

def Write_Excel(row:int,col:int,value,excel:str,ws,wb):
    ws.cell(row=row, column=col,value = value)
    wb.save(excel)

def Read_Excel(row,col,ws):
    return ws.cell(row=row, column=col).value


def Create_Excel_List(row,col,ws):
    error_list=str(Read_Excel(row,col,ws))+','
    error_list=list(error_list)
    [error_list.remove(',') for i in range(int(len(error_list)/2))]
    error_list.sort()
    return [int(i) for i in error_list]


def Create_Pge_List(driver,error_dict):
    WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,'//div/span[@class="error"]')))
    errors=driver.find_elements(By.XPATH,'//div/span[@class="error"]') 
    errors=[error_dict[i.text] for i in errors]
    errors.sort()
    return errors 