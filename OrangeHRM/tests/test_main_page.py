import pytest 
from pages.main_page import Main_Page
from tests.base_test import Base_Test


class TestMainPage(Base_Test):

    def test_Logout(self):
        mainpage=Main_Page(self.driver)
        mainpage.Logout()
        assert self.driver.title=='OrangeHRM',f'The title was {self.driver.title} but should be OrangeHRM'
    
    def test_Left_Menu(self):
        mainpage=Main_Page(self.driver)
        mainpage.Access_Menu_Option(2)
        assert self.driver.title=='Reports and Analytics',f'The title was {self.driver.title} but it should be Reports and Analytics'


    @pytest.mark.parametrize("search,page_title",[("employee l",'Employee Management'),("leave list",'Leave')])
    def test_Search_Bar(self,search,page_title):
        mainpage=Main_Page(self.driver)
        mainpage.Quick_Search_On_Bar(search)
        assert self.driver.title==page_title,f'The title was {self.driver.title} but it should be {page_title}'

    @pytest.mark.function_test
    def test_Calendar_Error(self):
        mainpage=Main_Page(self.driver)
        with pytest.raises(ValueError):
           mainpage.Click_Calendar_Date('2064-01-10')
        