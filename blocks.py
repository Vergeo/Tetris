import tkinter as tk
from time import sleep

class L_block :
	def __init__(self, board) :
		self.rotation = 0
		self.initial = "L"
		self.board = board
		self.shapes =	([(0,2),(1,0),(1,1),(1,2)],
						[(0,1),(1,1),(2,1),(2,2)],
						[(1,0),(1,1),(1,2),(2,0)],
						[(0,0),(0,1),(1,1),(2,1)])
		self.row = 0
		self.col = 3
		self.finish = False

	def spawn(self) :
		for i in range(4) :
			self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "LN"

	def move_down(self) :
		rows = []
		for i in range(4) :
			rows.append(self.shapes[self.rotation][i][0])

		if (max(rows)+self.row+1>=20) :
			self.finish = True
		
		if not self.finish :
			for i in range(4) :
				if self.board[self.shapes[self.rotation][i][0]+self.row+1][self.shapes[self.rotation][i][1]+self.col] != "O" and self.board[self.shapes[self.rotation][i][0]+self.row+1][self.shapes[self.rotation][i][1]+self.col] != f"{self.initial}N" :
					self.finish = True

		if not self.finish :
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "O"
			self.row +=1
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "LN"
			return True

		if self.finish :
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = self.initial

	def rotate(self) :
		condition = True
		if self.rotation == 3 :
			for i in range(4) :
				if ((self.row+self.shapes[0][i][0] < 20 and self.col+self.shapes[0][i][1] < 10) and (self.row+self.shapes[0][i][0] >= 0 and self.col+self.shapes[0][i][1] >=0)) :
					if not(self.board[self.row+self.shapes[0][i][0]][self.col+self.shapes[0][i][1]] == "O" or self.board[self.row+self.shapes[0][i][0]][self.col+self.shapes[0][i][1]] == f"{self.initial}N" ) :
						condition = False
				else :
					condition = False
		else :
			for i in range(4) :
				if ((self.row+self.shapes[self.rotation+1][i][0] < 20 and self.col+self.shapes[self.rotation+1][i][1] < 10) and (self.row+self.shapes[self.rotation+1][i][0] >= 0 and self.col+self.shapes[self.rotation+1][i][1] >=0)) :
					if not(self.board[self.row+self.shapes[self.rotation+1][i][0]][self.col+self.shapes[self.rotation+1][i][1]] == "O"or self.board[self.row+self.shapes[self.rotation+1][i][0]][self.col+self.shapes[self.rotation+1][i][1]] == f"{self.initial}N") :
						condition = False
				else :
					condition = False
		if condition :
			for i in range(4) :
					self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "O"
			if self.rotation == 3 :
				self.rotation = 0
			else :
				self.rotation +=1
			for i in range(4) :
					self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = f"{self.initial}N"

	def move_left(self) :
		status = True
		cols = []
		for i in range(4) :
			cols.append(self.shapes[self.rotation][i][1])

		if not(min(cols)+self.col-1<0) :
			for i in range(4) :
				if not(self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]-1]=="O" or (self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]-1] == f"{self.initial}N")) :
					status=False

		if not(min(cols)+self.col-1<0) and status :
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "O"
			self.col -=1
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "LN"

	def move_right(self) :
		status = True
		cols = []
		for i in range(4) :
			cols.append(self.shapes[self.rotation][i][1])
			
		for i in range(4) :
			if not(max(cols)+self.col+1>=10) :
				if not(self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]+1]=="O" or (self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]+1] == f"{self.initial}N")) :
					status=False

		if not(max(cols)+self.col+1>=10) and status:
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "O"
			self.col +=1
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "LN"

	def delete(self) :
		for i in range(4) :
			self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "O"

	def show(self) :
		for i in range(4) :
			self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = f"{self.initial}N"

class J_block :
	def __init__(self, board) :
		self.rotation = 0
		self.initial = "J"
		self.board = board
		self.shapes =	([(0,0),(1,0),(1,1),(1,2)],
						[(0,1),(0,2), (1,1),(2,1)],
						[(1,0),(1,1),(1,2),(2,2)],
						[(0,1),(1,1),(2,0),(2,1)])
		self.row = 0
		self.col = 3
		self.finish = False

	def spawn(self) :
		for i in range(4) :
			self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "JN"

	def move_down(self) :
		rows = []
		for i in range(4) :
			rows.append(self.shapes[self.rotation][i][0])

		if (max(rows)+self.row+1>=20) :
			self.finish = True
		
		if not self.finish :
			for i in range(4) :
				if self.board[self.shapes[self.rotation][i][0]+self.row+1][self.shapes[self.rotation][i][1]+self.col] != "O" and self.board[self.shapes[self.rotation][i][0]+self.row+1][self.shapes[self.rotation][i][1]+self.col] != f"{self.initial}N" :
					self.finish = True

		if not self.finish :
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "O"
			self.row +=1
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "JN"
			return True

		if self.finish :
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = self.initial

	def rotate(self) :
		condition = True
		if self.rotation == 3 :
			for i in range(4) :
				if ((self.row+self.shapes[0][i][0] < 20 and self.col+self.shapes[0][i][1] < 10) and (self.row+self.shapes[0][i][0] >= 0 and self.col+self.shapes[0][i][1] >=0)) :
					if not(self.board[self.row+self.shapes[0][i][0]][self.col+self.shapes[0][i][1]] == "O" or self.board[self.row+self.shapes[0][i][0]][self.col+self.shapes[0][i][1]] == f"{self.initial}N" ) :
						condition = False
				else :
					condition = False
		else :
			for i in range(4) :
				if ((self.row+self.shapes[self.rotation+1][i][0] < 20 and self.col+self.shapes[self.rotation+1][i][1] < 10) and (self.row+self.shapes[self.rotation+1][i][0] >= 0 and self.col+self.shapes[self.rotation+1][i][1] >=0)) :
					if not(self.board[self.row+self.shapes[self.rotation+1][i][0]][self.col+self.shapes[self.rotation+1][i][1]] == "O"or self.board[self.row+self.shapes[self.rotation+1][i][0]][self.col+self.shapes[self.rotation+1][i][1]] == f"{self.initial}N") :
						condition = False
				else :
					condition = False
		if condition :
			for i in range(4) :
					self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "O"
			if self.rotation == 3 :
				self.rotation = 0
			else :
				self.rotation +=1
			for i in range(4) :
					self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = f"{self.initial}N"

	def move_left(self) :
		status = True
		cols = []
		for i in range(4) :
			cols.append(self.shapes[self.rotation][i][1])

		if not(min(cols)+self.col-1<0) :
			for i in range(4) :
				if not(self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]-1]=="O" or (self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]-1] == f"{self.initial}N")) :
					status=False

		if not(min(cols)+self.col-1<0) and status :
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "O"
			self.col -=1
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "JN"

	def move_right(self) :
		status = True
		cols = []
		for i in range(4) :
			cols.append(self.shapes[self.rotation][i][1])
			
		for i in range(4) :
			if not(max(cols)+self.col+1>=10) :
				if not(self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]+1]=="O" or (self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]+1] == f"{self.initial}N")) :
					status=False

		if not(max(cols)+self.col+1>=10) and status:
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "O"
			self.col +=1
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "JN"

	def delete(self) :
		for i in range(4) :
			self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "O"

	def show(self) :
		for i in range(4) :
			self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = f"{self.initial}N"

class I_block :
	def __init__(self, board) :
		self.rotation = 0
		self.initial = "I"
		self.board = board
		self.shapes =	([(1,0),(1,1),(1,2),(1,3)],
						[(0,2),(1,2),(2,2),(3,2)],
						[(2,0),(2,1),(2,2),(2,3)],
						[(0,1),(1,1),(2,1),(3,1)])
		self.row = 0
		self.col = 2
		self.finish = False

	def spawn(self) :
		for i in range(4) :
			self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "IN"

	def move_down(self) :
		rows = []
		for i in range(4) :
			rows.append(self.shapes[self.rotation][i][0])

		if (max(rows)+self.row+1>=20) :
			self.finish = True
		
		if not self.finish :
			for i in range(4) :
				if self.board[self.shapes[self.rotation][i][0]+self.row+1][self.shapes[self.rotation][i][1]+self.col] != "O" and self.board[self.shapes[self.rotation][i][0]+self.row+1][self.shapes[self.rotation][i][1]+self.col] != f"{self.initial}N" :
					self.finish = True

		if not self.finish :
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "O"
			self.row +=1
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "IN"
			return True

		if self.finish :
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = self.initial

	def rotate(self) :
		condition = True
		if self.rotation == 3 :
			for i in range(4) :
				if ((self.row+self.shapes[0][i][0] < 20 and self.col+self.shapes[0][i][1] < 10) and (self.row+self.shapes[0][i][0] >= 0 and self.col+self.shapes[0][i][1] >=0)) :
					if not(self.board[self.row+self.shapes[0][i][0]][self.col+self.shapes[0][i][1]] == "O" or self.board[self.row+self.shapes[0][i][0]][self.col+self.shapes[0][i][1]] == f"{self.initial}N" ) :
						condition = False
				else :
					condition = False
		else :
			for i in range(4) :
				if ((self.row+self.shapes[self.rotation+1][i][0] < 20 and self.col+self.shapes[self.rotation+1][i][1] < 10) and (self.row+self.shapes[self.rotation+1][i][0] >= 0 and self.col+self.shapes[self.rotation+1][i][1] >=0)) :
					if not(self.board[self.row+self.shapes[self.rotation+1][i][0]][self.col+self.shapes[self.rotation+1][i][1]] == "O"or self.board[self.row+self.shapes[self.rotation+1][i][0]][self.col+self.shapes[self.rotation+1][i][1]] == f"{self.initial}N") :
						condition = False
				else :
					condition = False
		if condition :
			for i in range(4) :
					self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "O"
			if self.rotation == 3 :
				self.rotation = 0
			else :
				self.rotation +=1
			for i in range(4) :
					self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = f"{self.initial}N"

	def move_left(self) :
		status = True
		cols = []
		for i in range(4) :
			cols.append(self.shapes[self.rotation][i][1])

		if not(min(cols)+self.col-1<0) :
			for i in range(4) :
				if not(self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]-1]=="O" or (self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]-1] == f"{self.initial}N")) :
					status=False

		if not(min(cols)+self.col-1<0) and status :
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "O"
			self.col -=1
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "IN"

	def move_right(self) :
		status = True
		cols = []
		for i in range(4) :
			cols.append(self.shapes[self.rotation][i][1])
			
		for i in range(4) :
			if not(max(cols)+self.col+1>=10) :
				if not(self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]+1]=="O" or (self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]+1] == f"{self.initial}N")) :
					status=False

		if not(max(cols)+self.col+1>=10) and status:
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "O"
			self.col +=1
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "IN"

	def delete(self) :
		for i in range(4) :
			self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "O"

	def show(self) :
		for i in range(4) :
			self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = f"{self.initial}N"

class O_block :
	def __init__(self, board) :
		self.rotation = 0
		self.initial = "0"
		self.board = board
		self.shapes =	([(0,0),(0,1),(1,0),(1,1)],
						[(0,0),(0,1),(1,0),(1,1)],
						[(0,0),(0,1),(1,0),(1,1)],
						[(0,0),(0,1),(1,0),(1,1)])
		self.row = 0
		self.col = 4
		self.finish = False

	def spawn(self) :
		for i in range(4) :
			self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "0N"

	def move_down(self) :
		rows = []
		for i in range(4) :
			rows.append(self.shapes[self.rotation][i][0])

		if (max(rows)+self.row+1>=20) :
			self.finish = True
		
		if not self.finish :
			for i in range(4) :
				if self.board[self.shapes[self.rotation][i][0]+self.row+1][self.shapes[self.rotation][i][1]+self.col] != "O" and self.board[self.shapes[self.rotation][i][0]+self.row+1][self.shapes[self.rotation][i][1]+self.col] != f"{self.initial}N" :
					self.finish = True

		if not self.finish :
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "O"
			self.row +=1
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "0N"
			return True

		if self.finish :
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = self.initial

	def rotate(self) :
		condition = True
		if self.rotation == 3 :
			for i in range(4) :
				if ((self.row+self.shapes[0][i][0] < 20 and self.col+self.shapes[0][i][1] < 10) and (self.row+self.shapes[0][i][0] >= 0 and self.col+self.shapes[0][i][1] >=0)) :
					if not(self.board[self.row+self.shapes[0][i][0]][self.col+self.shapes[0][i][1]] == "O" or self.board[self.row+self.shapes[0][i][0]][self.col+self.shapes[0][i][1]] == f"{self.initial}N" ) :
						condition = False
				else :
					condition = False
		else :
			for i in range(4) :
				if ((self.row+self.shapes[self.rotation+1][i][0] < 20 and self.col+self.shapes[self.rotation+1][i][1] < 10) and (self.row+self.shapes[self.rotation+1][i][0] >= 0 and self.col+self.shapes[self.rotation+1][i][1] >=0)) :
					if not(self.board[self.row+self.shapes[self.rotation+1][i][0]][self.col+self.shapes[self.rotation+1][i][1]] == "O"or self.board[self.row+self.shapes[self.rotation+1][i][0]][self.col+self.shapes[self.rotation+1][i][1]] == f"{self.initial}N") :
						condition = False
				else :
					condition = False
		if condition :
			for i in range(4) :
					self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "O"
			if self.rotation == 3 :
				self.rotation = 0
			else :
				self.rotation +=1
			for i in range(4) :
					self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = f"{self.initial}N"

	def move_left(self) :
		status = True
		cols = []
		for i in range(4) :
			cols.append(self.shapes[self.rotation][i][1])

		if not(min(cols)+self.col-1<0) :
			for i in range(4) :
				if not(self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]-1]=="O" or (self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]-1] == f"{self.initial}N")) :
					status=False

		if not(min(cols)+self.col-1<0) and status :
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "O"
			self.col -=1
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "0N"

	def move_right(self) :
		status = True
		cols = []
		for i in range(4) :
			cols.append(self.shapes[self.rotation][i][1])
			
		for i in range(4) :
			if not(max(cols)+self.col+1>=10) :
				if not(self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]+1]=="O" or (self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]+1] == f"{self.initial}N")) :
					status=False

		if not(max(cols)+self.col+1>=10) and status:
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "O"
			self.col +=1
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "0N"

	def delete(self) :
		for i in range(4) :
			self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "O"

	def show(self) :
		for i in range(4) :
			self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = f"{self.initial}N"

class S_block :
	def __init__(self, board) :
		self.rotation = 0
		self.initial = "S"
		self.board = board
		self.shapes =	([(0,1),(0,2),(1,0),(1,1)],
						[(0,1),(1,1),(1,2),(2,2)],
						[(1,1),(1,2),(2,0),(2,1)],
						[(0,0),(1,0),(1,1),(2,1)])
		self.row = 0
		self.col = 3
		self.finish = False

	def spawn(self) :
		for i in range(4) :
			self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "SN"

	def move_down(self) :
		rows = []
		for i in range(4) :
			rows.append(self.shapes[self.rotation][i][0])

		if (max(rows)+self.row+1>=20) :
			self.finish = True
		
		if not self.finish :
			for i in range(4) :
				if self.board[self.shapes[self.rotation][i][0]+self.row+1][self.shapes[self.rotation][i][1]+self.col] != "O" and self.board[self.shapes[self.rotation][i][0]+self.row+1][self.shapes[self.rotation][i][1]+self.col] != f"{self.initial}N" :
					self.finish = True

		if not self.finish :
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "O"
			self.row +=1
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "SN"
			return True

		if self.finish :
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = self.initial

	def rotate(self) :
		condition = True
		if self.rotation == 3 :
			for i in range(4) :
				if ((self.row+self.shapes[0][i][0] < 20 and self.col+self.shapes[0][i][1] < 10) and (self.row+self.shapes[0][i][0] >= 0 and self.col+self.shapes[0][i][1] >=0)) :
					if not(self.board[self.row+self.shapes[0][i][0]][self.col+self.shapes[0][i][1]] == "O" or self.board[self.row+self.shapes[0][i][0]][self.col+self.shapes[0][i][1]] == f"{self.initial}N" ) :
						condition = False
				else :
					condition = False
		else :
			for i in range(4) :
				if ((self.row+self.shapes[self.rotation+1][i][0] < 20 and self.col+self.shapes[self.rotation+1][i][1] < 10) and (self.row+self.shapes[self.rotation+1][i][0] >= 0 and self.col+self.shapes[self.rotation+1][i][1] >=0)) :
					if not(self.board[self.row+self.shapes[self.rotation+1][i][0]][self.col+self.shapes[self.rotation+1][i][1]] == "O"or self.board[self.row+self.shapes[self.rotation+1][i][0]][self.col+self.shapes[self.rotation+1][i][1]] == f"{self.initial}N") :
						condition = False
				else :
					condition = False
		if condition :
			for i in range(4) :
					self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "O"
			if self.rotation == 3 :
				self.rotation = 0
			else :
				self.rotation +=1
			for i in range(4) :
					self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = f"{self.initial}N"

	def move_left(self) :
		status = True
		cols = []
		for i in range(4) :
			cols.append(self.shapes[self.rotation][i][1])

		if not(min(cols)+self.col-1<0) :
			for i in range(4) :
				if not(self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]-1]=="O" or (self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]-1] == f"{self.initial}N")) :
					status=False

		if not(min(cols)+self.col-1<0) and status :
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "O"
			self.col -=1
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "SN"

	def move_right(self) :
		status = True
		cols = []
		for i in range(4) :
			cols.append(self.shapes[self.rotation][i][1])
			
		for i in range(4) :
			if not(max(cols)+self.col+1>=10) :
				if not(self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]+1]=="O" or (self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]+1] == f"{self.initial}N")) :
					status=False

		if not(max(cols)+self.col+1>=10) and status:
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "O"
			self.col +=1
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "SN"

	def delete(self) :
		for i in range(4) :
			self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "O"

	def show(self) :
		for i in range(4) :
			self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = f"{self.initial}N"

class Z_block :
	def __init__(self, board) :
		self.rotation = 0
		self.initial = "Z"
		self.board = board
		self.shapes =	([(0,0),(0,1),(1,1),(1,2)],
						[(0,2),(1,1),(1,2),(2,1)],
						[(1,0),(1,1),(2,1),(2,2)],
						[(0,1),(1,0),(1,1),(2,0)])
		self.row = 0
		self.col = 3
		self.finish = False

	def spawn(self) :
		for i in range(4) :
			self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "ZN"

	def move_down(self) :
		rows = []
		for i in range(4) :
			rows.append(self.shapes[self.rotation][i][0])

		if (max(rows)+self.row+1>=20) :
			self.finish = True
		
		if not self.finish :
			for i in range(4) :
				if self.board[self.shapes[self.rotation][i][0]+self.row+1][self.shapes[self.rotation][i][1]+self.col] != "O" and self.board[self.shapes[self.rotation][i][0]+self.row+1][self.shapes[self.rotation][i][1]+self.col] != f"{self.initial}N" :
					self.finish = True

		if not self.finish :
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "O"
			self.row +=1
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "ZN"
			return True

		if self.finish :
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = self.initial

	def rotate(self) :
		condition = True
		if self.rotation == 3 :
			for i in range(4) :
				if ((self.row+self.shapes[0][i][0] < 20 and self.col+self.shapes[0][i][1] < 10) and (self.row+self.shapes[0][i][0] >= 0 and self.col+self.shapes[0][i][1] >=0)) :
					if not(self.board[self.row+self.shapes[0][i][0]][self.col+self.shapes[0][i][1]] == "O" or self.board[self.row+self.shapes[0][i][0]][self.col+self.shapes[0][i][1]] == f"{self.initial}N" ) :
						condition = False
				else :
					condition = False
		else :
			for i in range(4) :
				if ((self.row+self.shapes[self.rotation+1][i][0] < 20 and self.col+self.shapes[self.rotation+1][i][1] < 10) and (self.row+self.shapes[self.rotation+1][i][0] >= 0 and self.col+self.shapes[self.rotation+1][i][1] >=0)) :
					if not(self.board[self.row+self.shapes[self.rotation+1][i][0]][self.col+self.shapes[self.rotation+1][i][1]] == "O"or self.board[self.row+self.shapes[self.rotation+1][i][0]][self.col+self.shapes[self.rotation+1][i][1]] == f"{self.initial}N") :
						condition = False
				else :
					condition = False
		if condition :
			for i in range(4) :
					self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "O"
			if self.rotation == 3 :
				self.rotation = 0
			else :
				self.rotation +=1
			for i in range(4) :
					self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = f"{self.initial}N"

	def move_left(self) :
		status = True
		cols = []
		for i in range(4) :
			cols.append(self.shapes[self.rotation][i][1])

		if not(min(cols)+self.col-1<0) :
			for i in range(4) :
				if not(self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]-1]=="O" or (self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]-1] == f"{self.initial}N")) :
					status=False

		if not(min(cols)+self.col-1<0) and status :
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "O"
			self.col -=1
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "ZN"

	def move_right(self) :
		status = True
		cols = []
		for i in range(4) :
			cols.append(self.shapes[self.rotation][i][1])
			
		for i in range(4) :
			if not(max(cols)+self.col+1>=10) :
				if not(self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]+1]=="O" or (self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]+1] == f"{self.initial}N")) :
					status=False

		if not(max(cols)+self.col+1>=10) and status:
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "O"
			self.col +=1
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "ZN"

	def delete(self) :
		for i in range(4) :
			self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "O"

	def show(self) :
		for i in range(4) :
			self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = f"{self.initial}N"

class T_block :
	def __init__(self, board) :
		self.rotation = 0
		self.initial = "T"
		self.board = board
		self.shapes =	([(0,1),(1,0),(1,1),(1,2)],
						[(0,1),(1,1),(1,2),(2,1)],
						[(1,0),(1,1),(1,2),(2,1)],
						[(0,1),(1,0),(1,1),(2,1)])
		self.row = 0
		self.col = 3
		self.finish = False

	def spawn(self) :
		for i in range(4) :
			self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "TN"

	def move_down(self) :
		rows = []
		for i in range(4) :
			rows.append(self.shapes[self.rotation][i][0])

		if (max(rows)+self.row+1>=20) :
			self.finish = True
		
		if not self.finish :
			for i in range(4) :
				if self.board[self.shapes[self.rotation][i][0]+self.row+1][self.shapes[self.rotation][i][1]+self.col] != "O" and self.board[self.shapes[self.rotation][i][0]+self.row+1][self.shapes[self.rotation][i][1]+self.col] != f"{self.initial}N" :
					self.finish = True

		if not self.finish :
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "O"
			self.row +=1
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "TN"
			return True

		if self.finish :
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = self.initial

	def rotate(self) :
		condition = True
		if self.rotation == 3 :
			for i in range(4) :
				if ((self.row+self.shapes[0][i][0] < 20 and self.col+self.shapes[0][i][1] < 10) and (self.row+self.shapes[0][i][0] >= 0 and self.col+self.shapes[0][i][1] >=0)) :
					if not(self.board[self.row+self.shapes[0][i][0]][self.col+self.shapes[0][i][1]] == "O" or self.board[self.row+self.shapes[0][i][0]][self.col+self.shapes[0][i][1]] == f"{self.initial}N" ) :
						condition = False
				else :
					condition = False
		else :
			for i in range(4) :
				if ((self.row+self.shapes[self.rotation+1][i][0] < 20 and self.col+self.shapes[self.rotation+1][i][1] < 10) and (self.row+self.shapes[self.rotation+1][i][0] >= 0 and self.col+self.shapes[self.rotation+1][i][1] >=0)) :
					if not(self.board[self.row+self.shapes[self.rotation+1][i][0]][self.col+self.shapes[self.rotation+1][i][1]] == "O"or self.board[self.row+self.shapes[self.rotation+1][i][0]][self.col+self.shapes[self.rotation+1][i][1]] == f"{self.initial}N") :
						condition = False
				else :
					condition = False
		if condition :
			for i in range(4) :
					self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "O"
			if self.rotation == 3 :
				self.rotation = 0
			else :
				self.rotation +=1
			for i in range(4) :
					self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = f"{self.initial}N"

	def move_left(self) :
		status = True
		cols = []
		for i in range(4) :
			cols.append(self.shapes[self.rotation][i][1])

		if not(min(cols)+self.col-1<0) :
			for i in range(4) :
				if not(self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]-1]=="O" or (self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]-1] == f"{self.initial}N")) :
					status=False

		if not(min(cols)+self.col-1<0) and status :
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "O"
			self.col -=1
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "TN"

	def move_right(self) :
		status = True
		cols = []
		for i in range(4) :
			cols.append(self.shapes[self.rotation][i][1])
			
		for i in range(4) :
			if not(max(cols)+self.col+1>=10) :
				if not(self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]+1]=="O" or (self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]+1] == f"{self.initial}N")) :
					status=False

		if not(max(cols)+self.col+1>=10) and status:
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "O"
			self.col +=1
			for i in range(4) :
				self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "TN"

	def delete(self) :
		for i in range(4) :
			self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = "O"

	def show(self) :
		for i in range(4) :
			self.board[self.row+self.shapes[self.rotation][i][0]][self.col+self.shapes[self.rotation][i][1]] = f"{self.initial}N"
