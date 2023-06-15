import tkinter as tk
from PIL import Image, ImageTk

class htp1(tk.Frame) :
	def __init__(self, parent, app) :
		self.settings = app.settings
		self.app =app

		super().__init__(parent)
		self.grid(row=0, column=0, sticky="nsew")

		self.image = ImageTk.PhotoImage(Image.open(self.settings.htp1))
		self.L_htp1 = tk.Label(self, image=self.image, borderwidth=0, bd=0)
		self.L_htp1.grid(row=0, column=0)

		self.B_next = tk.Button(self, text="Next", command=self.next,font = ("Arial", 16, "bold"))
		self.B_next.grid(row=0, column=0, sticky="es", pady=10, padx=10)

	def next(self) :
		self.app.change_page("htp2")

class htp2(tk.Frame) :
	def __init__(self, parent, app) :
		self.settings = app.settings
		self.app =app

		super().__init__(parent)
		self.grid(row=0, column=0, sticky="nsew")

		self.image = ImageTk.PhotoImage(Image.open(self.settings.htp2))
		self.L_htp2 = tk.Label(self, image=self.image, borderwidth=0)
		self.L_htp2.grid(row=0, column=0)

		self.B_next = tk.Button(self, text="Next", command=self.next,font = ("Arial", 16, "bold"))
		self.B_next.grid(row=0, column=0, sticky="es", pady=10, padx=10)

	def next(self) :
		self.app.change_page("htp3")

class htp3(tk.Frame) :
	def __init__(self, parent, app) :
		self.settings = app.settings
		self.app =app

		super().__init__(parent)
		self.grid(row=0, column=0, sticky="nsew")

		self.image = ImageTk.PhotoImage(Image.open(self.settings.htp3))
		self.L_htp3 = tk.Label(self, image=self.image, borderwidth=0)
		self.L_htp3.grid(row=0, column=0)

		self.B_next = tk.Button(self, text="Finish", command=self.next,font = ("Arial", 16, "bold"))
		self.B_next.grid(row=0, column=0, sticky="es", pady=10, padx=10)

	def next(self) :
		self.app.change_page("Home_page")