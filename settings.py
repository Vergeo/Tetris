import json

class Settings() :
	def __init__(self) :
		self.w_ratio, self.h_ratio = 3,4
		self.base = 150
		self.width = self.w_ratio*self.base
		self.height = self.h_ratio*self.base
		self.screen = f"{self.width}x{self.height}+500+50"

		self.title = "Tetris"
		self.FPS = 1

		self.logo_path = "image/logo.png"
		self.logo_path2 = "image/logo2.png"

		self.background_path = "image/background3.png"
		self.game_page_path = "image/game_page_4.png"
		self.play_path = "image/game_page_5.png"

		self.o_block = "image/o_block.png"
		self.l_block = "image/l_block.png"
		self.z_block = "image/z_block.png"
		self.t_block = "image/t_block.png"
		self.j_block = "image/j_block.png"
		self.i_block = "image/i_block.png"
		self.s_block = "image/s_block.png"
		self.black_block = "image/black_block.png"

		self.o_block_back = "image/oblock.png"
		self.l_block_back = "image/lblock.png"
		self.z_block_back = "image/zblock.png"
		self.t_block_back = "image/tblock.png"
		self.j_block_back = "image/jblock.png"
		self.i_block_back = "image/iblock.png"
		self.s_block_back = "image/sblock.png"
		self.empty_back = "image/empty.png"

		self.htp1 = "image/htp1.png"
		self.htp2 = "image/htp2.png"
		self.htp3 = "image/htp3.png"

		self.leaderboard_logo = "image/leaderboard_logo.png"

		self.users_path = "data/users.json"
		self.leaderboard_path = "data/leaderboard.json"

	def load_data(self, path) :
		with open(path, "r") as json_data :
			data = json.load(json_data)
		return data

	def login(self, username, password) :
		users = self.load_data(self.users_path)
		if username in users :
			if password == users[username]["password"] :
				return True
		else :
			return False

	def save_data(self, item, path) :
		with open(path, "w") as json_data :
			json.dump(item, json_data)