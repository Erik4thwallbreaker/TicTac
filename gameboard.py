class GameBoard:
	def __init__(self, state=[[-1 for i in range(3)] for i in range(3)], turn=0):
		self.state = state
		self.turn = turn

	@staticmethod
	def gametoken(value):
		if value <= -1:
			return " "
		elif value % 2 == 0:
			return "X"
		elif value % 2 == 1:
			return "O"
		else: return "E"

	def print(self):
		print("               ------- ")
		currentline = " Turn: " + str(self.turn) + " "*(7-min(len(str(self.turn)), 7)) + "| "
		for i in range(3):
			for j in range(3):
				currentline += GameBoard.gametoken(self.state[i][j])
				if j != 2: currentline += " "
			currentline += " |"
			print(currentline)
			if i == 0:
				currentline = " (Player: " + GameBoard.gametoken(self.turn) + ")  | "
			else:
				currentline = "              | "
		print("               ------- ")
	
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
		
	@staticmethod
	def _validKey(hotkey):
		return hotkey in ["1","4","7","q","a","z"] + ["2","5","8","w","s","x"] + ["3","6","9","e","d","c"] 

	def _legalPlaceKey(self, hotkey):
		return self.state[GameBoard.gety(hotkey)][GameBoard.getx(hotkey)] == -1

	def _legalRemoveKey(self, hotkey):
		return 0 <= self.state[GameBoard.gety(hotkey)][GameBoard.getx(hotkey)] == self.turn % 2

	def askForPlacement(self):
		hotkey = input("Where do you want to place your piece? :")
		while not GameBoard._validKey(hotkey) or not self._legalPlaceKey(hotkey):
			if not GameBoard._validKey(hotkey): hotkey = input("Invalid key. Where do you want to place your piece? :")
			elif not self._legalPlaceKey(hotkey): hotkey = input("Illegal move. Place select an empty square: ")
		self.pla(hotkey)
		
	def askForRemoval(self):
		hotkey = input("Which piece do you want to remove? :")
		while not GameBoard._validKey(hotkey) or not self._legalRemoveKey(hotkey):
			if not GameBoard._validKey(hotkey): hotkey = input("Invalid key. Which piece do you want to remove? :")
			elif not self._legalRemoveKey(hotkey): hotkey = input("Illegal move. Please select one of your own pieces to remove: ")
		self.rem(hotkey)

	def mirrorBoard(self):
		newState = [self.state[i] for i in reversed(range(3))]
		return GameBoard(state = newState, turn = self.turn)

	def flipBoard(self):
		newState = [[self.state[j][i] for j in range(3)] for i in reversed(range(3))]
		return GameBoard(state = newState, turn = self.turn)
		
	def hasWon(self):		#How should I implement turning the board 90deg and reconsider?
		virt = self
		for i in range(2):
			for j in range(3):
				if virt.state[j][0] == virt.state[j][1] == virt.state[j][2] >= 0:
					return virt.state[j][0]			
			if virt.state[0][0] == virt.state[1][1] == virt.state[2][2] >= 0:
				return virt.state[0][0]			
			if i == 0:
				virt = virt.flipBoard()
		return -1

	def playTurn(self):
		print("_____________________________________")
		self.print()
		if self.turn >= 6: self.askForRemoval()
		self.askForPlacement()
		self.turn += 1
		print()

	def playGame(self):
		winner = -1
		while winner == -1:
			self.playTurn()
			winner = self.hasWon()
		self.turn -= 1		#Counteract the turn increase that happens after every turn.k
		print("_____________________________________")
		print("           - Game Finished -        ")
		print("_____________________________________")
		self.print()
		print("Player " + GameBoard.gametoken(self.turn) + " has won. Congratulations!")
		return
	#TODO:	
	#		Make a single helping method to give the correct string tokens for each player X and O.
	#		Edit the print() method to display game turn on the same line.
	#		Edit the placement method to only allow placing pieces on unused squares.
	#		Method to start the game, hence successively play turn after turn.
