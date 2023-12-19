class GameBoard:
	def __init__(self, state=[[-1 for i in range(3)] for i in range(3)], turn=0):
		self.state = state
		self.turn = turn

	def print(self):
		print(" ------- ")
		currentline = "| "
		for i in range(3):
			for j in range(3):
				# currentline += str(self.state[i][j])
				if self.state[i][j] == -1:
					currentline += " "
				elif self.state[i][j] == 0:
					currentline += "X"
				elif self.state[i][j] == 1:
					currentline += "O"

				if j != 2: currentline += " "
			currentline += " |"
			print(currentline)
			currentline = "| "
		print(" ------- ")
	
	def getTurn(self):
		return self.turn
	
	@staticmethod
	def gety(hotkey):
		if hotkey in ["1","2","3","q","w","e"]:
			return	 0
		elif hotkey in ["4","5","6","a","s","d"]:
			return 1
		elif hotkey in ["7","8","9","z","x","c"]:
			return 2
		else:
			return -1

	@staticmethod
	def getx(hotkey):
		if hotkey in ["1","4","7","q","a","z"]:
			return 0
		elif hotkey in ["2","5","8","w","s","x"]:
			return 1
		elif hotkey in ["3","6","9","e","d","c"]:
			return 2
		else:
			return -1

	def pla(self, hotkey):
		self.state[GameBoard.gety(hotkey)][GameBoard.getx(hotkey)] = self.turn % 2


	def rem(self, hotkey):
		self.state[GameBoard.gety(hotkey)][GameBoard.getx(hotkey)] = -1

	def incTurn(self):
		self.turn = self.turn + 1
		
	#TODO:	Method to ask for piece placement
	#		Method to ask for peace removal
	#		Method to check if any player has won
	#		Method to play a single turn, including all the UI, input handling, gameboard manipulation, turn increasement and winn checking. Might in the future also include UI to pause the game
	#		Method to start the game, hence successively play turn after turn.
