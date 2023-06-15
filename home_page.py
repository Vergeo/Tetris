import tkinter as tk
from PIL import Image, ImageTk
import sys

class Home_page(tk.Frame) :
	def __init__(self, parent, app) :
		self.settings = app.settings
		self.app = app

		super().__init__(parent)
		self.grid(row=0, column=0, sticky="nsew")

		self.mainframe = tk.Frame(self, width =self.settings.width, height = self.settings.height, bg="gray70")
		self.mainframe.pack(fill="both", expand=True)

		self.create_logo()
		self.create_button()

	def quit_game(self) :
		sys.exit()

	def create_button(self) :
		self.B_start = tk.Button(self.mainframe, text="Start",font = ("Arial", 16, "bold"), command=lambda:self.app.change_page("Game_page"), bg="gray60", bd=1, fg="white", width=15,height=1)
		self.B_start.pack(pady=10)

		self.B_htp = tk.Button(self.mainframe, text="How to Play",font = ("Arial", 16, "bold"), bg="gray60", bd=1, fg="white",height=1, width=15, command=self.htp)
		self.B_htp.pack(pady=10)

		self.B_leaderboard = tk.Button(self.mainframe, text="Leaderboard",font = ("Arial", 16, "bold"), bg="gray60", bd=1, fg="white",height=1, width=15, command=self.leaderboard)
		self.B_leaderboard.pack(pady=10)

		self.B_quit = tk.Button(self.mainframe, text="Quit",font = ("Arial", 16, "bold"), bg="gray60", bd=1, fg="white",height=1, width=15, command=self.quit_game)
		self.B_quit.pack(pady=10)

	def create_logo(self) :
		self.logo = ImageTk.PhotoImage(Image.open(self.settings.logo_path))
		self.L_logo = tk.Label(self.mainframe, image=self.logo, bg="gray70")
		self.L_logo.pack(pady=30)

	def htp(self) :
		self.app.change_page("htp1")

	def leaderboard(self) :
		self.app.change_page("Leaderboard")
		