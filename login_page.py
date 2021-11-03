import tkinter as tk
from PIL import Image, ImageTk

class Login_page(tk.Frame) :
	def __init__(self, parent, app) :
		self.settings = app.settings
		self.app = app

		super().__init__(parent)
		self.grid(row=0, column=0, sticky="nsew")

		parent.grid_columnconfigure(0, weight=1)
		parent.grid_rowconfigure(0, weight=1)

		self.background = "gray80"
		self.mainframe = tk.Frame(self, width =self.settings.width, height = self.settings.height, bg=self.background)
		self.mainframe.pack(fill="both", expand=True)

		self.pixel = tk.PhotoImage(width=1,height=1)

		self.create_logo()
		self.create_login_button()
		self.create_login_label()
		# self.create_sign_up_button()

	def create_logo(self) :
		self.logo = ImageTk.PhotoImage(Image.open(self.settings.logo_path))
		self.L_logo = tk.Label(self.mainframe, image=self.logo, bg=self.background)
		self.L_logo.grid(row=0, column=0, sticky="nsew", padx=11, columnspan=1, pady=30)

	def create_login_label(self) :
		self.username = tk.StringVar()
		self.password = tk.StringVar()

		self.L_username = tk.Label(self.mainframe, text="Username ",font = ("Times New Roman CE", 16),bg=self.background, fg="black")
		self.L_username.grid(row=1,column=0,padx=115,sticky="w")

		self.E_username = tk.Entry(self.mainframe,font = ("Times New Roman CE", 14),width=20, borderwidth=1, selectborderwidth=1, fg="gray20", textvariable=self.username)
		self.E_username.grid(row=2,column=0,sticky="w",padx=115)

		self.L_password = tk.Label(self.mainframe, text="Password ",font = ("Times New Roman CE", 16),bg=self.background, fg="black")
		self.L_password.grid(row=3,column=0,padx=115,sticky="w")

		self.E_password = tk.Entry(self.mainframe,font = ("Times New Roman CE", 14),width=20, borderwidth=1, selectborderwidth=1, fg="gray20", textvariable=self.password, show="*")
		self.E_password.grid(row=4,column=0,sticky="w",padx=115)

	def create_login_button(self) :
		self.B_login = tk.Button(self.mainframe, text="Login",font = ("Times New Roman CE", 18), command=lambda:self.app.login(), width=220,image=self.pixel, compound="c", bg="SkyBlue2", fg="white", borderwidth=0, activebackground ="RoyalBlue1",bd=0)
		self.B_login.grid(row=5, column=0, pady=30, columnspan=1)

	def create_sign_up_button(self) :
		self.B_sign_up = tk.Button(self.mainframe, text="Sign up",font = ("Times New Roman CE", 18), command=lambda:self.app.change_page("Home_page"), width=220,image=self.pixel, compound="c", bg="white", fg="gray50", borderwidth=0,bd=0)
		self.B_sign_up.grid(row=6,column=0)