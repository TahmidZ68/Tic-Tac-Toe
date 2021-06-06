
def ConstBoard(board):
    print("Current State Of Board : \n\n")
    for i in range (0,9):
        if((i>0) and (i%3)==0):
            print("\n")
        if(board[i]==0):
            print("- ",end=" ")
        if (board[i]==1):
            print("O ",end=" ")
        if(board[i]==-1):
            print("X ",end=" ")
    print("\n\n")


def User1Turn(board):
    pos=input("Enter X's position from [1...9]: ")
    pos=int(pos)
    if(board[pos-1]!=0):
        print("Wrong Move!!!")
        exit(0)
    board[pos-1]=-1

def User2Turn(board):
    pos=input("Enter O's position from [1...9]: ")
    pos=int(pos)
    if(board[pos-1]!=0):
        print("Wrong Move!!!")
        exit(0)
    board[pos-1]=1

#MinMax function.
def minimax(board,player):
    x=ana_board(board)
    if(x!=0):
        return (x*player)
    pos=-1
    value=-2
    for i in range(0,9):
        if(board[i]==0):
            board[i]=player
            score=-minimax(board,(player*-1))
            if(score>value):
                value=score
                pos=i
            board[i]=0

    if(pos==-1):
        return 0
    return value

def CompTurn(board):
    pos=-1
    value=-2
    for i in range(0,9):
        if(board[i]==0):
            board[i]=1
            score=-minimax(board, -1)
            board[i]=0
            if(score>value):
                value=score
                pos=i

    board[pos]=1;



def ana_board(board):
    com=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]

    for i in range(0,8):
        if(board[com[i][0]] != 0 and
           board[com[i][0]] == board[com[i][1]] and
           board[com[i][0]] == board[com[i][2]]):
            return board[com[i][2]]
    return 0


def main():
    choice=input("Enter 1 for single player and 2 for multiplayer: ")
    choice=int(choice)

    board=[0,0,0,0,0,0,0,0,0]
    if(choice==1):
        print("Computer : O Vs. You : X")
        player= input("Enter 1(st) or 2(nd) to select position :")
        player = int(player)
        for i in range (0,9):
            if(ana_board(board)!=0):
                break
            if((i+player)%2==0):
                CompTurn(board)
            else:
                ConstBoard(board)
                User1Turn(board)
    else:
        for i in range (0,9):
            if(ana_board(board)!=0):
                break
            if((i)%2==0):
                ConstBoard(board)
                User1Turn(board)
            else:
                ConstBoard(board)
                User2Turn(board)


    x=ana_board(board)
    if(x==0):
         ConstBoard(board)
         print("Draw!!!")
    if(x==-1):
         ConstBoard(board)
         print("X Wins!!! 0 Loose !!!")
    if(x==1):
         ConstBoard(board)
         print("X Loose!!! 0 Wins !!!!")

main()



