import pytest 
import random 
from pages.hr_page import HR_Page
from tests.base_test import Base_Test



class Test_HR_Page(Base_Test):

    def test_Add_User_Role(self):
        hrpage=HR_Page(self.driver)
        banner=hrpage.Add_User_Role(f'JOB{random.randint(1, 200)}')

        assert banner=='Successfully Saved',f'The message was: {banner} but it should be: Successfully Saved'

    @pytest.mark.function_test
    def test_HR_Checkbox_Error(self):
        hrpage=HR_Page(self.driver)
        with pytest.raises(ValueError):
            hrpage.Hr_Checkbox_Option(5,13,0)