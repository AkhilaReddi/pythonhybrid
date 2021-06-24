from time import sleep

class Login:
    element_email = '//*[@id="idp-discovery-username"]'
    element_submit = '//*[@id="idp-discovery-submit"]'
    element_password = "password"
    element_oktasubmit = "//input[@id='okta-signin-submit']"
    element_input_box = " //*[@id='form2']/div[2]/input"
    element_verify = "//input[@value='Verify']"
    element_walkthrough_window = "//*[@title='Stop Walk-thru']"
    def __init__(self,driver):
        self.driver = driver
    def setuserName(self,email):
        sleep(20)
        #self.driver.find_element_by_name(self.element_email).clear()
        self.driver.find_element_by_xpath(self.element_email).send_keys(email)
        self.driver.find_element_by_xpath(self.element_submit).click()
    def setPassword(self,password):
        sleep(20)
        self.driver.find_element_by_name(self.element_password).send_keys(password)
        self.driver.find_element_by_xpath(self.element_oktasubmit).click()
        sleep(50)
        self.driver.find_element_by_xpath(self.element_input_box).click()
        sleep(70)
        #self.driver.find_element_by_xpath(self.element_verify).click()
        sleep(70)
        self.driver.switch_to.active_element
        self.driver.find_element_by_xpath(self.element_walkthrough_window).click()
        print('Loin succesfully')








