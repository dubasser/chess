def check_inputs():
    try:

        temp_squares = [int((a)) for a in squares.rsplit()]
    except ValueError:
        print('Неверный формат ввода, попробуйте снова')
        return False
    if len(temp_squares) != 4:
        print('Неверный формат ввода, попробуйте снова')
        return False
    for i in range(4):
        if (temp_squares[i] >= 1) and (temp_squares[i] <= 8):
            pass
        else:
            print('Неверный формат ввода, попробуйте снова')
            return False
    pieces_list=['ЛАДЬЯ','ФЕРЗЬ','СЛОН','КОНЬ']
    if piece.upper() not in pieces_list:
        print('Неверно введено название фигуры')
        return False
    return temp_squares


def is_same_color():
    if (int(squares[0] + squares[1]) % 2) == (int(squares[2] + squares[3]) % 2):
        return True
    else:
        return False


def is_attacked_by_knight():
    counter = 0
    knight_moves = [(1, 2), (2, 1), (-1, 2), (-2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
    current_square = (squares[0], squares[1])
    target_square = (squares[2], squares[3])
    for move in knight_moves:
        if (
                current_square[0] + knight_moves[counter][0],
                current_square[1] + knight_moves[counter][1]) == target_square:
            print('Конь на поле' + str((squares[0], squares[1])) + ' аттакует поле ' + str((squares[2], squares[3])))
            return True
        counter += 1
    print('Конь на поле' + str((squares[0], squares[1])) + ' не аттакует поле ' + str((squares[2], squares[3])))
    return False


def is_attacked_by_bishop():
    diagonal_moves = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
    current_square = (squares[0], squares[1])
    target_square = (squares[2], squares[3])
    for move in diagonal_moves:
        if (current_square[0] + move[0], current_square[1] + move[1]) == target_square:
            print('Слон на поле' + str((squares[0], squares[1])) + ' аттакует поле ' + str((squares[2], squares[3])))
            return True
    print('Слон на поле' + str((squares[0], squares[1])) + ' не аттакует поле ' + str((squares[2], squares[3])))
    return False


def is_attacked_by_rook():
    current_square = (squares[0], squares[1])
    target_square = (squares[2], squares[3])
    if current_square[0] == target_square[0] or current_square[1] == target_square[1]:
        print('Ладья на поле '+str((squares[0], squares[1])) +' аттакует поле ' + str((squares[2], squares[3])))
        return True
    print('Ладья на поле '+str((squares[0], squares[1])) +' не аттакует поле ' + str((squares[2], squares[3])))
    return False


def is_attacked_by_queeen():
    if is_attacked_by_bishop() == True or is_attacked_by_rook() == True:
        print('Ферзь на поле'+str((squares[0], squares[1]))+' аттакует поле ' + str((squares[2], squares[3])))
        return True
    print('Ферзь на поле'+str((squares[0], squares[1]))+' не аттакует поле ' + str((squares[2], squares[3])))
    return False


def get_diagonal_moves():
    diagonal_moves = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
    possible_moves = []
    current_square = (squares[0], squares[1])
    for move in diagonal_moves:
        for index in range(8):
            current_move = (current_square[0] + move[0] * index, current_square[1] + move[1] * index)
            if 1 <= current_move[0] <= 8 and 1 <= current_move[1] <= 8:
                if current_move not in possible_moves:
                    possible_moves.append(current_move)
    return possible_moves


def get_vertical_moves():
    current_square = (squares[0], squares[1])
    possible_moves=[]
    for index in range(-8,8):
        current_vertical=current_square[0]+index
        if 1<=current_vertical <= 8:
            if current_vertical!=current_square[0]:
                possible_moves.append((current_vertical,current_square[1]))
    print(possible_moves)
    return possible_moves


def get_horizontal_moves():
    current_square = (squares[0], squares[1])
    possible_moves = []
    for index in range(-8, 8):
        current_horizontal = current_square[1] + index
        if 1 <= current_horizontal <= 8:
            if current_horizontal != current_square[1]:
                possible_moves.append((current_square[0],current_horizontal))
    print(possible_moves)
    return possible_moves


def get_knight_moves(square1,square2):
    result=[]
    knight_moves = [(1, 2), (2, 1), (-1, 2), (-2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
    current_square = (square1, square2)
    for move in knight_moves:
        aprox_square=list(map(lambda x, y: x + y, current_square, move))
        if 1<aprox_square[0]<8 and 1<aprox_square[1]<8:
            result.append(aprox_square)
    return result


while True:
    squares = input('Введите 4 координаты через пробел\n')
    piece=str(input('Введите название фигуры: '))
    squares = check_inputs()
    if squares == False:
        continue
    if is_same_color() == True:
        print('Поля одного цвета')
    else:
        print('Поля разного цвета')
    if piece.upper()=='КОНЬ':
        is_attacked_by_knight()
    if piece.upper()=='ЛАДЬЯ':
        is_attacked_by_rook()
    if piece.upper()=='ФЕРЗЬ':
        is_attacked_by_queeen()
    if piece.upper()=='СЛОН':
        is_attacked_by_bishop()




