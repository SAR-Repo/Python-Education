from base_page import BasePage
from selenium.webdriver.common.by import By
import time

class ProfilePage(BasePage):
	BUTTON_EXIT=(By.XPATH, '//*[@id="userbar"]/div[1]/div[1]/div/div[1]/div[1]/div[2]/div/a')
	ICON_PROFILE=(By.XPATH, '//*[@id="userbar"]/div[1]/div[1]/a/div')

	def open_profile_popup(self):
		self.click_on(self.ICON_PROFILE)
		
	def get_exit_button_text(self):
		time.sleep(1)
		return self.get_element(self.BUTTON_EXIT).text
	
	def logout(self):
		self.click_on(self.BUTTON_EXIT)