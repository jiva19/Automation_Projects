from pages.base_page import Base_Page 
import time
from selenium.webdriver.common.by import By

class Login_Page(Base_Page):

	#locators from this page
    user_field=(By.ID,'txtUsername')
    password_field=(By.ID,'txtPassword')
    login_button=(By.XPATH,"//button[@type='submit']")

    def __init__(self,driver): 
       super().__init__(driver)
	   
	   

	 #Actions done in this page
    def Set_Username(self,user):
        self.wait(5,self.user_field,0)
        self.write_text(self.User_Bar(),user)

    def Set_Password(self,password):
        self.write_text(self.Password_Bar(),password)

    def Click_Login_Button(self):
        self.click(self.Login_Button())
        self.wait(3,(By.XPATH,"//div[text()='Employee Management']"),0)   
        
        
	
    # Elements from this page 
    def User_Bar(self):
       return self.find(self.user_field[0],self.user_field[1])
       
    def Password_Bar(self):
       return self.find(self.password_field[0],self.password_field[1])

    def Login_Button(self):
       return self.find(self.login_button[0],self.login_button[1]) 