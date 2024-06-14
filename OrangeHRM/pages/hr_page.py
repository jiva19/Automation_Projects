from pages.main_page import Main_Page
from selenium.webdriver.common.by import By




class HR_Page(Main_Page):

    #Locators from this pages
    #List of roles 
    add_role_button=(By.XPATH,'//a[contains(@class,"btn-floating")]')
    succes=(By.XPATH,'//div[contains(@class,"toast-suc")]')
    #Locators when adding a role
    user_role_name=(By.XPATH,'//input[contains(@id,"user_role")]')
    hr_checkboxes=(By.XPATH,'//label[contains(@translate,"Data Group")]/following-sibling::ul[1]//label[not(contains(@for,"_") or contains(@translate,"-") or contains(@class,"data"))]')
    save_button=(By.XPATH,'//a[contains(@class,"modal-action waves")]')
    last_checkboxes=(By.XPATH,'//label[contains(@translate,"Data Group")]/following-sibling::ul[1]//label[@for="Other"]')
    element_to_present=(By.XPATH,'//label[@for="checkbox_Request Approve Actor Workflow"]')

    def __init__(self,driver):
        super().__init__(driver)

    #Actions in This page 
    def Add_User_Role(self,role:str):
        self.Access_Menu_Option(0)
        self.click(self.Top_Level_Option(1)) 
        self.wait(20,self.add_role_button,1)
        self.click(self.Add_Role_Button())
        self.write_text(self.User_Role_Name(),role)
        self.wait(20,self.element_to_present,1)
        boxes=self.Hr_Checkbox_Option(0,5,10)
        #[(self.wait(20,i,1),self.click(i)) for i in boxes]
        [(self.wait(20,i,1),self.driver.execute_script("arguments[0].click();", i)) for i in boxes]
        self.click(self.Save_Button())
        self.wait(20,self.succes,0)
        return (self.Success_Banner().text)

    #Elements in this page

    def Add_Role_Button(self):
        return self.find(self.add_role_button[0],self.add_role_button[1])

    def User_Role_Name(self):
        return self.find(self.user_role_name[0],self.user_role_name[1])

    def Hr_Checkbox_Option(self,*options:int):
        options=[*options]
        for i in options:   
          if i<0 or i>11:
            raise ValueError("Options only Available are these:0-11")
        check_list=self.finds(self.hr_checkboxes[0],self.hr_checkboxes[1])
        return [check_list[i] for i in options]
        
    def Save_Button(self):
        return self.find(self.save_button[0],self.save_button[1])

    def Success_Banner(self):
        return self.find(self.succes[0],self.succes[1])