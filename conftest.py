import pytest


@pytest.fixture(scope='class')
def test_setup(request):
    from selenium import webdriver
    driver = webdriver.Chrome(
        executable_path="C:/Users/Rakshith Yenadka/PycharmProjects/POM_Automation2/drivers/chromedriver.exe")
    driver.get("http://localhost:8080/login")
    driver.implicitly_wait(30)
    request.cls.driver = driver
