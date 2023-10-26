import time

from selenium import webdriver

from Src.Pages.LandingPage import LandingPage
from Src.Pages.RegPage import RegPage
from Src.Pages.LoginPage import LoginPage
from Src.Pages.ProductPage import ProductPage
from Src.Pages.OrderPage import OrderPage

from Src.Pages.CartPage import CartPage

driver = webdriver.Firefox()

driver.get("http://shop.icraftsoft.net:8095/")
driver.maximize_window()

# Landing Page
lp = LandingPage(driver)  # object create
lp.click_signin()
time.sleep(3)

# Register username and password
rg = RegPage(driver)
rg.getUsername()
rg.getEmail()
rg.getButton()

time.sleep(3)

# Login page
lg = LoginPage(driver)
lg.get_login()
time.sleep(2)
lg.login_textbox()
time.sleep(2)
lg.click_login()
time.sleep(2)
lg.click_home()
time.sleep(2)
lg.login_textbox2()
time.sleep(2)
lg.get_login_again()
time.sleep(2)

# ProductPage
pp = ProductPage(driver)
pp.search_box()
time.sleep(2)
pp.add_to_cart()
time.sleep(2)

# cart page
cart = CartPage(driver)
time.sleep(2)
cart.click_on_cart()
time.sleep(2)
cart.click_buy_now()
time.sleep(2)


# OrderPage
PO = OrderPage(driver)
time.sleep(2)
PO.remove_items()
time.sleep(2)
PO.click_on_Buy_now()
time.sleep(2)
PO.click_on_home()