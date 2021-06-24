import pytest
from selenium import webdriver
import os

@pytest.fixture(scope="class")
def setup(browser,request):
    if browser == 'chrome':
        chromedriver = "C:\\Users\\aravula2\\OneDrive - DXC Production\\Desktop\\Akhila Documents\\2020\\Selenium\\chromedriver.exe"
        os.environ["webdriver.chrome.driver"] = chromedriver
        driver = webdriver.Chrome(chromedriver)
        request.cls.driver = driver
        print("Launching chrome browser")
    elif browser == 'firefox':
         driver= webdriver.Firefox(0)
         request.cls.driver = driver
         print("Launching Firefox browser")
    return driver
#pytest -s -v TestCases/Test_login.py --browser chrome
def pytest_addoption(parser):
    parser.addoption('--browser')

@pytest.fixture(scope="class")
def browser(request):
    return request.config.getoption('--browser')

##########pyTest Html report###################
def pytest_configure(config):
    config._metadata['Project Name'] = 'ZRA Web Application'
    config._metadata['Module Name'] = 'Zurich Risk Advisor Tab'
    config._metadata["Tester"] = "Akhila Reddy Ravula"

### It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)
