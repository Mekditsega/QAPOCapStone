from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class ProductPage:
    def __init__(self, driver):  # this method is called when object of the class is created
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)  # implicity define time sleep

    def search_box(self):
        try:
            submit_button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//input[contains(@type,'search')]"))
            )
            assert submit_button.is_displayed(), "search textbox is not displayed on the page."
            submit_button.send_keys("acer pc")

        except Exception as e:
            print(f"Assertion failed: {e}")

    # def Quick_view_product(self):
    #     try:
    #         submit_button = WebDriverWait(self.driver, 10).until(
    #             EC.presence_of_element_located((By.XPATH, "(//button[@type='button'])[2]"))
    #         )
    #         assert submit_button.is_displayed(), "product textbox is not displayed on the page."
    #         submit_button.click()
    #
    #     except Exception as e:
    #         print(f"Assertion failed: {e}")

    # def select_product1(self):
    #     try:
    #         submit_button = WebDriverWait(self.driver, 10).until(
    #                 EC.presence_of_element_located((By.XPATH, "(//select[contains(@class,'form-control')])[5]"))
    #             )
    #         assert submit_button.is_displayed(), "search textbox is not displayed on the page."
    #         submit_button.send_keys(Keys.ARROW_DOWN)
    #         submit_button.send_keys(Keys.ARROW_DOWN)
    #         submit_button.send_keys(Keys.ARROW_DOWN).click()
    #     except Exception as e:
    #         print(f"Assertion failed: {e}")

    def add_to_cart(self):
        try:
            add_cart = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "(//button[contains(@type,'submit')])[1]"))
            )
            assert add_cart.is_displayed(), "search textbox is not displayed on the page."
            add_cart.click()
        except Exception as e:
            print(f"Assertion failed: {e}")

    # def second_cart(self):
    #     try:
    #
    #         adcart = WebDriverWait(self.driver, 3).until(
    #             EC.presence_of_element_located((By.XPATH, "(//button[contains(@class,'btn btn-primary')])[1]"))
    #         )
    #         assert adcart.is_displayed(), "search textbox is not displayed on the page."
    #         adcart.click()
    #     except Exception as e:
    #         print(f"Assertion failed: {e}")