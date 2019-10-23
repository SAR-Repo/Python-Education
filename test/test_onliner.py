from selenium import webdriver
from login_page import LoginPage
from profile_page import ProfilePage

driver = webdriver.Chrome("../chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(5)

driver.get("https://onliner.by")

login_page = LoginPage(driver)
login_page.click_open()
login_page.enter_username('jeloxasa@mail-hub.top')
login_page.enter_password('P1234567890')
login_page.click_login()

profile_page = ProfilePage(driver)
profile_page.open_profile_popup()
print(profile_page.get_exit_button_text())
#assert "Выйти" in profile_page.get_exit_button_text

