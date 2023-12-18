class GameBoard:
	def __init__(self, state=[[0 for i in range(3)] for i in range(3)], turn=0):
		self.state = state
#		self.turn = turn
	def print(self):
		print(" ------- ")
		currentline = "| "
		for i in range(3):
			for j in range(3):
				currentline += str(self.state[i][j])
				if j != 2: currentline += " "
			currentline += " |"
			print(currentline)
			currentline = "| "
		print(" ------- ")
