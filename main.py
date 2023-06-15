import tkinter as tk
import time
from tkinter import messagebox


from settings import Settings
from login_page import Login_page
from home_page import Home_page
from game_page2 import Game_page
from htp import htp1, htp2, htp3
from leaderboard import Leaderboard

class MainWindow(tk.Tk) :
	def __init__(self, app) :
		self.settings = app.settings
		self.app = app
		super().__init__()

		self.title(self.settings.title)
		self.geometry(self.settings.screen)
		self.resizable(0,0)

		self.create_container()
		self.pages = {}
		self.create_htp_page()
		self.create_leaderboard()
		self.create_home_page()
		self.create_game_page()
		self.create_login_page()

	def create_container(self) :
		self.container = tk.Frame(bg="grey")
		self.container.pack(fill="both", expand=True)

	def create_login_page(self) :
		self.pages["login_page"] = Login_page(self.container, self)

	def create_home_page(self) :
		self.pages["Home_page"] = Home_page(self.container, self)

	def create_game_page(self) :
		self.pages["Game_page"] = Game_page(self.container, self)

	def create_htp_page(self) :
		self.pages["htp1"] = htp1(self.container, self)
		self.pages["htp2"] = htp2(self.container, self)
		self.pages["htp3"] = htp3(self.container, self)

	def create_leaderboard(self) :
		self.pages["Leaderboard"] = Leaderboard(self.container, self)
		
	def change_page(self, page) :
		page2 = self.pages[page]
		page2.tkraise()
		
		if page == "Game_page" :
			self.bind("<Key>", self.pages["Game_page"].keyboard_bind)
			self.pages["Game_page"].run_game()
		elif page == "Leaderboard" :
			self.pages["Leaderboard"].run()

	def login(self) :
		username = self.pages["login_page"].username.get()
		password = self.pages["login_page"].password.get()
		match = self.settings.login(username,password)
		if match :
			self.change_page("Home_page")
		else :
			# tk.messagebox.showerror(title="Login Error!", message="Wrong username or password!")
			messagebox.showerror("Login Error!", "Wrong username or password!")

class App :
	def __init__(self) :
		self.settings = Settings()
		self.main_window = MainWindow(self)

	def run(self) :
		self.main_window.mainloop()

if __name__ == "__main__" :
	MyApp = App()
	MyApp.run()