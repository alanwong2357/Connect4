def connect4():
	'''runs the game'''
	win = False
	team = 1
	row = 6
	col = 7
	table = []
	for i in range(row):
		table += [[0] * col]
	while not win:
		printboard(table)
		table = addPiece(table, team)
		team = switchteams(team)


def printboard(t: 'table'):
	'''prints the board'''
	for i in t:
		for j in i:
			print(j, end=' ')
		print()
	print()


def switchteams(s: 'team') -> int:
	'''changes what team's turn it is'''
	result = 1
	if s == 1:
		result = 2
	return result


def addPiece(t: 'table', team: int) -> 'table':
	'''print(type(table[currCol]))'''
	currCol = int(input("What number column would you like to put a piece in?\n")) - 1
	isValid = validMove(currCol)
	if isValid:
		for i in range(6):
			if t[5 - i][currCol] == 0:
				t[5 - i][currCol] = team
				gameOver(t, team)
				return t

	else:
		print('Invalid move, column already filled up')
		addPiece(team)


def validMove(num: 'currCol') -> bool:
	'''Checks if the move is valid'''
	result = False
	if (type(num) == type(1)) and (num >= 0) and (num <= 6):
		result = True
	return result


def gameOver(t:'table', team: int):
	'''Checks whether one player has gotten a connect 4'''


	count = 0
	global win
	'''check horizontal'''
	for i in range(5):
		for j in range(6):
			if i < 5 and j < 6:
				if t[i + 1][j]==team:
					count += 1
		if count==4:
			win = True
			break
		else:
			count = 0
	'''check vertical'''
	for i in range(6):
		for j in range(5):
			if i < 5 and j < 6:
				if t[i][j + 1]==team:
					count += 1
		if count==4:
			print('you win')
			win = True
			break
		else:
			count = 0
	'''check top left-bottom right +1, +1'''
	for i in range(2):
		for j in range(6 - i):
			if i < 5 and j < 6:
				if t[i + 1][j + 1]==team:
					count += 1
		if count==4:
			win = True
			break
		else:
			count = 0
	'''check bottom left-top right -1, +1'''
	for i in range(3,6):
		for j in range(i + 1):
			if i < 5 and j < 6:
				if t[i - 1][j + 1]==team:
					count += 1
		if count==4:
			win = True
			break
		else:
			count = 0

connect4()