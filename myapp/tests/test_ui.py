from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import unittest

class MyUITests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def tearDown(self):
        self.driver.quit()

    def test_login_page(self):
        driver = self.driver
        driver.get("http://localhost:8000/")
        assert "Login" in driver.title

        # Ensure the form is present
        form = driver.find_element(By.TAG_NAME, 'form')
        assert form is not None

        # Fill out the form and submit
        password_input = driver.find_element(By.NAME, 'password')
        password_input.send_keys('testpassword')
        password_input.send_keys(Keys.RETURN)

if __name__ == "__main__":
    unittest.main()
