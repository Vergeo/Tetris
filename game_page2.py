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

		self.mainframe = tk.Frame(self, width=self.settings.width, height =self.settings.height, bg="gray20")
		self.mainframe.pack(fill="both", expand=True)
		self.pixel = tk.PhotoImage(width=1, height=1)

		self.current_block = None
		self.hold = 0
		self.board =[]
		self.blocks = []
		self.next = [[None, None], [None, None],[None, None], [None, None]]
		self.frame_count = 0
		self.score = 0
		self.lose = False

		self.leaderboard = self.settings.load_data(self.settings.leaderboard_path)

		self.L_game_over = tk.Label()
		self.B_back_to_home = tk.Button()

		# self.lost()

	def create_logo(self) :
		self.logo = ImageTk.PhotoImage(Image.open(self.settings.logo_path2))
		self.L_logo = tk.Label(self.mainframe, image=self.logo, bg="gray20")
		self.L_logo.grid(row=0, column=0, sticky="nsew", columnspan=32, pady=10)

	def show_background(self) :
		self.background = ImageTk.PhotoImage(Image.open(self.settings.play_path))
		self.L_background = tk.Label(self.mainframe, image=self.background,borderwidth=0, bg="gray20")
		self.L_background.grid(row=1,column=1,rowspan=5)

	def game_frame(self) :
		self.F_game = tk.Frame(self.mainframe, bg="black", width=200, height=400)
		self.F_game.grid(row=1,column=1,rowspan=5)
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

		self.o_block_back = ImageTk.PhotoImage(Image.open(self.settings.o_block_back))
		self.l_block_back = ImageTk.PhotoImage(Image.open(self.settings.l_block_back))
		self.z_block_back = ImageTk.PhotoImage(Image.open(self.settings.z_block_back))
		self.t_block_back = ImageTk.PhotoImage(Image.open(self.settings.t_block_back))
		self.j_block_back = ImageTk.PhotoImage(Image.open(self.settings.j_block_back))
		self.i_block_back = ImageTk.PhotoImage(Image.open(self.settings.i_block_back))
		self.s_block_back = ImageTk.PhotoImage(Image.open(self.settings.s_block_back))
		self.empty_back = ImageTk.PhotoImage(Image.open(self.settings.empty_back))
	
	def get_random_block(self) :
		number = randint(0,6)
		# print(number)
		if number == 0 :
			block = O_block(self.board)
			init = "O"
		elif number == 1 :
			block = L_block(self.board)
			init = "L"
		elif number == 2 :
			block = Z_block(self.board)
			init = "Z"
		elif number == 3 :
			block = T_block(self.board)
			init = "T"
		elif number == 4 :
			block = J_block(self.board)
			init = "J"
		elif number == 5 :
			block = I_block(self.board)
			init = "I"
		elif number == 6 :
			block = S_block(self.board)
			init = "S"
		# self.current_block = O_block(self.board)
		# block.spawn()
		return block, init

	def create_board(self) :
		for i in range(20) :
			self.board.append(["O"]*10)

	def run_game(self) :
		self.current_block = None
		self.hold = 0
		self.board =[]
		self.blocks = []
		self.next = [[None, None], [None, None],[None, None], [None, None]]
		self.frame_count = 0
		self.score = 0
		self.lose = False
		self.L_game_over.destroy()
		self.B_back_to_home.destroy()

		self.create_logo()
		self.show_background()
		self.game_frame()
		self.create_block_model()
		self.create_board()
		# print(self.get_random_block())
		self.current_block,temp = self.get_random_block()
		self.current_block.spawn()
		self.make_background()
		self.make_next_block()
		self.show_score()
		self.show_blocks()
		self.show_next_block()
		self.loop()

	def loop(self) :
		if self.frame_count == self.settings.FPS :
			self.frame_count = 0
			self.current_block.move_down()
			if self.current_block.finish :
				self.current_block_finish()
		self.frame_count+=1

		self.show_blocks()

		if self.lose :	
			self.lost()
		else :
			self.app.after(1000//self.settings.FPS,self.loop)
		
		system("cls")
		for every_row in self.board :
			print(" ".join(every_row))

	def show_blocks(self) :
		blocks = []
		for bloc in blocks :
			bloc.destroy()
		for row in range(20) :
			for column in range(10) :
				if self.board[row][column] == "O" :
					self.blocks[row][column].configure(image=self.black_block)
				elif self.board[row][column] == "L" or self.board[row][column] == "LN" :
					self.blocks[row][column].configure(image=self.l_block)
				elif self.board[row][column] == "0" or self.board[row][column] == "0N" :
					self.blocks[row][column].configure(image=self.o_block)
				elif self.board[row][column] == "Z" or self.board[row][column] == "ZN" :
					self.blocks[row][column].configure(image=self.z_block)
				elif self.board[row][column] == "T" or self.board[row][column] == "TN" :
					self.blocks[row][column].configure(image=self.t_block)
				elif self.board[row][column] == "J" or self.board[row][column] == "JN" :
					self.blocks[row][column].configure(image=self.j_block)
				elif self.board[row][column] == "I" or self.board[row][column] == "IN" :
					self.blocks[row][column].configure(image=self.i_block)
				elif self.board[row][column] == "S" or self.board[row][column] == "SN" :
					self.blocks[row][column].configure(image=self.s_block)
		self.update_score()

	def make_background(self) :
		for row in range(20) :
			self.blocks.append([])
			for column in range(10) :
				block = tk.Label(self.F_game, image=self.black_block, width=20,height=20, borderwidth=0,  highlightthickness=0, bg="black")
				block.grid(row=row+1, column=column, sticky="w")
				self.blocks[row].append(block)

	def keyboard_bind(self, event) :
		if not self.lose :
			if event.char in ["a", "A", "\uf702"]:
				self.current_block.move_left()
				self.show_blocks()
			elif event.char in ["d", "D", "\uf703"]:
				self.current_block.move_right()
				self.show_blocks()
			elif event.char in ["w", "W", "\uf701"]:
				self.current_block.rotate()
				self.show_blocks()
			elif event.char in ["s", "S", "\uf700"]:
				# self.current_block.move_down()
				self.s_button_pushed()
				self.show_blocks()
			elif event.char in ["f", "F"]:
				self.holds()
				self.show_hold()
				# self.show_blocks()

	def s_button_pushed(self) :
		status = self.current_block.move_down()
		self.show_blocks()
		if status :
			self.score+=1

	def move_button(self) :
		self.B_left = tk.Button(self.mainframe, text="Left", command=self.current_block.move_left)
		self.B_left.grid(row=1, column=1,padx=100)
		self.B_right = tk.Button(self.mainframe, text="Right", command=self.current_block.move_right)
		self.B_right.grid(row=2, column=1,padx=100)

	def clear_line (self) :
		for row in range(20) :
			row=19-row
			line_status = True
			for elem in self.board[row] :
				if elem == "O" :
					line_status = False
			if line_status :
				self.score += 100
				self.board.pop(row)
				self.board.append(["O"]*10)
				for row2 in range(20) :
					self.board[19-row2] = self.board[18-row2]
				self.board[0] = ["O"]*10
				self.current_block.row +=1
				# self.current_block.col -=1
				# continue
				self.clear_line()

	def holds(self) :
		# print(self.hold)
		# print(self.current_block)
		row = self.current_block.row
		column = self.current_block.col
		if self.hold == 0 :
			# self.current_block.finish = True
			self.current_block.delete()
			self.hold = self.current_block
			self.current_block_finish(hold=True)
			# self.current_block.row = row
			# self.current_block.col = column
			self.current_block.show()
			self.show_blocks()
			
		else :
			self.current_block.delete()
			temp = self.current_block
			self.current_block = self.hold
			self.current_block.row = row
			self.current_block.col = column
			self.hold = temp
			self.current_block.show()
			self.show_blocks()

	def make_next_block(self) :
		self.L_next = tk.Label(self.mainframe,text="Next", font=("Arial",20,"bold"), bg="gray20", fg="white")
		self.L_next.grid(row=1,column=2,padx=7)
		self.next[0][0],self.next[0][1] = self.get_random_block()
		self.next[1][0],self.next[1][1] = self.get_random_block()
		self.next[2][0],self.next[2][1] = self.get_random_block()
		self.next[3][0],self.next[3][1] = self.get_random_block()

		self.L_hold = tk.Label(self.mainframe,text="Hold", font=("Arial",20,"bold"), bg="gray20", fg="white")
		self.L_hold.grid(row=1,column=0,padx=7)
		self.L_hold_block = tk.Label(self.mainframe, bg="gray20", image =self.empty_back)
		self.L_hold_block.grid(column=0, row =2, padx=7)

	def current_block_finish(self, hold=False) :
		if not hold :
			self.check_lose()
		self.current_block = self.next[0][0]
		self.next[0][0],self.next[0][1] = self.next[1][0],self.next[1][1]
		self.next[1][0],self.next[1][1] = self.next[2][0],self.next[2][1]
		self.next[2][0],self.next[2][1] = self.next[3][0],self.next[3][1]
		self.next[3][0],self.next[3][1] = self.get_random_block()
		self.show_next_block()
		self.current_block.spawn()
		self.clear_line()

	def show_next_block(self) :
		self.L_next_blocks = []

		for i in range(4) :
			self.L_next_block = tk.Label(self.mainframe,text="Next", bg="gray20")
			self.L_next_block.grid(row=i+2, column=2,padx=7)
			self.L_next_blocks.append(self.L_next_block)

		for i in range(4) :
			if self.next[i][1] == "O" :
				self.L_next_blocks[i].configure(text="O",image=self.o_block_back)
			elif self.next[i][1] == "L" :
				self.L_next_blocks[i].configure(text="L",image=self.l_block_back)
			elif self.next[i][1] == "Z" :
				self.L_next_blocks[i].configure(text="Z",image=self.z_block_back)
			elif self.next[i][1] == "T" :
				self.L_next_blocks[i].configure(text="T",image=self.t_block_back)
			elif self.next[i][1] == "J" :
				self.L_next_blocks[i].configure(text="J",image=self.j_block_back)
			elif self.next[i][1] == "I" :
				self.L_next_blocks[i].configure(text="I",image=self.i_block_back)
			elif self.next[i][1] == "S" :
				self.L_next_blocks[i].configure(text="S",image=self.s_block_back)

	def show_hold(self) :
		if self.hold.initial == "0" :
			self.L_hold_block.configure(image=self.o_block_back)
		elif self.hold.initial == "L" :
			self.L_hold_block.configure(image=self.l_block_back)
		elif self.hold.initial == "Z" :
			self.L_hold_block.configure(image=self.z_block_back)
		elif self.hold.initial == "T" :
			self.L_hold_block.configure(image=self.t_block_back)
		elif self.hold.initial == "J" :
			self.L_hold_block.configure(image=self.j_block_back)
		elif self.hold.initial == "I" :
			self.L_hold_block.configure(image=self.i_block_back)
		elif self.hold.initial == "S" :
			self.L_hold_block.configure(image=self.s_block_back)

	def show_score(self) :
		self.L_score = tk.Label(self.mainframe, text="Score", bg="gray20", fg="white", font=("Arial",20,"bold"))
		self.L_score.grid(column=0, row=3, padx=7)

		self.L_score_back = tk.Label(self.mainframe, bg="gray20", image=self.empty_back)
		self.L_score_back.grid(column=0, row=4, padx=7)

		self.L_score_score = tk.Label(self.mainframe, text=self.score, bg="slateblue3",fg="white", font=("Arial",14,"bold"))
		self.L_score_score.grid(column=0, row=4, padx=7)

	def update_score(self) :
		self.L_score_score.configure(text=self.score)

	def check_lose(self) :
		if self.current_block.row == 0 :
			self.lose = True

	def back_to_home(self) :
		self.app.change_page("Home_page")

	def lost(self) :
		self.L_game_over = tk.Label(self.mainframe, text="Game\nOver", font=("Arial",30,"bold"), bg="gray30", borderwidth=2)
		self.L_game_over.grid(columnspan=3, column=0, row=2)

		self.var_name = tk.StringVar()

		self.L_name = tk.Label(self.mainframe, text="Name : ", font=("Arial", 12, "bold"), bg="gray20", fg="white")
		self.L_name.grid(row=6, column=0, pady=10)

		self.E_name = tk.Entry(self.mainframe, font=("Arial", 12), textvariable=self.var_name)
		self.E_name.grid(row=6, column=1, pady=10,sticky="w")

		self.B_save = tk.Button(self.mainframe, text="Save", font=("Arial", 12, "bold"), command=self.save)
		self.B_save.grid(row=6,column=2, columnspan=2, pady=10)
		
	def save(self) :
		self.name = self.var_name.get()
		self.leaderboard.append({self.name :{"score" : self.score, "block" :0}})
		self.settings.save_data(self.leaderboard, self.settings.leaderboard_path)
		self.app.change_page("Home_page")