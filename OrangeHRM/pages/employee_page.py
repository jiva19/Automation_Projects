from pages.main_page import Main_Page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time



class Employee_Page(Main_Page):
    #Locators from this page 

    #Employee list locators
    employe_search_bar=(By.XPATH,"//input[contains(@id,'employee_name_quick')]")
    add_employee_button=(By.XPATH,'//a[@id="addEmployeeButton"]')
    dropdown_employee=(By.XPATH,'//div[contains(@class,"angucomplete-row angu")]//span[contains(@class,"angucomplete-ti")]')
    drop_employee=(By.XPATH,'//div[contains(@class,"angucomplete-row angucomplete-selected-row")]')

    #Adding Employee locators
    add_first_name=(By.ID,'first-name-box')
    add_middle_name=(By.ID,'middle-name-box')  
    add_last_name=(By.ID,'last-name-box')
    add_joined_date=(By.ID,'joinedDate')
    calendar_button=(By.XPATH,'//button[@class="btn date-picker-button"]')
    location_button=(By.XPATH,'//button[@data-id="location"]')
    location_options=(By.XPATH,'//a[@class="dropdown-item"]')
    continue_button=(By.ID,'modal-save-button')
    next_button=(By.XPATH,'//button[@class="btn btn-secondary right"]')
    table_names=(By.XPATH,'//td[3]')
    table_first_name=(By.XPATH,'//tr[1]//td[3]')
    #Uploading document to employee
    add_contact_document=(By.XPATH,'//a[contains(@class,"waves-effect waves-teal")]')
    browse_document=(By.XPATH,'//input[@type="file"]')
    save_button=(By.XPATH,'//button[@class="btn btn-secondary"]')
    table_documents=(By.XPATH,'//table[@class="highlight bordered classic-table"]//td[2]')
  
    def __init__(self,driver):
        super().__init__(driver)
		
	#Page Elements in Employee Page:
    def Employee_Search_Bar(self):
       return self.find(self.employe_search_bar[0],self.employe_search_bar[1])

    def Add_Employee_Button(self):
       return self.find(self.add_employee_button[0],self.add_employee_button[1])

    def Dropdown(self):
       return self.find(self.drop_employee[0],self.drop_employee[1])

    #Actions that can be done in this page

    def Add_Employee(self,first,middle,last,date):

        self.click(self.Top_Level_Option(0)) 
        self.wait(10,self.add_employee_button,1)
        self.click(self.Add_Employee_Button()) 
        self.wait(15,self.add_first_name,0)
        self.write_text(self.Add_First_Name(),first)
        self.write_text(self.Add_Middle_name(),middle)
        self.write_text(self.Add_Last_name(),last)
        self.click(self.Add_Date())
        self.Click_Calendar_Date(date)
        self.click(self.Location_Button())
        self.click(self.Location_Options()[0])
        self.click(self.Continue_Button())
        title_list=['Personal Details','Job','Onboarding']
        [(self.wait(20,self.next_button,3,title_list[i]),
          self.wait(20,self.next_button,1),
          self.click(self.Next_Button())) 
         for i in range(3)]
        self.wait(30,self.back_button,1)
        self.click(self.Back_Button())
        
    def Search_Employee_Name(self,employee):
        
        self.write_text(self.Employee_Search_Bar(),employee)
        self.wait(10,self.drop_employee,1)
        self.click(self.Dropdown())
        self.wait(30,self.table_first_name,2,employee)
        return [self.Table_First_Name().text]


    def Add_File_To_Contact_Details(self,employee,document):
        self.click(self.Top_Level_Option(0)) 
        self.wait(15,self.add_employee_button,1)
        self.write_text(self.Employee_Search_Bar(),employee)
        #self.wait(10,self.drop_employee,1)
        #self.click(self.Dropdown())
        self.wait(20,self.table_first_name,2,employee)
        self.click(self.Table_Names()[0])
        self.wait(25,self.top_level_option,1)
        self.click(self.Top_Level_Option(4))
        self.wait(20,self.add_contact_document,0)
        self.click(self.Add_Document_Button())
        self.wait(20,self.browse_document,0)
        self.write_text(self.Browse_Document_Button(),document)
        self.wait(20,self.save_button,1)
        self.click(self.Save_Button())
        return [i.text for i in self.Table_Documents()]
    

	#Elements when Adding an Employee 

    def Add_First_Name(self):
      return self.find(self.add_first_name[0],self.add_first_name[1])

    def Add_Middle_name(self):
      return self.find(self.add_middle_name[0],self.add_middle_name[1])

    def Add_Last_name(self):
      return self.find(self.add_last_name[0],self.add_last_name[1])

    def Add_Joined_Date(self):
      return self.find(self.add_joined_date[0],self.add_joined_date[1])

    def Add_Date(self):
        return self.find(self.calendar_button[0],self.calendar_button[1])

    def Location_Button(self):
      return self.find(self.location_button[0],self.location_button[1])

    def Location_Options(self):
      return self.finds(self.location_options[0],self.location_options[1])

    def Continue_Button(self):
      return self.find(self.continue_button[0],self.continue_button[1])

    def Next_Button(self):
      return self.find(self.next_button[0],self.next_button[1])

    def Table_Names(self):
       return self.finds(self.table_names[0],self.table_names[1])

    def Table_First_Name(self):
        return self.find(self.table_first_name[0],self.table_first_name[1])

   #Elements when uploading a document to an employee

    def Add_Document_Button(self):
        return self.find(self.add_contact_document[0],self.add_contact_document[1])

    def Browse_Document_Button(self):
        return self.find(self.browse_document[0],self.browse_document[1])

    def Save_Button(self):
        return self.find(self.save_button[0],self.save_button[1])

    def Table_Documents(self):
        return self.finds(self.table_documents[0],self.table_documents[1])

   
    
