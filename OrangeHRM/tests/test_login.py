import pytest 
from tests.base_test import Base_Test



class TestLogin(Base_Test):

    def test_Login_Username(self):
        assert self.driver.title=='Employee Management', f'The title was {self.driver.title} but it should be Employee Management'