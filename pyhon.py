from random import randrange
    
def display_board(board):
    # La función acepta un parámetro el cual contiene el estado actual del tablero
    # y lo muestra en la consola.
    print("+--------" * 3, "+", sep="")
    for row in range (3):
        print("|        "*3, "|", sep = "")
        for col in range(3):
            print("|   " + str(board[row][col]) + "    ", end="")
        print("|")
        print("|        "*3, "|", sep = "")
        print("+--------" * 3, "+", sep="")

def enter_move(board):
    # La función acepta el estado actual del tablero y pregunta al usuario acerca de su movimiento,  
    # verifica la entrada y actualiza el tablero acorde a la decisión del usuario.
    ok = False
    while not ok:
        move = input("Ingrese su movimiento: ")
        ok = len(move) == 1 or move >= '1' or move <= '9'
        if not ok:
            print("Movimiento no valido, ingrese nuevamente")
            continue
        move = int(move) - 1
        row = move // 3
        col = move % 3
        sign = board[row][col]
        ok = sign not in ['\x1b[1;32mO\x1b[1;0m', '\x1b[1;33mX\x1b[1;0m']
        if not ok:
            print("Cuadro ocupado, ingrese nuevamente")
            continue
    board[row][col] = '\x1b[1;32mO\x1b[1;0m'
            
def make_list_of_free_fields(board):
    # La función examina el tablero y construye una lista de todos los cuadros vacíos. 
    # La lista esta compuesta por tuplas, cada tupla es un par de números que indican la fila y columna.
    free = []
    for row in range(3):
        for col in range(3):
            if board[row][col] not in ['\x1b[1;32mO\x1b[1;0m', '\x1b[1;33mX\x1b[1;0m']:
                free.append((row, col))
    return free


def victory_for(board, sign):
    # La función analiza el estatus del tablero para verificar si 
    # el jugador que utiliza las 'O's o las 'X's ha ganado el juego.
    if sign == '\x1b[1;32mO\x1b[1;0m':
        who = 'you'
    elif sign == '\x1b[1;33mX\x1b[1;0m':
        who = 'me'
    else:
        who = None
    diag1 = diag2 = True
    for index in range(3):
        if board[index][0] == sign and board[index][1] == sign and board[index][2] == sign :
            return who
        if board[0][index] == sign and board[1][index] == sign and board [2][index] == sign :
            return who
        if board[index][index] != sign:
            diag1 = False
        if board[2 - index][2 - index] != sign:
            diag2 = False
    if diag1 or diag2:
        return who
    return None    
    
def draw_move(board):
    # La función dibuja el movimiento de la máquina y actualiza el tablero.
    free = make_list_of_free_fields(board)
    size = len(free)
    if size > 0:
        this = randrange(size)
        row, col = free[this]
        board[row][col] = '\x1b[1;33mX\x1b[1;0m'


board = [ [3 * j + i + 1 for i in range(3)] for j in range(3) ]
board[1][1] = '\x1b[1;33mX\x1b[1;0m'
free = make_list_of_free_fields(board)
user_turn = True
while len(free):
    display_board(board)
    if user_turn:
        enter_move(board)
        victory = victory_for(board, '\x1b[1;32mO\x1b[1;0m')
    else:
        draw_move(board)
        victory = victory_for(board, '\x1b[1;33mX\x1b[1;0m')
    if victory != None:
        break
    user_turn = not user_turn
    free = make_list_of_free_fields(board)
    
display_board(board)
if victory == 'you':
    print("\n\t!Has ganado¡")
elif victory == 'me':
    print("\n\t!He ganado¡")
else:
    print("\n\tEmpate...")






























