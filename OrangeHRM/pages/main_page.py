from pages.base_page import Base_Page
from selenium.webdriver.common.by import By


class Main_Page(Base_Page):
    
	#locators found in this page or could possibly be frequently found
    logout_button=(By.XPATH,"//li[@id='navbar-logout']//span[@class='profile-name']")
    left_menu_option=(By.XPATH,"//div[@id='menu-content']//li[@class='menu-level-2']")
    top_level_option=(By.XPATH,'//a[contains(@class,"top-level-menu-item")]')
    search_bar=(By.XPATH,'//input[contains(@id,"menuQuick")]')
    quick_search=[By.XPATH,'//div[contains(text(),"{search}") and @class="menu-title"]']
    back_button=(By.XPATH,'//a[@data-tooltip="Employee List"]')
    #locators from calendars
    calendar_day=(By.XPATH,'//tr//td//div[@class="picker__day picker__day--infocus" and @aria-label=')
    calendar_month=(By.XPATH,'//div[contains(@class,"select--month show")]//a[substring(@id, string-length(@id) - string-length')
    calendar_year=(By.XPATH,'//li//a[@class="dropdown-item" and @id="bs-select-22-')
    calendar_month_button=(By.XPATH,'//div[contains(@class,"--month")]//button[@class="btn dropdown-toggle"]')
    calendar_year_button=(By.XPATH,'//div[contains(@class,"year")]//button[@class="btn dropdown-toggle"]')

    def __init__(self,driver):
      super().__init__(driver)


	#Actions done in this page 
    def Logout(self):
        self.click(self.Logout_Button())

    def Access_Menu_Option(self,option):
        self.click(self.Left_Menu_Option(option))

    def Quick_Search_On_Bar(self,search):
        search=''.join([search[i].upper() if i==0 or search[i-1]==" "
                        else search[i].lower()
                        for i in range(len(search))
                        ])
        self.write_text(self.Left_Menu_Search_Bar(),search)
        self.click(self.find(self.quick_search[0],f'//div[contains(text(),{"search"}) and @class="menu-title"]'))

    def Click_Calendar_Date(self,date: str):
        
        year=date[0:4]
        month=date[5:7]
        day=date[8:10]

        if len(date)!= 10:
           raise ValueError("Date must have next syntax yyyy-mm-dd")
        if int(year)<2004 or int(year)>2044:
           raise ValueError("Year must be from 2004 and 2044")
        if int(month)<1 or int(month)>12:
           raise ValueError("Month Must be from 1-12")
        if int(day)<1 or int(day)>31:
           raise ValueError("Day Must be from 1-31")
       
        if month[0]==0:
            month=month[1:]
        month=int(month)-1
        month=str(month)

        numbers=range(2004,2045)
        years={}
        for i in numbers:
             years[f'{i}']= i-2004
        year= years[year]
        
        self.click(self.Calendar_Year())
        self.click(self.finds(By.XPATH,'//div[contains(@class,"year")]//a[contains(@id,"bs-select-")]')[year])
        self.click(self.Calendar_Month())
        self.click(self.find(self.calendar_month[0],self.calendar_month[1]+f'("-{month}") +1) = "-{month}"]'))
        self.click(self.find(self.calendar_day[0],self.calendar_day[1]+f'"{date}"]'))
        
      
	#Page Elements found in this page
    def Logout_Button(self):
        return self.find(self.logout_button[0],self.logout_button[1])

    def Left_Menu_Option(self,option:int):
        menu_list=self.finds(self.left_menu_option[0],self.left_menu_option[1])
        return menu_list[option]

    def Left_Menu_Search_Bar(self):
        return self.find(self.search_bar[0],self.search_bar[1])

    def Search_Bar_Option_Selected(self):
        return self.find(self.quick_search[0],'//div[contains(text(),{search}) and @class="menu-title"]')

    def Top_Level_Option(self,option:int):
        menu_list=self.finds(self.top_level_option[0],self.top_level_option[1])
        return menu_list[option]

    def Back_Button(self):
        return self.find(self.back_button[0],self.back_button[1])

    #Calender Elements

    def Calendar_Month(self):
        return self.find(self.calendar_month_button[0],self.calendar_month_button[1])

    def Calendar_Year(self):
        return self.find(self.calendar_year_button[0],self.calendar_year_button[1])