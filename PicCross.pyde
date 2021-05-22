gameboard = []
CELL_DIM = 20
START_X, START_Y, END_X, END_Y = 0, 0, 0, 0

GAME_DIM = (10, 20)
MOUSE_PRESSED = False

def renderBoard(board):
    for i in range(len(board)):
        if i%5 == 0:
            strokeWeight(3)
        else:
            strokeWeight(1)
        line(START_X, START_Y+CELL_DIM*i, END_X, START_Y+CELL_DIM*i)
    for i in range(len(board[0])):
        if i%5 == 0:
            strokeWeight(3)
        else:
            strokeWeight(1)
        line(START_X+CELL_DIM*i, START_Y, START_X+CELL_DIM*i, END_Y)    
    
    strokeWeight(3)
    line(END_X, START_Y, END_X, END_Y)
    line(START_X, END_Y, END_X, END_Y)
    strokeWeight(1)
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                fill(0)
                rect(START_X+CELL_DIM*j, START_Y+CELL_DIM*i, CELL_DIM, CELL_DIM)
            elif board[i][j] == -1:            
                line(START_X+CELL_DIM*j, START_Y+CELL_DIM*i, START_X+CELL_DIM*(j+1), START_Y+CELL_DIM*(i+1))
                line(START_X+CELL_DIM*j, START_Y+CELL_DIM*(i+1), START_X+CELL_DIM*(j+1), START_Y+CELL_DIM*i)

def handleClick(pos):
    global gameboard
    X, Y = (pos[0] - START_X)//CELL_DIM, (pos[1] - START_Y)//CELL_DIM
    print(X, Y)
    if mouseButton == LEFT:
        gameboard[Y][X] = 1 if gameboard[Y][X] == 0 or gameboard[Y][X] == -1 else 0
    elif mouseButton == RIGHT:
        gameboard[Y][X] = -1

def setup():
    global gameboard
    global START_X, START_Y, END_X, END_Y
    
    size(600, 600)
    
    gameboard = [[0 for i in range(GAME_DIM[0])] for j in range(GAME_DIM[1])]
    
    START_X, START_Y = (width - len(gameboard[0])*CELL_DIM)//2, (height - len(gameboard)*CELL_DIM)//2
    END_X, END_Y = (width + len(gameboard[0])*CELL_DIM)//2, (height + len(gameboard)*CELL_DIM)//2
    
    print("Start: %d, %d\nEnd: %d, %d" % (START_X, START_Y, END_X, END_Y))
    
def draw():
    global gameboard, MOUSE_PRESSED
    
    clear()
    background(255)
    
    if mousePressed and not MOUSE_PRESSED:
        mouse_position = (mouseX, mouseY)
        
        if START_X < mouseX < END_X and START_Y < mouseY < END_Y:
            handleClick(mouse_position)
        MOUSE_PRESSED = True
        
    elif not mousePressed and MOUSE_PRESSED:
        MOUSE_PRESSED = False
        
    renderBoard(gameboard)
