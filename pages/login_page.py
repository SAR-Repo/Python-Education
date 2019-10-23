# -*- coding: utf-8 -*-
from base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
	FIELD_USERNAME = (By.XPATH, "//*[@placeholder='Ник или e-mail']") 
	FIELD_PASSWORD = (By.XPATH, "//*[@placeholder='Пароль']")
	BUTTON_LOGIN = (By.XPATH, '//*[@class="auth-button auth-button_primary auth-button_middle auth-form__button auth-form__button_width_full"]')
	BUTTON_PROFILE = (By.XPATH, '//*[@id="userbar"]/div[1]/div/div/div[1]')

	def enter_username(self, username): 
		self.type_in(self.FIELD_USERNAME, username)

	def enter_password(self, password): 
		self.type_in(self.FIELD_PASSWORD, password)

	def click_login(self): 
		self.click_on(self.BUTTON_LOGIN)

	def click_open(self):
		self.click_on(self.BUTTON_PROFILE)
