from pages.LoginPage import Login
from data.TestData import *
import pytest

@pytest.mark.usefixtures("test_setup")
class TestLogin:
    def test_jenkinslogin(self):
        driver=self.driver
        lp=Login(driver)
        lp.jenkinslogin(USER_NAME,PASSWORD)

    #def test_logout():
        #driver.find_element_by_xpath("//b[text()='log out']").click()

    #global driver
    # Launch browser and navigate to url- section 1 >>S1
    #driver = webdriver.Chrome(executable_path="C:/Users/Rakshith Yenadka/PycharmProjects/POM_Automation2/drivers/chromedriver.exe")
    #driver.get("http://localhost:8080/login")

    # Logint to application - section 2 >>S2
    #driver.find_element_by_id("j_username").send_keys("madhuri")
    #driver.find_element_by_name("j_password").send_keys("rakmad035*")
    #driver.find_element_by_name("Submit").click()
