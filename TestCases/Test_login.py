from PageObjects.Loginpage import Login
import pytest
from selenium import webdriver
from Utilities.readProperties import Readconfig
from Utilities.customLogger import LogGen


@pytest.mark.usefixtures("setup")
class Test_001_login:
    url = Readconfig.getApplicationurl()
    username = Readconfig.getUsername()
    password = Readconfig.getPassword()
    logger= LogGen.loggen()
    def test_homepageTitle(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        act_title = self.driver.title
        print(act_title)
        self.driver.close
    @pytest.mark.sanity
    def test_login(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.lp = Login(self.driver)
        self.lp.setuserName(self.username)
        self.lp.setPassword(self.password)
        titleOfWebPage = self.driver.title
        if titleOfWebPage == "My updates":
            assert True
            self.logger.info("************************** Home page Title****************")
        else:
            self.driver.save_screenshot("C://Users//aravula2//testpy//pythonhybrid//Screenshots"+"test_homepageTitle.png")
            self.driver.close()
            self.logger.error("********My Updates page is failed to load**************")
            assert False
        print(titleOfWebPage)
