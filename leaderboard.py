import tkinter as tk
from PIL import Image, ImageTk
import tkinter.ttk as ttk
import tkinter.font as tkFont

class Leaderboard(tk.Frame) :
	def __init__(self, parent, app) :
		self.settings = app.settings
		self.app = app

		super().__init__(parent)
		self.grid(column=0, row=0, sticky="nsew")
		self.background = "gray50"

		self.mainframe = tk.Frame(self, bg=self.background, width = self.settings.width, height = self.settings.height)
		self.mainframe.pack(fill="both", expand=True)

		self.get_leaderboard_data()
		self.create_logo()
		self.create_content()
		self.create_return_button()

	def run(self) :
		self.get_leaderboard_data()
		self.create_logo()
		self.create_content()
		self.create_return_button()

	def create_logo(self) :
		self.logo = ImageTk.PhotoImage(Image.open(self.settings.leaderboard_logo))
		self.L_logo = tk.Label(self.mainframe, image=self.logo, bg=self.background)
		self.L_logo.grid(row=1, column=0, sticky="nsew", padx=11, columnspan=1, pady=4)

	def create_content(self) :
		# self.L_title = tk.Label(self.mainframe,text="Name\t\t\tScore", height=1, bd=0, font=("Arial", 16))
		# self.L_title.grid(column=0, row=2, sticky="nsew", padx=14)

		# self.LB_leaderboard = tk.Listbox(self.mainframe,width=70, height=25, bd=0)
		# self.LB_leaderboard.grid(column=0, row=3, sticky="nsew", padx=14)

		# for row in self.leaderboard :
		# 	print(row)
		# 	for name, detail in row.items() :
		# 		score = detail["score"]
		# 		namescore = f"{name}\t\t\t\t{score}"
		# 		namescore2 = namescore
		# 		print(namescore)
		# 		self.LB_leaderboard.insert("end", namescore2)

		style = ttk.Style()
		style.configure("MyStyle.Treeview", highlightthickness=0, bd=0, font=('Calibri', 11))

		self.T_leaderboard = ttk.Treeview(self.mainframe, columns=self.header, show="headings", height=20, style="MyStyle.Treeview")
		self.T_leaderboard.grid(column=0, row=2, sticky="nsew", padx=25)

		for col in self.header :
			self.T_leaderboard.heading(col, text=col.title())
		for item in self.leaderboard :
			self.T_leaderboard.insert('', 'end', values=item)

	def get_leaderboard_data(self) :
		board = self.settings.load_data(self.settings.leaderboard_path)
		self.leaderboard = []
		for row in board :
			for name, detail in row.items() :
				score = detail["score"]
				tuples = (name, score)
				self.leaderboard.append(tuples)
		self.header = ["Name", "Score"]

	def create_return_button(self) :
		self.B_return = tk.Button(self.mainframe, text="Return", font=("Arial",13), command=lambda:self.app.change_page("Home_page"))
		self.B_return.grid(column=0, row=3, pady=5)