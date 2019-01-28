board=[]
numPlayers=2
numRows=6 
numColumns=7
numWins=4
count=1
turn=0
end=0
checker=['\033[1;31mX\033[0m','\033[0;32mO\033[0m',"\033[1;34m@\033[0m",]
players=['Player 1 (X)','Player 2 (O)',]

import os

for r in range(numRows):
	list=[]
	for c in range(numColumns):
		list.append('.')
	board.append(list)

while end!=1 and '.' in board[0]:
	
        os.system("cls")
        for	c in range(numColumns):
        	print('   '+str(c+1),end='')
        print()
        for r in range(numRows):
        	print(str(r+1)+'  ',end='')
        	for c in range(numColumns):
        		print(board[r][c]+' | ',end='')
        	print("\n  "+"---+"*numColumns)
        
        if count==1:
                print('Welcome to Connect 4!')

        move=input(players[turn]+": Please enter the column you want to insert your checker in (from 1-7): ")
        while move.isdigit() == False or int(move)>numColumns or int(move)-1<0:
                print('Invalid move.')
                move=(input(players[turn]+": Please enter the column you want to insert your checker in (from 1-7): "))

        for x in range(numRows,0,-1):
                if board[x-1][int(move)-1]=='.':
                        board[x-1][int(move)-1]=checker[turn]
                        break

        for x in range(numRows):
                for y in range(numColumns - numWins+1):
                        cnt = 0
                        for i in range(numWins):
                                if board[x][y+i] ==checker[turn]:
                                        cnt+=1
                        if cnt == numWins:
                                end+=1
    
        for y in range(numColumns):
                for x in range(numRows - numWins+1):
                        cnt = 0
                        for i in range(numWins):
                                if board[x+i][y]==checker[turn]:
                                        cnt+=1
                        if cnt==numWins:
                                end+=1

        for y in range(numWins-1, numColumns):
                for x in range(numRows-numWins+1):
                        cnt=0
                        for i in range(numWins):
                                if board[x+i][y-i]==checker[turn]:
                                        cnt+=1
                        if cnt==numWins:
                                end+=1

        for y in range(numWins):
                for x in range(numRows-numWins+1):
                        cnt=0
                        for i in range(numWins):
                                if board[x+i][y+i]==checker[turn]:
                                        cnt+=1
                        if cnt==numWins:
                                end+=1

        os.system("cls")
        for	c in range(numColumns):
        	print('   '+str(c+1),end='')
        print()
        for r in range(numRows):
        	print(str(r+1)+'  ',end='')
        	for c in range(numColumns):
        		print(board[r][c]+' | ',end='')
        	print("\n  "+"---+"*numColumns)

        turn=(turn+1)%numPlayers
        count+=1

if end==1:
        print('Congratulations, '+players[turn-1]+' is the winner!')
else:
        print("It's a draw!")