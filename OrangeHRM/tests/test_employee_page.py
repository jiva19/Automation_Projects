import pytest 
from utilities.test_data import Test_Data
from pages.employee_page import Employee_Page
from tests.base_test import Base_Test




class TestMainPage(Base_Test):

            def test_Add_Employee(self):
                employeepage=Employee_Page(self.driver)
                                                                    #YYYY-MM-DD
                employeepage.Add_Employee('Carol','Molinas','Tores','2024-01-10')
                employeepage.click(employeepage.Top_Level_Option(0)) 
                employeepage.wait(15,employeepage.employe_search_bar,0) 
                names=employeepage.Search_Employee_Name('Carol Molinas Tores')
                
                assert 'Carol Molinas Tores' in names, f'Name Not Found,{names}'

            def test_Add_Document_To_Contact_Details(self):
                employeepage=Employee_Page(self.driver)
                documents=employeepage.Add_File_To_Contact_Details('Cece Bonaparte',Test_Data.document)
                
                assert "cisco.PNG" in documents,f'No document found, only these:{documents}'

            
                