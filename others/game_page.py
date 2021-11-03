import tkinter as tk
from PIL import Image, ImageTk
from blocks import *
from random import randint
from os import system

class Game_page(tk.Frame) :
	def __init__(self, parent, app) :
		self.settings = app.settings
		self.app =app

		super().__init__(parent)
		self.grid(row=0,column=0, sticky="nsew")

		self.mainframe = tk.Frame(self, width=self.settings.width, height =self.settings.height, bg="blue")
		self.mainframe.pack(fill="both", expand=True)
		self.pixel = tk.PhotoImage(width=1, height=1)

		self.current_block = None
		self.board =[]
		self.frame_count = 0

		self.show_background()
		self.game_frame()
		self.create_block_model()
		self.create_board()
		self.get_random_block()
		# self.make_background()
		self.show_blocks()
		self.move_button()

		# self.mainframe.grid_columnconfigure(0, weight=1)
		# self.mainframe.grid_rowconfigure(0, weight=1)

	def show_background(self) :
		self.background = ImageTk.PhotoImage(Image.open(self.settings.game_page_path))
		self.L_background = tk.Label(self.mainframe, image=self.background)
		self.L_background.grid()

	def game_frame(self) :
		self.F_game = tk.Frame(self.mainframe, bg="black", width=200, height=400)
		self.F_game.grid(row=0,column=0)
		# self.gameback = ImageTk.PhotoImage(Image.open(self.settings.play_path))
		# self.L_gameback = tk.Label(self.F_game, image=self.gameback)
		# self.L_gameback.grid(row=0,column=0)

		self.F_game.grid_columnconfigure(0,weight=10)
		self.F_game.grid_rowconfigure(0,weight=20)

	def create_block_model(self) :
		self.o_block = ImageTk.PhotoImage(Image.open(self.settings.o_block))
		self.l_block = ImageTk.PhotoImage(Image.open(self.settings.l_block))
		self.z_block = ImageTk.PhotoImage(Image.open(self.settings.z_block))
		self.t_block = ImageTk.PhotoImage(Image.open(self.settings.t_block))
		self.j_block = ImageTk.PhotoImage(Image.open(self.settings.j_block))
		self.i_block = ImageTk.PhotoImage(Image.open(self.settings.i_block))
		self.s_block = ImageTk.PhotoImage(Image.open(self.settings.s_block))
		self.black_block = ImageTk.PhotoImage(Image.open(self.settings.black_block))
	
	def get_random_block(self) :
		number = randint(0,6)
		# print(number)
		if number == 0 :
			self.current_block = O_block(self.board)
		elif number == 1 :
			self.current_block = L_block(self.board)
		elif number == 2 :
			self.current_block = Z_block(self.board)
		elif number == 3 :
			self.current_block = T_block(self.board)
		elif number == 4 :
			self.current_block = J_block(self.board)
		elif number == 5 :
			self.current_block = I_block(self.board)
		elif number == 6 :
			self.current_block = S_block(self.board)
		self.current_block.spawn()
		self.app.current_block = self.current_block

	def create_board(self) :
		for i in range(20) :
			self.board.append(["O"]*10)

	def run_game(self) :
		self.app.after(1000//self.settings.FPS,self.run_game)

		if self.frame_count == self.settings.FPS :
			self.frame_count = 0
			self.current_block.move_down()
			self.update_background_down()
		self.frame_count+=1

		self.show_blocks()
		
		# system("cls")
		# for every_row in self.board :
		# 	print(" ".join(every_row))

	def show_blocks(self) :
		blocks = []
		for bloc in blocks :
			bloc.destroy()
		for row in range(20) :
			for column in range(10) :
				
				if self.board[row][column] == "L" :
					block = tk.Label(self.F_game, image=self.l_block, width=20,height=20, borderwidth=0,  highlightthickness=0, bg="black")
					block.grid(row=row, column=column, sticky="w")
					blocks.append(block)
				elif self.board[row][column] == "0" :
					block = tk.Label(self.F_game, image=self.o_block, width=20,height=20, borderwidth=0,  highlightthickness=0, bg="black")
					block.grid(row=row, column=column, sticky="w")
					blocks.append(block)
				elif self.board[row][column] == "Z" :
					block = tk.Label(self.F_game, image=self.z_block, width=20,height=20, borderwidth=0,  highlightthickness=0, bg="black")
					block.grid(row=row, column=column, sticky="w")
					blocks.append(block)
				elif self.board[row][column] == "T" :
					block = tk.Label(self.F_game, image=self.t_block, width=20,height=20, borderwidth=0,  highlightthickness=0, bg="black")
					block.grid(row=row, column=column, sticky="w")
					blocks.append(block)
				elif self.board[row][column] == "J" :
					block = tk.Label(self.F_game, image=self.j_block, width=20,height=20, borderwidth=0,  highlightthickness=0, bg="black")
					block.grid(row=row, column=column, sticky="w")
					blocks.append(block)
				elif self.board[row][column] == "I" :
					block = tk.Label(self.F_game, image=self.i_block, width=20,height=20, borderwidth=0,  highlightthickness=0, bg="black")
					block.grid(row=row, column=column, sticky="w")
					blocks.append(block)
				elif self.board[row][column] == "S" :
					block = tk.Label(self.F_game, image=self.s_block, width=20,height=20, borderwidth=0,  highlightthickness=0, bg="black")
					block.grid(row=row, column=column, sticky="w")
					blocks.append(block)

	def update_background_down(self) :
		blocks = []
		for block in blocks :
			block.destroy()
		for i in range(4) :
			row = self.current_block.shapes[self.current_block.rotation][i][0] + self.current_block.row
			col = self.current_block.shapes[self.current_block.rotation][i][1] + self.current_block.col
			block = tk.Label(self.F_game, image=self.black_block, width=20,height=20, borderwidth=0,  highlightthickness=0, bg="black")
			block.grid(row=row-1, column=col, sticky="w")
			blocks.append(block)
			print("down = ", blocks)

	def update_background_left(self) :
		blocks = []
		for block in blocks :
			block.destroy()
		for i in range(4) :
			row = self.current_block.shapes[self.current_block.rotation][i][0] + self.current_block.row
			col = self.current_block.shapes[self.current_block.rotation][i][1] + self.current_block.col
			# if self.board[row][col+1] == "O" :
			block = tk.Label(self.F_game, image=self.black_block, width=20,height=20, borderwidth=0,  highlightthickness=0, bg="black")
			block.grid(row=row, column=col+1, sticky="w")
			blocks.append(block)
			self.show_blocks()
			print("left = ", blocks)

	def update_background_right(self) :
		blocks = []
		for block in blocks :
			block.destroy()
		for i in range(4) :
			row = self.current_block.shapes[self.current_block.rotation][i][0] + self.current_block.row
			col = self.current_block.shapes[self.current_block.rotation][i][1] + self.current_block.col
			# if self.board[row][col-1] == "O" :
			block = tk.Label(self.F_game, image=self.black_block, width=20,height=20, borderwidth=0,  highlightthickness=0, bg="black")
			block.grid(row=row, column=col-1, sticky="w")
			block.destroy()
			blocks.append(block)
			self.show_blocks()
			print("right = ", blocks)

	def make_background(self) :
		for row in range(20) :
			for column in range(10) :
				block = tk.Label(self.F_game, image=self.black_block, width=20,height=20, borderwidth=0,  highlightthickness=0, bg="black")
				block.grid(row=row, column=column, sticky="w")

	def move_left(self) :
		self.current_block.move_left()
		self.update_background_left()

	def move_right(self) :
		self.current_block.move_right()
		self.update_background_right()

	def keyboard_bind(self, event) :
		if event.char in ["a", "A", "\uf702"]:
			self.move_left()
		elif event.char in ["d", "D", "\uf703"]:
			self.move_right()

	def move_button(self) :
		self.B_left = tk.Button(self.mainframe, text="Left", command=self.move_left)
		self.B_left.grid(row=0, column=1,padx=100)
		self.B_right = tk.Button(self.mainframe, text="Right", command=self.move_right)
		self.B_right.grid(row=1, column=1,padx=100)